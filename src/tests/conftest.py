import pytest

from src import create_app, db  # updated
# from src.api.users.models import User
from src.config import config_by_name


@pytest.fixture(scope="module")
def test_app():
    app = create_app()
    app.config.from_object(config_by_name["testing"])
    with app.app_context():
        yield app


@pytest.fixture(scope="module")
def test_database():
    db.create_all()
    yield db
    db.session.remove()
    db.drop_all()


# @pytest.fixture(scope="function")
# def add_user():
#     def _add_user(username, email):
#         user = User(username=username, email=email)
#         db.session.add(user)
#         db.session.commit()
#         return user

#     return _add_user
