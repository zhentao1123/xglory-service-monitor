"""
生产环境gunicorn启动文件
"""

from xgmonitor.web import build_app

app = build_app()

if __name__ == '__main__':
    pass