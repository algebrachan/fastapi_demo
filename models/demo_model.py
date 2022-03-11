from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, BigInteger, Integer, String, Date, DateTime, TIMESTAMP, Float

Base = declarative_base()
# 使用mysql需要用到model


class FurnaceList(Base):
    """[furnace_list table]

    Args:
        key 自增ID
        gmt_create 创建时间
        gmt_modified 修改时间
        furnace_id 炉台ID
        furnace_series 系列
        furnace_state 炉台状态
        running_time 运行时间
        server_ip 服务器ip

    """
    __tablename__ = 'furnace_list'
    key = Column(BigInteger, primary_key=True, autoincrement=True)
    gmt_create = Column(DateTime)
    gmt_modified = Column(DateTime)
    furnace_id = Column(Integer, nullable=False, default=0)
    furnace_series = Column(String, nullable=False, default='')
    furnace_state = Column(Integer, nullable=False, default=0)
    running_time = Column(Integer, nullable=False, default=0)
    server_ip = Column(String, nullable=False, default='')

    def setData(self, data: object, host: str):
        self.furnace_id = data.furnace_id
        self.furnace_series = data.furnace_series
        self.furnace_state = data.furnace_state
        self.server_ip = host
        if(data.running_time != None):
            self.running_time = data.running_time
