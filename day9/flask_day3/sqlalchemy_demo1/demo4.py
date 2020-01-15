from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Float,
    Boolean,
    DECIMAL,
    Enum,
    DateTime,
    DATE,
    Time,
    Text
)
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker # 这是个基类
# 数据库的配置变量
HOSTNAME = '127.0.0.1' #数据库地址
PORT     = '3306'      #数据库端口号
DATABASE = '1904_sqlalchemy' #数据库名称
USERNAME = 'root'  #用户名
PASSWORD = '123456' #密码
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)

# 创建数据库引擎
engine = create_engine(DB_URI)
#1创建基类
Base = declarative_base(engine)
#对数据库增删该查 都是通过一个session对象
session = sessionmaker(engine)()
import enum
class TagEnum(enum.Enum):
    nanshen = '男神'
    xueba = '学霸'
    geshen = '楼德华'

class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer,primary_key=True,autoincrement=True)
    # price_sale = Column(Float)
    # is_delete = Column(Boolean)
    price_ding = Column(DECIMAL(10,4)) #总长10位 小数点以后最多4位
    # tag = Column(Enum(TagEnum))
    # create_time1 = Column(DateTime)
    # create_time2 = Column(DATE)
    # create_time3 = Column(Time)
    title = Column(String(50),default='默认值')
    # content = Column(Text)
    # content2 = Column(LONGTEXT)

# Base.metadata.drop_all() #修改字段类型等不能更新需要先把原来的 drop掉
# Base.metadata.create_all()
from datetime import datetime
from datetime import date
from datetime import time

article = Article(price_ding=1000.456677) #规定小数点后最多只能4位
#存进去就是 1000.4567
session.add(article)
session.commit()


