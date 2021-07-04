from flask_restx import Api


from src.api.orders.views import orders_namespace

from src.api.services.views import services_namespace


api = Api(version="1.0", title="Service Request API", doc="/")

api.add_namespace(orders_namespace, path="/orders")
api.add_namespace(services_namespace, path="/services")
