from peewee import Model
from playhouse.shortcuts import model_to_dict

from .database import db


class BaseModel(Model):
    def get_small_data(self):
        return model_to_dict(self, recurse=False, backrefs=False)

    class Meta:
        database = db