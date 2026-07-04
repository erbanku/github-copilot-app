# AGENTS.md — github-copilot-app

Public mirror of [github/app](https://github.com/github/app). No application source lives here; this repo holds release notes, issue specs, and feedback templates.

## Layout

|           Path            |                                       Purpose                                        |
| :-----------------------: | :----------------------------------------------------------------------------------: |
|      `changelog.md`       |                   Upstream release notes (synced from github/app)                    |
|      `docs/issues/`       |                       Feature specs and triage for open issues                       |
|   `contrib/issue-622/`    | Local implementation for #622: CLI, HTTP helper, CDP inject, `launch-with-button.py` |
| `.github/ISSUE_TEMPLATE/` |                            Upstream issue form templates                             |

## Issue specs

When working an issue from github/app, add a spec under `docs/issues/{number}-{slug}.md` with problem, existing behavior, proposal, related issues, and acceptance criteria. Comment on the upstream issue with a triage summary and link to the spec.

## Changelog

App-facing changelog is `changelog.md` (lowercase, upstream convention). Repo maintenance log is `CHANGELOG.md`.

Last updated: 2026-07-04
