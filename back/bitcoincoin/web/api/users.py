from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource

from bitcoincoin.controllers.users import *
from bitcoincoin.errors.bad_resource import *
from bitcoincoin.errors.forbidden import *
from bitcoincoin.web.admins_id import admins_id


class Users(Resource):
    def get(self):
        filters = {}
        if "user" in request.args:
            try:
                user_id = int(request.args["user"])
                assert user_id > 0
            except:
                raise BadIdError(request.args["user"])
            else:
                filters["user_id"] = user_id

        if "username" in request.args:
            filters["username"] = request.args["username"]
        if "email" in request.args:
            filters["email"] = request.args["email"]
        if "sorted" in request.args:
            filters["sorted"] = request.args["sorted"]
        return search_users(filters)


class User(Resource):
    def get(self, user_id):
        try:
            user_id = int(user_id)
            assert user_id > 0
        except:
            raise BadIdError(user_id)
        return get_user_by_id(user_id)

    @jwt_required
    def delete(self, user_id):
        identity_id = int(get_jwt_identity()['id'])
        try:
            user_id = int(user_id)
            assert user_id > 0
        except:
            raise BadIdError(user_id)
        if identity_id not in admins_id and user_id != identity_id:
            raise ForbiddenAdminError()
        return delete_user(user_id)


class UserTransactions(Resource):
    def get(self, user_id):
        filters = {}
        if "currency" in request.args:
            try:
                currency_id = int(request.args["currency"])
                assert currency_id > 0
            except:
                raise BadIdError(user_id)
            else:
                filters["currency"] = currency_id
        if "limit" in request.args:
            try:
                limit = int(request.args["limit"])
                assert limit > 0
            except:
                raise BadLimitError(request.args["limit"])
            else:
                filters["limit"] = request.args["limit"]
        return get_user_transactions(user_id, filters)


class UserWallet(Resource):
    @jwt_required
    def get(self, user_id):
        identity_id = int(get_jwt_identity()['id'])
        try:
            user_id = int(user_id)
            assert user_id > 0
        except:
            raise BadIdError(user_id)
        if identity_id not in admins_id and user_id != identity_id:
            raise ForbiddenAdminError()
        return get_user_wallet(user_id)


class UserWalletCurrency(Resource):
    @jwt_required
    def get(self, user_id, currency_id):
        identity_id = int(get_jwt_identity()['id'])
        try:
            user_id = int(user_id)
            assert user_id > 0
        except:
            raise BadIdError(user_id)
        if identity_id not in admins_id and user_id != identity_id:
            raise ForbiddenAdminError()
        try:
            currency_id = int(currency_id)
            assert currency_id > 0
        except:
            raise BadIdError(currency_id)
        return get_user_wallet(user_id, currency_id)
