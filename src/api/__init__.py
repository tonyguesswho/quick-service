from flask_restx import Api


from src.api.orders.views import orders_namespace


api = Api(version="1.0", title="Service Request API", doc="/doc")

api.add_namespace(orders_namespace, path="/orders")
