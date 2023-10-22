'''
Script for loading historical rates data into app db
'''
import asyncio
import logging
import argparse
from typing import Iterable
import datetime as dt
# import sys
import os

from fixer import FixerAPI
from app.dals.currency_dal import CurrencyDAL, CurrencyValueDAL
from app.db.session import async_session


parser = argparse.ArgumentParser(
    description='sum the integers at the command line')
parser.add_argument(
    'days', metavar='d', nargs=1, type=int,
)
parser.add_argument(
    'origin', metavar='o', nargs=1, type=str,
)
parser.add_argument(
    'currencies', metavar='c', nargs='+', type=str,
)

args = parser.parse_args()


async def main(_date: dt.date, _origin: str, _currencies: Iterable[str]):
    api = FixerAPI(os.getenv('FIXER_API_TOKEN', ''))
    data = await api.historical(date=_date, source=_origin, currencies=_currencies)

    async with async_session() as db:
        # cur_dal = CurrencyDAL(db)
        cur_val_dal = CurrencyValueDAL(db)
        for currencies, rate in data['quotes']:
            from_curr = currencies[:3]
            to_curr = currencies[3:]
            created = await cur_val_dal.create(
                date=data['date'],
                currency_from_id=from_curr,
                currency_to_id=to_curr,
                value=rate
            )
            logging.info('%s created', created)
    await db.commit()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    logging.getLogger('utils')
    logging.info(args)

    date_range = [dt.date.today() - dt.timedelta(days=n) for n in range(args.days[0])]
    for date in date_range:
        asyncio.run(main(date, args.origin[0], args.currencies))
