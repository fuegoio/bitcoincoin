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
    return [user.get_small_data() for user in users]


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
