import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin

from .config import config_by_name
from flask_cors import CORS

# instantiate the db
db = SQLAlchemy()

admin = Admin(template_mode="bootstrap3")


def create_app(script_info=None):

    # instantiate the app
    app = Flask(__name__)

    CORS(app)

    # set config
    ENV = os.getenv("FLASK_ENV", "development")
    app.config.from_object(config_by_name[ENV])

    # set up extensions
    db.init_app(app)
    if os.getenv("FLASK_ENV") == "development":
        admin.init_app(app)

    # register api
    from src.api import api

    api.init_app(app)

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {"app": app, "db": db}

    return app
