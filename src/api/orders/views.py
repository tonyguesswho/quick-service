from flask import Blueprint, request
from flask_restx import Api, Resource, fields, Namespace, marshal
from src.api.services.views import service_marshaller
from .utils import validate_email, validate_order

# from src.api.holiday.models import Holiday
import datetime


from src.api.orders.crud import get_all_orders, add_order  # isort:skip

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
        return get_all_orders(), 200

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
        error, message = validate_order(order_datetime)
        if error:
            response_object["message"] = message
            return response_object, 400

        end_date = order_datetime + datetime.timedelta(minutes=service.duration)
        new_order = add_order(service_id, customer_id, request_date, end_date)

        response_object["message"] = "service request was created successfully!"
        response_object["data"] = marshal(new_order, order)
        return response_object, 201


orders_namespace.add_resource(OrdersList, "")
