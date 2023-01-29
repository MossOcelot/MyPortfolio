from . import db


class Folio(db.Model):
    id = db.Column(
        db.BigInteger().with_variant(db.Integer, "sqlite"),
        primary_key=True,
        autoincrement=True,
    )

    name = db.Column(db.String)
    age = db.Column(db.BigInteger().with_variant(db.Integer, "sqlite"),)
    experience = db.Column(db.BigInteger().with_variant(db.Integer, "sqlite"))
    phone = db.Column(db.String)
    email = db.Column(db.String)
    degree = db.Column(db.String)
    fax = db.Column(db.String)
    website = db.Column(db.String)
    careerlevel = db.Column(db.String)
    
