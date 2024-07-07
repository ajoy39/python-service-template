from celery import Celery
from config import config

app = Celery(broker=str(config.queue.broker_url), backend=str(config.queue.backend_url))