#在当前目录生成 requirements.txt
pipreqs . --encoding=utf8 --force

#使用requirements.txt安装依赖的方式
pip install -r requirements.txt