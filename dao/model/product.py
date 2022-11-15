from setup_db import db
from marshmallow import Schema, fields


class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False, unique=True)
    description = db.Column(db.String, nullable=False)
    cost = db.Column(db.Integer, nullable=False)


class ProductSchema(Schema):
    title = fields.Str()
    description = fields.Str()
    cost = fields.Int()
