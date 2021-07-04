from src.api.orders.models import Order


def get_all_orders():
    return Order.query.all()
