import datetime

import requests
from playhouse.shortcuts import update_model_from_dict
from .currencies import create_currency, create_currency_rate
from bitcoincoin.models.currency import Currency, CurrencyRate
from .data.currencies_list import currencies_list

headers = {'authorization': 'Apikey {}'.format('7bdf4764d02940ee49fa5198c51d2cfb1ca440d3dbe2de46d3fb9391e0a9f045')}

def update_currency(*args):
    url_all = 'https://min-api.cryptocompare.com/data/blockchain/list'
    response_all = requests.get(url_all, headers=headers)
    use_favorites = args
    for cur in response_all.json()['Data']:
        if use_favorites != []:
            if cur in use_favorites:
                url_unique = 'https://min-api.cryptocompare.com/data/v2/histominute?fsym={}&tsym=USD&limit=1'.format(cur)
                try:
                    currency = Currency.get_or_none(symbol=cur)
                    response_unique = requests.get(url_unique, headers=headers)
                    value = response_unique.json()['Data']['Data'][-1]
                    if currency is None:
                        currency = create_currency(name=cur, symbol=cur, last_value=value['close'], provider='cryptocompare')
                    create_currency_rate(currency_id=currency.id, value=value['close'], provider='cryptocompare')
                except Exception as e:
                    print(e)
                    continue
        else:
            url_unique = 'https://min-api.cryptocompare.com/data/v2/histominute?fsym={}&tsym=USD&limit=1'.format(cur)
            try:
                currency = Currency.get_or_none(symbol=cur)
                if currency:
                    response_unique = requests.get(url_unique, headers=headers)
                    value = response_unique.json()['Data']['Data'][-1]
                    create_currency_rate(currency_id=currency.id, value=value['close'], provider='cryptocompare')
            except Exception as e:
                print(e)
                continue
    return True


def get_historic(symbol, nb_days=730):
    url = 'https://min-api.cryptocompare.com/data/v2/histoday?fsym={}&tsym=USD&limit={}'.format(str(symbol),str(nb_days))
    response = requests.get(url, headers=headers)
    currency = Currency.get_or_none(symbol=symbol)
    if currency:
        for day in response.json()['Data']['Data']:
            try:
                create_currency_rate(currency_id=currency.id, datetime=datetime.datetime.fromtimestamp(day['time']), value=day['close'], provider='cryptocompare')
            except Exception as e:
                print(e)
                continue
    return True


# update_currency()
