from fastapi import Depends, FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.currency import Currency
from app.dals.currency_dal import CurrencyDAL
from app.db.session import get_db
from app.schemes.currency import CurrencyScheme

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")


@app.get("/", response_class=HTMLResponse)
async def index_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


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


@app.post("/currency/create")
async def create_currency(
    request: Request,
    currency: CurrencyScheme,
    db: AsyncSession = Depends(get_db),
) -> CurrencyScheme:
    new_curr = await _create_currency(db=db, currency=currency)
    return CurrencyScheme(new_curr)
