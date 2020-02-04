from peewee import *
from playhouse.shortcuts import model_to_dict

from bitcoincoin.core import db

from . import User
from .base_model import BaseModel


class Bank(BaseModel):
    id = AutoField()
    name = CharField()
    symbol = CharField()

    @property
    def wallet_value(self):
        return sum([m.user.wallet_value for m in self.memberships])

    @property
    def cash_flow(self):
        return sum([m.user.cash_flow for m in self.memberships])

    def get_small_data(self):
        data = model_to_dict(self, recurse=False)
        data['wallet_value'] = self.wallet_value
        data['cash_flow'] = self.cash_flow
        return data

    def get_data(self):
        data = self.get_small_data()
        data['memberships'] = [m.get_small_data() for m in self.memberships]
        return data


class BankUser(BaseModel):
    id = AutoField()
    bank = ForeignKeyField(Bank, backref='memberships')
    user = ForeignKeyField(User)
    rank = CharField()

    def get_small_data(self):
        data = model_to_dict(self, recurse=False)
        data['user'] = self.user.get_small_data()
        return data


class BankJoinDemand(BaseModel):
    id = AutoField()
    bank = ForeignKeyField(Bank, backref='demands')
    user = ForeignKeyField(User)
    message = TextField()

    def get_small_data(self):
        data = model_to_dict(self, recurse=False)
        data['user'] = self.user.get_small_data()
        return data


with db:
    Bank.create_table(safe=True)
    BankUser.create_table(safe=True)
    BankJoinDemand.create_table(safe=True)
