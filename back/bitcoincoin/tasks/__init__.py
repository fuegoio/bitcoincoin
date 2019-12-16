from celery import Celery

from bitcoincoin.core import config

celery = Celery(
    'bitcoincoin',
    broker=config.get('CELERY_BROKER_URL', 'redis://localhost'),
    backend=config.get('CELERY_BACKEND_URL', 'redis://localhost')
)
celery.conf.update({'worker_hijack_root_logger': False})

from . import currencies
