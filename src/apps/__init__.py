import sentry_sdk

sentry_sdk.init(
        dsn="https://5324547ad7d1eaa9691365a56f0fbfee@o4507558908198912.ingest.us.sentry.io/4507559350763520",
        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for performance monitoring.
        traces_sample_rate=1.0,
        # Set profiles_sample_rate to 1.0 to profile 100%
        # of sampled transactions.
        # We recommend adjusting this value in production.
        profiles_sample_rate=1.0,
        debug=True
    )