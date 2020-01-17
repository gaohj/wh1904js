from flask import Blueprint,render_template

posts = Blueprint('posts',__name__)

@posts.route('/',methods=['GET','POST'])
def index():
    return '欢迎发表'