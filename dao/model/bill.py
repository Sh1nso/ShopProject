from setup_db import db


class Bill(db.Model):
    __tablename__ = 'bill'
    id = db.Column(db.Integer, primary_key=True)
    balance = db.Column(db.Integer, default=0)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))
    transaction = db.relationship("Transaction", backref='bill', cascade="all, delete", passive_deletes=True)