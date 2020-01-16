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

article_tag = Table(
    'article_tag',
    Base.metadata,
    Column('article_id',Integer,ForeignKey("article.id"),primary_key=True),
    Column('tag_id',Integer,ForeignKey("tag.id"),primary_key=True),
)



class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    content = Column(Text,nullable=False)

    def __repr__(self):
        return "<Article:(title:%s,content:%s)>" % (self.title,self.content)


class Tag(Base):
    __tablename__ = 'tag'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)

    articles = relationship("Article",backref="tags",secondary=article_tag)
    def __repr__(self):
        return "<Tag:(name:%s)>" % self.name


# Base.metadata.drop_all()
# Base.metadata.create_all()

##将两个 多对多关系的模型定义出来
## 使用Table 定义一个中间表 中间表 由两个表的  外键 字段   并且让它们两个作为一个复合主键
## 随便选一个模型  定义一个relationship 绑定他们三个之间的关系   需要传入一个secondary 作为中间表


# article1 = Article(title="钢铁是怎样炼成的",content="武功再好也怕菜刀")
# article2 = Article(title="每天晚上最喜欢看你运动为我热菜",content="热菜完了以后就为爱情鼓掌")
#
# tag1 = Tag(name="张宇老司机")
# tag2 = Tag(name="费玉清老司机")
#
# article1.tags.append(tag1) 给文章1 添加一个标签
# article1.tags.append(tag2) 给文章1 再添加一个标签
#
# article2.tags.append(tag1)给文章2 添加一个标签
# article2.tags.append(tag2)给文章1 再添加一个标签
#
# session.add_all([article1,article2])  保存文章
# session.commit()  #提交数据库


#查询
article = session.query(Article).get(2)
print(article.tags)


tags = session.query(Tag).first()
print(tags.articles)



