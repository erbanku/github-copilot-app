import { MarkGithubIcon } from "@primer/octicons-react";
import { IconButton } from "@primer/react";
import { invoke } from "@tauri-apps/api/core";

type Props = {
    projectId: string | null;
    disabled?: boolean;
};

export function OpenOnGitHubButton({ projectId, disabled }: Props) {
    if (!projectId) return null;

    return (
        <IconButton
            aria-label="Open repository on GitHub"
            title="Open repository on GitHub"
            icon={MarkGithubIcon}
            disabled={disabled}
            onClick={() => invoke("open_project_on_github", { projectId })}
        />
    );
}
