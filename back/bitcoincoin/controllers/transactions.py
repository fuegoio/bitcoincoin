from bitcoincoin.models.transaction import Transaction
from .currencies import get_currency_last_rate
from .users import get_user_cash_flow, get_user_wallet


def search_transactions(filters: dict):
    # TODO: startdate and endate in query

    # HOW TO DO THIS WITH PEEWEE SYNTAX
    # filters = {"user": 3, "currency": 4}
    # transactions_found = Transaction.select().where(**filters)
    #   ==> where(user=3, currency=4)
    # peewee syntax : where(Transaction.user == 3)

    # Disjonction des cas
    transactions_found = Transaction.select()
    if "user" in filters:
        transactions_found = transactions_found.where(
            Transaction.user == filters["user"]
        )
    if "currency" in filters:
        transactions_found = transactions_found.where(
            Transaction.currency == filters["currency"]
        )

    return [transaction.get_small_data() for transaction in transactions_found]


def create_transaction(user_id: int, currency_id: int, quantity: int, is_sell: bool):
    value = get_currency_last_rate(currency_id) * quantity
    if is_sell:
        currency_available = get_user_wallet(user_id, currency_id)
        if currency_available < quantity:
            raise Exception("Not enough money available to make this transaction")
    else:
        dollars_available = get_user_cash_flow(user_id)
        if dollars_available < value:
            raise Exception("Not enough dollars available to make this transactions")
    return Transaction.create(
        user=user_id,
        currency=currency_id,
        quantity=quantity,
        value=value,
        is_sell=is_sell,
    )
