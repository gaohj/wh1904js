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
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True,autoincrement=True)
    username = Column(String(50),nullable=False)
    # articles = relationship('Article')
    extend = relationship("UsersExtend",uselist=False)
    def __repr__(self):
        return "<Users:(username:%s)>" % self.username

class UsersExtend(Base):
    __tablename__ = 'user_extend'
    id = Column(Integer, primary_key=True, autoincrement=True)
    cardid = Column(String(18), nullable=False)
    uid = Column(Integer,ForeignKey('user.id'))

    user = relationship("Users",backref="extends")
    def __repr__(self):
        return "<UsersExtend:(cardid:%s)>" % self.cardid

class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    content = Column(Text,nullable=False)
    uid = Column(Integer,ForeignKey('user.id')) #外键也是在表中多了一个字段
    author = relationship("Users",backref="articles")


    def __repr__(self):
        return "<Article:(title:%s,content:%s)>" % (self.title,self.content)


# Base.metadata.drop_all()
# Base.metadata.create_all()

# users = Users(username='扛把子666') #先创建用户对象
# extends = UsersExtend(cardid='123456789111131516')
# users.extend = extends   #给用户对象的 extend属性 赋值
#
# session.add(users)
# session.commit()

# user = session.query(Users).first()  查用户的 身份证号
# print(user.extends)

user = session.query(Users).first()  #查用户的 身份证号
print(user.extend)

#身份证号对应的用户

# userextends = session.query(UsersExtend).first()
# print(userextends.user)