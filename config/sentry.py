from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import HttpUrl

class SentrySettings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', extra='ignore')

    SENTRY_DSN: HttpUrl

sentry_settings = SentrySettings()
