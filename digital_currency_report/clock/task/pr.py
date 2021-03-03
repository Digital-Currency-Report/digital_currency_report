import time

from digital_currency_report.clock.base import Timer
from digital_currency_report.common.log import logger
from digital_currency_report.common.task import task

async def test(t):
    logger.info(f"test clock {t}")

@task.register_timer
class PR(Timer):
    # 每 12 个小时监测 过期文件进行删除
    delay = 10

    @staticmethod
    async def job():
        task.create_task(test(time.time()))


if __name__ == '__main__':
    while True:
        pass
