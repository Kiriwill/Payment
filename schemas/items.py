from marshmallow import fields, Schema
from config import db

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(24), nullable=False)
    value_unit = db.Column(db.Numeric(precision=5, scale=2), nullable=False)


class ItemSchema(Schema):
    id = fields.Int(
        required=False,
        allow_none=False,
        allow_empty=False)

    name = fields.Str(
        required=True,
        allow_none=False,
        allow_empty=False)

    value_unit = fields.Float(
        required=True,
        allow_none=False,
        allow_empty=False)