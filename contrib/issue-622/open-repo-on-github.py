#!/usr/bin/env python3
"""Open active GitHub Copilot workspace repo (CLI + local helper for in-app button)."""

from __future__ import annotations

import argparse
import json
import os
import sqlite3
import subprocess
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

DEFAULT_PORT = 19622
HELPER_PORT_FILE = Path.home() / ".copilot" / "run" / "open-repo.port"


def db_path() -> Path:
    home = Path(os.environ.get("USERPROFILE") or os.environ.get("HOME") or ".")
    return home / ".copilot" / "data.db"


def resolve_repo_url() -> str:
    conn = sqlite3.connect(db_path())
    cur = conn.cursor()

    row = cur.execute("SELECT value FROM app_state WHERE key = 'workspace-mru'").fetchone()
    if not row:
        raise RuntimeError("No workspace MRU state.")

    recent = json.loads(row[0]).get("state", {}).get("recentIds") or []
    if not recent:
        raise RuntimeError("No recent workspace.")

    workspace_id = recent[0]
    cur.execute(
        """
        SELECT p.github_owner, p.github_repo, w.branch, COALESCE(ga.host, 'github.com')
        FROM workspaces w
        JOIN projects p ON p.id = w.project_id
        LEFT JOIN github_accounts ga ON ga.id = p.github_account_id
        WHERE w.id = ?
        """,
        (workspace_id,),
    )
    owner, repo, branch, host = cur.fetchone() or (None, None, None, None)
    if not owner or not repo:
        raise RuntimeError("Workspace has no GitHub remote.")

    base = host if str(host).startswith("http") else f"https://{host}"
    url = f"{base.rstrip('/')}/{owner}/{repo}"
    if branch:
        url = f"{url}/tree/{branch}"
    return url


def open_url(url: str) -> None:
    if sys.platform == "win32":
        os.startfile(url)  # noqa: S606
    elif sys.platform == "darwin":
        subprocess.run(["open", url], check=False)
    else:
        subprocess.run(["xdg-open", url], check=False)


class Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt: str, *args) -> None:
        pass

    def do_GET(self) -> None:
        if self.path not in ("/", "/url", "/health"):
            self.send_error(404)
            return
        try:
            url = resolve_repo_url()
            body = json.dumps({"url": url}).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        except Exception as exc:
            body = json.dumps({"error": str(exc)}).encode("utf-8")
            self.send_response(500)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)


def serve(port: int) -> int:
    HELPER_PORT_FILE.parent.mkdir(parents=True, exist_ok=True)
    HELPER_PORT_FILE.write_text(str(port), encoding="utf-8")
    server = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    print(f"open-repo helper on http://127.0.0.1:{port}/url", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
        if HELPER_PORT_FILE.exists():
            HELPER_PORT_FILE.unlink(missing_ok=True)
    return 0


def cmd_open(_: argparse.Namespace) -> int:
    url = resolve_repo_url()
    print(url)
    open_url(url)
    return 0


def cmd_serve(args: argparse.Namespace) -> int:
    return serve(args.port)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="cmd", required=True)

    open_p = sub.add_parser("open", help="Print URL and open in default browser")
    open_p.set_defaults(func=cmd_open)

    serve_p = sub.add_parser("serve", help="Run HTTP helper for in-app button inject")
    serve_p.add_argument("--port", type=int, default=DEFAULT_PORT)
    serve_p.set_defaults(func=cmd_serve)

    args = parser.parse_args()
    try:
        return args.func(args)
    except RuntimeError as exc:
        print(str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
