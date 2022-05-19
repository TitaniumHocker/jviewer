"""Handlers for systemd journal."""
import typing as t
from datetime import datetime

from systemd.journal import Reader as JournalReader


def journal_stream(
    name: str,
) -> t.Generator[t.Tuple[datetime, str], None, None]:
    """Endless generator of messages from journald.

    :param name: Name of systemd unit.
    :yields: Tuple with datetime and message.
    """
    if not name.endswith(".service"):
        name = f"{name}.service"
    reader = JournalReader()
    reader.this_boot()
    reader.this_machine()
    reader.add_match(_SYSTEMD_UNIT=name)
    while True:
        if entry := reader.get_next():
            yield entry["__REALTIME_TIMESTAMP"], entry["MESSAGE"]
        else:
            reader.wait()
