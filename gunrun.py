'''
生产环境gunicorn启动文件
'''
from xgmonitor.web import run_app

app = None

if __name__ == '__main__':
    app = run_app(host='0.0.0.0', port=80) #python main.py