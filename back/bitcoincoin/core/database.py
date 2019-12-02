from peewee import PostgresqlDatabase

from .config import config

db = PostgresqlDatabase(
    'bitcoincoin',
    user='bitcoincoin',
    password='bitcoincoin',
    host=config['database']['host'],
    autorollback=True
)
