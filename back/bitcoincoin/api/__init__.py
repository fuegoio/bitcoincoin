from flask import Blueprint
from flask_restful import Api

from bitcoincoin.models.database import db

from .users import User, Users, UserTransactions
from .currencies import Currencies, Currency, CurrencyLastRate, CurrencyRates

api_bp = Blueprint("api", __name__)
api = Api(api_bp)


def register_api(app):
    @api_bp.before_request
    def before_request():
        # db.connect(reuse_if_open=True)
        pass

    @api_bp.teardown_request
    def after_request(exception=None):
        db.close()

    # @api_bp.errorhandler(pokedex.errors.NotFoundError)
    # def if_not_found(error):
    #     response = {"error": f"{error.resource} {error.resource_id} not found"}
    #     return response, 404

    api.add_resource(Users, "/users")
    api.add_resource(User, "/user/<user_id:int>")
    api.add_resource(
        UserTransactions, "/user/<user_id:int>/transactions"
    )  # TODO: ajouter un paramètre temporel pour ne pas get tout l'historique

    api.add_resource(Currencies, "/currencies")
    api.add_resource(Currency, "/currencies/<currency_id:int>")
    api.add_resource(
        CurrencyRates, "/currencies/<currency_id:int>/rates"
    )  # TODO: ajouter un paramètre temporel pour ne pas get tout l'historique
    api.add_resource(CurrencyLastRate, "/currencies/<currency_id:int>/rates/last")

    app.register_blueprint(api_bp, url_prefix="/api/v1")
