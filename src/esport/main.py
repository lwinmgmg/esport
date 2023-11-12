from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import FastAPI, Depends
from esport.models.common import Base
from esport.services.engine import pg_engine, get_session
from esport.models.esport import Esport

Base.metadata.drop_all(pg_engine)
Base.metadata.create_all(pg_engine)

app = FastAPI()

count = [10]

@app.get("/")
async def home(
    session: Annotated[AsyncSession, Depends(get_session)]
):
    esport_account = Esport(name=f"Dota-{count[0]}")
    count[0] += 1
    session.add(esport_account)
    await session.flush()
    session.add(Esport(name="Dota-2"))
    await session.flush()
    return esport_account.__dict__
