# -*- coding: utf8 -*-

"""
 gunicon configuration file

"""
import multiprocessing

bind = "0.0.0.0:5000"
check_config = False

daemon = False

# work type
worker_class = "gevent"
workers = multiprocessing.cpu_count()*2 + 1
worker_connections = 100

max_requests = 0
timeout = 4500

# logging
loglevel = "error"
errorlog = '-'

preload_app = True




