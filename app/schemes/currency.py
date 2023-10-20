import datetime as dt

from pydantic import BaseModel, ConfigDict


class TunedModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)



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
