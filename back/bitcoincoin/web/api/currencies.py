from flask import request
from flask_restful import Resource

# TODO: import from managers all useful functions
# search_currencies(query)
# create_currency(name, symbol)
# get_currency_by_id(currency_id)
# delete_currency(currency_id)
# get_currency_last_rate(currency_id)
# get_currency_rates_history(currency_id, query)
# create_currency_rate(currency_id, value)

from bitcoincoin.controllers.currencies import *
from bitcoincoin.errors.bad_resource import *


class Currencies(Resource):
    def get(self):
        return search_currencies(request.args)

    # is it useful ? or we create currencies only in backend ?
    def post(self):
        data = request.json
        try:
            name = str(data["name"])
            assert len(name) > 0
        except:
            raise EmptyStringError(data["name"])
        try:
            symbol = str(data["symbol"])
            assert len(name) > 0
        except:
            raise EmptyStringError(data["symbol"])
        try:
            last_value = float(data["last_value"])
            assert last_value > 0
        except:
            raise BadCurrencyValueError(data["last_value"])
        try:
            provider = str(data["provider"])
            assert provider in ["cryptocompare", "coincap"]
        except:
            raise BadCurrencyProviderError(data["provider"])
        return create_currency(
            name=name, symbol=symbol, last_value=last_value, provider=provider
        )


class Currency(Resource):
    def get(self, currency_id):
        try:
            currency_id = int(currency_id)
            assert currency_id > 0
        except:
            raise BadIdError(currency_id)
        return get_currency_by_id(currency_id)

    def delete(self, currency_id):
        try:
            currency_id = int(currency_id)
            assert currency_id > 0
        except:
            raise BadIdError(currency_id)
        return delete_currency(currency_id)


class CurrencyRates(Resource):
    def get(self, currency_id):
        try:
            currency_id = int(currency_id)
            assert currency_id > 0
        except:
            raise BadIdError(currency_id)
        return get_currency_rates_history(currency_id, request.args)

    def post(self, currency_id):
        data = request.json
        try:
            currency_id = int(currency_id)
            assert currency_id > 0
        except:
            raise BadIdError(currency_id)
        # try:
        #     datetime = #TODO
        # except:
        #     raise TypeError('date in not well given')
        try:
            value = float(data["value"])
            assert value > 0
        except:
            raise BadCurrencyValueError(value)
        return create_currency_rate(currency_id=currency_id, value=value)


class CurrencyLastRate(Resource):
    def get(self, currency_id):
        return get_currency_last_rate(currency_id)
