from flask import Blueprint
from flask_restful import Api

from bitcoincoin.core import db
from .currencies import Currencies, Currency, CurrencyLastRate, CurrencyRates
from .transactions import Transactions
from .users import (
    User,
    Users,
    UserTransactions,
    UserLastTransaction,
    UserWallet,
    UserWalletCurrency,
)
from .. import app

api_bp = Blueprint("api", __name__)
api = Api(api_bp)


@api_bp.before_request
def before_request():
    db.connect(reuse_if_open=True)
    pass


@api_bp.teardown_request
def after_request(exception=None):
    db.close()


api.add_resource(Users, "/users")
api.add_resource(User, "/users/<user_id>")
api.add_resource(UserTransactions, "/users/<user_id>/transactions")
api.add_resource(UserLastTransaction, "/users/<user_id>/transactions/last")
api.add_resource(UserWallet, "/users/<user_id>/wallet")
api.add_resource(UserWalletCurrency, "/users/<user_id>/wallet/<currency_id>")

api.add_resource(Currencies, "/currencies")
api.add_resource(Currency, "/currencies/<currency_id>")
api.add_resource(CurrencyRates, "/currencies/<currency_id>/rates")
api.add_resource(CurrencyLastRate, "/currencies/<currency_id>/rates/last")

api.add_resource(Transactions, "/transactions")

app.register_blueprint(api_bp, url_prefix="/api/v1")
