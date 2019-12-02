from peewee import *

from .base_model import BaseModel


class Currency(BaseModel):
    id = PrimaryKeyField()
    name = TextField()
    last_value = FloatField()


class CurrencyRate(BaseModel):
    id = PrimaryKeyField()
    currency = ForeignKeyField(Currency)
    datetime = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    value = FloatField()

    def save(self, **kwargs):
        super().save(self, **kwargs)
        currency = Currency.get(Currency.id == self.currency_id)
        currency.last_value = self.value
        currency.save()
