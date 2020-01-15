from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base
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
#create table person(id int(11) primary key auto_increment not null,username varchar(64) not null,password varchar(64) not null)
#declarative_base 根据 引擎 创建一个基类
#我们要写模型  必须继承于 sqlalchemy提供的 基类
#2 创建模型
class Person(Base):
    __tablename__ = 'person' #指定数据库的表名
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(50))
    age = Column(Integer)
    country = Column(String(20))

#将模型映射到数据库中

Base.metadata.create_all()


