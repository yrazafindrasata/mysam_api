from api.database import db
from api.model.person import Person


class Client(Person):
    __mapper_args__ = {'polymorphic_identity': 'client'}


