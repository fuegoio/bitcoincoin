from flask import Blueprint
from flask_restful import Api

from bitcoincoin.core import db

api_bp = Blueprint("api", __name__)
api = Api(api_bp)


def register_api(app):
    @api_bp.before_request
    def before_request():
        db.connect(reuse_if_open=True)
        pass

    @api_bp.teardown_request
    def after_request(exception=None):
        db.close()

    app.register_blueprint(api_bp, url_prefix="/api/v1")
