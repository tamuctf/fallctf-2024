from src.util.db_schema import db

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import config


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(config.Config)

    db.init_app(app)

    with app.app_context():
        from src.blueprints import pages

        app.register_blueprint(pages.pages)

        db.create_all()

    return app
