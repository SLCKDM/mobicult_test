import datetime as dt
import asyncio

from sqlalchemy.orm.exc import UnmappedInstanceError

from app.dals.currency_dal import CurrencyDAL, CurrencyValueDAL
from app.tests.conftest import AsyncTestingSessionLocal


async def cur_dal():
    async with AsyncTestingSessionLocal() as session:
        return CurrencyDAL(session)


async def cur_val_dal():
    async with AsyncTestingSessionLocal() as session:
        return CurrencyValueDAL(session)

currency_dal = asyncio.run(cur_dal())
currency_val_dal = asyncio.run(cur_val_dal())


async def test_create_good_vals():
    res = await currency_val_dal.create(dt.date(2023, 1, 1), 'RUB', 'USD', 1)
    assert res is not None


async def test_get_vals():
    res = await currency_val_dal.get(1)
    assert 1==1


def test_list_vals():

    assert 1==1

