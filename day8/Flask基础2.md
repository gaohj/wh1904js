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