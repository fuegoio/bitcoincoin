from flask import request
from flask_restful import Resource

# TODO: import from managers all useful functions
# search_currencies(query)
# create_currency(name, symbol)
# get_currency_by_id(currency_id)
# delete_currency(currency_id)


class Currencies(Resource):
    def get(self):
        return search_currencies(request.args["query"])

    # is it useful ? we create currencies only in backend
    def post(self):
        data = request.json
        return create_currency(data["name"], data["symbol"])


class Currency(Resource):
    def get(self, currency_id):
        return get_currency_by_id(currency_id)

    def delete(self, currency_id):
        return delete_currency(currency_id)
