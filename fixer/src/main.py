from typing import Iterable, Sequence
import aiohttp
import datetime as dt

BASE_URL = 'http://apilayer.net/api/'


class FixerAPI:

    def __init__(self, token: str):
        self._access_key = token
        self.params = {'access_key': token}

    async def latest(
        self,
        source: str | None,
        currencies: Sequence[str] | None,
    ):
        _payload = {
            "source": source,
            "currencies": ','.join(currencies or []) or None,
        }
        async with aiohttp.ClientSession() as session:
            async with session.get(
                url=f'{BASE_URL}/live',
                params={**_payload, **self.params}
            ) as response:
                return await response.json()

    async def historical(
        self,
        date: dt.date,
        source: str | None = None,
        currencies: Iterable[str] | None = None,
    ):
        _payload = {
            "date": date.strftime('%Y-%m-%d'),
            "source": source,
            "currencies": ','.join(currencies or []) or None,
        }
        async with aiohttp.ClientSession() as session:
            async with session.get(
                url=f'{BASE_URL}/historical',
                params={**_payload, **self.params}
            ) as response:
                return await response.json()
