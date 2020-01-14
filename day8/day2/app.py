from flask import Flask,url_for,redirect,request


app = Flask(__name__)

@app.route('/')
def index():
    print(url_for('articles',id=10))
    #/article/10/
    return '首页'

#http://127.0.0.1:5001/article/10/
@app.route('/article/<int:id>/')
def articles(id):
    return '第%s篇文章' % id


#http://127.0.0.1:5001/login/?username=qianghua&password=123456

@app.route('/profile/',methods=['GET','POST'])
def profile():#想查看个人中心必须先登录
    name = request.args.get('username')#接收前端提交过来的参数
    # print(name)
    if not name: #如果没有传递username参数 那么跳到登录页面
        #http://127.0.0.1:5001/ 跳到登录页
        return redirect(url_for('logins'))
    else:
        #http://127.0.0.1:5001/profile/?username=haha 跳到个人中心
        return '欢迎来到个人中心'


@app.route('/login/',methods=['GET'])
def logins():
    return '欢迎登录'




# if __name__ == "__main__":
#     app.run()