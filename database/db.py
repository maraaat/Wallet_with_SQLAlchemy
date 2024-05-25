from database.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

engine = create_engine(settings.DATABASE_URL_psycopg, echo=True)

session = sessionmaker(engine)


class Base(DeclarativeBase):
    pass
