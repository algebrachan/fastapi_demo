import configparser
from datetime import datetime
import os
import platform
from utils.redis import Operation_Redis
from utils.mysql import Operation_Mysql
from utils.mongodb import Operation_Mongo
from utils.log import Logger

CONFIG_PATH = os.path.join(os.path.dirname(__file__), 'config.ini')
config = configparser.ConfigParser()
config.read(CONFIG_PATH, encoding="utf-8")
sections = config.sections()

mongo_session = object
# mysql_session = object
redis_session = object
logger = object

if 'mongodb' in sections:
    mongo_session = Operation_Mongo(
        usr=config.get('mongodb', 'usr'),
        passwd=config.get('mongodb', 'pwd'),
        host=config.get('mongodb', 'host'),
        port=config.getint('mongodb', 'port'),
        db=config.get('mongodb', 'db'),
    )
else:
    mongo_session = Operation_Mongo()

if 'mysql' in sections:
    mysql_session = Operation_Mysql(
        usr=config.get('mysql', 'usr'),
        pwd=config.get('mysql', 'pwd'),
        host=config.get('mysql', 'host'),
        port=config.getint('mysql', 'port'),
        db=config.get('mysql', 'db'),
    )
else:
    mysql_session = Operation_Mysql()

if 'redis' in sections:
    redis_session = Operation_Redis(
        host=config.get('redis', 'host'),
        port=config.getint('redis', 'port'),
        db=config.getint('redis', 'db'),
    )
else:
    redis_session = Operation_Redis()

log_path = ''
if(platform.system() == 'Windows'):
    log_path = 'D:\\log\\fastapi_log\\'
elif(platform.system() == 'Linux'):
    log_path = '../log/fastapi_log/'
    # log_path = '~/project/log/fastapi_log/'
else:
    pass
os.makedirs(log_path, exist_ok=True)
# os.makedirs(os.path.expanduser(log_path),exist_ok=True)

if 'log' in sections:
    logger = Logger(
        log_path+config.get('log', 'filename'),
        level=config.get('log', 'level'),
        when=config.get('log', 'when'),
        interval=config.getint('log', 'interval'),
        backCount=config.getint('log', 'backCount'),
    ).logger
else:
    logger = Logger(log_path+'server.log', when='midnight').logger

# 配置mongodb数据库的初始数据


def set_init_account(username, password, type):
    mongo_dict = mongo_session.select_one_collection(
        'user_info', {'username': username})
    if mongo_dict == None:
        mongo_dict = {}
    mongo_dict['update'] = datetime.now()
    mongo_dict['username'] = username
    mongo_dict['password'] = password
    mongo_dict['server_ip'] = ''
    mongo_dict['type'] = type  # 0 超级管理员 4 web后台管理
    mongo_dict['login_time'] = datetime.now()
    mongo_dict['state'] = 1  # 0 不可用 1 可用
    mongo_session.save_collection('user_info', mongo_dict)
    pass


# 设置 tjsemi 账户
set_init_account('tjsemi', 'tjsemi', 4)


if __name__ == '__main__':
    pass
