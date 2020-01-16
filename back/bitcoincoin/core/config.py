import logging
import os

config = {
    "database": {
        "host": os.environ.get('DB_HOST', 'localhost'),
        "schema": "public"
    }
}

logger = logging.getLogger()
formatter = logging.Formatter('%(process)d %(asctime)s %(name)-12s %(levelname)-8s %(message)s')

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

log_level = config.get('log', 'INFO')
if log_level == 'DEBUG':
    logger.setLevel(logging.DEBUG)
else:
    logger.setLevel(logging.INFO)

logger = logging.getLogger('bitcoincoin')

version = '0.1.0'
