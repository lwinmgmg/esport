from sqlalchemy.engine import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker
from .postgres import POSTGRES_URL, POSTGRES_ASYNC_URL

pg_engine = create_engine(POSTGRES_URL, echo=True)
pg_async_engine = create_async_engine(POSTGRES_ASYNC_URL, echo=True)

async def get_session():
    async with async_sessionmaker(pg_async_engine, expire_on_commit=False)() as session:
        try:
            yield session
        except Exception as err:
            await session.rollback()
            raise err
        finally:
            await session.commit()
