from flask import Flask,render_template

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def hello_world():
    return render_template('index/index.html', username='扛把子')



if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5002)
