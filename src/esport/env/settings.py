import os
from typing import Optional
from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

ENV_PATH = os.environ.get("ENV_PATH", ".env")

class Postgres(BaseModel):
    host : str
    port : int
    db   : str
    user : str
    password : str

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=ENV_PATH, env_file_encoding='utf-8', env_nested_delimiter="__")

    HOST      : Optional[str] = "localhost"
    PORT      : Optional[int] = 5432

    ESPORT_PG : Postgres

settings = Settings()
