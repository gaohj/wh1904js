from flask import Flask,url_for,views,render_template,jsonify,request

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD']=True


@app.route('/',methods=['GET','POST'])
def hello_world():
    print(request.method) #GET
    if request.method == 'GET':
        username = request.args.get('username')
        return 'hello world %s' % username
    else:
        return '你是post过来的'


class JsonView(views.View):
    def datas(self):
        raise NotImplementedError

    def dispatch_request(self):
        return jsonify(self.datas())

#如果有几个url 想返回json数据
class ListView(JsonView):
    def datas(self):
        return {'username':'kangbazi','password':'123456'}

app.add_url_rule('/list/',endpoint='my_list',view_func=ListView.as_view('list'))






class FuView(views.View):
    def __init__(self):
        super(FuView, self).__init__()
        self.context = {
            'fu':'全家福、万能福、各种福'
        }
class RegisterView(FuView):
    def dispatch_request(self):
        return render_template('register.html',**self.context)
class LoginView(FuView):
    def dispatch_request(self):
        self.context.update({
            'username':'我们都是扛把子'
        })
        return render_template('login.html',**self.context)

class BookView(views.View):
    def dispatch_request(self):
        return {'username':'xiaowen','age':18}

app.add_url_rule('/login/',view_func=LoginView.as_view('login'))
app.add_url_rule('/book/',view_func=BookView.as_view('book'))
app.add_url_rule('/register/',view_func=RegisterView.as_view('register'))
if __name__ == '__main__':
    app.run(debug=True,port=5002)

