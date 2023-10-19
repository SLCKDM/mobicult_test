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
    new_curr = await cur_dal.create(
        id=currency.id,
        short=currency.short,
        name=currency.name,
    )
    return new_curr


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
