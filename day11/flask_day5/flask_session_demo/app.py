from flask import Flask,session,request
import os
from datetime import timedelta
app = Flask(__name__)

app.config['SECRET_KEY'] = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)
#session.permanent = True 默认31天
#如果修改 设置PERMANENT_SESSION_LIFETIME  后面就是指定过期时间

@app.route('/')
def hello_world():
    username = request.args.get('username')
    password = request.args.get('password')
    if username == 'kangbazi' and password == '123123':
        session['username'] = 'kangbazi'
        session['user_id'] = '007'
        session.permanent = True #如果这个为True说明session的过期时间为31

        return 'hello world'
    else:
        return '请先登录'
@app.route('/get_session/')
def get_session():
    username = session.get('username')
    user_id = session.get('user_id')

    print(user_id)

    return username or '没有获取到session'


@app.route('/delete_session/')
def delete_session():
    session.pop('username')
    session.clear()
    return '删除成功'


if __name__ == '__main__':
    app.run()
