from flask import Flask
from flask_cors import CORS

from .encoder import EnhancedJSONEncoder

app = Flask('bitcoincoin')
app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['JWT_SECRET_KEY'] = 'test'
app.config['RESTFUL_JSON'] = {'cls': EnhancedJSONEncoder}

CORS(app, resources={r"*": {"origins": "*"}}, supports_credentials=True)

from . import errors
from . import auth
from . import api
