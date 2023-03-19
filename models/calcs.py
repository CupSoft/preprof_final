from flask_login import UserMixin
from main import db


class Calc(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    input_data = db.Column(db.String(10000))
    output_data = db.Column(db.String(10000))
