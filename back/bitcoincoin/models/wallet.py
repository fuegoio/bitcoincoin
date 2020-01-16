from peewee import *
from playhouse.shortcuts import model_to_dict

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

    def get_small_data(self):
        wallet_dict = model_to_dict(self, recurse=False)
        wallet_dict['currency'] = self.currency.get_small_data()
        return wallet_dict


with db:
    Wallet.create_table(safe=True)
