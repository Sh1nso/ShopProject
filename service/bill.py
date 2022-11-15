from dao.bill import BillDAO


class BillService:
    def __init__(self, dao: BillDAO):
        self.dao = dao

    def get_one(self, bid: int) -> BillDAO:
        return self.dao.get_one(bid)

    def get_all(self) -> BillDAO:
        return self.dao.get_all()

    def decrease_balance(self, bid: int, amount: int):
        return self.dao.decrease_balance(bid, amount)

    def increase_balance(self, bid: int, amount: int):
        return self.dao.increase_balance(bid, amount)

    def check_for_exist(self, bid: int) -> bool:
        if self.get_one(int(bid)) is None:
            return False
        return True

    def get_balance(self, bid):
        return self.dao.get_balance(bid)

    def check_availability_money(self, bid: int, amount: int) -> bool:
        if self.get_balance(bid) < amount:
            return False
        return True

    def create(self, bill_d: dict) -> BillDAO:
        return self.dao.create(bill_d)
