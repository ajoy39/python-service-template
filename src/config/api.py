from pydantic_settings import SettingsConfigDict, BaseSettings
from pydantic import HttpUrl


class ApiSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', extra='ignore')

    API_V1_STR: str = "/api/v1"

api_settings = ApiSettings()