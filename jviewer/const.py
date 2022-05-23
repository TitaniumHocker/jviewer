"""Constants."""
from pathlib import Path

if Path("/usr/bin/systemctl").is_file():
    SYSTEMCTL_PATH = Path("/usr/bin/systemctl")
elif Path("/bin/systemctl").is_file():
    SYSTEMCTL_PATH = Path("/bin/systemctl")
else:
    raise ValueError("systemctl binary not found")
