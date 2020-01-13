from flask import Blueprint

movies = Blueprint('movies',__name__,url_prefix='/movies')

@movies.route('/')
def index():
    return '<h1>电影首页</h1>'

#http://127.0.0.1:9000/movies/detail/100/
@movies.route('/detail/<int:num>/')
def detail(num):
    return '您正在收看的是第%s部电影'% num