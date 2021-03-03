from time import time

from fastapi import Request
from starlette.responses import Response

from digital_currency_report.api.base.app import app
from digital_currency_report.api.base.exceptions import exception_handler
from digital_currency_report.common.database.postgresql import postgresql, maker_session
from digital_currency_report.common.log import logger
from digital_currency_report.common.redis import redis


@app.on_event("startup")
async def startup():
    await redis.init()


@app.on_event("shutdown")
async def shutdown():
    # 关闭 redis
    redis.client.close()
    await redis.client.wait_closed()


@app.middleware("http")
async def close_session(request: Request, call_next):
    # 记录请求时间
    before = time()
    # 添加日志 traceId 跟踪
    if Ts_Request_Id := request.headers.get('Ts-Request-Id'):
        logger.add_globals(Ts_Request_Id=Ts_Request_Id)

    async with maker_session() as session:
        postgresql.session = session
        # 序列化异常
        try:
            response: Response = await call_next(request)
        except Exception as e:
            response: Response = await exception_handler(request, e)

    response.headers["X-Response-Time"] = str(time() - before)
    return response
