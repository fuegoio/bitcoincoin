from peewee import *

from bitcoincoin.core import db

from .base_model import BaseModel


class Currency(BaseModel):
    id = AutoField()
    name = TextField()
    symbol = FixedCharField()
    last_value = FloatField()
    provider = TextField()


class CurrencyRate(BaseModel):
    id = AutoField()
    currency = ForeignKeyField(Currency)
    datetime = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    value = FloatField()
    provider = TextField()

    def save(self, **kwargs):
        super().save(self, **kwargs)
        currency = Currency.get(Currency.id == self.currency_id)
        currency.last_value = self.value
        currency.provider = self.provider
        currency.save()


with db:
    Currency.create_table(safe=True)
    CurrencyRate.create_table(safe=True)
