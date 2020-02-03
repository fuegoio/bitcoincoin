from peewee import *
from playhouse.shortcuts import model_to_dict

from bitcoincoin.core import db
from .base_model import BaseModel
from .currency import Currency
from .user import User


class Transaction(BaseModel):
    user = ForeignKeyField(User)
    currency = ForeignKeyField(Currency)
    quantity = FloatField()
    value = FloatField()
    is_sale = BooleanField()
    datetime = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    def get_small_data(self, currency=False, user=False):
        data = model_to_dict(self, recurse=False, backrefs=False)

        if user:
            data['user'] = self.user.get_small_data()
        if currency:
            data['currency'] = self.currency.get_small_data()

        return data


with db:
    Transaction.create_table(safe=True)
