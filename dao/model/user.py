from marshmallow import Schema, fields

from setup_db import db
from dao.model.bill import Bill


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    role = db.Column(db.String, nullable=True, default='customer')
    is_active = db.Column(db.Boolean, unique=False, default=False)

    bill = db.relationship("Bill", backref='user', cascade="all, delete", passive_deletes=True)


class UserSchema(Schema):
    username = fields.Str()
    bill_id = fields.Str()
