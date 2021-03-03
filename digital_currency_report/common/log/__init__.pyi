from typing import Any, overload


class BaseLogger:
    globals: dict

    @overload
    def trace(self, __message: str, *args: Any, **kwargs: Any) -> None: ...

    @overload
    def trace(self, __message: Any) -> None: ...

    @overload
    def debug(self, __message: str, *args: Any, **kwargs: Any) -> None: ...

    @overload
    def debug(self, __message: Any) -> None: ...

    @overload
    def info(self, __message: str, *args: Any, **kwargs: Any) -> None: ...

    @overload
    def info(self, __message: Any) -> None: ...

    @overload
    def success(self, __message: str, *args: Any, **kwargs: Any) -> None: ...

    @overload
    def success(self, __message: Any) -> None: ...

    @overload
    def warning(self, __message: str, *args: Any, **kwargs: Any) -> None: ...

    @overload
    def warning(self, __message: Any) -> None: ...

    @overload
    def error(self, __message: str, *args: Any, **kwargs: Any) -> None: ...

    @overload
    def error(self, __message: Any) -> None: ...

    @overload
    def critical(self, __message: str, *args: Any, **kwargs: Any) -> None: ...

    @overload
    def critical(self, __message: Any) -> None: ...

    @overload
    def exception(self, __message: str, *args: Any, **kwargs: Any) -> None: ...

    @overload
    def exception(self, __message: Any) -> None: ...

    @overload
    def log(self, __level: str, __message: str, *args: Any, **kwargs: Any) -> None: ...

    @overload
    def globals(self) -> dict: ...

    @overload
    def add_globals(self, **kwargs) -> None: ...


logger: BaseLogger
