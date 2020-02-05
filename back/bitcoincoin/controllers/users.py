import pendulum
from peewee import fn

from bitcoincoin.models.currency import CurrencyRate
from bitcoincoin.models.transaction import Transaction
from bitcoincoin.models.user import User
from bitcoincoin.models.wallet import Wallet


def search_users(filters: dict):
    users = User.select()
    if "user_id" in filters:
        users = users.where(User.id == filters["user_id"])
    if "username" in filters:
        users = users.where(User.username == filters["username"])
    if "email" in filters:
        users = users.where(User.email == filters["email"])
    list_users = [user.get_small_data() for user in users]
    return sorted(list_users, key=lambda k: k['value'], reverse=True)


def get_user_by_id(user_id: int):
    return User.get(id=user_id).get_small_data()


def delete_user(user_id: int):
    return User.get(id=user_id).delete_instance()


def get_user_transactions(user_id, filters: dict):
    transactions = Transaction.select().where(Transaction.user == user_id).order_by(Transaction.datetime.desc())
    if "currency" in filters:
        transactions = transactions.where(Transaction.currency == filters["currency"])
    if "limit" in filters:
        transactions = transactions.limit(filters["limit"])
    return [transaction.get_small_data(currency=True) for transaction in transactions]


def get_user_wallet(user_id, currency_id=None):
    wallets = Wallet.select().where(Wallet.user_id == user_id)
    if currency_id is not None:
        wallets = wallets.where(Wallet.currency == currency_id)
    return [wallet.get_small_data() for wallet in wallets]


def get_user_cash_flow(user_id: int):
    user = User.get_by_id(user_id)
    return user.cash_flow


def get_user_banks(user_id):
    user = User.get_by_id(user_id)
    return [b.bank.get_small_data() for b in user.banks]


def get_user_value_history(user_id, interval_type='minute'):
    limit = {f"{interval_type}s": 500}
    interval = {f"{interval_type}s": 1}
    limit_date = pendulum.now('utc').subtract(**limit)

    user = User.get_by_id(user_id)

    wallets = Wallet.select().where(Wallet.user_id == user_id)
    wallets_by_currency = {}
    for w in wallets:
        wallets_by_currency[w.currency] = w

    values = []

    transactions_history = list(Transaction.select().where(Transaction.user == user_id, Transaction.datetime >= limit_date))
    transactions_processed = []
    for hour in range(500):
        limit = {f"{interval_type}s": hour}
        limit_date = pendulum.now('utc').subtract(**limit)
        for t in transactions_history:
            t_datetime = pendulum.instance(t.datetime)
            if t_datetime >= limit_date and t not in transactions_processed:
                if t.is_sale:
                    wallets_by_currency[t.currency].volume += t.quantity
                    user.cash_flow -= t.value
                else:
                    wallets_by_currency[t.currency].volume -= t.quantity
                    user.cash_flow += t.value
                transactions_processed.append(t)

        # Compute the wallet value
        rates = CurrencyRate.select(CurrencyRate.currency, fn.AVG(CurrencyRate.value).alias('value')).where(CurrencyRate.currency << list(wallets_by_currency.keys()))
        rates = rates.where(CurrencyRate.datetime >= limit_date.subtract(**interval), CurrencyRate.datetime <= limit_date)
        rates = rates.group_by(CurrencyRate.currency)

        hour_value = 0
        for rate in rates:
            currency = rate.currency
            value = rate.value
            wallet_value = wallets_by_currency[currency].volume * value
            hour_value += wallet_value

        values.append({"date": str(limit_date), "value": hour_value + user.cash_flow})

    return values[::-1]
