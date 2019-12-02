from peewee import *

from bitcoincoin.core import db

from .base_model import BaseModel
from .currency import Currency
from .user import User


class Transaction(BaseModel):
    user = ForeignKeyField(User)
    currency = ForeignKeyField(Currency)
    quantity = IntegerField(default=0)
    value = DecimalField(decimal_places=2)
    datetime = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])


with db:
    Transaction.create_table(fail_silently=True)
