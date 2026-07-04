//! Tauri command — upstream reference for github/app issue #622

use tauri::{AppHandle, Manager};
use tauri_plugin_opener::OpenerExt;

#[tauri::command]
pub async fn open_project_on_github(app: AppHandle, project_id: String) -> Result<(), String> {
    let project = app
        .state::<ProjectStore>()
        .get(&project_id)
        .ok_or_else(|| "Project not found".to_string())?;

    let owner = project.github_owner.ok_or("Project has no GitHub owner")?;
    let repo = project.github_repo.ok_or("Project has no GitHub repository")?;
    let host = project
        .github_host
        .unwrap_or_else(|| "https://github.com".to_string());
    let url = format!("{}/{}/{}", host.trim_end_matches('/'), owner, repo);

    app.opener()
        .open_url(url, None::<&str>)
        .map_err(|e| e.to_string())
}
