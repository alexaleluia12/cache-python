from flask import Flask

from . import example_app
from .common import AppException


def create_app(config=None):
    app = Flask(__name__)
    app.register_blueprint(example_app.blueprint)

    if config:
        app.config.update(config)
    return app
