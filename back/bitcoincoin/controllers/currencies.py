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
    if 'symbol' in query:
        try:
            symbol = str(query['symbol'])
        except:
            raise TypeError('symbol must be str')
        currencies = currencies.where(Currency.symbol==symbol)
    if 'name' in query:
        try:
            name = str(query['name'])
        except TypeError:
            print('currency_name must be str')
        currencies = currencies.where(Currency.name==name)
    return [cur.get_small_data() for cur in currencies]

def create_currency(name:str, symbol:str, last_value:float, provider:str):
    try:
        name = str(name)
    except:
        raise TypeError('name must be string')
    try:
        symbol = str(symbol)
    except:
        raise TypeError('symbol must be string')
    try:
        last_value = float(last_value)
        assert last_value > 0
    except:
        raise TypeError('last_value must be float')
    try:
        provider = str(provider)
        assert provider in ['cryptocompare','coincap']
    except:
        raise TypeError('provider is not known')  
    data = {'symbol': symbol, 'last_value': last_value, 'name': name, 'provider':provider}
    return Currency.create(**data)

def get_currency_by_id(currency_id:int):
    try:
        currency_id = int(currency_id)
        assert currency_id > 0
    except:
        raise TypeError('currency_id must be int and positive')
    return Currency.get_or_none(id=currency_id).get_small_data()

def delete_currency(currency_id:int):
    try:
        currency_id = int(currency_id)
        assert currency_id > 0
    except:
        raise TypeError('currency_id must be int and positive')
    return Currency.get_or_none(id=currency_id).delete_instance()

def get_currency_rates_history(currency_id:int, query:dict):
    try:
        currency_id = int(currency_id)
        assert currency_id > 0
    except:
        raise TypeError('currency_id must be int and positive')
    history = CurrencyRate.select().where(CurrencyRate.currency==currency_id)
    if 'date_debut' in query:
        try:
            date_debut = date(query['date_debut'])
        except:
            raise TypeError('date debut is not well given')
        history = history.where(CurrencyRate.datetime >= query['date_debut'])
    if 'date_fin' in query:
        try:
            date_debut = date(query['date_debut'])
        except:
            raise TypeError('date debut is not well given')
        history = history.where(CurrencyRate.datetime <= query['date_fin'])
    return [hist.get_small_data() for hist in history]

def create_currency_rate(currency_id:int, datetime:date, value:float):
    try:
        currency_id = int(currency_id)
        assert currency_id > 0
    except:
        raise TypeError('currency_id must be int and positive')
    try:
        datetime = #TODO
    except:
        raise TypeError('date in not well given')
    try:
        value = float(value)
        assert value>0
    except:
        raise TypeError('value is not int or not positive')
    data = {'currency': currency_id, 'datetime': datetime,
                    'value': value}
    return CurrencyRate.create(**data)

def get_currency_last_rate(currency_id:int):
    currency = get_currency_by_id(currency_id)
    return currency['last_value']
