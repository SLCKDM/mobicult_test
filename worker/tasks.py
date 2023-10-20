from worker.app import app
from fixer.main import FixerAPI
from app.dals.currency_dal import CurrencyValueDAL, CurrencyDAL
from app.db.session import async_session
from asgiref.sync import async_to_sync

async def _load_current_xchange_rate():
    api = FixerAPI('c2d088d2826118705a1035f11fdf4fd1')
    data = await api.latest('RUB', ('EUR', "USD"))
    async with async_session() as db:
        curr_val_dal = CurrencyValueDAL(db)
        curr_dal = CurrencyDAL(db)
        curr_dal.get()
        curr_val_dal.create(date=data['date'], )


@app.task
def load_current_xchange_rate():
    async_to_sync(_load_current_xchange_rate)()