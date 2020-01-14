from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)
from datetime import datetime
from time import time


@app.route('/')
def hello_world():
    context = {
        'username':'xiaowen',
        'height':'181cm',
        'age':18,
        'child':{
            'name':'xiaoxiaowen',
            'height':'100cm'
        }
    }
    return render_template('index.html',**context)

@app.route('/profile/',methods=['GET','POST'])
def profile():
    name = request.args.get('username')
    if not name:
        return redirect(url_for('logins'))
    else:
        return '大金链子小手表,一天三顿小烧烤'

@app.route('/login/<int:id>/',methods=['GET','POST'])
def logins(id):
    return render_template('login.html',userid=id)

@app.errorhandler(404)
def not_found(error):
    return '去火星了我也没办法',500


@app.route('/filters/')
def filters():
    context = {
        'position':-10,
        'signature':'<script>alert("美女跟我处对象呗,我非常擅解人衣")</script>',
        'person':['zhangsan','lisi'],
        'age':18,
        'message':'jiayou is a good man<a>haha</a>',
        'pub_time':datetime(2020,1,14,15,1,30),
        'username':'kangbazi',
        'users':['李逵','恶汉','武松'],
        'people':{
            'username':'西门官人',
            'height':'五大三粗',
            'coutry':'浪奔浪流'
        },
        'books':[
            {
              'name':'深入浅出MySQL',
              'price':18,
              'author':'西门君'

            },
            {
                'name': '进进出出java',
                'price': 100,
                'author': '钢板君'
            },
            {
                'name': 'js从入门到放弃',
                'price': 200,
                'author': '云涛哥'
            },
            {
                'name':'从删库到跑路',
                'price':0.1,
                'author':'范跑跑',
            }
        ]
    }
    return render_template('filters.html',**context)
"""
@:param time datetime  日期 
"""
#一分钟内显示刚刚
#大于1分钟 小于一个小时  显示几分钟之前啊
#大于1小时 小于24小时  显示 几个小时之前
#大于24小时 小于30天   显示 几天之前
#否则就显示  年月日时分秒
@app.template_filter('handle_time')
def handle_times(time):
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
