import datetime as dt
from typing import List

import sqlalchemy as sa
from sqlalchemy.orm import mapped_column, Mapped, relationship, DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs


class Base(AsyncAttrs, DeclarativeBase):
    ...


class Currency(Base):
    '''
    Currency model
    '''
    __tablename__ = 'currencies'
    id: Mapped[str] = mapped_column(sa.String(length=3), primary_key=True)


class CurrencyValue(Base):
    '''
    Currency values model
    '''
    __tablename__ = 'currencies_values'
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True, autoincrement=True)
    date: Mapped[dt.date] = mapped_column(sa.Date)
    currency_from_id: Mapped[int] = mapped_column(sa.ForeignKey("currencies.id"))
    currency_to_id: Mapped[int] = mapped_column(sa.ForeignKey("currencies.id"))
    currency_from: Mapped["Currency"] = relationship(foreign_keys=currency_from_id)
    currency_to: Mapped["Currency"] = relationship(foreign_keys=currency_to_id)
    value: Mapped[float] = mapped_column(sa.Float)
