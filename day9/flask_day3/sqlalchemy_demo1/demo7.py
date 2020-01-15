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
    or_
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
    content = Column(Text)
    def __str__(self):
        return "<Article(title:%s,price:%s)>" % (self.title,self.price)

# Base.metadata.drop_all() #修改字段类型等不能更新需要先把原来的 drop掉
# Base.metadata.create_all()
# import random
# for x in range(100):
#     article = Article(title='title%s'%x,price=random.randint(20,100),content='content%s'% random.randint(1,100))
#     session.add(article)
# session.commit()

# res = session.query(Article).filter(Article.id==1).first()
# print(res)

# res = session.query(Article).filter_by(id=1).first()
# print(res)

#ilike表示不区分大小写
# articles = session.query(Article).filter(Article.title.ilike('title%')).all()
# for article in articles:
#     print(article)

#in
# articles = session.query(Article).filter(Article.title.in_(['title20','title99'])).all()
# for article in articles:
#     print(article)
#not in
# articles = session.query(Article).filter(~Article.title.in_(['title20','title99'])).all()
# for article in articles:
#     print(article)

#not in 第二种写法
# articles = session.query(Article).filter(Article.title.notin_(['title20','title99'])).all()
# for article in articles:
#     print(article)

#and
# articles = session.query(Article).filter(Article.title=='title20',Article.content=='content76').all()
# for article in articles:
#     print(article)

articles = session.query(Article).filter(or_(Article.title=='title20',Article.content=='content20')).all()
for article in articles:
    print(article)