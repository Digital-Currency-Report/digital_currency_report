from fastapi import APIRouter as Router

routers = []


class APIRouter(Router):
    def __init__(self, *args, **kwargs):
        super(APIRouter, self).__init__(*args, **kwargs)
        routers.append(self)


auth_router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)
