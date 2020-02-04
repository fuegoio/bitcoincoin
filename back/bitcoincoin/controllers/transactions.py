import pendulum

from bitcoincoin.models.transaction import Transaction
from bitcoincoin.models.user import User
from bitcoincoin.models.wallet import Wallet
from bitcoincoin.core import db
from .currencies import get_currency_last_rate
from .users import get_user_cash_flow, get_user_wallet


def search_transactions(filters: dict):
    transactions_found = Transaction.select().order_by(Transaction.datetime.desc()).limit(20)
    if "user" in filters:
        transactions_found = transactions_found.where(
            Transaction.user == filters["user"]
        )
    if "currency" in filters:
        transactions_found = transactions_found.where(
            Transaction.currency == filters["currency"]
        )
    if "from_date" in filters:
        transactions_found = transactions_found.where(
            Transaction.datetime >= filters["from_date"]
        )
    if "to_date" in filters:
        transactions_found = transactions_found.where(
            Transaction.datetime <= filters["to_date"]
        )
    return [transaction.get_small_data(user=True) for transaction in transactions_found]


def create_transaction(user_id: int, currency_id: int, quantity: float, is_sale: bool):
    with db.transaction():
        value = get_currency_last_rate(currency_id) * quantity
        if is_sale:
            user_wallet_list = get_user_wallet(user_id, currency_id)
            if len(user_wallet_list) > 0 and user_wallet_list[0]["volume"] >= quantity:
                if (
                    not Wallet.update(volume=Wallet.volume - quantity)
                    .where(Wallet.user == user_id, Wallet.currency == currency_id)
                    .execute()
                ):
                    raise Exception(
                        "Problem while updating user's wallet for currency, transaction cancelled"
                    )
                if (
                    not User.update(cash_flow=User.cash_flow + value)
                    .where(User.id == user_id)
                    .execute()
                ):
                    raise Exception(
                        "Problem while updating user's cash flow, transaction cancelled"
                    )
            else:
                raise Exception(
                    "Not enough money available for this currency to make this transaction"
                )
        else:
            dollars_available = get_user_cash_flow(user_id)
            if dollars_available < value:
                raise Exception(
                    "Not enough dollars available to make this transactions"
                )
            if (
                not User.update(cash_flow=User.cash_flow - value)
                .where(User.id == user_id)
                .execute()
            ):
                raise Exception(
                    "Problem while updating user's cash flow, transaction cancelled"
                )

            wallet = Wallet.get_or_none(user=user_id, currency=currency_id)
            if wallet is None:
                wallet = Wallet.create(user=user_id, currency=currency_id, volume=0)
            wallet.volume += quantity
            wallet.save()

        return Transaction.create(
            user=user_id,
            currency=currency_id,
            quantity=quantity,
            value=value,
            is_sale=is_sale,
        )
