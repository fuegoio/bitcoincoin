from flask import Flask
from flask_cors import CORS

from bitcoincoin.api import register_api
from bitcoincoin.auth import register_auth


def create_app():
    app = Flask(__name__)
    app.config['ENV'] = 'development'
    app.config['DEBUG'] = True

    CORS(app, resources={r"*": {"origins": "*"}}, supports_credentials=True)

    register_auth(app)
    register_api(app)

    return app
