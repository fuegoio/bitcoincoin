import requests
from playhouse.shortcuts import update_model_from_dict
import datetime

from bitcoincoin.models.currency import Currency, CurrencyRate

headers = {'Accept-Encoding' : 'gzip'}
def load_currency_rates():
    request = requests.get('https://api.coincap.io/v2/rates', headers=headers)
    currency_rates = request.json()
    timestamp = currency_rates['timestamp']
    print(timestamp)
    time = datetime.datetime.fromtimestamp(timestamp)
    for currency_rate in currency_rates['data']:
        try:
            symbol = currency_rate['symbol']
            print(symbol)
            name = currency_rate["id"]
            last_value = currency_rate["rateUsd"]
            data = {'name': name, 'last_value': last_value, 'symbol': symbol}
            currency = Currency.get_or_none(symbol=symbol)
            if currency is None:
                currency = Currency.create(**data)
            else:
                update_model_from_dict(currency, data)
                currency.save()
            data = {'currency': currency.id, 'value': last_value, 'datetime': time}
            currency_rate = CurrencyRate(**data)
            currency_rate.save()
        except Exception as e:
            print(e)
    return True

load_currency_rates()