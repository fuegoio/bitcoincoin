from peewee import *
from playhouse.shortcuts import model_to_dict


class CurrencyRates(BaseModel):
    id = PrimaryKeyField()
    currency_id = ForeignKeyField()
    datetime = DateTimeField()
    value = FloatField()

class LastCurrency(BaseModel):
    id = PrimaryKeyField()
    name = TextField()