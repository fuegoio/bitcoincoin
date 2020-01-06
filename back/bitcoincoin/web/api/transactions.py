from flask import request
from flask_restful import Resource

from bitcoincoin.controllers.transactions import search_transactions, create_transaction
from bitcoincoin.errors.bad_resource import BadIdError, BadQuantityError


class Transactions(Resource):
    def get(self):
        filters = {}
        if "user" in request.args:
            try:
                user_id = int(request.args["user"])
                assert user_id > 0
            except:
                raise BadIdError(request.args["user"])
            filters["user"] = user_id
        if "currency" in request.args:
            try:
                user_id = int(request.args["currency"])
                assert user_id > 0
            except:
                raise BadIdError(request.args["currency"])
            filters["user"] = user_id
        return search_transactions(filters)

    def post(self):
        data = request.json
        try:
            user_id = int(data["user_id"])
            assert user_id > 0
        except:
            raise BadIdError(data["user_id"])
        try:
            currency_id = int(data["currency_id"])
            assert currency_id > 0
        except:
            raise BadIdError(data["currency_id"])
        try:
            quantity = int(data["quantity"])
            assert quantity > 0
        except:
            raise BadQuantityError(data["quantity"])
        return create_transaction(user_id, currency_id, quantity)
