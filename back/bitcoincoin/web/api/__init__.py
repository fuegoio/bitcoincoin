from flask import Blueprint
from flask_restful import Api

from bitcoincoin.core import db
from .currencies import Currencies, Currency, CurrencyRates
from .transactions import Transactions
from .users import (
    User,
    Users,
    UserTransactions,
    UserWallet,
    UserWalletCurrency,
)
from .me import Me, MeTransactions, MeWallet, MeWalletCurrency, MeHistoric
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
api.add_resource(User, "/users/<int:user_id>")
api.add_resource(UserTransactions, "/users/<int:user_id>/transactions")
api.add_resource(UserWallet, "/users/<int:user_id>/wallet")
api.add_resource(UserWalletCurrency, "/users/<int:user_id>/wallet/<int:currency_id>")

api.add_resource(Me, "/me")
api.add_resource(MeHistoric, "/me/historic")
api.add_resource(MeTransactions, "/me/transactions")
api.add_resource(MeWallet, "/me/wallet")
api.add_resource(MeWalletCurrency, "/me/wallet/<int:currency_id>")

api.add_resource(Currencies, "/currencies")
api.add_resource(Currency, "/currencies/<int:currency_id>")
api.add_resource(CurrencyRates, "/currencies/<int:currency_id>/rates")

api.add_resource(Transactions, "/transactions")

app.register_blueprint(api_bp, url_prefix="/api/v1")
