from setup_db import db


class Transaction(db.Model):
    __tablename__ = 'transaction'
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer)

    bill_id = db.Column(db.Integer, db.ForeignKey('bill.id', ondelete='CASCADE'))
