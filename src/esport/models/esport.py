from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer
from .common import Base

class Esport(Base):
    __tablename__ = "esport"

    id   : Mapped[int] = mapped_column(Integer, primary_key=True)
    name : Mapped[str] = mapped_column(String(20), index=True, unique=True)
