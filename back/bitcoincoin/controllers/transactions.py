from bitcoincoin.models.transaction import Transaction


def search_transactions(query: dict):
    filters = {}
    if "user" in query:
        try:
            user = int(query["user"])
        except:
            print("User should be an int")
        else:
            filters["user"] = user
    if "currency" in query:
        try:
            currency = int(query["currency"])
        except:
            print("Currency should be an int")
        else:
            filters["currency"] = currency
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


def create_transaction(user_id: int, currency_id: int, quantity: int):
    return Transaction.create(user=user_id, currency=currency_id, quantity=quantity)
