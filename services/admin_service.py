from common.entity import ResponseBase, Error
from common.admin_req import ReqLogin
from config import redis_session, logger, mongo_session


def login(item: ReqLogin, res: ResponseBase):
    # denglu
    data = {'token': '', 'account': 'admin', 'type': 0}
    try:
        print(item)
        res.msg = "登录成功"
        res.data = data
        pass
    except Exception as e:
        res.error(Error.OPT_ERR)
        logger.error(e)
        pass
    return res
