"""JViewer: simple realtime journald viewer."""
import typing as t
from os import environ

from dynaconf import FlaskDynaconf
from flask import Flask

from jviewer import views


def create_app(env: t.Optional[str] = None) -> Flask:
    """Application factory.

    :returns: Application.
    """
    app = Flask(__name__)

    FlaskDynaconf(
        app,
        env=env
        if env is not None
        else environ.get("FLASK_ENV", "development"),
    )
    app.config.load_extensions()  # type: ignore

    app.add_url_rule("/", "index", views.index, methods=["GET", "POST"])
    app.add_url_rule("/journal/<unit>", "journal", views.journal)

    return app
