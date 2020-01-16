## Ubuntu连接数据库报 2003 10061  错误 

```shell
sudo vim /etc/mysql/mysql.conf.d/mysqld.cnf  

bind-address = 127.0.0.1 #将它注释或者改成 0.0.0.0 

service mysql restart #重启mysql服务  




mysql -u root -p  

use mysql;  #每个数据安装成功以后 都有自己的mysql 数据库   这里边存放响应的 权限等   

grant 权限  on 库名.表名 to '用户名'@'地址' identified by '密码' with grant option;


1 权限  可以写成 insert,select,update,delete 多个权限  用,隔开   all 代表所有的权限  
2 库名  数据库名 *代表所有数据库的名字  
3 地址  % 代表所有的地址都可以访问   


grant insert,select on test.test to 'qianghua'@'%' identified by '123321' with grant option;   #新建一个用户qianhua 密码123456 可以从任何主机访问数据库服务器 但是只能对 test数据库 test数据表 拥有 插入 和 选择的权限   

flush privileges; #别忘了 更新权限   

revoke 权限名字 on 库名.表名 from '用户名'@'主机地址';
revoke insert on test.test from 'qianghua'@'%'; #删除权限   
#删除qianghua 对 test数据库 test数据表的插入权限   



grant all on *.* to 'root'@'%' identified by '你的密码' with grant option;
flush privileges; #别忘了 更新权限

```





# SQLAlchemy介绍和基本使用

数据库是一个网站的基础。`Flask`可以使用很多种数据库。比如`MySQL`，`MongoDB`,`SQLite`,`PostgreSQL`等。这里我们以`MySQL`为例进行讲解。而在`Flask`中，如果想要操作数据库，我们可以使用`ORM`来操作数据库，使用`ORM`操作数据库将变得非常简单。

在讲解`Flask`中的数据库操作之前，先确保你已经安装了以下软件：

- `mysql`：如果是在`windows`上，到[官网](http://dev.mysql.com/downloads/windows/)下载。如果是`ubuntu`，通过命令`sudo apt-get install mysql-server libmysqlclient-dev -yq`进行下载安装。
- `MySQLdb`：`MySQLdb`是用`Python`来操作`mysql`的包，因此通过`pip`来安装，命令如下：`pip install mysql-python`。
- `pymysql`：`pymysql`是用`Python`来操作`mysql`的包，因此通过`pip`来安装，命令如下：`pip3 install pymysql`。如果您用的是`Python 3`，请安装`pymysql`。
- `SQLAlchemy`：`SQLAlchemy`是一个数据库的`ORM`框架，我们在后面会用到。安装命令为：`pip3 install SQLAlchemy`。

### 通过`SQLAlchemy`连接数据库：

首先来看一段代码：

```python
from sqlalchemy import create_engine

# 数据库的配置变量
HOSTNAME = '127.0.0.1'
PORT     = '3306'
DATABASE = 'xt_flask'
USERNAME = 'root'
PASSWORD = 'root'
DB_URI = 'mysql+mysqldb://{}:{}@{}:{}/{}'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)

# 创建数据库引擎
engine = create_engine(DB_URI)

#创建连接
with engine.connect() as con:
    rs = con.execute('SELECT 1')
    print rs.fetchone()
```

首先从`sqlalchemy`中导入`create_engine`，用这个函数来创建引擎，然后用`engine.connect()`来连接数据库。其中一个比较重要的一点是，通过`create_engine`函数的时候，需要传递一个满足某种格式的字符串，对这个字符串的格式来进行解释：

```
dialect+driver://username:password@host:port/database?charset=utf8
```

`dialect`是数据库的实现，比如`MySQL`、`PostgreSQL`、`SQLite`，并且转换成小写。`driver`是`Python`对应的驱动，如果不指定，会选择默认的驱动，比如MySQL的默认驱动是`MySQLdb`。`username`是连接数据库的用户名，`password`是连接数据库的密码，`host`是连接数据库的域名，`port`是数据库监听的端口号，`database`是连接哪个数据库的名字。

如果以上输出了`1`，说明`SQLAlchemy`能成功连接到数据库。

### 用SQLAlchemy执行原生SQL：

我们将上一个例子中的数据库配置选项单独放在一个`constants.py`的文件中，看以下例子：

```python
from sqlalchemy import create_engine
from constants import DB_URI

#连接数据库
engine = create_engine(DB_URI,echo=True)

# 使用with语句连接数据库，如果发生异常会被捕获
with engine.connect() as con:
    # 先删除users表
    con.execute('drop table if exists authors')
    # 创建一个users表，有自增长的id和name
    con.execute('create table authors(id int primary key auto_increment,'name varchar(25))')
    # 插入两条数据到表中
    con.execute('insert into persons(name) values("abc")')
    con.execute('insert into persons(name) values("xiaotuo")')
    # 执行查询操作
    results = con.execute('select * from persons')
    # 从查找的结果中遍历
    for result in results:
        print(result)
```

# SQLAlchemy

### 使用SQLAlchemy：

要使用`ORM`来操作数据库，首先需要创建一个类来与对应的表进行映射。现在以`User表`来做为例子，它有`自增长的id`、`name`、`fullname`、`password`这些字段，那么对应的类为：

```python
    from sqlalchemy import Column,Integer,String
    from constants import DB_URI
    from sqlalchemy import create_engine
    from sqlalchemy.ext.declarative import declarative_base

    engine = create_engine(DB_URI,echo=True)

    # 所有的类都要继承自`declarative_base`这个函数生成的基类
    Base = declarative_base(engine)
    class User(Base):
        # 定义表名为users
        __tablename__ = 'users'

        # 将id设置为主键，并且默认是自增长的
        id = Column(Integer,primary_key=True)
        # name字段，字符类型，最大的长度是50个字符
        name = Column(String(50))
        fullname = Column(String(50))
        password = Column(String(100))

        # 让打印出来的数据更好看，可选的
        def __repr__(self):
            return "<User(id='%s',name='%s',fullname='%s',password='%s')>" % (self.id,self.name,self.fullname,self.password)
```

`SQLAlchemy`会自动的设置第一个`Integer`的主键并且没有被标记为外键的字段添加自增长的属性。因此以上例子中`id`自动的变成自增长的。以上创建完和表映射的类后，还没有真正的映射到数据库当中，执行以下代码将类映射到数据库中：

```python
Base.metadata.create_all()
```

在创建完数据表，并且做完和数据库的映射后，接下来让我们添加数据进去：

```python
ed_user = User(name='ed',fullname='Ed Jones',password='edspassword')
# 打印名字
print ed_user.name
> ed
# 打印密码
print ed_user.password
> edspassword
# 打印id
print ed_user.id
> None
```

可以看到，name和password都能正常的打印，唯独`id`为`None`，这是因为`id`是一个自增长的主键，还未插入到数据库中，`id`是不存在的。接下来让我们把创建的数据插入到数据库中。和数据库打交道的，是一个叫做`Session`的对象：

```python
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
# 或者
# Session = sessionmaker()
# Session.configure(bind=engine)
session = Session()
ed_user = User(name='ed',fullname='Ed Jones',password='edspassword')
session.add(ed_user)
```

现在只是把数据添加到`session`中，但是并没有真正的把数据存储到数据库中。如果需要把数据存储到数据库中，还要做一次`commit`操作：

```python
session.commit()
# 打印ed_user的id
print ed_user.id
> 1
```

# SQLAlchemy的ORM

### Column常用参数：

- `default`：默认值。
- `nullable`：是否可空。
- `primary_key`：是否为主键。
- `unique`：是否唯一。
- `autoincrement`：是否自动增长。
- `onupdate`：更新的时候执行的函数。
- `name`：该属性在数据库中的字段映射。

### sqlalchemy常用数据类型：

- `Integer`：整形。
- `Float`：浮点类型。
- `Boolean`：传递`True/False`进去。
- `DECIMAL`：定点类型。
- `enum`：枚举类型。
- `Date`：传递`datetime.date()`进去。
- `DateTime`：传递`datetime.datetime()`进去。
- `Time`：传递`datetime.time()`进去。
- `String`：字符类型，使用时需要指定长度，区别于`Text`类型。
- `Text`：文本类型。
- `LONGTEXT`：长文本类型。

### query可用参数：

1. 模型对象。指定查找这个模型中所有的对象。
2. 模型中的属性。可以指定只查找某个模型的其中几个属性。
3. from sqlalchemy import func 
4. 聚合函数。
   - `func.count`：统计行的数量。



   - `func.avg`：求平均值。
   - `func.max`：求最大值。
   - `func.min`：求最小值。
   - `func.sum`：求和。

   ```python
   	result = session.query(func.count(Persons.id)).first()
       result = session.query(func.avg(Persons.id)).first()
       result = session.query(func.max(Persons.id)).first()
       result = session.query(func.min(Persons.id)).first()
       result = session.query(func.sum(Persons.id)).first()
   ```


### 过滤条件：

过滤是数据提取的一个很重要的功能，以下对一些常用的过滤条件进行解释，并且这些过滤条件都是只能通过`filter`方法实现的：

1. `equals`：

   ```python
   query.filter(User.name == 'ed')
   ```

2. `not equals`:

   ```python
   query.filter(User.name != 'ed')
   ```

3. `like`：

   ```python
   query.filter(User.name.like('%ed%'))
   ```

4. `in`：

   ```python
   query.filter(User.name.in_(['ed','wendy','jack']))
   # 同时，in也可以作用于一个Query
   query.filter(User.name.in_(session.query(User.name).filter(User.name.like('%ed%'))))
   ```

5. `not in`：

   ```python
   query.filter(~User.name.in_(['ed','wendy','jack']))
   ```

6. `is null`：

   ```python
   query.filter(User.name==None)
   # 或者是
   query.filter(User.name.is_(None))
   ```

7. `is not null`:

   ```python
   query.filter(User.name != None)
   # 或者是
   query.filter(User.name.isnot(None))
   ```

8. `and`：

   ```python
   from sqlalchemy import and_
   query.filter(and_(User.name=='ed',User.fullname=='Ed Jones'))
   # 或者是传递多个参数
   query.filter(User.name=='ed',User.fullname=='Ed Jones')
   # 或者是通过多次filter操作
   query.filter(User.name=='ed').filter(User.fullname=='Ed Jones')
   ```

9. `or`：

   ```python
   from sqlalchemy import or_  query.filter(or_(User.name=='ed',User.name=='wendy'))
   ```







# Flask-SQLAlchemy插件

另外一个框架，叫做`Flask-SQLAlchemy`，`Flask-SQLAlchemy`是对`SQLAlchemy`进行了一个简单的封装，使得我们在`flask`中使用`sqlalchemy`更加的简单。可以通过`pip install flask-sqlalchemy`。使用`Flask-SQLAlchemy`的流程如下：

- 数据库初始化：数据库初始化不再是通过`create_engine`，请看以下示例：

  ```python
  from flask import Flask
  from flask_sqlalchemy import SQLAlchemy
  from constants import DB_URI
  app = Flask(__name__)
  app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
  db = SQLAlchemy(app)
  ```

- `ORM`类：之前都是通过`Base = declarative_base()`来初始化一个基类，然后再继承，在`Flask-SQLAlchemy`中更加简单了（代码依赖以上示例）：

  ```python
  class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(80),unique=True)
    email = db.Column(db.String(120),unique=True)
    def __init__(self,username,email):
        self.username = username
        self.email = email
    def __repr__(self):
        return '<User %s>' % self.username
  ```

- 映射模型到数据库表：使用`Flask-SQLAlchemy`所有的类都是继承自`db.Model`，并且所有的`Column`和数据类型也都成为`db`的一个属性。但是有个好处是不用写表名了，`Flask-SQLAlchemy`会自动将类名小写化，然后映射成表名。
  写完类模型后，要将模型映射到数据库的表中，使用以下代码创建所有的表：

  ```python
  db.create_all()
  ```

- 添加数据：这时候就可以在数据库中看到已经生成了一个`user`表了。接下来添加数据到表中：

  ```python
  admin = User('admin','admin@example.com')
  guest = User('guest','guest@example.com')
  db.session.add(admin)
  db.session.add(guest)
  db.session.commit()
  ```

  添加数据和之前的没有区别，只是`session`成为了一个`db`的属性。

- 查询数据：查询数据不再是之前的`session.query`了，而是将`query`属性放在了`db.Model`上，所以查询就是通过`Model.query`的方式进行查询了：

  ```python
  users = User.query.all()
  # 再如：
  admin = User.query.filter_by(username='admin').first()
  # 或者：
  admin = User.query.filter(User.username='admin').first()
  ```

- 删除数据：删除数据跟添加数据类似，只不过`session`是`db`的一个属性而已：

  ```python
  db.session.delete(admin)
  db.session.commit()
  ```

# Flask-Migrate

在实际的开发环境中，经常会发生数据库修改的行为。一般我们修改数据库不会直接手动的去修改，而是去修改`ORM`对应的模型，然后再把模型映射到数据库中。这时候如果有一个工具能专门做这种事情，就显得非常有用了，而`flask-migrate`就是做这个事情的。`flask-migrate`是基于`Alembic`进行的一个封装，并集成到`Flask`中，而所有的迁移操作其实都是`Alembic`做的，他能跟踪模型的变化，并将变化映射到数据库中。

使用`Flask-Migrate`需要安装，命令如下：

```python
pip install flask-migrate
```

要让`Flask-Migrate`能够管理`app`中的数据库，需要使用`Migrate(app,db)`来绑定`app`和数据库。假如现在有以下`app`文件：

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from constants import DB_URI
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
# 绑定app和数据库
migrate = Migrate(app,db)

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20))

    addresses = db.relationship('Address',backref='user')

class Address(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    email_address = db.Column(db.String(50))
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))

db.create_all()

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
```

之后，就可以在命令行中映射`ORM`了。要操作当前的`flask app`，首先需要将当前的`app`导入到环境变量中：

```shell
# windows
$env:FLASK_APP='your_app.py'

#linux/unix
export FLASK_APP='your_app.py'
```

将当前的`app`导入到环境变量中后，接下来就是需要初始化一个迁移文件夹：

```shell
    flask db init 第一次需要执行 
```

然后再把当前的模型添加到迁移文件中：

```shell
    flask db migrate
```

最后再把迁移文件中对应的数据库操作，真正的映射到数据库中：

```shell
    flask db upgrade
```

