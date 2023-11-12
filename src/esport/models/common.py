"""
Common class and functions for models
"""
# pylint: disable=wrong-import-position
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    """Base Declaration for sqlalchemy

    Args:
        DeclarativeBase (_type_): Sqlalchemy Base
    """
