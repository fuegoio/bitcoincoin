from flask import request
from flask_restful import Resource

# TODO: import from managers all useful functions
# search_users(query)
# get_user_by_id(user_id)
# delete_user(user_id)
# get_user_transactions(user_id, query)
# get_user_last_transaction(user_id, query)
# get_user_wallet(user_id, currency_id=None)


class Users(Resource):
    def get(self):
        return search_users(request.args["query"])


class User(Resource):
    def get(self, user_id):
        return get_user_by_id(user_id)

    def delete(self, user_id):
        return delete_user(user_id)


class UserTransactions(Resource):
    def get(self, user_id):
        return get_user_transactions(user_id, request.args["query"])


class UserLastTransaction(Resource):
    def get(self, user_id):
        return get_user_last_transaction(user_id, request.args["query"])


class UserWallet(Resource):
    def get(self, user_id):
        return get_user_wallet(user_id)


class UserWalletCurrency(Resource):
    def get(self, user_id, currency_id):
        return get_user_wallet(user_id, currency_id)
