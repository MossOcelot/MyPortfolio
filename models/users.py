from flask_login import UserMixin
from . import db


class User(db.Model, UserMixin):
    id = db.Column(
        db.BigInteger().with_variant(db.Integer, "sqlite"),
        primary_key=True,
        autoincrement=True,
    )
    password = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String)

    name = db.Column(db.String)
    surname = db.Column(db.String)
