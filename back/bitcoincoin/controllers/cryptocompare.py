import datetime

import requests
from playhouse.shortcuts import update_model_from_dict

from bitcoincoin.models.currency import Currency, CurrencyRate

headers = {'authorization': 'Apikey {}'.format('7bdf4764d02940ee49fa5198c51d2cfb1ca440d3dbe2de46d3fb9391e0a9f045')}


def update_currency():
    url_all = 'https://min-api.cryptocompare.com/data/blockchain/list'
    response_all = requests.get(url_all, headers=headers)
    for cur in response_all.json()['Data']:
        url_unique = 'https://min-api.cryptocompare.com/data/v2/histominute?fsym={}&tsym=USD&limit=1'.format(cur)
        try:
            currency = Currency.get_or_none(symbol=cur)
            response_unique = requests.get(url_unique, headers=headers)
            value = response_unique.json()['Data']['Data'][-1]
            data = {'symbol': cur, 'last_value': value['close'], 'name': cur}
            if currency is None:
                currency = Currency.create(**data)
            else:
                update_model_from_dict(currency, data)
            data = {'currency': currency.id, 'datetime': datetime.datetime.fromtimestamp(value['time']),
                    'value': value['close']}
            currency_rate = CurrencyRate(**data)
            currency_rate.save()
        except Exception as e:
            print(e)
            continue
    return True


def get_historic(symbol, nb_days=730):
    url = 'https://min-api.cryptocompare.com/data/v2/histoday?fsym={}&tsym=USD&limit={}'.format(symbol, nb_days)
    response = requests.get(url, headers=headers)
    currency = Currency.get_or_none(symbol=symbol)
    if currency:
        for day in response.json()['Data']:
            try:
                data = {'currency': currency.id, 'datetime': datetime.datetime.fromtimestamp(day['time']),
                        'value': day['close']}
                currency_rate = CurrencyRate(**data)
                currency_rate.save()
            except Exception as e:
                print(e)
                continue
    return True


update_currency()
