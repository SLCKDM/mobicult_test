import asyncio

from sqlalchemy.orm.exc import UnmappedInstanceError

from app.dals.currency_dal import CurrencyDAL
from app.tests.conftest import AsyncTestingSessionLocal


async def dal():
    async with AsyncTestingSessionLocal() as session:
        return CurrencyDAL(session)

currency_dal = asyncio.run(dal())


def test_create():
    asyncio.run(currency_dal.create('RUB'))
    asyncio.run(currency_dal.create('USD'))


async def test_get_success():
    currency = await currency_dal.get('RUB')
    assert currency is not None
    assert currency.id == 'RUB'


async def test_get_wrong():
    currency1 = await currency_dal.get(5123123)
    currency2 = await currency_dal.get('23423453')
    assert currency1 is None
    assert currency2 is None


def test_delete_existing():
    currency = asyncio.run(currency_dal.get('RUB'))
    asyncio.run(currency_dal.delete(currency))  # type: ignore


def test_delete_not_existing():
    currency = asyncio.run(currency_dal.get(1234))
    try:
        asyncio.run(currency_dal.delete(currency))
    except UnmappedInstanceError:
        pass
    else:
        raise
