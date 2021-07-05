import os
from src.api.services.models import Service
from src.database.models import BaseModel


from src import db


class Order(BaseModel):

    __tablename__ = "orders"
    service_id = db.Column(db.Integer, db.ForeignKey(Service.id), nullable=False)
    customer_id = db.Column(db.String(128), nullable=False)
    request_date = db.Column(db.DateTime, index=True, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    service = db.relationship(Service, backref="orders")

    def __init__(self, service_id, customer_id, request_date, end_date):
        self.service_id = service_id
        self.customer_id = customer_id
        self.request_date = request_date
        self.end_date = end_date

    def __repr__(self):
        return "<Order %r>" % self.customer_id


if os.getenv("FLASK_ENV") == "development":
    from src import admin

    from src.api.orders.admin import OrdersAdminView

    admin.add_view(OrdersAdminView(Order, db.session))
