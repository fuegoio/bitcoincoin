import os

from peewee import PostgresqlDatabase

db = PostgresqlDatabase(
    'bitcoincoin',
    user='bitcoincoin',
    password='bitcoincoin',
    host=os.environ.get('DB_HOST', 'localhost'),
    autorollback=True
)
