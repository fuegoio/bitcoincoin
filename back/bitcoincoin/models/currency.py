from peewee import *
from playhouse.shortcuts import model_to_dict
from base_model import BaseModel

class CurrencyRates(BaseModel):
    id = PrimaryKeyField()
    currency_id = ForeignKeyField(Currencies)
    datetime = DateTimeField()
    value = FloatField()

    def save(self):
        BaseModel.save(self)
        currency = Currencies.get(Currencies.id == self.currency_id)
        currency.last_value = self.value

class Currencies(BaseModel):
    id = PrimaryKeyField()
    name = TextField()
    last_value = FloatField()
