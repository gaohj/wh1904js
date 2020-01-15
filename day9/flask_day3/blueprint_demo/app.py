from flask import Flask
from views import books_bp,cms_bp
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SERVER_NAME'] = '91.com:5000'
app.register_blueprint(books_bp)
app.register_blueprint(cms_bp)


#
@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
