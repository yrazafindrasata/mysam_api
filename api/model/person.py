from sample_api.database import db


class Person(db.Model):
    __tablename__ = "person"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String, nullable=False)
    balance  = db.Column(db.Float(), nullable=False)


