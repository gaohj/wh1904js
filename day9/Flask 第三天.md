# Flask 第三天    

* 类视图  
  * add_url_rule  
  * 标准类视图  
  * 基于调度方法的类视图 
* ORM    
  * sqlalchemy      



## add_url_rule 

```python
from flask import Flask,url_for

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD']=True

@app.route('/')     #原来我们通过装饰器的形式将方法暴露出去   
def hello_world():
    print(url_for('tiantianquan'))
    return 'Hello World!'

def world_list():
    # print(url_for('world_list'))
    return '弱肉强食,首先胆子大,之后提升个人能力'

app.add_url_rule('/list/',endpoint='tiantianquan',view_func=world_list) 
#现在通过add_url_rule暴漏出去   


if __name__ == '__main__':
    app.run(debug=True,port=5002)

```

### endpoint   

> 如果写了endpoint  想要反转拿到 路由的名字 那么必须用endpoint指定的那个值 

```python
def world_list():
    print(url_for('tiantianquan')) #如果你写了endpoint 就不能再通过方法名获取路由
    #只能用endpoint 指定的
    return '弱肉强食,首先胆子大,之后提升个人能力'

app.add_url_rule('/list/',endpoint='tiantianquan',view_func=world_list)  
```



## 标准类视图  

* 继承于 flask.views.View
* 必须实现 dispatch_request方法 以后请求过来以后 都会执行这个方法  这个方法的返回值就想之前的视图函数一样  Response、字符串 、make_response、元祖   

```python
from flask import Flask,url_for,views,render_template,jsonify

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD']=True

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


```





### 基于调度方法的类视图 

```python
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

    
页面: 
     {% if error %}
             <p style="color: red">{{ error }}</p>
        {% endif %}

```





## 子域名  

> 一个产品 有好多模块 为了方便开发  使用蓝图  
>
> 1.url_profix  使用前缀来区分  
>
> ​	http://127.0.0.1:5000/cms/
>
>    http://127.0.0.1:5000/books/
>
> 2.subdomain 使用子域名来区分       
>
> 但是有个问题  
>
> 顶级域名  .com 
>
> 一级域名  baidu.com 
>
> 二级域名  wenku.baidu.com
>
> ip地址 不可能有子域名 （二级域名）  cms.127.0.0.1 不存在  
>
> 同样 localhost 等同于 127.0.0.1 也没有子域名   

```python
蓝本中: 
	将 url_profix 改成 subdomain
	
from flask import Blueprint

# cms_bp = Blueprint('cms',__name__,url_prefix='/cms')
cms_bp = Blueprint('cms',__name__,subdomain='cms')

@cms_bp.route('/')
def index():
    return 'cms首页'


实例中: 
 from flask import Flask
from views import books_bp,cms_bp
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SERVER_NAME'] = '91.com:5000' #需要这么配置  
app.register_blueprint(books_bp)
app.register_blueprint(cms_bp)


#如果 域名没有备案 指向  我们需要到  
C:\Windows\System32\drivers\etc 修改 hosts 文件  
    
    添加： 
    	127.0.0.1		91.com
		127.0.0.1		cms.91.com
		127.0.0.1		book.91.com
        
linux  /etc/hosts/ 
```

