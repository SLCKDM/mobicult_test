import pytest
import datetime as dt
from fixer.src.main import FixerAPI

api = FixerAPI('c2d088d2826118705a1035f11fdf4fd1')


@pytest.mark.asyncio
async def test_request_latest_ru():
    data = await api.latest('RUB', ('USD', 'EUR'))
    assert isinstance(data, dict)


@pytest.mark.asyncio
async def test_request_historical_ru():
    data = await api.historical(dt.date(2023, 10, 19), 'USD', ('RUB'))
    assert isinstance(data, dict)
