from flask import Blueprint,render_template

user = Blueprint('user',__name__)

@user.route('/register/',methods=['GET','POST'])
def register():
    return '欢迎注册'