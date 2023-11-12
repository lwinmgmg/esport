from esport.env.settings import settings

POSTGRES_URL = (
    f"postgresql://{settings.ESPORT_PG.user}:{settings.ESPORT_PG.password}@"
    f"{settings.ESPORT_PG.host}:{settings.ESPORT_PG.port}/{settings.ESPORT_PG.db}"
    )

POSTGRES_ASYNC_URL = (
    f"postgresql+asyncpg://{settings.ESPORT_PG.user}:{settings.ESPORT_PG.password}@"
    f"{settings.ESPORT_PG.host}:{settings.ESPORT_PG.port}/{settings.ESPORT_PG.db}"
)
