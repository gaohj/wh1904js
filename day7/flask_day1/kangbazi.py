from flask import Flask #导入类库

#创建一个实例

kangbazi = Flask(__name__)

@kangbazi.route('/')
def index():
    return '<h1>hello world</h1>'

@kangbazi.route('/admin/')
def admin():
    return '<h1>欢迎来到管理后台</h1>'

@kangbazi.route('/haha/')
def haha():
    return '<h1>haha</h1>'

@kangbazi.route('/haha1/')
def haha1():
    return '<h1>haha1</h1>'

@kangbazi.route('/haha3/')
def haha3():
    return '<h1>haha3</h1>'
#启动实例

if __name__ == "__main__":
    kangbazi.run()
