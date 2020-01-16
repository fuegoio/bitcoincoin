from peewee import *

from bitcoincoin.core import db

from .base_model import BaseModel


class User(BaseModel):
    id = AutoField()
    email = CharField(unique=True)
    username = CharField(unique=True)
    password = CharField()
    cash_flow = DecimalField(decimal_places=2, default=0)
    join_date = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    def get_identity(self):
        return {"id": self.id, "username": self.username, "email": self.email}


with db:
    User.create_table(safe=True)
