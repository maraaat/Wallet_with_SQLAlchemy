import datetime

from sqlalchemy import text
from sqlalchemy.orm import Mapped, mapped_column
import enum

from database.db import Base


class Categories(enum.Enum):
    profit = "profit"
    food = "food"
    clothes = "clothes"
    fun = "fun"
    health = "health"
    transport = "transport"
    other = "other"


class TransactionsTable(Base):
    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(primary_key=True)
    cost: Mapped[int]
    category: Mapped[Categories]
    date: Mapped[datetime.datetime] = mapped_column(server_default=text("TIMEZONE('utc', now())"))


class WalletsTable(Base):
    __tablename__ = "wallets"

    id: Mapped[int] = mapped_column(primary_key=True)
    balance: Mapped[int]
    moneybox: Mapped[int]
