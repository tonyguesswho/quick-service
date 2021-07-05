from flask import Blueprint
from flask_restx import Api, Resource, fields, Namespace


from src.api.holiday.crud import get_all_holiday

holiday_blueprint = Blueprint("holiday", __name__)
api = Api(holiday_blueprint)

holiday_namespace = Namespace("holiday")

holiday_marshaller = {
    "id": fields.Integer(readOnly=True),
    "name": fields.String(required=True),
    "date": fields.DateTime,
}


holiday = holiday_namespace.model(
    "Holiday",
    holiday_marshaller,
)


class HolidayList(Resource):
    @holiday_namespace.marshal_with(holiday, as_list=True, envelope="data")
    def get(self):
        """Returns all services"""
        return get_all_holiday(), 200


holiday_namespace.add_resource(HolidayList, "")
