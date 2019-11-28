from peewee import *

from .base_model import BaseModel
from .user import User
from .currency import Currency


class Transaction(BaseModel):
    user = ForeignKeyField(User)
    currency = ForeignKeyField(Currency)
    quantity = IntegerField(default=0)
    value = DecimalField(decimal_places=2)
    datetime = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
