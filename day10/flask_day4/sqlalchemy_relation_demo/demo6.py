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
    # articles = relationship('Article')

    def __repr__(self):
        return "<Users:(username:%s)>" % self.username

class Articles(Base):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    content = Column(Text,nullable=False)
    uid = Column(Integer,ForeignKey('useres.id')) #外键也是在表中多了一个字段
    author = relationship("Users",backref="article")


    def __repr__(self):
        return "<Article:(title:%s,content:%s)>" % (self.title,self.content)


# Base.metadata.drop_all()
# # Base.metadata.create_all()

# users= Users(username='kangbazi')
# articles = Articles(title="我想把草莓重在你37.2℃的土壤里",content="送快递的黄瓜送到了,送鸡蛋的还在框框的砸门")
#
# articles.author = users
# session.add(articles)
# session.commit()
user = session.query(Users).first()
session.delete(user)
session.commit()

