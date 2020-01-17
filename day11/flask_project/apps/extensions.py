from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy



#创建对象
bootstrap = Bootstrap()
db = SQLAlchemy()


#封装一个方法 让其跟app完成绑定
def config_extensions(app):
    bootstrap.init_app(app)
    db.init_app(app)