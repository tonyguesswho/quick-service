import os
from sqlalchemy.sql import func
from src.api.services.models import Service


from src import db


class Order(db.Model):

    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    service_id = db.Column(db.Integer, db.ForeignKey(Service.id), nullable=False)
    customer_id = db.Column(db.String(128), nullable=False)
    created_date = db.Column(
        db.DateTime, default=func.now(), index=True, nullable=False
    )
    updated_date = db.Column(
        db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now()
    )
    service = db.relationship(Service, backref="orders")

    def __init__(self, service_id, customer_id):
        self.service_id = service_id
        self.customer_id = customer_id

    def __repr__(self):
        return "<Order %r>" % self.customer_id


if os.getenv("FLASK_ENV") == "development":
    from src import admin

    from src.api.orders.admin import OrdersAdminView

    admin.add_view(OrdersAdminView(Order, db.session))
