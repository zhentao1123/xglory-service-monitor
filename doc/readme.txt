#退出虚拟环境
deactivate

#重启虚拟环境
source venv/bin/activate

#在当前目录生成 requirements.txt
pipreqs . --encoding=utf8 --force

#使用requirements.txt安装依赖的方式
pip install -r requirements.txt

#生产环境
部署： nginx+gunicorn+flash
起停及状态监控：supervisior