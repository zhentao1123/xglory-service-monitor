"""
home
"""

import json
from flask import Blueprint

home = Blueprint('home', __name__)


@home.route(rule='/', methods=['get', 'post'])
def index():
    return 'home page'


