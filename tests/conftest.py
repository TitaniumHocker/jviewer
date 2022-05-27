import pytest

from jviewer import create_app


@pytest.fixture(scope="session")
def app():
    app = create_app("testing")
    with app.app_context():
        yield app


@pytest.fixture(scope="session")
def client(app):
    with app.test_client() as client:
        yield client

