import datetime as dt

from pydantic import BaseModel


class TunedModel(BaseModel):

    class Config:
        orm_mode = True  # Tells pydantic to convert even not dict obj to json


class CurrencyScheme(TunedModel):
    '''
    Currency scheme
    '''
    id: str


class CurrencyValueScheme(TunedModel):
    '''
    Currency values scheme
    '''
    id: int
    date: dt.date
    currency_from: CurrencyScheme
    currency_to: CurrencyScheme
    value: float
