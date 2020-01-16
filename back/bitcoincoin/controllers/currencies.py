from datetime import datetime

from bitcoincoin.models.currency import Currency, CurrencyRate


def search_currencies(query: dict):
    currencies = Currency.select()
    if "symbol" in query:
        currencies = currencies.where(Currency.symbol == query["symbol"])
    if "name" in query:
        currencies = currencies.where(Currency.name == query["name"])
    return [cur.get_small_data() for cur in currencies]


def create_currency(name: str, symbol: str, last_value: float, provider: str):
    return Currency.create(
        name=name, symbol=symbol, last_value=last_value, provider=provider
    )


def get_currency_by_id(currency_id: int):
    return Currency.get(id=currency_id).get_small_data()


def delete_currency(currency_id: int):
    return Currency.get(id=currency_id).delete_instance()


def get_currency_rates_history(currency_id: int, from_date: datetime = None, to_date: datetime = None):
    history = CurrencyRate.select().where(CurrencyRate.currency == currency_id)
    if from_date:
        history = history.where(CurrencyRate.datetime >= from_date)
    if to_date:
        history = history.where(CurrencyRate.datetime <= to_date)
    return [hist.get_small_data() for hist in history]


def create_currency_rate(currency_id: int, value: float, provider: str):
    return CurrencyRate.create(currency=currency_id, value=value, provider=provider)


def get_currency_last_rate(currency_id: int):
    currency = get_currency_by_id(currency_id)
    return currency["last_value"]
