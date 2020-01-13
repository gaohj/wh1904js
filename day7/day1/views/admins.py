from flask import Blueprint

admins = Blueprint('admins',__name__,url_prefix='/admins') #注意这里右边加上/下面左边就不加了  避免拼接的时候出现//


@admins.route('/')
def index():
    return '<h1>管理后台首页</h1>'

#http://127.0.0.1:9000/admins/detail/100/
@admins.route('/detail/<int:num>/')
def detail(num):
    return '您正在修改的是第%s个模块'% num