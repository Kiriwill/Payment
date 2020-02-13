import os
from flask import Flask
from dotenv import load_dotenv
from services.item.views import items
from services.payment.views import payment
from config import db

app = Flask(__name__)
load_dotenv()

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db.init_app(app)

app.register_blueprint(items)
app.register_blueprint(payment)

app.run(port=int(os.getenv("PORTA")), host=os.getenv("HOST"))
