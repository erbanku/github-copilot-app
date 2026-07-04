#!/usr/bin/env rust-script
//! ```cargo
//! [dependencies]
//! rusqlite = { version = "0.32", features = ["bundled"] }
//! serde_json = "1"
//! ```
//! Open the most recently used GitHub Copilot app workspace repository in the browser.

use rusqlite::Connection;
use serde_json::Value;
use std::env;
use std::path::PathBuf;
use std::process::Command;

fn copilot_db_path() -> PathBuf {
    dirs_home().join(".copilot").join("data.db")
}

fn dirs_home() -> PathBuf {
    env::var("USERPROFILE")
        .or_else(|_| env::var("HOME"))
        .map(PathBuf::from)
        .unwrap_or_else(|_| PathBuf::from("."))
}

fn recent_workspace_id(conn: &Connection) -> rusqlite::Result<Option<String>> {
    let raw: String = conn.query_row(
        "SELECT value FROM app_state WHERE key = 'workspace-mru' LIMIT 1",
        [],
        |row| row.get(0),
    )?;
    let json: Value = serde_json::from_str(&raw).unwrap_or(Value::Null);
    let id = json
        .pointer("/state/recentIds/0")
        .and_then(Value::as_str)
        .map(str::to_string);
    Ok(id)
}

fn repo_url(conn: &Connection, workspace_id: &str) -> rusqlite::Result<Option<String>> {
    conn.query_row(
        "SELECT p.github_owner, p.github_repo, w.branch, COALESCE(ga.host, 'github.com')
         FROM workspaces w
         JOIN projects p ON p.id = w.project_id
         LEFT JOIN github_accounts ga ON ga.id = p.github_account_id
         WHERE w.id = ?1",
        [workspace_id],
        |row| {
            let owner: Option<String> = row.get(0)?;
            let repo: Option<String> = row.get(1)?;
            let branch: String = row.get(2)?;
            let host: String = row.get(3)?;
            let (owner, repo) = match (owner, repo) {
                (Some(o), Some(r)) if !o.is_empty() && !r.is_empty() => (o, r),
                _ => return Ok(None),
            };
            let base = if host.starts_with("http") {
                host.trim_end_matches('/').to_string()
            } else {
                format!("https://{host}")
            };
            let mut url = format!("{base}/{owner}/{repo}");
            if !branch.is_empty() {
                url.push_str("/tree/");
                url.push_str(&branch.replace('/', "%2F"));
            }
            Ok(Some(url))
        },
    )
}

fn open_in_browser(url: &str) {
    #[cfg(target_os = "windows")]
    {
        let _ = Command::new("cmd").args(["/C", "start", "", url]).spawn();
    }
    #[cfg(target_os = "macos")]
    {
        let _ = Command::new("open").arg(url).spawn();
    }
    #[cfg(all(unix, not(target_os = "macos")))]
    {
        let _ = Command::new("xdg-open").arg(url).spawn();
    }
}

fn main() {
    let db = copilot_db_path();
    let conn = Connection::open(&db).unwrap_or_else(|e| {
        eprintln!("Failed to open {}: {e}", db.display());
        std::process::exit(1);
    });

    let workspace_id = recent_workspace_id(&conn)
        .ok()
        .flatten()
        .unwrap_or_else(|| {
            eprintln!("No recent workspace in Copilot app state.");
            std::process::exit(1);
        });

    let url = repo_url(&conn, &workspace_id)
        .ok()
        .flatten()
        .unwrap_or_else(|| {
            eprintln!("Workspace is not linked to a GitHub repository.");
            std::process::exit(1);
        });

    println!("{url}");
    open_in_browser(&url);
}
