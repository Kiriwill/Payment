from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///store.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =  True

db = SQLAlchemy(app)

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

    def __repr__(self):
        return '<Payment %r>' % self.id

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(24))
    value_unit = db.Column(db.Numeric(precision=5, scale=2), nullable=False)

    def __repr__(self):
        return '<Item %r>' % self.id

db.create_all()


