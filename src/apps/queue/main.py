from celery import Celery
from src.config import config

app = Celery("Queue", broker=str(config.queue.broker_url), backend=str(config.queue.backend_url))