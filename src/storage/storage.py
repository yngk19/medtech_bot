from typing import Union

from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession
from sqlalchemy.orm import sessionmaker

def create_async_engine(url: Union[URL, str]) -> AsyncEngine:
    return create_engine(url=url, echo=True, encoding="utf-8", pool_pre_ping=True)


def get_session_maker(engine: AsyncEngine) -> sessionmaker
    return sessionmaker(engine, class_=AsyncSession)