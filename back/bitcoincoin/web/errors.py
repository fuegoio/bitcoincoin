from . import app
from ..errors import NotFoundError


@app.errorhandler(NotFoundError)
def handle_error(error):
    return error.get_dict(), 404
