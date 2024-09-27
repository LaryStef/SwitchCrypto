from typing import TYPE_CHECKING

from sqlalchemy import Float, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.postgre import db


if TYPE_CHECKING:
    from .cryptocourse import CryptoCourse
    from .cryptocurrency_wallet import CryptocurrencyWallet


class CryptoCurrency(db.Model):
    __tablename__: str = "CryptoCurrency"

    ticker: Mapped[str] = mapped_column(String(8), primary_key=True)
    name: Mapped[str] = mapped_column(String(32))
    description: Mapped[str] = mapped_column(String(4096))
    volume: Mapped[float] = mapped_column(Float, default=0)
    crypto_course: Mapped[list["CryptoCourse"]] = relationship()
    curr_wallet: Mapped["CryptocurrencyWallet"] = relationship(
        backref="CryptocurrencyWallet.cryptocurrency"
    )

    def __init__(
        self,
        *,
        ticker: str,
        name: str,
        description: str,
        volume: float,
    ) -> None:
        self.ticker = ticker
        self.name = name
        self.description = description
        self.volume = volume
