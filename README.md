# 下载依赖
pip install -r requirements.txt
# 开发环境
$ cd src
$ cd python manage.py

# 部署生成时，通过docker部署
$ docker build -t realtimersrv:latest -f Dockerfile
$ docker stop realtimersrv && rm realtimersrv
$ docker run --name realtimesrv -p 5000:5000 -d -e DEPLOYMODE=prd realtimesrv:latest

