from flask import Blueprint

# books_bp = Blueprint('book',__name__,url_prefix='/book')
books_bp = Blueprint('book',__name__,subdomain='book')

@books_bp.route('/')
def index():
    return '图书首页'