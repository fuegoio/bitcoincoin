import peewee as pw
import pytest

from bitcoincoin.controllers import transactions

def test_add_transaction(set_up_database):
    transaction = transactions.create_transaction(1, 1, 10)
