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
    ForeignKey,
    Table
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
    def __repr__(self):
        return "<Users:(username:%s)>" % self.username


class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    content = Column(Text,nullable=False)
    uid = Column(Integer,ForeignKey("useres.id"),nullable=False)


    author = relationship("Users",backref=backref("articles",cascade="all"),cascade="save-update",single_parent=True)

    def __repr__(self):
        return "<Article:(title:%s,content:%s)>" % (self.title,self.content)


class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(Text, nullable=False)
    uid =  Column(Integer,ForeignKey("useres.id"))
    author = relationship("Users",backref="comments")
    def __repr__(self):
        return "<Comment:(content:%s)>" % self.content


# Base.metadata.drop_all()
# Base.metadata.create_all()

def init_db():
    user = Users(username='kangbazi')
    article = Article(title="没有金刚钻别揽瓷器活",content="持之以恒练习俯卧撑")
    article.author = user


    comment = Comment(content="赵忠祥是多少中老年妇女的偶像")
    comment.author = user

    session.add_all([article,comment])
    session.commit()

def operation():
    # user = Users(username='yangyang')
    # session.add(user)
    user = session.query(Users).get(1)
    # session.expunge(user)
    session.delete(user)
    session.commit()

if __name__ == "__main__":
    # init_db()
    operation()