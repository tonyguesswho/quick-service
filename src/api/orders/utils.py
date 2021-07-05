import re
import datetime
from src.api.holiday.models import Holiday
from src.api.orders.models import Order
from sqlalchemy import func, and_, or_

import math


EMAIL_REGEX = re.compile(r"\S+@\S+\.\S+")


def validate_email(value):
    if not value:
        return False
    if not EMAIL_REGEX.match(value):
        return False
    return True


def validate_order(order_datetime, request_date, service):

    datetime_now = datetime.datetime.now()

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

    stripped_datetime = re.sub("T", " ", request_date)

    is_booked = (
        Order.query.filter(
            or_(
                and_(
                    Order.request_date
                    >= func.TO_TIMESTAMP(
                        stripped_datetime,
                        "YYYY-MM-DD HH24:MI:SS",
                    ),
                    Order.request_date
                    < func.TO_TIMESTAMP(
                        stripped_datetime,
                        "YYYY-MM-DD HH24:MI:SS",
                    )
                    + func.make_interval(0, 0, 0, 0, 0, math.floor(service.duration)),
                ),
                and_(
                    Order.request_date
                    < func.TO_TIMESTAMP(
                        stripped_datetime,
                        "YYYY-MM-DD HH24:MI:SS",
                    ),
                    Order.end_date
                    > func.TO_TIMESTAMP(
                        stripped_datetime,
                        "YYYY-MM-DD HH24:MI:SS",
                    ),
                ),
            )
        )
        .limit(1)
        .one_or_none()
    )
    if is_booked:
        return True, "Slot is not available"

    return False, "Slot is available"
