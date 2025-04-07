from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import HttpUrl

class SentrySettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        extra='ignore',
        env_ignore_empty=True
    )

    SENTRY_DSN: HttpUrl | None = None

sentry_settings = SentrySettings()
