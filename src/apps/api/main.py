import sentry_sdk
from fastapi import FastAPI
from fastapi.routing import APIRoute
from starlette.middleware.cors import CORSMiddleware
from src.config import config


def custom_generate_unique_id(route: APIRoute) -> str:
    return f"{route.tags[0]}-{route.name}"


app = FastAPI(
    title=config.PROJECT_NAME,
    openapi_url=f"{config.api.API_V1_STR}/openapi.json",
)


@app.get("/sentry-debug")
async def trigger_error():
    division_by_zero = 1 / 0
