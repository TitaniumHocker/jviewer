"""JViewer: simple realtime journald viewer."""
from dynaconf import FlaskDynaconf
from flask import Flask

from jviewer import views


def create_app() -> Flask:
    """Application factory.

    :returns: Application.
    """
    app = Flask(__name__)

    FlaskDynaconf(app)
    app.config.load_extensions()  # type: ignore

    app.add_url_rule("/", "index", views.index, methods=["GET", "POST"])
    app.add_url_rule("/journal/<unit>", "journal", views.journal)

    return app
