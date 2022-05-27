import typing as t

import pytest
from flask import Flask
from pytest import MonkeyPatch
from wtforms import ValidationError
from wtforms.fields import Field

from jviewer import forms


@pytest.mark.parametrize(
    ("unit", "is_correct"),
    (("docker", True), ("adwawdwadwa", False)),
)
@pytest.mark.parametrize("valid_units", (("postfix", "docker", "dovecot"),))
def test_journal_form_validator(
    app: Flask,
    unit: str,
    is_correct: bool,
    valid_units: t.Iterable[str],
    monkeypatch: MonkeyPatch,
):
    def mocked_run(cmd: t.List[str], *args, **kwargs):
        class Result:
            def __init__(self, returncode):
                self.returncode = returncode

        return Result(0 if cmd[2] in valid_units else 1)

    monkeypatch.setattr(forms.subprocess, "run", mocked_run)
    form = forms.JournalForm()
    form.unit.process_data(unit)
    assert form.validate() == is_correct
