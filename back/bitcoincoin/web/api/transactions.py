from flask import request
from flask_restful import Resource

from bitcoincoin.controllers.transactions import search_transactions, create_transaction
from bitcoincoin.errors.bad_resource import BadIdError, BadQuantityError, BadBoolError


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
                currency_id = int(request.args["currency"])
                assert currency_id > 0
            except:
                raise BadIdError(request.args["currency"])
            filters["currency"] = currency_id
        return search_transactions(filters)

    def post(self):
        data = request.json
        try:
            user_id = int(data["user_id"])
            assert user_id > 0
        except ValueError, AssertionError:
            raise BadIdError(data["user_id"])
        try:
            currency_id = int(data["currency_id"])
            assert currency_id > 0
        except ValueError, AssertionError:
            raise BadIdError(data["currency_id"])
        try:
            quantity = int(data["quantity"])
            assert quantity > 0
        except ValueError, AssertionError:
            raise BadQuantityError(data["quantity"])
        if not isinstance(data["is_sell"], bool):
            raise BadBoolError(is_sell)
        return create_transaction(user_id, currency_id, quantity, data["is_sell"])
