from peewee import *

from bitcoincoin.core import db

from .base_model import BaseModel
from .currency import Currency
from .user import User


class Wallet(BaseModel):
    user = ForeignKeyField(User, backref='currencies')
    currency = ForeignKeyField(Currency)
    volume = FloatField()

    @property
    def value(self):
        return self.currency.last_value * self.volume


with db:
    Wallet.create_table(safe=True)
