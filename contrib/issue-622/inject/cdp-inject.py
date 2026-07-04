#!/usr/bin/env python3
"""Inject Open on GitHub button into GitHub Copilot app via Chrome DevTools Protocol."""

import json
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 9333
SCRIPT = Path(__file__).with_name("open-repo-button.js").read_text(encoding="utf-8")


def get_targets():
    with urllib.request.urlopen(f"http://127.0.0.1:{PORT}/json/list", timeout=3) as resp:
        return json.load(resp)


def inject_via_cdp(ws_url: str) -> None:
    try:
        import websocket
    except ImportError:
        import subprocess

        subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "websocket-client"])
        import websocket

    ws = websocket.create_connection(ws_url, timeout=5)
    try:
        ws.send(
            json.dumps(
                {
                    "id": 1,
                    "method": "Page.addScriptToEvaluateOnNewDocument",
                    "params": {"source": SCRIPT},
                }
            )
        )
        ws.recv()
        ws.send(json.dumps({"id": 2, "method": "Runtime.evaluate", "params": {"expression": SCRIPT}}))
        ws.recv()
    finally:
        ws.close()


def main() -> int:
    for _ in range(30):
        try:
            targets = get_targets()
            break
        except (urllib.error.URLError, TimeoutError):
            time.sleep(1)
    else:
        print(
            f"No DevTools on port {PORT}. Restart GitHub Copilot with:\n"
            f'  $env:WEBVIEW2_ADDITIONAL_BROWSER_ARGUMENTS="--remote-debugging-port={PORT} --remote-allow-origins=*"',
            file=sys.stderr,
        )
        return 1

    page = next((t for t in targets if t.get("type") == "page" and "GitHub" in t.get("title", "")), None)
    page = page or next((t for t in targets if t.get("type") == "page"), None)
    if not page:
        print("No WebView page target found.", file=sys.stderr)
        return 1

    inject_via_cdp(page["webSocketDebuggerUrl"])
    print(f"Injected into: {page.get('title') or page.get('url')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
