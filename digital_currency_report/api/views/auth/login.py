from uuid import UUID, uuid4

from fastapi import Response

from digital_currency_report.api.base.auth.auth import auth
from digital_currency_report.api.base.auth.user import User
from digital_currency_report.api.base.model.base_model import BaseModel
from digital_currency_report.api.base.model.response_model.base_response import format_response
from digital_currency_report.api.base.router import auth_router
from digital_currency_report.common.redis import redis
from digital_currency_report.config import config


class LoginRequest(BaseModel):
    username: str
    password: str


@format_response
class LoginResponse(BaseModel):
    token: UUID
    time: int = config.ACCESS_TOKEN_EXPIRE


@auth_router.post("/login",
                  summary="用户登录",
                  response_description="登录成功",
                  response_model=LoginResponse)
async def login(request: LoginRequest, response: Response):
    auth.user = User(username=request.username, password=request.password, token=uuid4())
    # token 写入 redis
    await redis.client.set(
        f'{config.PROJECT_NAME}_token:{auth.user.token}',
        auth.user.json(),
        expire=config.ACCESS_TOKEN_EXPIRE
    )
    # 设置 cookies
    response.set_cookie("token", str(auth.user.token), expires=config.ACCESS_TOKEN_EXPIRE)
    response.set_cookie("username", auth.user.username, expires=config.ACCESS_TOKEN_EXPIRE)
    return LoginResponse(
        token=auth.user.token,
        time=config.ACCESS_TOKEN_EXPIRE
    )
