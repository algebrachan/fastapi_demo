import time
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Request
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from routers.admin_router import admin_router
from utils.apscheduler import run_schd


app = FastAPI(title='大数据平台api', description='系统后端restful api')


# 跨域 CORS问题解决
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# app.include_router(base_router)
# 可以加前缀 prefix
app.include_router(admin_router, prefix="/api/admin")
run_schd()  # 定时任务


@app.get("/")
def read_root(request: Request):
    client = request.client
    return {"message": "ok", "client": client}


# 调试服务
if __name__ == '__main__':
    uvicorn.run(app='main:app', host="0.0.0.0",
                port=8050, reload=True, debug=True)
