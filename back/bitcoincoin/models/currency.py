from peewee import *
from playhouse.shortcuts import model_to_dict

from bitcoincoin.core import db

from .base_model import BaseModel


class Currency(BaseModel):
    id = AutoField()
    coincap = CharField()
    name = CharField()
    symbol = CharField()
    rank = IntegerField()
    last_value = FloatField(null=True)

    @property
    def icon(self):
        return f'https://static.coincap.io/assets/icons/{str(self.symbol).lower()}@2x.png'

    def get_small_data(self):
        data = model_to_dict(self)
        data['icon'] = self.icon
        return data


class CurrencyRate(BaseModel):
    id = AutoField()
    currency = ForeignKeyField(Currency)
    datetime = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    value = FloatField()


with db:
    Currency.create_table(safe=True)
    CurrencyRate.create_table(safe=True)
