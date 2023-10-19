from sqlalchemy.ext.asyncio import AsyncSession
from app.models.currency import Currency, CurrencyValue


class DAL:

    def __init__(self, db: AsyncSession) -> None:
        self.db = db


class CurrencyDAL(DAL):

    async def get(self, _id: int, /) -> Currency | None:
        """ get currency """
        return await self.db.get(Currency, _id)

    async def create(self, id: int, short: str, name: str) -> Currency:
        """ create currency """
        new_currency = Currency(
            id=id,
            short=short,
            name=name,
        )
        self.db.add(new_currency)
        await self.db.flush()
        return new_currency

    async def delete(self, instance: Currency, /) -> None:
        """ delete currency """
        await self.db.delete(instance=instance)
        await self.db.flush()
