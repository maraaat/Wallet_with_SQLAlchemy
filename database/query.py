from sqlalchemy import select, cast, Integer

from database.db import engine, Base, session
from database.models import TransactionsTable, WalletsTable, Categories


class WalletQueries:
    @staticmethod
    def create_tables():
        engine.echo = False
        # Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)
        engine.echo = True

    @staticmethod
    def insert_basic():
        with session() as sess:
            profit1 = WalletsTable(balance=100000)

            sess.add_all([profit1])
            sess.commit()

    @staticmethod
    def get_balance():
        with session() as sess:
            query = select(WalletsTable.balance)
            result = sess.execute(query)
            bal = result.scalars().all()

            print(f"Balance = {bal[0]}")
    @staticmethod
    def trans_params():
        title = input("Write transaction name: ")
        cost = int(input("Write how much it: "))
        category = input("Write your category: profit, food, clothes, fun, health, transport, other: ")

        WalletQueries.insert_trans(title, cost, category)

    @staticmethod
    def insert_trans(*args):
        with session() as sess:
            transaction = TransactionsTable(title=args[0], cost=args[1], category=args[2])
            bal = sess.get(WalletsTable, 1)

            if args[2] == "profit":
                bal.balance = cast(bal.balance, Integer) + args[1]
            else:
                bal.balance = cast(bal.balance, Integer) - args[1]

            sess.add_all([transaction])
            sess.commit()

    @staticmethod
    def delete_trans(del_id: int):
        with session() as sess:
            d = sess.get(TransactionsTable, del_id)
            bal = sess.get(WalletsTable, 1)
            if d.category == "profit":
                bal.balance = cast(bal.balance, Integer) - d.cost
            else:
                bal.balance = cast(bal.balance, Integer) + d.cost

            sess.delete(d)
            sess.commit()
        print(f"Transaction {del_id} deleted")

    @staticmethod
    def get_all_trans():
        with session() as sess:
            query = sess.query(TransactionsTable)

            for c in query:
                print(f"id = {c.id}, name = {c.title}, price = {c.cost}, category = {c.category.name}")
