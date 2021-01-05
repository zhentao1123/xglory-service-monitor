'''
开发环境启动模块
'''
from xgmonitor.web import run_app
#from xgmonitor.web import run_manager

if __name__ == '__main__':
    run_app(host='0.0.0.0', port=80) #python main.py
    # run_manager() #python main.py runserver -d -r -h 0.0.0.0 -p 80