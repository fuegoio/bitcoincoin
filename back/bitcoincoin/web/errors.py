from . import app
from ..errors import NotFoundError
from ..errors.bad_resource import BadResource


@app.errorhandler(NotFoundError)
def handle_not_founds(error):
    return error.get_dict(), 404


@app.errorhandler(BadResource)
def handle_bad_resources(error):
    return error.get_dict(), 400
