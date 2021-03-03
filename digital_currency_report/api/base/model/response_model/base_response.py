from typing import Any, Type

from digital_currency_report.api.base.model.base_model import BaseModel


class BaseResponse(BaseModel):
    code: int = 200
    message: str = 'ok'
    data: Any = None


name = []


def format_response(cls: Type[BaseModel]):
    response_name = cls.__name__
    cls.__name__ += "_data"

    class NewResponse(BaseResponse):
        data: cls = None

        def __init__(self, **kwargs):
            super(NewResponse, self).__init__(**(
                kwargs
                if "code" in kwargs or "message" in kwargs else
                {"data": cls(**kwargs)}
            ))

    NewResponse.__name__ = response_name
    return NewResponse


@format_response
class BaseResponseState(BaseModel):
    state: bool = True


if __name__ == '__main__':
    pass
