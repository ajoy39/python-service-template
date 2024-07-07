from sqlalchemy.orm import Session
from db import async_engine
from typing import Annotated
from collections.abc import AsyncGenerator
from fastapi import Depends


def get_db() -> AsyncGenerator:
    with Session(async_engine) as session:
        yield session


AsyncSession = Annotated[Session, Depends(get_db)]
