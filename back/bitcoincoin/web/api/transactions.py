from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from datetime import datetime

from bitcoincoin.controllers.transactions import *
from bitcoincoin.errors.bad_resource import *


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
        if "from_date" in request.args:
            try:
                from_date = datetime.strptime(request.args["from_date"],'%Y-%m-%dT%H:%M:%S%z')
            except:
                raise BadFromDatetimeError(request.args["from_date"])
            filters["from_date"] = from_date
        if "to_date" in request.args:
            try:
                to_date = datetime.strptime(request.args["to_date"],'%Y-%m-%dT%H:%M:%S%z')
            except:
                raise BadToDatetimeError(request.args["to_date"])
            filters["to_date"] = to_date
        return search_transactions(filters)

    @jwt_required
    def post(self):
        data = request.json

        user_id = int(get_jwt_identity()['id'])
        if user_id in admin_ids and "user_id" in data:
            user_id = data["user_id"]
        try:
            user_id = int(user_id)
            assert user_id > 0
        except (ValueError, AssertionError):
            raise BadIdError(data["user_id"])

        try:
            currency_id = int(data["currency_id"])
            assert currency_id > 0
        except (ValueError, AssertionError):
            raise BadIdError(data["currency_id"])

        try:
            quantity = float(data["quantity"])
            assert quantity > 0
        except (ValueError, AssertionError):
            raise BadQuantityError(data["quantity"])
        if not isinstance(data["is_sale"], bool):
            raise BadBoolError(data["is_sale"])

        transaction = create_transaction(user_id, currency_id, quantity, data["is_sale"])
        return transaction.get_small_data()
