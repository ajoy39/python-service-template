from .api import api_settings, ApiSettings
from .database import database_settings, DatabaseSettings
from .queue import queue_settings, QueueSettings
from .sentry import sentry_settings, SentrySettings
from pydantic_settings import BaseSettings, SettingsConfigDict


class Configuration(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', extra='ignore', env_nested_delimiter='__')

    api: ApiSettings = api_settings
    database: DatabaseSettings = database_settings
    queue: QueueSettings = queue_settings
    sentry: SentrySettings = sentry_settings

    ENVIRONMENT: str = 'local'
    PROJECT_NAME: str = "Podmanager"


config = Configuration()
