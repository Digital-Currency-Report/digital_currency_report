import asyncio
from asyncio import QueueEmpty
from typing import Union, Any

import uvloop

from digital_currency_report.api.base.auth.auth import auth
from digital_currency_report.api.base.auth.user import User
from digital_currency_report.api.base.model.base_model import BaseModel
from digital_currency_report.clock.base import Timer
from digital_currency_report.common.database.postgresql import postgresql, maker_session
from digital_currency_report.common.log import logger
from digital_currency_report.config import config


class Task(BaseModel):
    func: Any
    user: User = None
    clock: int = 0


class AsyncTask:
    worker = 0
    queue = asyncio.Queue()

    async def task_pull(self):
        self.worker += 1
        while True:
            # 读取异步任务
            try:
                task: Task = self.queue.get_nowait()
            # worker 回收
            except QueueEmpty:
                self.worker -= 1
                return True
            try:
                # 加载当前异步事件所属的用户
                auth.user = task.user
                # 执行
                async with maker_session() as session:
                    postgresql.session = session
                    if task.clock:
                        await task.func.job()
                    else:
                        await task.func
            except Exception as e:
                logger.exception(f'async error : {repr(e)}')

            # 如果是定时任务，则注册下一次事件
            if task.clock:
                self.create_task(task=task, delay=task.clock)

    @property
    def loop(self) -> Union[uvloop.Loop, asyncio.AbstractEventLoop]:
        return asyncio.get_event_loop()

    async def delay(self, task: Task, delay: int = None):
        if delay:
            await asyncio.sleep(delay)
        self._create_task(task)

    def _create_task(self, task: Task):
        self.queue.put_nowait(task)
        # 当任务队列还有任务未完成，而且未超过最大 worker 数量的情况下新建一个人 worker
        if self.queue.qsize() and self.worker < config.Pool_Size:
            self.loop.create_task(self.task_pull())

    # 返回一个 Future 对象，可以通过 result() 方法获取返回值
    def create_task(self, task: Union[Task, callable], delay: int = None) -> bool:
        """创建一个协程任务，无视任务结果
        如需链式调用，请使用以下方法
        from fastapi import BackgroundTasks
        background_tasks: BackgroundTasks
        background_tasks.add_task(func, *arg, **kwargs）
        """
        if not isinstance(task, Task):
            task = Task(
                # 异步事件
                func=task,
                # 触发异步用户
                user=auth.get_user(),
                clock=0
            )

        if delay:
            self.loop.create_task(self.delay(task, delay=delay))
        else:
            self._create_task(task)
        return True

    def register_timer(self, timer: Timer) -> bool:
        return self.create_task(Task(
            func=timer,
            clock=timer.delay
        ))


task = AsyncTask()

if __name__ == '__main__':
    pass
