# Issue #622: Open Repo in GitHub Button

|         Field         |                           Value                            |
| :-------------------: | :--------------------------------------------------------: |
|         Issue         | [github/app#622](https://github.com/github/app/issues/622) |
|        Status         |                            Open                            |
|     Reported from     |                          `/chat`                           |
| App version at report |                           0.2.19                           |

## Problem

Users in a chat or workspace session need a visible way to open the active repository on GitHub.com. The current path is buried: right-click the project in the sidebar and choose **Open on GitHub**. That is easy to miss when you are already focused on the chat surface.

## Existing behavior

|              Surface               |                   Action                   |  Since  |
| :--------------------------------: | :----------------------------------------: | :-----: |
|    Sidebar project context menu    |             **Open on GitHub**             | v0.2.31 |
| Project Settings (config file row) |          **Open on GitHub** link           |    —    |
|         Workspace dropdown         | Folder icon reveals session folder locally | v1.0.12 |

No first-class control exists in the window header or chat surface.

## Proposed solution

Add an **Open on GitHub** icon button in the **upper-right window toolbar**, immediately **to the left of the Run button**.

```
┌─────────────────────────────────────────────────────────────┐
│  …                                    [mark]  [Run ▾]  ─ □ × │
└─────────────────────────────────────────────────────────────┘
                                         ↑ new
```

### Placement

- **Region:** Top-right window chrome (same row as Run).
- **Order:** `[Open on GitHub]` then `[Run]` (left to right).
- **Style:** Icon-only ghost button using the GitHub mark; matches adjacent header controls.
- **Responsive:** At narrow widths, compact to icon-only before crowding Run (same pattern as automation run headers).

### Behavior

- Visible only for GitHub-backed repositories (hide for local-only or non-GitHub remotes).
- Opens `https://github.com/{owner}/{repo}` in the default browser.
- Respect GitHub Enterprise host from the signed-in account (same host resolution as sidebar **Open on GitHub**).
- Optional: append current branch as a tree URL segment when a branch is checked out.
- Tooltip: `Open repository on GitHub`.
- Keyboard shortcut (optional follow-up): none in v1; add to Settings → Keyboard Shortcuts if requested.

### Why upper-right, left of Run

- Always visible on `/chat` without opening a dropdown or context menu.
- Sits in established window chrome where users already look for session actions.
- Pairs naturally with Run: local execution on the right, remote repo on the left.

### Alternatives considered

|             Placement             |         Pros          |                   Cons                   |
| :-------------------------------: | :-------------------: | :--------------------------------------: |
|        Workspace dropdown         | Near branch/path info | Hidden behind a click; less discoverable |
|        Chat title popover         | Near session metadata |   Popover is infrequent; less visible    |
|         Composer toolbar          |    High visibility    | Crowded; not repo-specific in quick chat |
| Sidebar project row (inline icon) |    Always visible     | Clutter; duplicates context-menu action  |

## Related issues

|                       Issue                        |                        Overlap                         |
| :------------------------------------------------: | :----------------------------------------------------: |
| [#1359](https://github.com/github/app/issues/1359) |     Broader in-app GitHub browsing; complementary      |
| [#1657](https://github.com/github/app/issues/1657) | Open `github/app` for feedback; different target repo  |
| [#1314](https://github.com/github/app/issues/1314) | GHE host resolution for links; same host logic applies |

## Acceptance criteria

1. From an active workspace chat (`/chat`), an **Open on GitHub** button appears in the upper-right window toolbar, immediately left of **Run**.
2. One click opens the repository in the default browser without using the sidebar context menu.
3. Control is hidden when no GitHub remote is associated with the workspace.
4. GHE and github.com both resolve to the correct host.
5. Screen readers announce the button purpose (`Open repository on GitHub`).
6. At narrow window widths, the button remains usable and does not overlap or displace **Run**.

## Workaround (current)

Right-click the project name in the sidebar → **Open on GitHub**.

## Local implementation (this repo)

Upstream `github/app` has no public UI source. Working implementations live in [`contrib/issue-622/`](../../contrib/issue-622/):

|                       Artifact                        |                        Purpose                        |
| :---------------------------------------------------: | :---------------------------------------------------: |
| `inject/open-repo-button.js` + `inject/cdp-inject.py` | In-app button left of **Run** via WebView2 CDP inject |
|               `open-repo-on-github.py`                |   CLI: open MRU workspace repo in browser (SQLite)    |
|                     `reference/`                      | Upstream patch sketch (Tauri command + React button)  |
