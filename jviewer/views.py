"""Views."""
from flask import redirect, render_template, request, url_for
from flask.wrappers import Response

from .forms import JournalForm
from .journal import journal_stream


def index():
    """Index page."""
    form = JournalForm()
    if form.validate_on_submit():
        return redirect(url_for("journal", unit=form.unit.data))
    return (
        render_template("index.html.j2", form=form),
        400 if form.errors else 200,
    )


def journal(unit: str):
    """Journal page."""
    if request.accept_mimetypes.accept_html:
        return render_template(
            "journal.html.j2", title=f"Journal: {unit}", unit=unit
        )

    def stream():
        for dt, msg in journal_stream(unit):
            yield f"[{dt.isoformat()}] {msg}\n"

    return Response(
        stream(),
        mimetype="text/stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
    )
