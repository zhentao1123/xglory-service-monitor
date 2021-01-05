from flask import Flask
from flask_script import Manager

from xgmonitor.web.api import api
from xgmonitor.web.demo import demo
from xgmonitor.web.home import home


def run_manager():
    app = Flask(__name__)
    app.register_blueprint(blueprint=home, url_prefix='/')
    app.register_blueprint(blueprint=api, url_prefix='/api')
    app.register_blueprint(blueprint=demo, url_prefix='/demo')
    manager = Manager(app=app)
    manager.run()


def run_app(host, port):
    app = Flask(__name__)
    app.register_blueprint(blueprint=home, url_prefix='/')
    app.register_blueprint(blueprint=api, url_prefix='/api')
    app.register_blueprint(blueprint=demo, url_prefix='/demo')
    app.run(host=host, port=port)
    return app
