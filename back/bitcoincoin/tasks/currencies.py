from . import celery


@celery.task
def retrieve_currencies():
    pass
