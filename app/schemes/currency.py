import datetime as dt

from pydantic import BaseModel


class TunedModel(BaseModel):

    class Config:
        """ Tells pydantic to convert even not dict obj to json """
        from_attributes = True


class CurrencyScheme(TunedModel):
    '''
    Currency scheme
    '''
    id: int
    short: str
    name: str


class CurrencyValueScheme(TunedModel):
    '''
    Currency values scheme
    '''
    id: int
    date: dt.date
    currency: CurrencyScheme
