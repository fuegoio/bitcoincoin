import datetime

import pendulum
import requests

from bitcoincoin.controllers.currencies import create_currency, create_currency_rate
from bitcoincoin.models.currency import Currency

from . import celery
from ..core import logger

HEADERS = {'Accept-Encoding': 'gzip'}


@celery.task
def update_currencies():
    logger.info('[Currencies] Updating currencies ...')
    request = requests.get('https://api.coincap.io/v2/assets', headers=HEADERS)
    currency_rates = request.json()

    for i, currency_rate in enumerate(currency_rates['data']):
        logger.info(f'[Currencies] Updating currencies ... ({i}/{len(currency_rates["data"])})')

        coincap_name = currency_rate["id"]
        rank = currency_rate["rank"]
        symbol = currency_rate['symbol']
        name = currency_rate["name"]
        value = currency_rate["priceUsd"]
        currency = Currency.get_or_none(symbol=symbol)
        if currency is None:
            currency = create_currency(name=name, symbol=symbol, rank=rank, coincap_name=coincap_name)
        create_currency_rate(currency_id=currency.id, value=value)

    return True


@celery.task
def fetch_currency_history(currency_id):
    logger.info(f'[Currencies] Updating currency rate of currency {currency_id} ...')
    currency = Currency.get_or_none(id=currency_id)

    def insert_rates(request):
        history = request.json()
        for rate in history['data']:
            currency_rate = rate['priceUsd']
            time = pendulum.from_timestamp(rate['time'] / 1000, tz='UTC')
            create_currency_rate(currency_id=currency.id, value=currency_rate, datetime=time)

    if currency is not None:
        # 1 Day interval
        logger.info(f'[Currencies] Updating currency with 1 day interval ...')
        request = requests.get("https://api.coincap.io/v2/assets/{}/history?interval=d1".format(currency.coincap))
        insert_rates(request)

        # 1 Hour interval
        logger.info(f'[Currencies] Updating currency with 1 hour interval ...')
        request = requests.get("https://api.coincap.io/v2/assets/{}/history?interval=h1".format(currency.coincap))
        insert_rates(request)

        # 1 Minute interval
        logger.info(f'[Currencies] Updating currency with 1 minute interval ...')
        request = requests.get("https://api.coincap.io/v2/assets/{}/history?interval=m1".format(currency.coincap))
        insert_rates(request)

    return True
