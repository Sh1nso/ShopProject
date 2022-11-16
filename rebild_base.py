from flask import Flask
from flask_restx import Api

from config import Config
from setup_db import db
from flask_migrate import Migrate

api = Api()

class Bill(db.Model):
    __tablename__ = 'bill'
    id = db.Column(db.Integer, primary_key=True)
    balance = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))

    transaction = db.relationship("Transaction", backref='bill', cascade="all, delete", passive_deletes=True)


class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False, unique=True)
    description = db.Column(db.String, nullable=False)
    cost = db.Column(db.Integer, nullable=False)


class Transaction(db.Model):
    __tablename__ = 'transaction'
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer)

    bill_id = db.Column(db.Integer, db.ForeignKey('bill.id', ondelete='CASCADE'))


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    role = db.Column(db.String, nullable=True, default='customer')
    is_active = db.Column(db.Boolean, unique=False, default=False)

    bill = db.relationship("Bill", backref='user', cascade="all, delete", passive_deletes=True)


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)

    register_extensions(app)

    return app


def register_extensions(app):
    db.init_app(app)
    api.init_app(app)
    with app.app_context():
        #db.drop_all()
        db.create_all()


app = create_app(Config())
app.debug = True
migrate = Migrate(app, db)

# if __name__ == '__main__':
#     app.run(debug=True)
