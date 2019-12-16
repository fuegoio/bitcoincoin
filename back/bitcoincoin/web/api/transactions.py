from flask import request
from flask_restful import Resource

from bitcoincoin.controllers.transactions import search_transactions

# TODO: import from managers all useful functions
# search_transactions(query)
# create_transaction(user_id, currency_id, quantity)


class Transactions(Resource):
    def get(self):
        return search_transactions(request.args)

    def post(self):
        data = request.json
        return create_transaction(
            data["user_id"], data["currency_id"], data["quantity"]
        )
