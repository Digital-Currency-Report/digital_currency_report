from contextvars import ContextVar
from typing import Optional

from digital_currency_report.api.base.auth.user import User
from digital_currency_report.api.base.model.response_model.base_error import AccessTokenExpire

user_context_var = ContextVar('user', default=None)


class Auth:

    @property
    def user(self) -> Optional[User]:
        if user_context_var.get() is None:
            raise AccessTokenExpire()
        return user_context_var.get()

    def get_user(self, default=None):
        return user_context_var.get() or default

    @user.setter
    def user(self, u: User):
        user_context_var.set(u)


auth = Auth()

if __name__ == '__main__':
    pass
