from peewee import *

from .base_model import BaseModel


class User(BaseModel):
    user_id = AutoField()
    username = CharField(unique=True)
    password = CharField()
    email = CharField()
    cash_flow = DecimalField(decimal_places=2, default=0)
    join_date = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')])
