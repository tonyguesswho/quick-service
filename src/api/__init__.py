from flask_restx import Api
from jsonschema import FormatChecker


from src.api.orders.views import orders_namespace

from src.api.services.views import services_namespace
from src.api.holiday.views import holiday_namespace


api = Api(
    version="1.0",
    title="Service Request API",
    format_checker=FormatChecker(formats=("date-time", "email")),
    doc="/",
)

api.add_namespace(orders_namespace, path="/orders")
api.add_namespace(services_namespace, path="/services")
api.add_namespace(holiday_namespace, path="/holiday")
