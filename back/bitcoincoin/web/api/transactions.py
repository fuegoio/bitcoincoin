from flask import request
from flask_restful import Resource

from bitcoincoin.controllers.transactions import search_transactions, create_transaction


class Transactions(Resource):
    def get(self):
        return search_transactions(request.args)

    def post(self):
        data = request.json
        # TODO: raise errors for bad parameters
        user_id = int(data["user_id"])
        currency_id = int(data["currency_id"])
        quantity = int(data["quantity_id"])
        return create_transaction(=user_id, currency_id, quantity)
