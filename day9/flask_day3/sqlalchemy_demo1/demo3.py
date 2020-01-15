from sqlalchemy import create_engine,Column,Integer,String
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
#sessionmaker(engine) 这是一个类
#sessionmaker(engine)()就是对象了
class Person(Base):
    __tablename__ = 'person' #指定数据库的表名
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(50))
    age = Column(Integer)
    country = Column(String(20))

    def __str__(self):
        return "<Person(id:%d,name:%s,age:%s,country:%s)>" %(self.id,self.name,self.age,self.country)

#增
def add_data():
    p1 = Person(name='lisi',age=19,country='列支敦士登')
    p2 = Person(name='wangwu',age=20,country='china')
    p3 = Person(name='zhaoliu',age=21,country='中国')
    # session.add(p) #添加一条数据
    session.add_all([p1,p2,p3])
    session.commit()

#查

def search_data():
    # all_person = session.query(Person).all()
    # for p in all_person:
    #     print(p) 查询所有的数据
    # person = session.query(Person).first() #查询第一条数据
    # print(person)
    #根据条件查询
    # all_persion = session.query(Person).filter_by(name='wangwu').all()
    # for p in all_persion:
    #     print(p)

    all_persion = session.query(Person).filter(Person.id > 1).all()
    for p in all_persion:
        print(p)

#删 更改删除 首先应该先查出来
def delete_data():
    person = session.query(Person).first()
    session.delete(person)
    session.commit()

#改
def update_data():
    person = session.query(Person).first()
    person.name = '666888'
    session.commit()


if __name__ == "__main__":
    # add_data()
    # search_data()
    # update_data()
    delete_data()