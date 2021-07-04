import os


from src import db
from src.database.models import BaseModel


class Service(BaseModel):

    __tablename__ = "services"
    name = db.Column(db.String(128), nullable=False, unique=True)
    duration = db.Column(db.Float, nullable=False)

    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    def __repr__(self):
        return "<Service %r>" % self.name


if os.getenv("FLASK_ENV") == "development":
    from src import admin

    from src.api.services.admin import ServiceAdminView

    admin.add_view(ServiceAdminView(Service, db.session))
