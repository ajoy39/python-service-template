from src.config import config
from celery import Celery, signals
import sentry_sdk

app = Celery("queue", broker=str(config.queue.BROKER_URL), backend=str(config.queue.BACKEND_URL))


@signals.celeryd_init.connect
def init_sentry(**_kwargs):
    if config.sentry.SENTRY_DSN:
        sentry_sdk.init(
            dsn=config.sentry.SENTRY_DSN,
            # Set traces_sample_rate to 1.0 to capture 100%
            # of transactions for performance monitoring.
            traces_sample_rate=1.0,
            # Set profiles_sample_rate to 1.0 to profile 100%
            # of sampled transactions.
            # We recommend adjusting this value in production.
            profiles_sample_rate=1.0,
            debug=True,
        )
