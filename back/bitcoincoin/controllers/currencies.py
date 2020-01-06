# TODO: import from managers all useful functions
# search_currencies(query)
# create_currency(name, symbol)
# get_currency_by_id(currency_id)
# delete_currency(currency_id)
# get_currency_last_rate(currency_id)
# get_currency_rates_history(currency_id, query)
# create_currency_rate(currency_id, value)
from datetime import date
from bitcoincoin.models.currency import Currency, CurrencyRate

def search_currencies(query:dict):
    currencies = Currency.select()
    if 'currency_symbol' in query:
        currencies = currencies.where(Currency.symbol==query['currency_symbol'])
    if 'currency_name' in query:
        currencies = currencies.where(Currency.name==query['currency_name'])
    return [cur.get_small_data() for cur in currencies]

def create_currency(name:str, symbol:str, last_value:float, provider:str):
    data = {'symbol': symbol, 'last_value': last_value, 'name': name, 'provider':provider}
    return Currency.create(**data)

def get_currency_by_id(currency_id:int):
    return Currency.get_or_none(id=currency_id).get_small_data()

def delete_currency(currency_id:int):
    return Currency.get_or_none(id=currency_id).delete_instance()

def get_currency_rates_history(currency_id:int, query:dict):
    history = CurrencyRate.select().where(CurrencyRate.currency==currency_id)
    if 'date_debut' in query:
        history = history.where(CurrencyRate.datetime >= query['date_debut'])
    if 'date_fin' in query:
        history = history.where(CurrencyRate.datetime <= query['date_fin'])
    return [hist.get_small_data() for hist in history]

def create_currency_rate(currency_id:int, datetime:date, value:float):
    data = {'currency': currency_id, 'datetime': datetime,
                    'value': value}
    return CurrencyRate.create(**data)

def get_currency_last_rate(currency_id:int):
    currency = get_currency_by_id(currency_id)
    return currency['last_value']
