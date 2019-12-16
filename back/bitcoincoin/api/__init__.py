from flask import Blueprint
from flask_restful import Api

from .users import (
    User,
    Users,
    UserTransactions,
    UserLastTransaction,
    UserWallet,
    UserWalletCurrency,
)
from .currencies import Currencies, Currency, CurrencyLastRate, CurrencyRates
from .transactions import Transactions
from bitcoincoin.core import db


api_bp = Blueprint("api", __name__)
api = Api(api_bp)


def register_api(app):
    @api_bp.before_request
    def before_request():
        db.connect(reuse_if_open=True)
        pass

    @api_bp.teardown_request
    def after_request(exception=None):
        db.close()

    api.add_resource(Users, "/users")
    api.add_resource(User, "/users/<user_id:int>")
    api.add_resource(UserTransactions, "/users/<user_id:int>/transactions")
    api.add_resource(UserLastTransaction, "/users/<user_id:int>/transactions/last")
    api.add_resource(UserWallet, "/users/<user_id:int>/wallet")
    api.add_resource(UserWalletCurrency, "/users/<user_id:int>/wallet/<currency_id:int>")

    api.add_resource(Currencies, "/currencies")
    api.add_resource(Currency, "/currencies/<currency_id:int>")
    api.add_resource(CurrencyRates, "/currencies/<currency_id:int>/rates")
    api.add_resource(CurrencyLastRate, "/currencies/<currency_id:int>/rates/last")

    api.add_resource(Transactions, "/transactions")

    app.register_blueprint(api_bp, url_prefix="/api/v1")
