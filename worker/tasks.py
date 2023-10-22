from typing import Sequence
import datetime as dt
from os import getenv

import sqlalchemy as sa

from worker.app import app
from fixer.src.main import FixerAPI
from app.dals.currency_dal import CurrencyValueDAL, CurrencyDAL
from app.db.session import async_session, AsyncSession
from app.models.currency import CurrencyValue
from asgiref.sync import async_to_sync


async def check_if_exists(
    db: AsyncSession,
    date: dt.date,
    from_c: str,
    to_c: str
) -> bool:
    q = (sa.select(CurrencyValue.id)
           .where(CurrencyValue.date == date,
                  CurrencyValue.currency_from_id == from_c,
                  CurrencyValue.currency_to_id == to_c))
    async with db:
        res = await db.execute(q)
        res = res.scalar_one_or_none()
    return True if res else False


async def _load_current_xchange_rate(source: str, currencies: Sequence[str]):
    api = FixerAPI(getenv('FIXER_API_TOKEN', ''))
    data = await api.latest(source, currencies)
    if not data['success']:
        return
    async with async_session() as db:
        curr_val_dal = CurrencyValueDAL(db)
        curr_dal = CurrencyDAL(db)
        timestamp = data['timestamp']
        from_currency = data['source']

        if not await curr_dal.get(from_currency):
            await curr_dal.create(from_currency)
            await db.commit()

        for rate_name, rate in data['quotes'].items():
            date = dt.date.fromtimestamp(timestamp)
            to_currency = rate_name[3:]

            if not await curr_dal.get(to_currency):
                await curr_dal.create(to_currency)
                await db.commit()

            already_exists = await check_if_exists(db, date, from_currency, to_currency)

            if already_exists:
                continue

            await curr_val_dal.create(
                date=date,
                currency_from_id=from_currency,
                currency_to_id=to_currency,
                value=rate,
            )
        await db.commit()


@app.task
def load_current_xchange_rate(source: str, currencies: Sequence[str]):
    async_to_sync(_load_current_xchange_rate)(source, currencies)
