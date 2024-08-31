from sqlmodel import SQLModel, create_engine

from ..models.transaction import *

from .consts import DB_ECHO, DB_NAME
from .config import get_db_settings

db_settings = get_db_settings()

db_url = db_settings.db_url
engine = create_engine(db_url + DB_NAME, echo=DB_ECHO)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)