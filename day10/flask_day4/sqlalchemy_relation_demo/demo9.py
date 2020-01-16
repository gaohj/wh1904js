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

    def __repr__(self):
        return "<Users:(username:%s)>" % self.username

class Articles(Base):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    create_time = Column(DateTime,nullable=False,default=datetime.now)

    uid = Column(Integer,ForeignKey('useres.id')) #外键也是在表中多了一个字段
    author = relationship("Users",backref=backref("articles",lazy='dynamic'))
    __mapper_args__ = {
        'order_by':-create_time
    }

    def __repr__(self):
        return "<Article:(title:%s)>" % self.title


# Base.metadata.drop_all()
# Base.metadata.create_all()
# import time
# user =Users(username="kangbazi")
# for x in range(10):
#     article = Articles(title="title:%s" % x)
#
#     article.author = user
#     session.add(article)
#     time.sleep(1)
#     session.commit()


user = session.query(Users).first()
# print(type(user.articles))
#[<Article:(title:title:9)>, <Article:(title:title:8)>, <Article:(title:title:7)>, <Article:(title:title:6)>, <Article:(title:title:5)>, <Article:(title:title:4)>, <Article:(title:title:3)>, <Article:(title:title:2)>, <Article:(title:title:1)>, <Article:(title:title:0)>]

#SELECT articles.id AS articles_id, articles.title AS articles_title, articles.create_time AS articles_create_time, articles.uid AS articles_uid
#FROM articles
#WHERE %(param_1)s = articles.uid ORDER BY -articles.create_time
print(user.articles)
# 如果加上 lazy='dynamic'返回的是一个AppenderQuery
#如果没有 lazy=dynamic 返回的是个列表 用户写的所有的文章
#加上 lazy 获取的是一个
# article = user.articles.all()
# print(article)

print(user.articles.filter(Articles.id>5).all()) #这里就是返回的Query对象了
#[<Article:(title:title:9)>, <Article:(title:title:8)>, <Article:(title:title:7)>, <Article:(title:title:6)>, <Article:(title:title:5)>]

article = Articles(title='title50')
user.articles.append(article)  #可以继续追加数据
session.commit()
print(user.articles.filter(Articles.id>5).all())
