from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource

from bitcoincoin.controllers.banks import get_banks, create_bank, get_bank, ask_to_join_bank, join_bank


class Banks(Resource):
    @jwt_required
    def get(self):
        banks = get_banks()
        return banks

    @jwt_required
    def post(self):
        user_id = get_jwt_identity()['id']
        name = request.json['name']
        symbol = request.json['symbol']

        bank = create_bank(name, symbol, admin=user_id)
        return bank


class Bank(Resource):
    @jwt_required
    def get(self, bank_id):
        user_id = get_jwt_identity()['id']
        bank = get_bank(bank_id, user_id)
        return bank

    @jwt_required
    def post(self, bank_id):
        user_id = get_jwt_identity()['id']
        message = request.json['message']
        join_demand = ask_to_join_bank(bank_id, user_id, message=message)
        return join_demand
