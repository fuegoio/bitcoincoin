from peewee import *

from .base_model import BaseModel
from .user import User
from .currency import Currency


class Wallet(BaseModel):
    user = ForeignKeyField(User)
    currency = ForeignKeyField(Currency)
    volume = IntegerField(default=0)
