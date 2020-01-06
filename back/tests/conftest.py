import peewee

from bitcoincoin.core import config, db

import pytest


@pytest.fixture
def set_up_database():
    config['database']['schema'] = 'tests'

    db.connect()
    try:
        db.execute_sql('create schema tests;')
    except peewee.ProgrammingError:
        pass

    from bitcoincoin import models

    yield

    db.execute_sql('drop schema tests cascade;')
    db.close()
