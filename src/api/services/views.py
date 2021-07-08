from flask import Blueprint
from flask_restx import Api, Resource, fields, Namespace


from src.api.services.crud import get_all_services, get_service_by_id  # isort:skip

services_blueprint = Blueprint("services", __name__)
api = Api(services_blueprint)

services_namespace = Namespace("services")

service_marshaller = {
    "id": fields.Integer(readOnly=True),
    "name": fields.String(required=True),
    "duration": fields.Float(required=True),
    "created_date": fields.DateTime,
    "updated_date": fields.DateTime,
}


service = services_namespace.model(
    "Service",
    service_marshaller,
)


class ServicesList(Resource):
    @services_namespace.marshal_with(service, as_list=True, envelope="data")
    def get(self):
        """Returns all services"""
        try:
            return get_all_services(), 200
        except Exception:
            services_namespace.abort(400, "An error occured")


class Services(Resource):
    @services_namespace.marshal_with(service)
    @services_namespace.response(200, "Success")
    @services_namespace.response(404, "Service <service_id> does not exist")
    def get(self, service_id):
        """Returns a single user."""
        returned_service = get_service_by_id(service_id)
        if not returned_service:
            services_namespace.abort(404, f"Service {service_id} does not exist")
        try:
            return returned_service, 200
        except Exception:
            services_namespace.abort(400, "An error occured")


services_namespace.add_resource(ServicesList, "")
services_namespace.add_resource(Services, "/<int:service_id>")
