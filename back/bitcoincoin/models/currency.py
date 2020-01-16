from peewee import *

from bitcoincoin.core import db

from .base_model import BaseModel


class Currency(BaseModel):
    id = AutoField()
    coincap = CharField()
    name = CharField()
    symbol = CharField()
    rank = IntegerField()
    last_value = FloatField(null=True)


class CurrencyRate(BaseModel):
    id = AutoField()
    currency = ForeignKeyField(Currency)
    datetime = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    value = FloatField()


with db:
    Currency.create_table(safe=True)
    CurrencyRate.create_table(safe=True)
