#encoding:utf-8

#这里主要是单独的入口文件
from flask_script import Manager
from app import app

manager = Manager(app)



if __name__ == "__main__":
    manager.run()