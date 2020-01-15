from sqlalchemy import create_engine

# 数据库的配置变量
HOSTNAME = '127.0.0.1' #数据库地址
PORT     = '3306'      #数据库端口号
DATABASE = '1904_sqlalchemy' #数据库名称
USERNAME = 'root'  #用户名
PASSWORD = '123456' #密码
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)

# 创建数据库引擎
engine = create_engine(DB_URI)

#创建连接
with engine.connect() as con:
    rs = con.execute('SELECT 1')
    print(rs.fetchone())

class Person(object):
    def __init__(self,username,password,age):
        self.username = username
        self.password = password
        self.age = age

    def run(self):
        return self.username


p=Person()
p.username = 'kangbazi'
p.password = '123456'
p.age = 18

