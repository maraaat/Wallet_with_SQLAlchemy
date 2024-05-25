from database.config import settings
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, DeclarativeBase

engine = create_engine(url=settings.DATABASE_URL_psycopg, echo=False)

session = sessionmaker(engine)


class Base(DeclarativeBase):
    pass

