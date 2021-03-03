from contextvars import ContextVar
from functools import singledispatch
from typing import Any

import loguru

from digital_currency_report.api.base.model.base_model import BaseModel
from digital_currency_report.common.json import dumps

logger_context_var = ContextVar('logger', default=None)
logger_globals_context_var = ContextVar('logger', default=dict())


@singledispatch
def log_args_default(obj):
    return str(obj)


@log_args_default.register(dict)
@log_args_default.register(list)
@log_args_default.register(tuple)
def obj_to_decode(obj: Any):
    return dumps(obj)


@log_args_default.register(BaseModel)
def obj_to_decode(obj: BaseModel):
    return obj.json()


class BaseLogger:

    @property
    def globals(self) -> dict:
        return logger_globals_context_var.get()

    @staticmethod
    def add_globals(**kwargs) -> None:
        logger_globals_context_var.set({**logger_globals_context_var.get(), **kwargs})

    def log(self, __level: str, __message: str, *args: Any, **kwargs: Any) -> None:
        if __message:
            if not isinstance(__message, str):
                __message = str(__message)
            for key, value in self.globals.items():
                __message += f" {key}={log_args_default(value)}"
            return loguru.logger.log(__level, __message, *args, **kwargs)

    def exception(self, __message: str, *args: Any, **kwargs: Any) -> None:
        if __message:
            if not isinstance(__message, str):
                __message = str(__message)
            for key, value in self.globals.items():
                __message += f" {key}={log_args_default(value)}"
            return loguru.logger.exception(__message, *args, **kwargs)

    def _log(self, __level: str, *args: Any, **kwargs: Any) -> None:
        return self.log(__level, *args, **kwargs)

    def __getattr__(self, item) -> callable:
        return lambda *args, **kwargs: self._log(item.upper(), *args, **kwargs)


logger = BaseLogger()
