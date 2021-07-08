from src.api.orders.models import Order
from sqlalchemy import func, and_
import re
from src import db


def get_all_orders(service_id, start_date, end_date):
    q = Order.query
    if service_id:
        q = q.filter_by(service_id=service_id)
    if start_date and end_date:
        stripped_start_date = re.sub("T", " ", start_date)
        stripped_end_date = re.sub("T", " ", end_date)
        q = q.filter(
            and_(
                Order.request_date
                >= func.TO_TIMESTAMP(
                    stripped_start_date,
                    "YYYY-MM-DD HH24:MI:SS",
                ),
                Order.request_date
                < func.TO_TIMESTAMP(
                    stripped_end_date,
                    "YYYY-MM-DD HH24:MI:SS",
                ),
            )
        )
    return q.all()


def add_order(service_id, customer_id, request_date, end_date):
    order = Order(
        service_id=service_id,
        customer_id=customer_id,
        request_date=request_date,
        end_date=end_date,
    )
    order.save()
    return order


def delete_order(order):
    db.session.delete(order)
    db.session.commit()
    return order


def get_order_by_id(order_id):
    return Order.query.filter_by(id=order_id).first()
