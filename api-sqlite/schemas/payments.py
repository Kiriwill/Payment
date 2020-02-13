from marshmallow import fields, Schema
from config import db
from .items import ItemSchema

payment_items = db.Table('payment_items', 
    db.Column('item_id', db.Integer, db.ForeignKey('item.id'), primary_key=True),
    db.Column('payment_id', db.Integer, db.ForeignKey('payment.id'), primary_key=True)
)

class Payment(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    count_items = db.Column(db.Integer, nullable=False)
    total_value = db.Column(db.Numeric(precision=8, scale=2), nullable=False)
    items = db.relationship('Item', secondary=payment_items, lazy='subquery',
        backref=db.backref('payments', lazy=True))

class PaymentSchema(Schema):

    id = fields.Int(
        required=False,
        allow_none=False,
        allow_empty=False)
    
    count_items = fields.Int(
        required=True,
        allow_none=False,
        allow_empty=False)
    
    total_value = fields.Float(
        required=True,
        allow_none=False,
        allow_empty=False)
    
    items = fields.Nested(
        ItemSchema, 
        required=False, 
        allow_none=False, 
        allow_empty=False)
    
