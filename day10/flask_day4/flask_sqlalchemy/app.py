from flask import Flask
# from sqlalchemy.ext.declarative import declarative_base
# Base = declarative_base(engine)
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
HOSTNAME = '127.0.0.1'
PORT     = '3306'
DATABASE = '1904_sqlalchemy'
USERNAME = 'root'
PASSWORD = '123456'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__='user_model'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(50),nullable=False)
    password = db.Column(db.String(50),nullable=False)

    def __str__(self):
        return "<User:(username:%s)>" % self.username


class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)
    uid = db.Column(db.Integer,db.ForeignKey('user_model.id'))

    author = db.relationship("User",backref="articles")

    def __str__(self):
        return "<User:(username:%s)>" % self.username
# db.drop_all()
# db.create_all()

@app.route('/')
def hello_world():
    return 'Hello World!'

# user = User(username='qfedu',password='123456')
# article = Article(title='钢铁是怎么炼成的')
# article.author = user
#
# db.session.add(article)
# db.session.commit()

# users = User.query.order_by(User.id.desc()).all()
# print(users)

# users = User.query.filter(User.username=='qfedu').first()
# users.username='heyangyang'
# db.session.commit()

users = User.query.filter(User.id==1).first()
# print(users)
db.session.delete(users)
db.session.commit()
if __name__ == '__main__':
    app.run()
