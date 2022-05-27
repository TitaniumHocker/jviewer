"""WSGI entrypoint."""
from jviewer import create_app

app = application = create_app("production")
