from fastapi import Depends, APIRouter, Request

from sqlalchemy.ext.asyncio import AsyncSession
from app.models.currency import Currency
from app.dals.currency_dal import CurrencyDAL
from app.db.session import get_db
from app.schemes.currency import CurrencyScheme

bp = APIRouter(prefix='/currency')


async def _create_currency(
    db: AsyncSession,
    currency: CurrencyScheme,
) -> Currency:
    cur_dal = CurrencyDAL(db=db)
    new_curr = await cur_dal.create(id=currency.id)
    return new_curr


async def _get_all_currencies(
    db: AsyncSession,
) -> list[Currency]:
    cur_dal = CurrencyDAL(db=db)
    currencies = await cur_dal.list()
    return currencies


@bp.post("/create", response_model=CurrencyScheme)
async def create_currency(
    request: Request,
    currency: CurrencyScheme,
    db: AsyncSession = Depends(get_db),
):
    ''' endpoint for creating new currency '''
    new_curr = await _create_currency(db=db, currency=currency)
    await db.commit()
    return new_curr


@bp.get("/", response_model=list[CurrencyScheme])
async def get_currencies(
    request: Request,
    db: AsyncSession = Depends(get_db),
):
    ''' endpoint for creating new currency '''
    return await _get_all_currencies(db=db)
