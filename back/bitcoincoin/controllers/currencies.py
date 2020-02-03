import statistics
from datetime import datetime

import pendulum

from bitcoincoin.core import db
from bitcoincoin.models.currency import Currency, CurrencyRate


def search_currencies(query: dict):
    currencies = Currency.select().order_by(Currency.rank).limit(10)
    if "symbol" in query.keys():
        currencies = currencies.where(Currency.symbol == query["symbol"])

    if "name" in query.keys():
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
        from_date = now.subtract(days=days)
        to_date = from_date.add(days=1)
        available_rates = get_currency_rates_history(currency_id, from_date, to_date)
        if len(available_rates) > 0:
            mean = round(statistics.mean([r['value'] for r in available_rates]), 2)
            rates.append(mean)
        else:
            rates.append(None)
    return rates


def get_currency_rates_history(currency_id: int, from_date: datetime = None, to_date: datetime = None,
                               interval_type='day', interval_number=500):
    history = CurrencyRate.select().where(CurrencyRate.currency == currency_id).order_by(CurrencyRate.datetime)
    if from_date is not None:
        history = history.where(CurrencyRate.datetime >= from_date)
    if to_date is not None:
        history = history.where(CurrencyRate.datetime < to_date)

    limit = {f"{interval_type}s": interval_number}
    limit_date = pendulum.now('utc').subtract(**limit)
    history = history.where(CurrencyRate.datetime >= limit_date)

    history_by_interval = {}
    for rate in history:
        interval = pendulum.instance(rate.datetime)
        if interval_type is not None:
            interval = interval.start_of(interval_type)

        if interval not in history_by_interval.keys():
            history_by_interval[interval] = []
        history_by_interval[interval].append(rate)

    rates = []
    for interval in sorted(history_by_interval.keys()):
        mean = round(statistics.mean([r.value for r in history_by_interval[interval]]), 2)
        rates.append({"value": mean, "datetime": interval})

    return rates


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
