"""
api
"""

import json
from flask import Blueprint

api = Blueprint('api', __name__)


@api.route(rule='/', methods=['get', 'post'])
def index():
    return 'api home'


@api.route(rule='/test', methods=['get', 'post'])
def test():
    rsp = {'code': 200, 'message': 'API Test'}
    return json.dumps(obj=rsp, ensure_ascii=False)

