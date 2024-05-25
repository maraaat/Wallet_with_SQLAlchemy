from database.config import settings
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, DeclarativeBase

engine = create_engine(url=settings.DATABASE_URL_psycopg, echo=True)

session = sessionmaker(engine)


with engine.connect() as conn:
    res = conn.execute(text("SELECT VERSION()"))
    print(f"{res=}")

class Base(DeclarativeBase):
    pass
