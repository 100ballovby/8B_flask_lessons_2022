from app import db
from datetime import datetime


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(50), nullable=False)
    message = db.Column(db.String(1000), nullable=False)
    created_at = db.Column(db.Date, default=datetime.now())
    status = db.Column(db.Boolean, default=False)
