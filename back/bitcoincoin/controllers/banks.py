from bitcoincoin.models.bank import Bank, BankUser, BankJoinDemand


def get_banks():
    banks = Bank.select()
    return [bank.get_small_data() for bank in banks]


def get_bank(bank_id, user_id=None):
    bank = Bank.get_or_none(id=bank_id)
    if bank is not None:
        data = bank.get_data()
        if user_id is not None:
            user = BankUser.get_or_none(bank=bank, user=user_id)
            if user is not None and user.rank == 'Admin':
                data['demands'] = [bjd.get_small_data() for bjd in bank.demands]
        return data


def create_bank(name: str, symbol: str, admin: int):
    bank = Bank.create(name=name, symbol=symbol)
    admin_user = BankUser.create(bank=bank, user=admin, rank='Admin')
    return bank.get_data()


def join_bank(bank_id: int, user_id: int, rank: str):
    bank = Bank.get(id=bank_id)
    join_demand = BankJoinDemand.get_or_none(bank=bank, user_id=user_id)
    user = BankUser.create(bank=bank, user=user_id, rank=rank)
    join_demand.delete_instance()

    return bank.get_data()


def quit_bank(bank_id: int, user_id: int):
    user = BankUser.get_or_none(bank=bank_id, user=user_id)
    if user is None:
        return False

    user.delete_instance()
    return True


def ask_to_join_bank(bank_id: int, user_id: int):
    bank = Bank.get(id=bank_id)
    join_demand, created = BankJoinDemand.get_or_create(bank=bank, user=user_id)
    return created
