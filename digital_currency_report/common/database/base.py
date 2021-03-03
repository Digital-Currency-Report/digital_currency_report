from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import declarative_base

from digital_currency_report.config import config

engine = create_async_engine(
    config.DB_URL,
    echo=config.DB_ECHO,
    pool_size=5,
    max_overflow=20,
    pool_timeout=10,
    pool_recycle=1800
)
base = declarative_base()
