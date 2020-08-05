import multiprocessing

bind = 'unix:/var/run/sock/django.sock'

# Worker Processes
# workers = 1
# workers = multiprocessing.cpu_count() * 2 + 1
workers = multiprocessing.cpu_count()
worker_class = 'sync'
threads = 1
reload = True

# Logging
accesslog = '/var/log/django/access.log'
errorlog = '/var/log/django/error.log'
loglevel = 'error'
capture_output = True
