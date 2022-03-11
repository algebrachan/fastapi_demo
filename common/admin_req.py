from pydantic import BaseModel
from typing import Optional

# 对post请求参数进行过滤


class ReqLogin(BaseModel):
    """登录"""
    username: str
    password: str
    token: str = ''
    server: str = ''  # 赋值为不需要必填
