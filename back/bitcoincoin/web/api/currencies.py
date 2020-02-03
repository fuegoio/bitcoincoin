from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource

from bitcoincoin.controllers.currencies import *
from bitcoincoin.errors.bad_resource import *
from bitcoincoin.errors.forbidden import *
from bitcoincoin.tasks.coincap import update_currencies, fetch_currency_history
from bitcoincoin.web.admins_id import admins_id


class Currencies(Resource):
    def get(self):
        return search_currencies(request.args)

    @jwt_required
    def post(self):
        if get_jwt_identity()['id'] not in admins_id:
            raise ForbiddenAdminError()
        task = update_currencies.delay()
        return {"msg": "success"}


class Currency(Resource):
    def get(self, currency_id):
        try:
            currency_id = int(currency_id)
            assert currency_id > 0
        except:
            raise BadIdError(currency_id)
        return get_currency_by_id(currency_id)

    @jwt_required
    def delete(self, currency_id):
        if not get_jwt_identity()['id'] in admins_id:
            raise ForbiddenAdminError()
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
                from_date = datetime.strptime(request.args["from_date"], '%Y-%m-%dT%H:%M:%S%z')
            except:
                raise BadFromDatetimeError(request.args["from_date"])
        to_date = None
        if "to_date" in request.args:
            try:
                to_date = datetime.strptime(request.args["to_date"], '%Y-%m-%dT%H:%M:%S%z')
            except:
                raise BadToDatetimeError(request.args["to_date"])
        return get_currency_rates_history(currency_id, from_date, to_date)

    @jwt_required
    def post(self, currency_id):
        if get_jwt_identity()['id'] not in admins_id:
            raise ForbiddenAdminError()
        task = fetch_currency_history.delay(currency_id)
        return {"msg": "success"}
