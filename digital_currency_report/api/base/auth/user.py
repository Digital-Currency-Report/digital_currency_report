from uuid import UUID

from digital_currency_report.api.base.model.base_model import BaseModel


class User(BaseModel):
    username: str
    password: str
    token: UUID


if __name__ == '__main__':
    pass
