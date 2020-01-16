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
    username = Column(String(50), nullable=False)
    city = Column(String(50),nullable=False)
    age = Column(Integer,default=0)
    gender = Column(Enum('male','female','secret'),default='male')
    def __repr__(self):
        return "<Users:(username:%s)>" % self.username
# Base.metadata.drop_all()
# Base.metadata.create_all()

# user1 = Users(username='苍老师',age=30,city='东京',gender='female')
# user2 = Users(username='波多老师',age=35,city='京都',gender='male')
# user3 = Users(username='加老师',age=35,city='大阪',gender='female')
# user4 = Users(username='吉老师',age=25,city='名古屋',gender='male')
# user5 = Users(username='龙老师',age=30,city='京都',gender='female')
# #
# session.add_all([user1,user2,user3,user4,user5])
# session.commit()

#查找跟 波多老师 在同一个城市 并且 年龄一样的人
# users = session.query(Users).filter(Users.username=='波多老师').first()
# res = session.query(Users).filter(Users.city==users.city,Users.age==users.age).all()
# print(res)

#select username as '用户名'
dstmt = session.query(Users.city.label("城市"),Users.age.label("年龄")).filter(Users.username=='波多老师').subquery()
result = session.query(Users).filter(Users.city==dstmt.c.城市,Users.age==dstmt.c.年龄).all()
print(result)