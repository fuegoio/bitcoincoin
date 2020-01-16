from flask import request
from flask_restful import Resource
from datetime import datetime

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
        from_date = None
        if "from_date" in request.args:
            try:
                from_date = datetime.strptime(request.args["from_date"],'%Y-%m-%dT%H:%M:%S%z')
            except:
                raise BadFromDatetimeError(request.args["from_date"])
        to_date = None
        if "to_date" in request.args:
            try:
                to_date = datetime.strptime(request.args["to_date"],'%Y-%m-%dT%H:%M:%S%z')
            except:
                raise BadToDatetimeError(request.args["to_date"])
        return get_currency_rates_history(currency_id, from_date, to_date)

    def post(self, currency_id, provider):
        data = request.json
        try:
            currency_id = int(currency_id)
            assert currency_id > 0
        except:
            raise BadIdError(currency_id)
        try:
            value = float(data["value"])
            assert value > 0
        except:
            raise BadCurrencyValueError(value)
        try:
            provider = str(data["provider"])
            assert provider in ["cryptocompare", "coincap"]
        except:
            raise BadCurrencyProviderError(data["provider"])
        return create_currency_rate(currency_id=currency_id, value=value, provider=provider)


class CurrencyLastRate(Resource):
    def get(self, currency_id):
        return get_currency_last_rate(currency_id)
