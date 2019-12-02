from flask import request
from flask_restful import Resource

# TODO: import from managers all useful functions
# search_users(query)
# get_user_by_id(user_id)
# delete_user(user_id)


class Users(Resource):
    def get(self):
        return search_users(request.args["query"])


class User(Resource):
    def get(self, user_id):
        return get_user_by_id(user_id)

    def delete(self, user_id):
        return delete_user(user_id)
