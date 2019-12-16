from flask import Flask
from flask_cors import CORS


app = Flask('bitcoincoin')
app.config['ENV'] = 'development'
app.config['DEBUG'] = True

CORS(app, resources={r"*": {"origins": "*"}}, supports_credentials=True)

from . import errors
from . import auth
from . import api
