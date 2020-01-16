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
    author = relationship("Users",backref="article")
    __mapper_args__ = {
        'order_by':-create_time
    }

    def __repr__(self):
        return "<Article:(title:%s)>" % self.title


# Base.metadata.drop_all()
# Base.metadata.create_all()

# user1 = Users(username='兰陵笑笑生')
# user2 = Users(username='上帝也疯狂')
#
# for x in range(10):
#     article = Articles(title='title%s'%x)
#     article.author = user1
#     session.add(article)
# session.commit()
#
# for x in range(20):
#     article = Articles(title='title%s'%x)
#     article.author = user2
#     session.add(article)
# session.commit()

#所有的用户按照文章发表的数量进行排序

result = session.query(Users,func.count(Articles.id)).join(Articles).group_by(Users.id).order_by(func.count(Articles.id).desc()).all()
print(result)

#SELECT useres.username as 用户名,COUNT(articles.id) as 文章数量 FROM useres INNER JOIN articles on useres.id = articles.uid GROUP BY useres.id ORDER BY COUNT(articles.id) DESC;