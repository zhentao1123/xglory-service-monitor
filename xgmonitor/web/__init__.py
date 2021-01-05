from flask import Flask
from flask_script import Manager

from xgmonitor.web.api import api
from xgmonitor.web.demo import demo
from xgmonitor.web.home import home


# 供开发环境 "python run_manager.py runserver -d -r -h 0.0.0.0 -p 80" 方式启动
def run_manager():
    app = Flask(__name__)
    app.register_blueprint(blueprint=home, url_prefix='/')
    app.register_blueprint(blueprint=api, url_prefix='/api')
    app.register_blueprint(blueprint=demo, url_prefix='/demo')
    manager = Manager(app=app)
    manager.run()


# 供开发环境 "python run.py" 方式启动
def run_app(host, port):
    app = Flask(__name__)
    app.register_blueprint(blueprint=home, url_prefix='/')
    app.register_blueprint(blueprint=api, url_prefix='/api')
    app.register_blueprint(blueprint=demo, url_prefix='/demo')
    app.run(host=host, port=port)

# 供生产环境 "gunicorn -w 4 -b 0.0.0.0:80 run_gunicorn:app " 方式启动
def build_app():
    app = Flask(__name__)
    app.register_blueprint(blueprint=home, url_prefix='/')
    app.register_blueprint(blueprint=api, url_prefix='/api')
    app.register_blueprint(blueprint=demo, url_prefix='/demo')
    return app
