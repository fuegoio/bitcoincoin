from flask import request
from flask_restful import Resource

from bitcoincoin.errors.bad_resource import BadIdError, BadLimitError
from bitcoincoin.controllers.users import search_users, get_user_transactions, get_user_wallet, get_user_by_id, \
    delete_user


class Users(Resource):
    def get(self):
        filters = {}
        if "user" in request.args:
            try:
                user_id = int(request.args["user"])
                assert user_id > 0
            except:
                raise BadIdError(request.args["user"])
            else:
                filters["user_id"] = user_id

        if "username" in request.args:
            filters["username"] = request.args["username"]
        if "email" in request.args:
            filters["email"] = request.args["email"]

        return search_users(filters)


class User(Resource):
    def get(self, user_id):
        try:
            user_id = int(user_id)
            assert user_id > 0
        except:
            raise BadIdError(user_id)
        return get_user_by_id(user_id)

    def delete(self, user_id):
        try:
            user_id = int(user_id)
            assert user_id > 0
        except:
            raise BadIdError(user_id)
        return delete_user(user_id)


class UserTransactions(Resource):
    def get(self, user_id):
        filters = {}
        if "currency" in request.args:
            try:
                currency_id = int(request.args["currency"])
                assert currency_id > 0
            except:
                raise BadIdError(user_id)
            else:
                filters["currency"] = currency_id

        if "limit" in request.args:
            try:
                limit = int(request.args["limit"])
                assert limit > 0
            except:
                raise BadLimitError(request.args["limit"])
            else:
                filters["limit"] = request.args["limit"]

        return get_user_transactions(user_id, filters)


class UserLastTransaction(Resource):
    def get(self, user_id):
        pass
#        try:
#            user_id = int(user_id)
#            assert user_id > 0
#        except:
#            raise NameError("Id should be an int")
#        filters = {}
#        if "currency" in request.args:
#            try:
#                currency_id = int(request.args["currency"])                assert currency_id > 0
#            except:
#                raise NameError("Currency_id should be an int")
#            else:
#                filters["currency"] = currency_id
#        return get_user_last_transaction(user_id, filters)


class UserWallet(Resource):
    def get(self, user_id):
        try:
            user_id = int(user_id)
            assert user_id > 0
        except:
            raise BadIdError(user_id)
        return get_user_wallet(user_id)


class UserWalletCurrency(Resource):
    def get(self, user_id, currency_id):
        try:
            user_id = int(user_id)
            assert user_id > 0
        except:
            raise BadIdError(user_id)
        try:
            currency_id = int(currency_id)
            assert currency_id > 0
        except:
            raise BadIdError(currency_id)
        return get_user_wallet(user_id, currency_id)
