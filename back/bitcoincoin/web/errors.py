from . import app
from ..errors import NotFoundError
from ..errors.bad_resource import BadResourceError


@app.errorhandler(NotFoundError)
def handle_not_founds(error):
    return error.get_dict(), 404


@app.errorhandler(BadResourceError)
def handle_bad_resources(error):
    return error.get_dict(), 400
