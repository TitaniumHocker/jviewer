"""Forms."""
import subprocess

from flask_wtf import FlaskForm
from wtforms import fields, validators

from jviewer.const import SYSTEMCTL_PATH


class JournalForm(FlaskForm):
    """Form for unit selection."""

    unit = fields.StringField(
        "Unit",
        [validators.DataRequired()],
        description="Name of unit to view journal",
        render_kw={"placeholder": "Unit"},
    )
    submit = fields.SubmitField("Show")

    def validate_unit(self, field: fields.Field):
        """Validate unit field.

        :param field: Field to validate.
        :raise ValidationError: If field is invalid.
        """
        result = subprocess.run(
            [str(SYSTEMCTL_PATH), "is-active", field.data],
            capture_output=True,
        )
        if result.returncode != 0:
            raise validators.ValidationError(
                f"Unit {field.data} not found or inactive"
            )
