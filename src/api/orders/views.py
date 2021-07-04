from flask import Blueprint
from flask_restx import Api, Resource, fields, Namespace


from src.api.orders.crud import (  # isort:skip
    get_all_orders,
)

orders_blueprint = Blueprint("orders", __name__)
api = Api(orders_blueprint)

orders_namespace = Namespace("orders")

service_marshaller = {
    "id": fields.Integer(readOnly=True),
    "name": fields.String(required=True),
    "duration": fields.Float(required=True),
    "created_date": fields.DateTime,
    "updated_date": fields.DateTime,
}


order = orders_namespace.model(
    "Order",
    {
        "id": fields.Integer(readOnly=True),
        "service_id": fields.Integer(required=True),
        "customer_id": fields.String(required=True),
        "created_date": fields.DateTime,
        "updated_date": fields.DateTime,
        "service": fields.Nested(service_marshaller),
    },
)


class UsersList(Resource):
    @orders_namespace.marshal_with(order, as_list=True)
    def get(self):
        """Returns all orders"""
        return get_all_orders(), 200


orders_namespace.add_resource(UsersList, "")
