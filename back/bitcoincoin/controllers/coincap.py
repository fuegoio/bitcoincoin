import requests
from playhouse.shortcuts import update_model_from_dict
import datetime

from bitcoincoin.models.currency import Currency, CurrencyRate
from .currencies import search_currencies, create_currency_rate

headers = {'Accept-Encoding' : 'gzip'}
def load_currency_rates():
    request = requests.get('https://api.coincap.io/v2/rates', headers=headers)
    currency_rates = request.json()
    timestamp = currency_rates['timestamp']
    print(timestamp)
    time = datetime.datetime.fromtimestamp(timestamp/1000)
    for currency_rate in currency_rates['data']:
        try:
            symbol = currency_rate['symbol']
            print(symbol)
            name = currency_rate["id"]
            last_value = currency_rate["rateUsd"]
            data = {'name': name, 'last_value': last_value, 'symbol': symbol, 'provider': 'coincap'}
            currency = Currency.get_or_none(symbol=symbol)
            if currency is None:
                currency = Currency.create(**data)
            data = {'currency': currency.id, 'value': last_value, 'datetime': time, 'provider': 'coincap'}
            currency_rate = CurrencyRate(**data)
            currency_rate.save()
        except Exception as e:
            print(e)
    return True

def get_currency_history(symbol):
    currency = search_currencies({'symbol': symbol})[0]
    request = requests.get("https://api.coincap.io/v2/assets/{}/history?interval=d1".format(currency['name']))
    history = request.json()
    for rate in history['data']:
        try:
            currency_rate = rate['priceUsd']
            time = datetime.datetime.fromtimestamp(rate['time']/1000)
            print(time)
            data = {'currency': currency['id'], 'value': currency_rate, 'datetime': time, 'provider': 'coincap'}
            currency_rate = CurrencyRate(**data)
            currency_rate.save()
        except Exception as e:
            print(e)
    return True


