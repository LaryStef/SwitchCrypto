from datetime import datetime

from sqlalchemy import ForeignKey, String, Integer, Float, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column

from app.database.postgre import db, utcnow


class CryptoTransaction(db.Model):
    __tablename__: str = "CryptoTransaction"

    ID: Mapped[str] = mapped_column(String(36), primary_key=True)
    ticker: Mapped[str] = mapped_column(ForeignKey("CryptoCurrency.ticker"))
    amount: Mapped[int] = mapped_column(Integer)
    type_: Mapped[str] = mapped_column(String(8))
    time: Mapped[datetime] = mapped_column(TIMESTAMP, server_default=utcnow())
    price: Mapped[float] = mapped_column(Float)
    user_id: Mapped[str] = mapped_column(ForeignKey("User.uuid"))

    def __init__(
        self,
        *,
        ID: str,
        ticker: str,
        amount: int,
        type_: str,
        price: float,
        user_id: str
    ) -> None:
        self.ID = ID
        self.ticker = ticker
        self.amount = amount
        self.type_ = type_
        self.price = price
        self.user_id = user_id
