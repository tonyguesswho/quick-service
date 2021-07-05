import pytest
from src.api.services.models import Service
from src.api.holiday.models import Holiday

from src import create_app, db  # updated

# from src.api.users.models import User
from src.config import config_by_name


@pytest.fixture(scope="module")
def test_app():
    app = create_app()
    app.config.from_object(config_by_name["testing"])
    with app.app_context():
        yield app


@pytest.fixture(scope="function")
def test_database():
    db.create_all()
    yield db
    db.session.remove()
    db.drop_all()


@pytest.fixture(scope="function")
def add_service():
    def _add_service(name, duration):
        service = Service(name=name, duration=duration)
        db.session.add(service)
        db.session.commit()
        return service

    return _add_service


@pytest.fixture(scope="function")
def add_holiday():
    def _add_holiday(name, date):
        holiday = Holiday(name=name, date=date)
        db.session.add(holiday)
        db.session.commit()
        return holiday

    return _add_holiday
