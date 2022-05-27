import multiprocessing

bind = "0.0.0.0:5000"
worker_class = "gthread"
workers = multiprocessing.cpu_count()
threads = multiprocessing.cpu_count() * 3
