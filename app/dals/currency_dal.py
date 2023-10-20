import datetime as dt

import sqlalchemy as sa
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.currency import Currency, CurrencyValue


class DAL:

    def __init__(self, db: AsyncSession) -> None:
        self.db = db


class CurrencyDAL(DAL):

    async def get(self, _id: str, /) -> Currency | None:
        """ get currency """
        return await self.db.get(Currency, _id)

    async def list(self):
        """ get list of currencies """
        query = sa.select(Currency)
        res = await self.db.execute(query)
        return list(res.scalars())

    async def create(self, id: str) -> Currency:
        """ create currency """
        new_currency = Currency(id=id)
        self.db.add(new_currency)
        await self.db.flush()
        return new_currency

    async def delete(self, instance: Currency, /) -> None:
        """ delete currency """
        await self.db.delete(instance=instance)
        await self.db.flush()


class CurrencyValueDAL(DAL):

    async def get(self, _id: int, /) -> CurrencyValue | None:
        """ get currency value by id """
        return await self.db.get(CurrencyValue, _id)

    async def list(
        self,
        dt_from: dt.date | dt.datetime | None = None,
        dt_to: dt.date | dt.datetime | None = None,
        currency_from_id: str | None = None,
        currency_to_ids: list[str] | None = None,
    ) -> list[CurrencyValue]:
        """ get list of currencies values """
        clauses = (clause for clause in (
            (CurrencyValue.date >= dt_from if dt_from else None),
            (CurrencyValue.date <= dt_to if dt_to else None),
            (CurrencyValue.currency_from_id == currency_from_id if currency_from_id else None),
            (CurrencyValue.currency_to_id.in_(currency_to_ids) if currency_to_ids else None)
        ) if clause is not None)
        query = sa.select(CurrencyValue).where(*clauses)
        res = await self.db.execute(query)
        return list(res.scalars())

    async def create(
        self,
        date: dt.date,
        currency_from_id: str,
        currency_to_id: str,
        value: float
    ) -> CurrencyValue:
        """ create currency value  """
        new_currency_value = CurrencyValue(
            date=date,
            currency_from_id=currency_from_id,
            currency_to_id=currency_to_id,
            value=value,
        )
        self.db.add(new_currency_value)
        await self.db.flush()
        return new_currency_value

    async def delete(self, instance: CurrencyValue, /) -> None:
        """ delete currency """
        await self.db.delete(instance=instance)
        await self.db.flush()
