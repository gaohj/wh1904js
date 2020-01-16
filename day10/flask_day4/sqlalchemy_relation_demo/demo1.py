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

class Users(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True,autoincrement=True)
    username = Column(String(50),nullable=False)

    def __repr__(self):
        return "<Users:(username:%s)>" % self.username


class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    content = Column(Text,nullable=False)
    uid = Column(Integer,ForeignKey('user.id')) #外键也是在表中多了一个字段

    def __repr__(self):
        return "<Article:(title:%s,content:%s)>" % (self.title,self.content)

#
# Base.metadata.drop_all()
# Base.metadata.create_all()

#添加用户
# user = Users(username='kangbazi')
# session.add(user)
# session.commit()

#添加文章
# article = Article(title='钢铁是怎么炼成的,问问西门官人',content="这个棍子掉的很是时候",uid=1)
# session.add(article)
# session.commit()


#查找文章  只有外键 想查找文章是谁写的   先拿到外键 然后根据外键去查找 用户的信息

article = session.query(Article).first()
uid = article.uid


# user = session.query(Users).filter_by(id=uid).first()
user = session.query(Users).get(uid)
print(user)

# session.delete(user) #删除用户

