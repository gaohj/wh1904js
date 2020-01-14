from flask import Flask,render_template

app = Flask(__name__)


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



