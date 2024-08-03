from src.config import config
from celery import Celery

app = Celery("Queue", broker=str(config.queue.broker_url), backend=str(config.queue.backend_url))