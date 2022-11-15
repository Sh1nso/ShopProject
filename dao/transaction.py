from dao.model.transaction import Transaction


class TransactionDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, bid: int) -> Transaction:
        return self.session.query(Transaction).get(bid)

    def get_all(self) -> Transaction:
        return self.session.query(Transaction).all()

    def create(self, transaction_d: dict) -> Transaction:
        bill = Transaction(**transaction_d)
        self.session.add(bill)
        self.session.commit()
        return bill

    def delete(self, pid: int) -> str:
        product = self.get_one(pid)
        self.session.delete(product)
        self.session.commit()
        return ''
