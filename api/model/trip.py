from api.database import db


class Trip(db.Model):
    __tablename__ = "trip"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    id_driver = db.Column(db.Integer, db.ForeignKey("driver.id"), nullable=True)
    id_client = db.Column(db.Integer, db.ForeignKey("client.id"), nullable=False)
    distance = db.Column(db.Float(), nullable=False)
    state = db.Column(db.Integer(), db.ForeignKey("state.id"), nullable=False)


