import requests
from playhouse.shortcuts import update_model_from_dict

from bitcoincoin.models.currency import Currency, CurrencyRate


def load_currency_rates():
    request = requests.get('https///api.coincap.io/v2/rates')
    currency_rates = request.json()
    for currency_rate in currency_rates['data']:
        symbol = currency_rate['symbol']
        currency = Currency.get_or_none(symbol=symbol)
        name = currency["id"]
        last_value = currency["rateUsd"]
        data = {'name': name, 'last_value': last_value}
        if currency is None:
            Currency.create(**data)
        else:
            update_model_from_dict(currency, data)
            currency.save()
        currency_id = Currency.get_id_from_symbol(symbol)
        data = {'currency': currency_id, 'value': last_value}
        CurrencyRate.create(**data)
    return True
