from flask import Flask,render_template
from flask_script import Manager
app = Flask(__name__)
manager = Manager(app)

@app.route('/')
def hello_world():
    return render_template('index.html',username='kangbazi')


@app.route('/detail/')
def detail():
    return render_template('detail.html')


if __name__ == '__main__':
    manager.run()
