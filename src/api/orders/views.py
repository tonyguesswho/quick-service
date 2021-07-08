from flask import Blueprint, request
from flask_restx import Api, Resource, fields, Namespace, marshal
from src.api.services.views import service_marshaller
from .utils import validate_email, validate_order

# from src.api.holiday.models import Holiday
import datetime


from src.api.orders.crud import get_all_orders, add_order, get_order_by_id, delete_order

from src.api.services.crud import get_service_by_id  # isort:skip

orders_blueprint = Blueprint("orders", __name__)
api = Api(orders_blueprint)

orders_namespace = Namespace("orders")


order = orders_namespace.model(
    "Order",
    {
        "id": fields.Integer(readOnly=True),
        "service_id": fields.Integer(required=True),
        "email": fields.String(
            required=True, attribute="customer_id", example="some.user@email"
        ),
        "created_date": fields.DateTime,
        "updated_date": fields.DateTime,
        "request_date": fields.DateTime(
            required=True, validate=True, example="2020-12-01T01:59:39.297904Z"
        ),
        "end_date": fields.DateTime(readOnly=True),
        "service": fields.Nested(api.model("Service", service_marshaller)),
    },
)


class OrdersList(Resource):
    @orders_namespace.marshal_with(order, as_list=True, envelope="data")
    def get(self):
        """Returns all orders"""
        service_id = request.args.get("service_id")
        start_date = request.args.get("start_date")
        end_date = request.args.get("end_date")
        try:
            return get_all_orders(service_id, start_date, end_date), 200
        except Exception:
            orders_namespace.abort(400, "An error occured")

    @orders_namespace.expect(order, validate=True)
    @orders_namespace.response(201, "service request was created")
    @orders_namespace.response(400, "Service not available")
    def post(self):
        """Creates a new service request."""
        post_data = request.get_json()
        service_id = post_data.get("service_id")
        customer_id = post_data.get("email")
        request_date = post_data.get("request_date")
        response_object = {}
        order_datetime = datetime.datetime.strptime(
            request_date.split(".")[0], "%Y-%m-%dT%H:%M:%S"
        )

        if not validate_email(customer_id):
            response_object["message"] = "Invalid email"
            return response_object, 400

        service = get_service_by_id(service_id)
        if not service:
            response_object["message"] = "Service ID is invalid."
            return response_object, 400

        # Validate Order date/time
        error, message = validate_order(order_datetime, request_date, service)
        if error:
            response_object["message"] = message
            return response_object, 400

        end_date = order_datetime + datetime.timedelta(minutes=service.duration)
        try:
            new_order = add_order(service_id, customer_id, request_date, end_date)
        except Exception:
            orders_namespace.abort(400, "An error occured")

        response_object["message"] = "service request was created successfully!"
        response_object["data"] = marshal(new_order, order)
        return response_object, 201


class Orders(Resource):
    @orders_namespace.marshal_with(order)
    @orders_namespace.response(200, "Success")
    @orders_namespace.response(404, "Order <order_id> does not exist")
    def get(self, order_id):
        """Returns a single user."""
        returned_order = get_order_by_id(order_id)
        if not returned_order:
            orders_namespace.abort(404, f"Order {order_id} does not exist")
        try:
            return returned_order, 200
        except Exception:
            orders_namespace.abort(400, "An error occured")

    @orders_namespace.response(200, "<order_id> was removed!")  # new
    @orders_namespace.response(404, "Order <order_id> does not exist")  # new
    def delete(self, order_id):
        """ "Deletes an order."""  # new
        response_object = {}
        order = get_order_by_id(order_id)
        if not order:
            orders_namespace.abort(404, f"User {order_id} does not exist")
        try:
            delete_order(order)
        except Exception:
            orders_namespace.abort(400, "An error occured")

        response_object["message"] = "order was removed!"
        return response_object, 200


orders_namespace.add_resource(OrdersList, "")
orders_namespace.add_resource(Orders, "/<int:order_id>")
