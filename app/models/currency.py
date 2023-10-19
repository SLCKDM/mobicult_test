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
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
    short: Mapped[str] = mapped_column(sa.String)  # add constaints
    name: Mapped[str] = mapped_column(sa.String)  # add constaints
    values: Mapped[List["CurrencyValue"]] = relationship(back_populates="currency")


class CurrencyValue(Base):
    '''
    Currency values model
    '''
    __tablename__ = 'currencies_values'
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
    date: Mapped[dt.date] = mapped_column(sa.Date)
    currency_id: Mapped[int] = mapped_column(sa.ForeignKey("currencies.id"))
    currency: Mapped["Currency"] = relationship(back_populates="values")
