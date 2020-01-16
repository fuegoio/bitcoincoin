from peewee import *

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


with db:
    Transaction.create_table(safe=True)
