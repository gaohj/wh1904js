from flask import Blueprint,request


bp = Blueprint('cms',__name__,subdomain='cms')


@bp.route('/')
def index():
    # request.args.get() #获取url中的参数
    # request.form.get() #获取表单中的内容
    # request.files.get() #获取上传文件内容
    username = request.cookies.get('username')
    return  username or '没有获取到cookie'