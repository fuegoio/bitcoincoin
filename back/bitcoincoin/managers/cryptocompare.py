import requests
from bitcoincoin.models.currency import Currency,CurrencyRate
import datetime
from playhouse.shortcuts import update_model_from_dict

headers = {'authorization': 'Apikey {}'.format('7bdf4764d02940ee49fa5198c51d2cfb1ca440d3dbe2de46d3fb9391e0a9f045')}
def update_currency():
    url_all = 'https://min-api.cryptocompare.com/data/blockchain/list'
    response_all = requests.get(url_all, headers=headers)
    print('ok')
    for cur in response_all.json()['Data']:
        url_unique = 'https://min-api.cryptocompare.com/data/v2/histominute?fsym=AIT&tsym=GBP&limit=1'
        print('ok')
        try:
            currency = Currency.get_or_none(symbol=cur)
            response_unique = requests.get(url_unique, headers=headers)
            value = response_unique.json()['Data']['Data'][-1]
            data = {'symbol' : cur, 'last_value':value['close'], 'name':cur}
            print(cur)
            if currency is None:
                print('not exist')
                currency = Currency.create(**data)
            else:
                update_model_from_dict(currency,data)
            print(currency)
            data = {'currency':currency.id, 'datetime':datetime.datetime.fromtimestamp(value['time']), 'value':value['close']}
            currency_rate = CurrencyRate(**data)
            currency_rate.save()
        except Exception as e:
            print(e)
            continue
    return True

update_currency()
