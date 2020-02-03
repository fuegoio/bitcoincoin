from . import app
from bitcoincoin.errors.not_found import NotFoundError
from bitcoincoin.errors.bad_resource import BadResourceError
from bitcoincoin.errors.forbidden import ForbiddenError


@app.errorhandler(NotFoundError)
def handle_not_founds(error):
    return error.get_dict(), 404


@app.errorhandler(BadResourceError)
def handle_bad_resources(error):
    return error.get_dict(), 400


@app.errorhandler(ForbiddenError)
def handle_forbiddens(error):
    return error.get_dict(), 403
