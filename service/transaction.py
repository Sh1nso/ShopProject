from dao.transaction import TransactionDAO


class TransactionService:
    def __init__(self, dao: TransactionDAO):
        self.dao = dao

    def get_one(self, tid: int) -> TransactionDAO:
        return self.dao.get_one(tid)

    def get_all(self) -> TransactionDAO:
        return self.dao.get_all()

    def create(self, transaction_d: dict) -> TransactionDAO:
        return self.dao.create(transaction_d)

