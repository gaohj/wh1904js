from .main import main
from .user import user
from .posts import posts

DEFAULT_BLUEPRINT = (
    (main,''),
    (user,'/user'),
    (posts,'/posts'),

)

#单独封装一个方法 完成蓝本注册
def config_blueprint(app):
    for blueprint,url_prefix in DEFAULT_BLUEPRINT:
        app.register_blueprint(blueprint,url_prefix=url_prefix)