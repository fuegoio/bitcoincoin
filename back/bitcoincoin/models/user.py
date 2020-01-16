from peewee import *

from bitcoincoin.core import db

from .base_model import BaseModel


class User(BaseModel):
    id = AutoField()
    email = CharField(unique=True)
    username = CharField(unique=True)
    password = CharField()
    cash_flow = FloatField(default=1000000)
    join_date = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    @property
    def wallet_value(self):
        return round(sum([c.value for c in self.currencies]), 2)

    def get_small_data(self):
        return {"id": self.id, "username": self.username, "email": self.email,
                "cash_flow": self.cash_flow,
                "join_date": self.join_date,
                "wallet_value": self.wallet_value,
                "value": self.cash_flow + self.wallet_value}


with db:
    User.create_table(safe=True)
