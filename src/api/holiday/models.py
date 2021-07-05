import os


from src import db
from src.database.models import BaseModel


class Holiday(BaseModel):

    __tablename__ = "holiday"
    name = db.Column(db.String(128), nullable=False, unique=True)
    date = db.Column(db.Date, nullable=False, unique=True, index=True)

    def __init__(self, name, date):
        self.name = name
        self.date = date

    def __repr__(self):
        return "<Holiday %r>" % self.name


if os.getenv("FLASK_ENV") == "development":
    from src import admin

    from src.api.holiday.admin import HolidayAdminView

    admin.add_view(HolidayAdminView(Holiday, db.session))
