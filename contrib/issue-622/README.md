# Issue 622 — Open Repo on GitHub

Closed-source `github.exe` cannot be patched here. This folder ships a **working local implementation** plus an **upstream reference patch** for `github/app`.

## Quick start (in-app button left of Run)

```powershell
python3 contrib/issue-622/launch-with-button.py
```

Starts the SQLite helper, launches GitHub Copilot with WebView2 CDP, and injects the GitHub mark button immediately left of **Run**.

## CLI only (no inject)

```powershell
python3 contrib/issue-622/open-repo-on-github.py open
```

## Manual steps

```powershell
# Terminal 1 — helper (reads ~/.copilot/data.db)
python3 contrib/issue-622/open-repo-on-github.py serve

# Terminal 2 — app + inject
$env:WEBVIEW2_ADDITIONAL_BROWSER_ARGUMENTS="--remote-debugging-port=9333 --remote-allow-origins=*"
Start-Process "$env:LOCALAPPDATA\Programs\GitHub Copilot\github.exe"
python3 contrib/issue-622/inject/cdp-inject.py
```

## Upstream reference

See `reference/` for the Rust handler + React component GitHub would add in `github/app`.

## Limitations

- Inject is session-local until GitHub ships the native button (#622).
- CDP requires restarting the app with `WEBVIEW2_ADDITIONAL_BROWSER_ARGUMENTS`.
- Helper must be running for the in-app button (launch script starts it automatically).
