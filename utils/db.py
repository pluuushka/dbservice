from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import Session, sessionmaker, declarative_base
from sqlalchemy import URL, create_async_engine
from configs import settings

# engine for db
async_engine = create_async_engine(
    url=settings.DATABASE_URL_asyncpg,
    echo=False,
    pool_size=5,
    max_overflow=10
)

# session's fabrics
AsyncSessionLocal = sessionmaker(
    async_engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# base class for all models
Base = declarative_base()

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session


