from database.db import engine, Base, session
from database.models import TransactionsTable, WalletsTable


class WalletQueries:
    @staticmethod
    def create_tables():
        engine.echo = False
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)
        engine.echo = True

    @staticmethod
    def insert_basic():
        pass