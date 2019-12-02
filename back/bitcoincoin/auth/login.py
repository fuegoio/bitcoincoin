import hashlib

from flask import Blueprint, jsonify, request, redirect
from flask_jwt_extended import JWTManager, create_access_token

from bitcoincoin.core import config, db
from bitcoincoin.models.user import User


def register_auth(app):
    jwt = JWTManager(app)
    auth_bp = Blueprint('login', __name__)

    @auth_bp.route('/register')
    @db.connection_context()
    def register():
        email = request.json['email']
        password = request.json['password']
        username = request.json['username']

        hash = hashlib.sha256()
        hash.update(password)
        password_hash = hash.hexdigest()

        user = User.create(username=username, email=email, password=password_hash)

        access_token = create_access_token(identity=user.get_identity())
        return jsonify(access_token=access_token), 200

    @auth_bp.route('/login')
    @db.connection_context()
    def login():
        email = request.json['email']
        password = request.json['password']

        hash = hashlib.sha256()
        hash.update(password)
        password_hash = hash.hexdigest()

        user = User.get_or_none(email=email, password=password_hash)
        if user is None:
            return jsonify({'msg': 'Unknown email or password not matching'}), 403

        access_token = create_access_token(identity=user.get_identity())
        return jsonify(access_token=access_token), 200

    app.register_blueprint(auth_bp, url_prefix="/auth")
