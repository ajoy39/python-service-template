from fastapi import FastAPI
from fastapi.routing import APIRoute
from src.config import config
import sentry_sdk

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


def custom_generate_unique_id(route: APIRoute) -> str:
    return f"{route.tags[0]}-{route.name}"


app = FastAPI(
    title=config.PROJECT_NAME,
    openapi_url=f"{config.api.API_V1_STR}/openapi.json",
)


@app.get("/sentry-debug")
async def trigger_error():
    division_by_zero = 1 / 0
