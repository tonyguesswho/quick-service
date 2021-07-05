import re
import datetime
from src.api.holiday.models import Holiday

EMAIL_REGEX = re.compile(r"\S+@\S+\.\S+")


def validate_email(value):
    if not value:
        return False
    if not EMAIL_REGEX.match(value):
        return False
    return True


def validate_order(request_date):

    datetime_now = datetime.datetime.now()
    order_datetime = datetime.datetime.strptime(
        request_date.split(".")[0], "%Y-%m-%dT%H:%M:%S"
    )

    # check if datetime is in future
    if datetime_now >= order_datetime:
        return (True, "Order can only be placed in a future date/time.")

    # check if working day/hour
    working_day = order_datetime.weekday() in range(0, 6)
    working_hours = order_datetime.hour in range(9, 17)
    if not working_day or not working_hours:
        return (
            True,
            "Order can only be placed between 9 am and after 5 pm Monday - Saturday",
        )

    # check if date in holiday
    is_holiday = Holiday.query.filter_by(date=order_datetime.date()).first()
    if is_holiday:
        return True, "Order cannot be placed on a holiday."

    # check if date is free

    return False, "Slot is available"
