"""
开发环境启动模块
"""
from xgmonitor.web import run_app

if __name__ == '__main__':
    run_app(host='0.0.0.0', port=80)  # python run.py
