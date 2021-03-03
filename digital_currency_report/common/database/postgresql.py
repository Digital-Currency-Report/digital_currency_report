from contextvars import ContextVar
from functools import wraps
from typing import Optional

from sqlalchemy.exc import DisconnectionError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

from digital_currency_report.common.database.base import engine
from digital_currency_report.common.log import logger

postgresql_context_var = ContextVar('postgresql', default=None)

maker_session = sessionmaker(
    class_=AsyncSession,
    autocommit=False,
    autoflush=False,
    bind=engine
)


class Postgresql:

    @property
    def session(self) -> Optional[AsyncSession]:
        if postgresql_context_var.get() is None:
            raise DisconnectionError('session not init')
        return postgresql_context_var.get()

    @session.setter
    def session(self, s: AsyncSession):
        postgresql_context_var.set(s)


postgresql = Postgresql()


def database_rollback(func) -> callable:
    """ 提交失败回滚装饰器 """

    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            result = await func(*args, **kwargs)
            await postgresql.session.asycn_commit(last=True)
            return result
        except Exception as e:
            await postgresql.session.rollback()
            logger.exception(e)
            raise e

    return wrapper


if __name__ == '__main__':
    pass
