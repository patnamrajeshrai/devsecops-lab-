#!/usr/bin/env python3

import json
import platform
import shutil
import socket
import subprocess
from datetime import datetime, timezone


def get_command_output(command):
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=5,
            check=True
        )
        return result.stdout.strip()
    except (subprocess.SubprocessError, OSError):
        return "Unavailable"


disk = shutil.disk_usage("/")

health = {
    "hostname": socket.gethostname(),
    "os": platform.platform(),
    "python_version": platform.python_version(),
    "cpu_cores": __import__("os").cpu_count(),
    "root_disk_total_gb": round(disk.total / (1024 ** 3), 2),
    "root_disk_used_gb": round(disk.used / (1024 ** 3), 2),
    "root_disk_free_gb": round(disk.free / (1024 ** 3), 2),
    "uptime": get_command_output(["uptime", "-p"]),
    "checked_at_utc": datetime.now(timezone.utc).isoformat()
}

print(json.dumps(health, indent=2))
