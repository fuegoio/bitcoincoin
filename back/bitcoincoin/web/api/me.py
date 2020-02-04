from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource

from bitcoincoin.controllers.users import *
from bitcoincoin.errors.bad_resource import *


class Me(Resource):
    @jwt_required
    def get(self):
        user_id = get_jwt_identity()['id']
        return get_user_by_id(user_id)


class MeHistoric(Resource):
    @jwt_required
    def get(self):
        user_id = get_jwt_identity()['id']
        return get_user_value_history(user_id)


class MeTransactions(Resource):
    @jwt_required
    def get(self):
        user_id = get_jwt_identity()['id']

        filters = {}
        if "currency" in request.args:
            try:
                currency_id = int(request.args["currency"])
                assert currency_id > 0
            except:
                raise BadIdError(user_id)
            filters["currency"] = currency_id

        if "limit" in request.args:
            try:
                limit = int(request.args["limit"])
                assert limit > 0
            except:
                raise BadLimitError(request.args["limit"])

            filters["limit"] = request.args["limit"]

        return get_user_transactions(user_id, filters)


class MeWallet(Resource):
    @jwt_required
    def get(self):
        user_id = get_jwt_identity()['id']
        return get_user_wallet(user_id)


class MeWalletCurrency(Resource):
    @jwt_required
    def get(self, currency_id):
        user_id = get_jwt_identity()['id']

        try:
            currency_id = int(currency_id)
            assert currency_id > 0
        except:
            raise BadIdError(currency_id)

        wallets = get_user_wallet(user_id, currency_id)
        if len(wallets) > 0:
            return wallets[0]
        return None
