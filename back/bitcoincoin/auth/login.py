from flask import Blueprint, jsonify, request, redirect
from flask_jwt_extended import JWTManager, create_access_token

from bitcoincoin.core import config, db


def register_auth(app):
    jwt = JWTManager(app)
    auth_bp = Blueprint('login', __name__)

    @auth_bp.route('/login')
    @db.connection_context()
    def login():
        # TODO : Add user login check
        user = None

        access_token = create_access_token(identity=user.get_identity())
        return jsonify(access_token=access_token), 200

    app.register_blueprint(auth_bp, url_prefix="/auth")
