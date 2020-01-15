from flask import Flask,url_for

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD']=True

@app.route('/')
def hello_world():
    print(url_for('tiantianquan'))
    return 'Hello World!'

def world_list():
    print(url_for('tiantianquan')) #如果你写了endpoint 就不能再通过方法名获取路由
    #只能用endpoint 指定的
    return '弱肉强食,首先胆子大,之后提升个人能力'

app.add_url_rule('/list/',endpoint='tiantianquan',view_func=world_list)


if __name__ == '__main__':
    app.run(debug=True,port=5002)
