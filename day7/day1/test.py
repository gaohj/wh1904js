from flask import Flask
# from .views.books import books
# from .views.movies import movies
# from .views.admins import admins
from views import books,movies,admins
#创建一个实例  一个项目就是一个实例
app = Flask(__name__)
app.register_blueprint(books)
app.register_blueprint(movies)
app.register_blueprint(admins)
from flask_script import Manager
manager = Manager(app)
@app.route('/')
#写个试图函数  MTV 中的V  MVC中的 C
def index():
    return '<h1>首页</h1>'

@app.route('/admin/')
def admin():
    return '<h2>欢迎登录后台管理系统</h2>'

@app.route('/p/<string:name>/') #string是默认的 可以不用写
# name默认是string类型 除了 / 都识别
def profile(name):
    return 'hello %s' % name

@app.route('/book/<int:num>/') #要求这个num只能是数字
def book(num):
    return '您当前阅读的是第 %s本书' % num


@app.route('/movie/<uuid:nums>/') #要求这个num只能是数字
def movie(nums):
    return '您当前观看的是第%s个电影' % nums


@app.route('/addr/<path:address>/') #要求这个num只能是数字
def addr(address):
    return '您的地址是:%s' % address

#启动实例
if __name__ == "__main__":
    # app.run(host='0.0.0.0',debug=True,port=9000)
    manager.run()
    """
        python app.py  runserver -d -r -p 5005 -h 0.0.0.0 --threaded 
    
    -d 开启debug 模式 能够打印错误  
    -r reload 自动加载   
    -p 指定端口号  
    -h 指定允许访问的ip  0.0.0.0 表示允许所有的ip来访问   
    --threaded 表示多线程访问  
    """