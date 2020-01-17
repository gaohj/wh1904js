import os

#规定好项目的主目录  apps目录的绝对路径
#__file__ 当前文件所在的位置
#os.path.dirname
#返回规范会绝对路径
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:


    #bootstrap使用本地的库
    BOOTSTRAP_SERVE_LOCAL = True

    @staticmethod
    def init_app(app):
        pass

#开发环境
class DevelopmentConfig(Config):
    # 数据库配置
    DB_USERNAME = 'root'
    DB_PASSWORD = '123456'
    DB_HOST = '127.0.0.1'
    DB_PORT = '3306'
    DB_NAME = '1904project'
    DB_URI = 'mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8' %(DB_USERNAME,DB_PASSWORD,DB_HOST,DB_PORT,DB_NAME)

    SQLALCHEMY_DATABASE_URI = DB_URI




#测试环境
class ProductionConfig(Config):
    # 数据库配置 sqlite是一个文件 设置存储位置
    SQLALCHEMY_DATABASE_URI='sqlite:///'+os.path.join(basedir,'project-test.sqlite')
#生产环境

class TestingConfig(Config):
    # 数据库配置
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'project-product.sqlite')


#配置字典方便 设置

config = {
    'development':DevelopmentConfig,
    'testing':TestingConfig,
    'production':ProductionConfig,
    'default':DevelopmentConfig
}