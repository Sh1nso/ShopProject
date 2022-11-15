from dao.model.bill import Bill


class BillDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, bid: int) -> Bill:
        return self.session.query(Bill).get(bid)

    def get_all(self) -> Bill:
        return self.session.query(Bill).all()

    def get_balance(self, bid):
        bill = self.get_one(bid)
        return bill.balance

    def decrease_balance(self, bid, amount):
        bill = self.get_one(bid)
        bill.balance -= amount
        self.session.add(bill)
        self.session.commit()

    def increase_balance(self, bid, amount):
        bill = self.get_one(bid)
        bill.balance += amount
        self.session.add(bill)
        self.session.commit()


    def create(self, bill_d: dict) -> Bill:
        bill = Bill(**bill_d)
        self.session.add(bill)
        self.session.commit()
        return bill

    def delete(self, pid: int) -> str:
        product = self.get_one(pid)
        self.session.delete(product)
        self.session.commit()
        return ''
