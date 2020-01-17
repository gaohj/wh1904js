from flask import Flask,render_template
from apps.views import config_blueprint
from apps.extensions import config_extensions
from apps.config import config
#工厂设计模式

def create_app(config_name):

    app = Flask(__name__)
    #初始化配置文件
    app.config.from_object(config[config_name])

    #调用初始化方法 让配置文件生效
    config[config_name].init_app(app) #跟app绑定
    config_blueprint(app)
    config_extensions(app)
    config_errorhandler(app)
    return app

#配置错误页面
def config_errorhandler(app):
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('errors/404.html')
