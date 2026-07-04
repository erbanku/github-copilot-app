// Wire in workspace header toolbar — place before Run control.

import { OpenOnGitHubButton } from "./OpenOnGitHubButton";

export function WorkspaceHeaderActions({
    projectId,
}: {
    projectId: string | null;
}) {
    return (
        <div className="workspace-header-actions">
            <OpenOnGitHubButton projectId={projectId} />
            {/* existing Run menu/button follows */}
            <RunWorkspaceScriptButton />
        </div>
    );
}
