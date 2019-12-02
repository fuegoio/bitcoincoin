from peewee import PostgresqlDatabase

from .config import config

db = PostgresqlDatabase(
    'bitcoin',
    user='bitcoin',
    password='bitcoin',
    host=config['database']['host'],
    autorollback=True
)
