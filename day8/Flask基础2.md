# Flask基础2    

* url_for  
* http请求方法限制    
* 页面重定向    
* 响应  
* 模板   
  * 语法 
  * 过滤器  
  * 控制语句
  * include set  
  * 模板继承 
  * 静态文件配置   
* sqlalchemy  



## url_for  

> 构建一个url  在一个视图函数里获取另外的一个视图函数的路由  

```python
from flask import Flask,url_for #导入url_for 


app = Flask(__name__)

@app.route('/')
def index():
    print(url_for('articles',id=10)) #第一个参数是方法的名字 其它参数就是方法的参数 
    #/article/10/
    return '首页'

#http://127.0.0.1:5001/article/10/
@app.route('/article/<int:id>/')
def articles(id):
    return '第%s篇文章' % id


# if __name__ == "__main__":
#     app.run()
```



## 指定 http方法  

```python
@app.route('/login/',methods=['GET'])#@app.route('/login/',methods=['GET','POST','PUT'])

def login():
    return '欢迎登录'

postman测试工具
```



## 页面重定向  

> redirect   

> url中传递参数 http://127.0.0.1:5001/login/?参数名1=值1&参数名2=值2
>
> request.args.get('参数名')
>
> 状态码 3开头表示重定向    301  永久重定向   302 临时重定向  

```python
from flask import Flask,url_for,redirect,request

#request 这是一个对象  对象里边包含着前端用户所有的请求   

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

```



## 响应   

* Response对象   
* 字符串  
* 元组 
* 如果不是以上类型 那么flask也会转成  请求对象  

### Response对象

```python
from flask import Flask,url_for,Response

@app.route('/')
def index():
    resp = Response(response='千锋首页',status=500,content_type='text/html;charset=utf-8')
    return resp
```



### 使用make_response 来构建 Response对象   

> 设置cookie header头信息  

```
from flask import Flask,url_for,Response,make_response

@app.route('/hello/')
def hello_world():
    res = make_response('五福表示年到了,福字不要乱贴')
    res.headers['X-CXK'] = 'what a fucking boy'
    res.set_cookie('娃力宏','楼德华')
    return res
```

### 元祖  

```python
@app.errorhandler(404)   #之前如果找不到返回系统的错误页面  现在返回的是我们自己指定的错误页面
def not_found(error): #error对象别忘了加  
    return '您找的页面已经去火星了',500
```

## Jinja2模版概述

### 概要：

先看一个简单例子：

```html
1. <html lang="en">
2. <head>
3.    <title>My Webpage</title>
4. </head>
5. <body>
6.     <ul id="navigation">
7.     {% for item in navigation %}
8.         <li><a href="{{ item.href }}">{{ item.caption }}</a></li>
9.     {% endfor %}
10.    </ul>
11.
12.    {{ a_variable }}
13.    {{ user.name }}
14.    {{ user['name'] }}
15.
16.    {# a comment #}
17. </body>
18.</html>
```

以上示例有需要进行解释：

- 第12~14行的`{{ ... }}`：用来装载一个变量，模板渲染的时候，会把这个变量代表的值替换掉。并且可以间接访问一个变量的属性或者一个字典的`key`。关于点`.`号访问和`[]`中括号访问，没有任何区别，都可以访问属性和字典的值。
- 第7~9行的`{% ... %}`：用来装载一个控制语句，以上装载的是`for`循环，以后只要是要用到控制语句的，就用`{% ... %}`。
- 第14行的`{# ... #}`：用来装载一个注释，模板渲染的时候会忽视这中间的值。

## 页面 url_for 

```python
@app.route('/login/<int:id>/',methods=['GET','POST'])
def logins(id):
    return render_template('login.html',userid=id)

页面上这么写: 
<li><a href="{{ url_for('logins',id='666') }}">立即登录</a></li>

```



## 自定义过滤器  至多有两个参数  

* 系统提供的过滤器   
* 自定义过滤器   

```python
@app.template_filter('handle_time') #handletime就是在页面上使用的名字
def handle_times(time): #之多有两个参数  不能再多了  
    if isinstance(time,datetime):
        now = datetime.now() #当前的时间
        timestamps = (now-time).total_seconds()
        if timestamps < 60:
            return '刚刚'
        elif timestamps >=60 and timestamps< 60*60:
            minutes = timestamps / 60
            return "%s分钟前" % int(minutes)
        elif timestamps >=60*60 and timestamps< 60*60*24:
            hours = timestamps / (60*60)
            return "%s小时前" % int(hours)
        elif timestamps >=60*60*24 and timestamps< 60*60*24*30:
            days = timestamps / (60*60*24)
            return "%s天前" % int(days)
        else:
            return time.strftime('%Y/%m/%d %H/%M')
    else:
        return time

    在页面上
<p>发表时间:{{ pub_time|handle_time }}</p>
```

## include 语句

> 一个页面包含另外一个页面 

```python
 {% include 'common/header.html' %}
    <div class="container">
        中间的内容
    </div>
 {% include 'common/footer.html' %}
```





## set 语句和with 语句 

> 自己在页面上设置变量  不用从后台传递过来
>
> with只能在区域里边才能用  出来之后就不能用了  

```
{#  不从后台过来 页面自己设置变量  set全局设置#}
        {% set country="china" %}
        <p>{{ country }}</p>
{#        with的话 只能在这个区域里边才行 #}
        {% with  %}
            {% set age=18 %}
            <p>{{ age }}</p>
        {% endwith %}


    <p>{{ age }}</p>
```



## 页面的继承  

```html
base.html 


<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- 上述3个meta标签*必须*放在最前面，任何其他内容都*必须*跟随其后！ -->
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="icon" href="../../favicon.ico">
    {% block headers %}{% endblock %}
    <title>{% block title %}{% endblock %}</title>

    <!-- Bootstrap core CSS -->
    <link href="https://cdn.bootcss.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet">


    <!-- Custom styles for this template -->
    <link href="https://v3.bootcss.com/examples/blog/blog.css" rel="stylesheet">

  </head>

  <body>

    <div class="blog-masthead">
      <div class="container">
        <nav class="blog-nav">
          <a class="blog-nav-item active" href="{{ url_for('hello_world') }}">首页</a>
          <a class="blog-nav-item" href="{{ url_for('details') }}">详情页</a>
          <a class="blog-nav-item" href="#">Press</a>
          <a class="blog-nav-item" href="#">New hires</a>
          <a class="blog-nav-item" href="#">About</a>
        </nav>
      </div>
    </div>

    <div class="container">
        {% block content %}
           <div style="background: yellow;color: rebeccapurple;width: 200px;height: 200px"> 我是来自北方的狼,来南方找寻心爱的花姑娘</div>
        {% endblock %}
    </div><!-- /.container -->

    <footer class="blog-footer">
      <p>Blog template built for <a href="http://getbootstrap.com">Bootstrap</a> by <a href="https://twitter.com/mdo">@mdo</a>.</p>
      <p>
        <a href="#">Back to top</a>
      </p>
    </footer>


    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="https://cdn.bootcss.com/jquery/1.12.4/jquery.min.js"></script>
    <script>window.jQuery || document.write('<script src="../../assets/js/vendor/jquery.min.js"><\/script>')</script>
    <script src="https://cdn.bootcss.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    </body>
</html>


index.html 


{% extends 'base.html' %}
{% block headers %}
    <link rel="stylesheet" href="{{ url_for('static',filename='css.css') }}">
{% endblock %}
{% block title %}
    首页
{% endblock %}

{% block content %}
    <div class="test">
        <p>haha</p>
    </div>
    {{ super() }}  #即显示父模板内容 又显示子模板内容 
    <h1>我是首页的内容</h1>
    <div style="background:pink;width: 100px;height:100px;">我是子模板的内容</div>
    <img src="{{ url_for('static',filename='timg.jpg') }}" alt="美女">
{% endblock %}



```



## 页面加载静态文件  

```
{{ url_for('static',filename='timg.jpg') }} #第一个参数必须叫static  第二个参数 filename
```

