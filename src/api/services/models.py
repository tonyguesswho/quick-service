import os
from sqlalchemy.sql import func


from src import db


class Service(db.Model):

    __tablename__ = "services"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False, unique=True)
    duration = db.Column(db.Float, nullable=False)
    created_date = db.Column(db.DateTime, default=func.now(), nullable=False)
    updated_date = db.Column(
        db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now()
    )

    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    def __repr__(self):
        return "<Service %r>" % self.name


if os.getenv("FLASK_ENV") == "development":
    from src import admin

    from src.api.services.admin import ServiceAdminView

    admin.add_view(ServiceAdminView(Service, db.session))
