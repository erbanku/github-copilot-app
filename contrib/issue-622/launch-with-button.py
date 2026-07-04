#!/usr/bin/env python3
"""Start helper, restart GitHub Copilot with CDP, inject Open on GitHub button."""

from __future__ import annotations

import json
import os
import socket
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PY = sys.executable
CDP_PORT = 9333
HELPER_PORT = 19622
APP = Path(os.environ.get("LOCALAPPDATA", "")) / "Programs" / "GitHub Copilot" / "github.exe"


def port_open(port: int) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(0.5)
        try:
            s.connect(("127.0.0.1", port))
            return True
        except OSError:
            return False


def cdp_ready(port: int) -> bool:
    try:
        with urllib.request.urlopen(f"http://127.0.0.1:{port}/json/list", timeout=2) as resp:
            json.load(resp)
        return True
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError):
        return False


def start_helper() -> None:
    if port_open(HELPER_PORT):
        return
    subprocess.Popen(
        [PY, str(ROOT / "open-repo-on-github.py"), "serve", "--port", str(HELPER_PORT)],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0),
    )
    for _ in range(20):
        if port_open(HELPER_PORT):
            return
        time.sleep(0.25)


def restart_app_with_cdp() -> None:
    if sys.platform == "win32":
        subprocess.run(["taskkill", "/IM", "github.exe", "/F"], capture_output=True)
        time.sleep(2)
    env = os.environ.copy()
    env["WEBVIEW2_ADDITIONAL_BROWSER_ARGUMENTS"] = (
        f"--remote-debugging-port={CDP_PORT} --remote-allow-origins=*"
    )
    if not APP.is_file():
        raise SystemExit(f"GitHub Copilot not found: {APP}")
    subprocess.Popen([str(APP)], env=env)
    for _ in range(40):
        if cdp_ready(CDP_PORT):
            return
        time.sleep(0.5)
    raise SystemExit(f"CDP not available on port {CDP_PORT}")


def inject() -> None:
    rc = subprocess.call([PY, str(ROOT / "inject" / "cdp-inject.py"), str(CDP_PORT)])
    raise SystemExit(rc)


def main() -> None:
    start_helper()
    restart_app_with_cdp()
    inject()


if __name__ == "__main__":
    main()
