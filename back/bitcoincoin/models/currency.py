from peewee import *

from bitcoincoin.core import db

from .base_model import BaseModel


class Currency(BaseModel):
    id = AutoField()
    name = TextField()
    symbol = FixedCharField(max_length=3)
    last_value = FloatField()


class CurrencyRate(BaseModel):
    id = AutoField()
    currency = ForeignKeyField(Currency)
    datetime = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    value = FloatField()

    def save(self, **kwargs):
        super().save(self, **kwargs)
        currency = Currency.get(Currency.id == self.currency_id)
        currency.last_value = self.value
        currency.save()


with db:
    Currency.create_table(fail_silently=True)
    CurrencyRate.create_table(fail_silently=True)
