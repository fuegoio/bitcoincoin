from datetime import datetime

import pendulum

from bitcoincoin.core import db
from bitcoincoin.models.currency import Currency, CurrencyRate


def search_currencies(query: dict):
    currencies = Currency.select().order_by(Currency.rank).limit(20)
    if "symbol" in query:
        currencies = currencies.where(Currency.symbol == query["symbol"])
    if "name" in query:
        currencies = currencies.where(Currency.name.contains(query["name"]))
    return [cur.get_small_data() for cur in currencies]


def create_currency(name: str, symbol: str, rank: int, coincap_name: float):
    return Currency.create(name=name, symbol=symbol, rank=rank, coincap=coincap_name)


def get_currency_by_id(currency_id: int):
    return Currency.get(id=currency_id).get_small_data()


def delete_currency(currency_id: int):
    return Currency.get(id=currency_id).delete_instance()


def get_currency_rates_last_days(currency_id: int, number_days: int):
    rates = []
    now = pendulum.today('UTC')
    for days in range(number_days - 1, -1, -1):
        date = now.subtract(days=days)
        available_rates = CurrencyRate.select().where(CurrencyRate.currency == currency_id, CurrencyRate.datetime >= date).order_by(CurrencyRate.datetime).limit(1)
        if len(available_rates) > 0:
            rates.append(available_rates[0].value)
        else:
            rates.append(0)
    return rates


def get_currency_rates_history(currency_id: int, from_date: datetime = None, to_date: datetime = None):
    history = CurrencyRate.select().where(CurrencyRate.currency == currency_id).order_by(CurrencyRate.datetime)
    if from_date:
        history = history.where(CurrencyRate.datetime >= from_date)
    if to_date:
        history = history.where(CurrencyRate.datetime <= to_date)
    return [hist.get_small_data() for hist in history]


def create_currency_rate(currency_id: int, value: float, datetime=None):
    currency = Currency.get_by_id(currency_id)
    if datetime:
        c = CurrencyRate.get_or_create(currency=currency, datetime=datetime, defaults={'value': value})
    else:
        with db.transaction():
            c = CurrencyRate.create(currency=currency, value=value)
            currency.last_value = value
            currency.save()
    return c


def get_currency_last_rate(currency_id: int):
    currency = get_currency_by_id(currency_id)
    return currency["last_value"]
