# fastapi_demo
python fastapi框架 demo工程



## 1.文件目录说明

```shell
├─common # 请求响应文件
├─models # mysql数据库 数据模型文件
├─routers # 路由文件 匹配post、get请求
├─services # 服务文件 具体业务逻辑代码
└─utils # 工具库文件，封装一些工具或者中间件文件

config.ini # 配置文件
config.py # 初始化配置 代码初始化 redis、数据库、日志管理等服务
delcache.py # 快速清理缓存脚本
main.py # 工程入口文件
requirements.txt # 包版本管理文件

```



## 2.预处理

- [安装虚拟环境](https://gitee.com/mathchan/zvision-work/blob/master/2020-11/python.md)
- install 模块使用类似于js中 package.json这种类型的配置文件

```shell
# 启动虚拟环境
# 在安装包的时候 使用如下 形式安装
pip install fastapi[all] 
pip freeze > requirements.txt 
# 当 clone一个项目的时候 只需安装 配置文件中的包
pip install -r requirements.txt 
```

- 运行

```shell
uvicorn main:app --reload
uvicorn main:app --host '0.0.0.0' --port 8050 --reload --workers 2
# 退出
ctrl+C
```

- 测试
  - 测试案例

 ```python
 from fastapi.testclient import TestClient
 from main import app
 
 client = TestClient(app)
 def test_base():
 response = client.get("/base")
 assert response.status_code == 200
 ```

- 运行测试代码

 ```shell
 pip install pytest
 pytest
 ```

- 打印日志

  logging引入

- 清除缓存

  ```shell
  py delcache.py
  ```



### 3.相关链接

- [fastapi](https://fastapi.tiangolo.com/)
- [sqlalchemy](https://www.jianshu.com/p/65903a69d61d)

