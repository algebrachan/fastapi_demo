from enum import Enum, unique
from pydantic import BaseModel


@unique
class Error(Enum):
    UNKNOWN = -1
    SUCCESS = 0
    NO_DATA = 1
    TOKEN_OT = 2
    OPT_ERR = 3
    SERVER_EXCEPTION = 4
    NO_AUTH = 5
    PARAM_ERR = 6


dict_error = {
    'UNKNOWN': '未知错误',
    'SUCCESS': '请求成功',
    'NO_DATA': '没有数据',
    'TOKEN_OT': 'token过期',
    'OPT_ERR': '操作异常',
    'SERVER_EXCEPTION': '服务器异常',
    'NO_AUTH': '没有权限',
    'PARAM_ERR': '参数错误'
}

# 统一响应对象 ResponseBase


class ResponseBase(BaseModel):
    code: int = 0
    msg: str = "请求成功"
    data: dict = {}

    def error(self, err_code: Error, err_msg: str = ''):
        self.code = err_code.value
        self.msg = f'{dict_error[err_code.name]} {err_msg}'
        self.data = False
        # error枚举类

    def succ(self):
        self.code = 0
        self.msg = "操作成功"
        self.data = True

# 校验 ip地址


def valid_ip(ip: str):
    try:
        l = ip.split('.')
        if(len(l) != 4):
            return False
        first = int(l[0])
        second = int(l[1])
        third = int(l[2])
        forth = int(l[3])
        if(first < 0 or first > 255 or second < 0 or second > 255 or third < 0 or third > 255 or forth < 0 or forth > 255):
            return False
    except Exception as e:
        return False
    return True
