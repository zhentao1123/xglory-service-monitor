"""
开发环境启动模块
"""
from xgmonitor.web import run_manager

if __name__ == '__main__':
    run_manager() #python run_manager.py runserver -d -r -h 0.0.0.0 -p 80