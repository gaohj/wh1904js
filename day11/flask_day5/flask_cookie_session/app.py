from flask import Flask,Response
from datetime import datetime,timedelta
from cmsblueprint import bp
app = Flask(__name__)

app.register_blueprint(bp)
app.config['SERVER_NAME'] = '91.com:5000'


@app.route('/')
def hello_world():
    resp = Response('千锋教育')
    #expires = datetime(year=2020,month=1,day=17,hour=16,minute=10,second=20)
    #使用expires需要使用格林尼治时间 相对北京时间慢了八个小时
    expires = datetime.now() + timedelta(hours=8)
    resp.set_cookie('username','kangbazi',expires=expires,max_age=60,domain='.91.com')
    return resp
@app.route('/delete_cookie/')
def  delete_cookie():
    res = Response('扛把子')
    res.delete_cookie('username')
    return res

if __name__ == '__main__':
    app.run()
