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
    Text,
    func,
    or_,
    ForeignKey
)
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship,backref # 这是个基类
from datetime import datetime
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

class Users(Base):
    __tablename__ = 'useres'
    id = Column(Integer,primary_key=True,autoincrement=True)
    username = Column(String(50),nullable=False)
    age = Column(Integer,default=0)
    gender = Column(Enum('male','female','secret'),default='male')
    def __repr__(self):
        return "<Users:(username:%s)>" % self.username
# Base.metadata.drop_all()
# Base.metadata.create_all()

user1 = Users(username='苍老师',age=30,gender='female')
user2 = Users(username='波多老师',age=35,gender='female')
user3 = Users(username='加老师',age=35,gender='male')
user4 = Users(username='吉老师',age=25,gender='female')
user5 = Users(username='龙老师',age=30,gender='female')

# session.add_all([user1,user2,user3,user4,user5])
# session.commit()
# result = session.query(Users.age,func.count(Users.id)).group_by(Users.age).all()
# print(result)#[(25, 1), (30, 2), (35, 2)]

result = session.query(Users.age,func.count(Users.id)).group_by(Users.age).having(Users.age>25).all()
print(result)#[(30, 2), (35, 2)]

