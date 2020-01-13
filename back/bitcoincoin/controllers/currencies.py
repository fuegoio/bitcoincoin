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


def search_currencies(query: dict):
    currencies = Currency.select()
    if "symbol" in query:
        currencies = currencies.where(Currency.symbol == str(query["symbol"]))
    if "name" in query:
        currencies = currencies.where(Currency.name == str(query["name"]))
    return [cur.get_small_data() for cur in currencies]


def create_currency(name: str, symbol: str, last_value: float, provider: str):
    return Currency.create(
        name=name, symbol=symbol, last_value=last_value, provider=provider
    )


def get_currency_by_id(currency_id: int):
    return Currency.get(id=currency_id).get_small_data()


def delete_currency(currency_id: int):
    return Currency.get(id=currency_id).delete_instance()


def get_currency_rates_history(currency_id: int, query: dict):
    history = CurrencyRate.select().where(CurrencyRate.currency == currency_id)
    # if 'date_debut' in query:
    #     try:
    #         date_debut = date(query['date_debut'])
    #     except:
    #         raise TypeError('date debut is not well given')
    #     history = history.where(CurrencyRate.datetime >= query['date_debut'])
    # if 'date_fin' in query:
    #     try:
    #         date_debut = date(query['date_debut'])
    #     except:
    #         raise TypeError('date debut is not well given')
    #     history = history.where(CurrencyRate.datetime <= query['date_fin'])
    return [hist.get_small_data() for hist in history]


def create_currency_rate(currency_id: int, value: float):
    # TODO: add datetime
    return CurrencyRate.create(currency=currency_id, value=value)


def get_currency_last_rate(currency_id: int):
    currency = get_currency_by_id(currency_id)
    return currency["last_value"]
