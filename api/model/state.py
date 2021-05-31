from api.database import db


class State(db.Model):
    __tablename__ = "state"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    label = db.Column(db.String)




