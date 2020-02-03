from celery.bin import worker

from bitcoincoin.tasks import celery

options = {'loglevel': 'INFO', 'beat': True}

if __name__ == '__main__':
    worker = worker.worker(app=celery)
    worker.run(**options)
