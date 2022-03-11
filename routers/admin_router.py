from fastapi import APIRouter, Request
from services.admin_service import *

admin_router = APIRouter()


@admin_router.post('/login', summary="登录")
async def user_login(item: ReqLogin, request: Request):
    print(request.client)
    return login(item, res=ResponseBase())
