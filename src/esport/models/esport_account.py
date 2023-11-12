from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey
from .common import Base

class EsportAccount(Base):
    __tablename__ = "esport_account"

    id        : Mapped[int]      = mapped_column(Integer, primary_key=True)
    user_id   : Mapped[str]      = mapped_column(String(12), index=True)
    esport_id : Mapped[int]      = mapped_column(ForeignKey("esport.id"))
    ingame_id : Mapped[str]      = mapped_column(String(32), nullable=True)
    esport    : Mapped["Esport"] = relationship()
