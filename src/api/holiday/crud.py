from src.api.holiday.models import Holiday


def get_all_holiday():
    return Holiday.query.all()
