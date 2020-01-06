from peewee import *

from bitcoincoin.core import db

from .base_model import BaseModel
from .currency import Currency
from .user import User


class Wallet(BaseModel):
    user = ForeignKeyField(User)
    currency = ForeignKeyField(Currency)
    volume = IntegerField(default=0)


with db:
    Wallet.create_table(safe=True)
