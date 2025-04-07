from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import RedisDsn, computed_field, HttpUrl


class QueueSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', extra='ignore')

    QUEUE_BROKER_HOST: str | None = None
    QUEUE_BROKER_PORT: int | None = None
    QUEUE_BACKEND_HOST: str | None = None
    QUEUE_BACKEND_PORT: int | None = None

    @computed_field
    @property
    def BROKER_URL(self) -> RedisDsn | None:
        if self.QUEUE_BROKER_HOST is not None:
            return RedisDsn.build(
                scheme="redis",
                host=self.QUEUE_BROKER_HOST,
                port=self.QUEUE_BROKER_PORT
            )

    @computed_field
    @property
    def BACKEND_URL(self) -> RedisDsn | None:
        if self.QUEUE_BACKEND_HOST is not None:
            return RedisDsn.build(
                scheme="redis",
                host=self.QUEUE_BACKEND_HOST,
                port=self.QUEUE_BACKEND_PORT
            )

queue_settings = QueueSettings()
