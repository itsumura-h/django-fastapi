import multiprocessing

bind = 'unix:/var/run/sock/fastapi.sock'

# Worker Processes
# workers = 1
# workers = multiprocessing.cpu_count() * 2 + 1
workers = multiprocessing.cpu_count()
worker_class = 'uvicorn.workers.UvicornWorker'
threads = 1
reload = True

# Logging
accesslog = '/var/log/fastapi/access.log'
errorlog = '/var/log/fastapi/error.log'
loglevel = 'error'
capture_output = True
