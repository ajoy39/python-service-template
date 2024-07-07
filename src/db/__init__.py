from src.config import config
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import DeclarativeBase

async_engine = create_async_engine(str(config.database.url))


class BaseModel(DeclarativeBase):
    pass
