from api.database import db
from api.model.person import Person


class Driver(Person):
    __mapper_args__ = {'polymorphic_identity': 'driver'}


