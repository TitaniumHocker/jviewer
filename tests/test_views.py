import typing as t
from datetime import datetime

import pytest
from flask.testing import FlaskClient
from pytest import MonkeyPatch
from wtforms import ValidationError
from wtforms.fields import Field

from jviewer import views
from jviewer.forms import JournalForm


def test_index_get(client: FlaskClient):
    response = client.get("/")
    assert response.status_code == 200
    assert b"<form" in response.data


@pytest.mark.parametrize(
    ("payload", "response_status"),
    (({"unit": "docker"}, 302), ({"unit": "adadawdadadw"}, 400)),
)
@pytest.mark.parametrize("valid_units", (("postfix", "docker", "dovecot"),))
def test_index_post(
    client: FlaskClient,
    valid_units: t.Iterable[str],
    payload: t.Any,
    response_status: int,
    monkeypatch: MonkeyPatch,
):
    def mocked_validator(self, field: Field):
        if field.data not in valid_units:
            raise ValidationError()

    monkeypatch.setattr(JournalForm, "validate_unit", mocked_validator)

    response = client.post("/", data=payload)
    assert response.status_code == response_status


def test_journal_get_html(client):
    assert (
        client.get(
            "/journal/shit", headers={"Accept": "text/html"}
        ).status_code
        == 200
    )


def test_journal_get_stream(client, monkeypatch):
    def mocked_journal_stream(_):
        for i in range(10):
            yield datetime.now(), f"{i}"

    monkeypatch.setattr(views, "journal_stream", mocked_journal_stream)
    response = client.get("/journal/unit", headers={"Accept": "text/stream"})
    assert response.status_code == 200
    assert response.mimetype == "text/stream"
    assert response.is_streamed
