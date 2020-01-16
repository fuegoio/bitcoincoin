import requests
from playhouse.shortcuts import update_model_from_dict
import datetime

from bitcoincoin.models.currency import Currency, CurrencyRate
from .currencies import search_currencies, create_currency, create_currency_rate

headers = {'Accept-Encoding' : 'gzip'}
def load_currency_rates(currency_list = None):
    request = requests.get('https://api.coincap.io/v2/rates', headers=headers)
    currency_rates = request.json()
    timestamp = currency_rates['timestamp']
    time = datetime.datetime.fromtimestamp(timestamp/1000)
    for currency_rate in currency_rates['data']:
        if currency_list and currency_rate['symbol'] in currency_list:
            try:
                symbol = currency_rate['symbol']
                name = currency_rate["id"]
                last_value = currency_rate["rateUsd"]
                currency = Currency.get_or_none(symbol=symbol)
                if currency is None:
                    currency = create_currency(name = name, symbol=symbol, last_value=last_value, provider='coincap')
                create_currency_rate(currency_id=currency.id, value=last_value, provider= 'coincap')    
            except Exception as e:
                print(e)
        else :
            try:
                symbol = currency_rate['symbol']
                name = currency_rate['id']
                last_value = currency_rate['rateUsd']
                currency = Currency.get_or_none(symbol=symbol)
                if currency:
                    print(symbol)
                    create_currency_rate(currency_id=currency.id, value=last_value, provider='coincap')
            except Exception as e:
                print(e)                   
    return True

def get_currency_history(symbol):
    currency = Currency.get_or_none(symbol=symbol)
    if currency:
        request = requests.get("https://api.coincap.io/v2/assets/{}/history?interval=d1".format(currency.name))
        history = request.json()
        for rate in history['data']:
            try:
                currency_rate = rate['priceUsd']
                time = datetime.datetime.fromtimestamp(rate['time']/1000)
                print(time)
                create_currency_rate(currency_id=currency.id, value= currency_rate, datetime=time, provider='coincap')
            except Exception as e:
                print(e)
    return True


