from flask import Blueprint
from flask_restful import Api

from pokedex.models.database import db
import pokedex

from .pokemons import Pokemon, Pokemons
from .species import Species, Specie
from .types import Types
from .egg_groups import EggGroups

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

import requests
url = 'https://rest.coinapi.io/v1/exchanges'
headers = {'X-CoinAPI-Key' : '2A4700C5-30A8-4713-88F9-E32DA83071E0'}
response = requests.get(url, headers=headers)
print(response.json()[0])

import requests
url = 'https://rest.coinapi.io/v1/assets'
headers = {'X-CoinAPI-Key' : '2A4700C5-30A8-4713-88F9-E32DA83071E0'}
response = requests.get(url, headers=headers)
print(response.json()[0])

import requests
url = 'https://rest.coinapi.io/v1/symbols'
headers = {'X-CoinAPI-Key' : '73034021-THIS-IS-SAMPLE-KEY'}
response = requests.get(url, headers=headers)
print(response.json()[0])


def register_api(app):
    @api_bp.before_request
    def before_request():
        # db.connect(reuse_if_open=True)
        pass

    @api_bp.teardown_request
    def after_request(exception=None):
        db.close()

    @api_bp.errorhandler(pokedex.errors.NotFoundError)
    def if_not_found(error):
        response = {"error": f"{error.resource} {error.resource_id} not found"}
        return response, 404

    api.add_resource(Pokemons, '/pokemons')
    api.add_resource(Pokemon, '/pokemon/<pokemon_name>')
    api.add_resource(Types, '/types')
    api.add_resource(Species, '/species')
    api.add_resource(Specie, '/specie/<specie_id>')
    api.add_resource(EggGroups, '/egggroups')

    app.register_blueprint(api_bp, url_prefix="/api/v1")
