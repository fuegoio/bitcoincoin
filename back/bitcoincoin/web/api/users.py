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
        filters = {}
        if "id" in request.args:
        try:
            id = int(request.args["user"]) 
            assert id > 0
        except:
            raise NameError("Id should be an int")
        else:
            filters["id"] = id
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
            raise NameError("Id should be an int")
        return get_user_by_id(user_id)

    def delete(self, user_id):
        try:
            user_id = int(user_id)
            assert user_id > 0
        except:
            raise NameError("Id should be an int")
        return delete_user(user_id)


class UserTransactions(Resource):
    def get(self, user_id):
        filters = {}
        if "currency" in request.args:
            try:
                currency_id = int(request.args["currency"])
                assert currency_id > 0
            except:
                raise NameError("Currency_id should be an int")
            else:
                filters["currency"] = currency_id 
        if "limit" in request.args:
            try:
                limit = int(limit)
                assert limit > 0
            except:
                raise NameError("Limit should be an int")
            else filters["limit"] = limit             
        return get_user_transactions(user_id, filters)


#class UserLastTransaction(Resource):
#    def get(self, user_id):
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
            raise NameError("Id should be an int")
        return get_user_wallet(user_id)


class UserWalletCurrency(Resource):
    def get(self, user_id, currency_id):
        try:
            user_id = int(user_id)
            assert user_id > 0
        except:
            raise NameError("user_id should be an int")
        try:
            currency_id = int(currency_id)
            assert currency_id > 0
        except:
            raise NameError("currency_id should be an int")
        return get_user_wallet(user_id, currency_id)
