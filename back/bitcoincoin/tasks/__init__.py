from celery import Celery

from bitcoincoin.core import config


celery = Celery(
    'bitcoincoin',
    broker=config.get('CELERY_BROKER_URL', 'redis://localhost'),
    backend=config.get('CELERY_BACKEND_URL', 'redis://localhost')
)
celery.conf.update({'worker_hijack_root_logger': False})
celery.conf.beat_schedule = {
    'update_currencies_every_seconds': {
        'task': 'bitcoincoin.tasks.coincap.update_currencies',
        'schedule': 1.0,
    },
}
celery.conf.timezone = 'UTC'

from . import coincap
