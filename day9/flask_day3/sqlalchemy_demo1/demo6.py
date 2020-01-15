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
    func
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
from datetime import datetime

class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String(50),nullable=False,name='my_title')
    price = Column(Float,nullable=False)
    def __str__(self):
        return "<Article(title:%s,price:%s)>" % (self.title,self.price)

# Base.metadata.drop_all() #修改字段类型等不能更新需要先把原来的 drop掉
# Base.metadata.create_all()
# import random
# for x in range(100):
#     article = Article(title='title%s'%x,price=random.randint(20,100))
#     session.add(article)
# session.commit()

#显示所有的字段
# articles = session.query(Article).all()
# for article in articles:
#     print(article)

#只显示 价格字段
# articles = session.query(Article.price).all()
# for article in articles:
#     print(article)

#聚合函数
#select count(price) from article;
# result = session.query(func.count(Article.id)).first()
# print(result)
# result = session.query(func.sum(Article.price)).first()
# print(result)

# result = session.query(func.avg(Article.price)).first()
# print(result)

# result = session.query(func.max(Article.price)).first()
# print(result)

result = session.query(func.min(Article.price)).first()
print(result)