from flask import Blueprint

books = Blueprint('books',__name__,url_prefix='/books')

@books.route('/')
def index():
    return '<h1>图书首页</h1>'

#http://127.0.0.1:9000/books/detail/100/
@books.route('/detail/<int:num>/')
def detail(num):
    return '您正在收看的是第%s篇文章'% num