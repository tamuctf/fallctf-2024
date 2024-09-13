from os import environ
import uuid


class Config:
    FLAG = environ.get('FLAG')
    PORT = environ.get('PORT')
    SECRET_KEY = uuid.uuid4().hex

    FLASKAPP = "app.py"
    FLAG_DEBUG = False

    SQLALCHEMY_DATABASE_URI = "sqlite:///submissions.db"
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
