from src.api.orders.models import Order


def get_all_orders():
    return Order.query.all()


def add_order(service_id, customer_id, request_date, end_date):
    order = Order(
        service_id=service_id,
        customer_id=customer_id,
        request_date=request_date,
        end_date=end_date,
    )
    order.save()
    return order
