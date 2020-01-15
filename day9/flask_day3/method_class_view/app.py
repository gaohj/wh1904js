from flask import Flask,request,views,render_template

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/',methods=['GET','POST'])
def hello_world():
    if request.method == 'GET':
        return 'Hello World!'
    else:
        return '你是post过来的'


class LoginView(views.MethodView):
    def __render(self,error=None):
        return render_template('login.html',error=error)
    #实现登录需求 先展示页面
    #提交数据到后台
    def get(self): #展示界面的
        return self.__render()
    def post(self): #提交数据到后台的
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'kangbazi' and password == '123456':
            return '登录成功'
        else:
            return self.__render(error='用户名或者密码错误')

    # def put(self):
    #     return '你是put过来的'
    # def patch(self):
    #     return '你是patch过来的'
    # def delete(self):
    #     return '你是delete过来的'
app.add_url_rule('/login/',view_func=LoginView.as_view('login'),endpoint='signin')


if __name__ == '__main__':
    app.run(debug=True,port=5002)
