from peewee import *

from bitcoincoin.core import db

from .base_model import BaseModel


class User(BaseModel):
    id = AutoField()
    username = CharField(unique=True)
    password = CharField()
    email = CharField()
    cash_flow = DecimalField(decimal_places=2, default=0)
    join_date = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])


with db:
    User.create_table(fail_silently=True)
