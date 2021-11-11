# -*- coding: utf-8 -*-
# @Time    : 2021/3/29 1:28 下午
# @Author  : HuangSir
# @FileName: gconfig.py
# @Software: PyCharm
# @Desc: 生产配置

import multiprocessing
bind = '0.0.0.0:8004'  # Nginx监听 8005 并转发给 8004
timeout = 60      #超时
worker_class = 'uvicorn.workers.UvicornWorker' #使用,uvicornt模式，备选模式: geven, sync

worker_connections = 1000 # 最大并发量
workers = multiprocessing.cpu_count() * 2 + 1    #进程数

max_requests = 0 # 默认防止内存泄露
max_requests_jitter = 0 # 默认 防止抖动将导致每个工作的重启被随机化
reload=False # 调试模式

loglevel = 'info' #日志级别 dubug
access_log_format = '%(t)s %(p)s %(h)s "%(r)s" %(s)s %(L)s %(b)s %(f)s" "%(a)s"'    #设置gunicorn访问日志格式

accesslog = './log/gunicorn_access.log'      #访问日志文件
errorlog = './log/gunicorn_error.log'      #错误日志文件