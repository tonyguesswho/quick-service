from src.api.services.models import Service


def get_all_services():
    return Service.query.all()


def get_service_by_id(service_id):
    return Service.query.filter_by(id=service_id).first()
