"""
demo
"""

import json
from flask import Blueprint
from flask import jsonify

demo = Blueprint('demo', __name__)


user_date = [
    {
        'name': 'tom',
        'id': 1
    },
    {
        'name': 'jack',
        'id': 2
    }
]


@demo.route(rule='/', methods=['get', 'post'])
def index():
    return 'demo home'


@demo.route(rule='/test', methods=['get', 'post'])
def test():
    rsp = {'code': 200, 'message': 'Demo Test'}
    return json.dumps(obj=rsp, ensure_ascii=False)


@demo.route('/user/<int:id>', methods=['get'])
def user_get(id):
    for user in user_date:
        if int(user['id']) == id:
            return jsonify(success='True', user=user)

    return jsonify(success='False', msg='user not found')


@demo.route('/user', methods=['get'])
def user_all():
    return jsonify(success='True', users=user_date)