# Changelog

## v0.2.14

### Added

- Added a copy button to the markdown editor toolbar so you can copy the full document contents to your clipboard without manually selecting all the text.
- The app now prompts you to review and trust a repository's `.github/github-app.yml` configuration file before applying any of its customizations (scripts, system-prompt injections, or automation settings). The conversation input is blocked until you approve or dismiss, and you can review or revoke trust at any time from the project settings.
- The rubber-duck agent is now enabled by default for all users, providing constructive feedback on code and designs via the /rubber-duck slash command.

### Changed

- Exporting a reply as a secret gist no longer shows a success toast — the browser opens the gist automatically and the URL is copied to your clipboard.
- Improved the MCP Servers settings page with a unified Add server button, a searchable popular servers grid with text highlighting, and a better empty state with actionable guidance.
- Reordered settings for easier access — Scripts now appears higher in Project Settings, and Default model now appears higher in General Settings.
- The Status filter in the filter bar now supports multi-select, letting you view open and closed items at the same time.

### Fixed

- Expanded sidebar project groups with no sessions now show a 'No sessions yet' label instead of appearing blank.
- Fixed spurious "git-lfs is not installed" errors when creating worktree sessions for repositories that use Git LFS, even with git-lfs installed and working in your terminal.
- Fixed the keyboard shortcuts dialog so the "Current view" tab (previously "Contextual") only shows shortcuts specific to the active view, hides the tab selector entirely when no view-specific shortcuts exist, and scrolls to the top when switching tabs
- Loading spinners now rotate around their own center instead of an offset point.
- On macOS, the bash tool in agent sessions now correctly inherits your login shell's PATH, so tools installed via Homebrew, fnm, nvm, and similar managers no longer report "command not found".
- Slash commands (such as /chronicle) now show their short command text in the conversation timeline instead of the full verbose system prompt.
- The Changes toolbar no longer shows a branch sync button for folder workspaces that have no local git context.

## v0.2.13

### Added

- Added experimental Voice mode that lets you capture speech locally and insert transcripts into the composer using a configurable shortcut, with support for push-to-talk or toggle mode, microphone device selection, and local transcription model management.

### Changed

- In workspace sessions, Cmd+T (Ctrl+T on Windows/Linux) now opens the add-tab palette for the right panel instead of creating a new chat session.
- Inline review threads the agent skipped (e.g. when several comments arrive at once and the agent collapses them into a single reply) now show an "Unanswered" badge instead of the alarming "Error" badge. The "Error" label is reserved for true failures where a reply was produced but didn't stick. The inline review prompt also now explicitly tells the agent that each thread in a batch needs its own reply_to_comment call.
- Skill invocations (e.g. /e2e-test-author, /design-foundations) now appear as a labeled card pill in the conversation instead of showing the raw prompt text.
- The branch sync indicator now shows 'Behind origin/<base> (N↓) · Update branch' when your branch is behind its PR base, making it easier to distinguish this case from being diverged from your own remote.
- The macOS Help menu now has working links to Documentation, What's New, Automations, MCP Servers, and Skills resources, and menu items have been reorganized and relabeled for clarity.
- Workspaces now silently auto-sync to their server branch when it's safe to do so. PR review workspaces fast-forward when the local tree is clean and there are no unpushed commits; author workspaces fast-forward or, when there are clean unpushed commits and `merge-tree` predicts no conflicts, auto-merge upstream into the local branch. Anything riskier (dirty tree, predicted conflicts) keeps today's manual "Sync" / "Resolve conflicts" affordance.

### Fixed

- Clicking a session or action in the system tray menu now reliably brings the app to the foreground on macOS.
- Filter queries using GitHub's comma-list shorthand (e.g. `repo:a/b,c/d`, `label:bug,docs`) now parse into separate filter pill values instead of a single literal value with embedded commas.
- Fixed crash when editing certain MCP servers in Settings and corrected server type badge display
- Help menu items (Keyboard Shortcuts, Share Feedback, Run Health Check, Show Home Tips Again, Credits, Manage Copilot Subscription) are now correctly disabled and grayed out during onboarding instead of appearing active but doing nothing when clicked.
- Pasting a full GitHub URL (e.g. an issue or PR link) into the Add GitHub Repository field now correctly resolves to the repository instead of returning no results.
- Pasting a GitHub repository URL into the quick-open dialog now correctly finds and shows the matching repository.
- Selecting multiple values in a filter pill (e.g. Author, Assignee) now correctly matches any of the selected values instead of silently returning no results.
- The session list now only includes sessions that were directly created by the CLI.

## v0.2.12

### Added

- Added a Comments filter pill to My work for filtering by total comment count. Pick an operator (greater than, at least, less than, at most, exactly, or between) and enter a number.
- Added a copy-to-clipboard button to the pasted text preview dialog, and made the text selectable so content can be copied via standard text selection.
- Added a hidden minigame to the home screen — find the secret platform to start an infinite jumping adventure with power-ups, hazards, and a persistent high score.
- Added a native system tray menu with live session status, PR checks and review info, badge notifications for sessions needing attention, quick actions to create sessions and chats, and a Settings toggle to show or hide the tray icon.
- Added a terminal font picker in Settings that lists your installed fonts, previews each in its own typeface, and applies your selection to the embedded terminal.
- Right-clicking a pull request or issue reference in a conversation now shows a context menu with a "Copy link" option to quickly copy the GitHub URL.

### Changed

- Error screens now show a plain text recovery UI instead of an illustration.
- Project color picker in the repository context menu now displays as a compact 4x2 grid of color tiles, making it faster to scan and select. Orange has been added as a new color option.

### Fixed

- Avatar fallback initials no longer overflow for multi-word names — they are now capped at two letters.
- Fixed a spurious "Error" badge appearing on inline review comment threads after the agent successfully replied to a review comment.
- PR and issue badges now correctly respect the 'Use a pointer cursor over buttons and links' accessibility setting instead of always showing a pointer cursor.

## v0.2.11

### Added

- Added a Conversation timeline toggle in Settings > General, letting you enable a timeline scrubber and bookmark controls for quickly navigating long conversations.
- Added Toolbox in Foundry to the popular MCP servers list in Settings, making it easy to connect a Microsoft Foundry-hosted toolbox endpoint without manual configuration.

### Changed

- Account usage in Settings now shows AI credits terminology, contextual Manage budget and Upgrade plan links, and updated overage copy for users on usage-based billing plans.
- The copy button next to the PR or issue number now copies the full GitHub URL instead of just the bare number.
- Users on usage-based billing plans now see AI credit quota labels, accurate quota error messages, and session AI-credit spend in the composer gauge and sidebar.

### Fixed

- Emoji reactions and the approve/request-changes badge are now shown on PR review summary comments in the pull request view.
- Fixed filter pills (Author, Assignees, etc.) appearing to return no results when typing — items were rendered but hidden behind an invisible block.
- Fixed scroll position drifting off the viewport in the pull request diff view when inline review threads grow taller (e.g., when a new reply is added to a review thread).
- Pasting a closed or merged pull request URL into the workspace creation dialog now correctly finds and shows the pull request.

## v0.2.10

### Changed

- Merging a pull request now updates the UI immediately with a pulsing "Finalizing merge…" indicator, rather than waiting for the full server round-trip to complete.
- Model picker now groups models by capability tier (Versatile, Powerful, Lightweight), shows recently used models, and adds an Unavailable section for policy-gated models. Anthropic model labels no longer include the redundant "Claude" prefix.

### Fixed

- Fixed the diff view jumping or shifting when the agent edits files while you are scrolling through changes.
- Slash-command menu on the home screen no longer appears behind the logo, making its options readable.

## v0.2.9

### Added

- Branch-mode scheduled workflows now bind to a dedicated branch workspace pinned at first run, with a workflow icon in the sidebar for workflow-owned workspaces. Project-less workflows run as general chat sessions, and the sidebar filter menu gains a "Hide workflow sessions" toggle.
- New /chronicle slash commands let you view session history, generate standup summaries, search past activity, and get workflow improvement tips directly from the chat input.
- Session automations (scheduled wake-ups and recurring prompts) are now supported in workspace sessions, in addition to general chat sessions.

### Changed

- Multiple workspace package scripts can now run at the same time. The Scripts menu shows running scripts first with per-script stop and log controls, and a Stop all option separates active scripts from idle ones.

### Fixed

- Clicking the find button in the markdown file toolbar now opens the find overlay and focuses the search input, matching the behavior of the Command-F keyboard shortcut.
- Fixed a bug where expanding a full file in the diff view after a prior partial expansion could leave some rows displaying stale line numbers and text from other lines.
- Fixed an issue where browser previews could become unresponsive after being hidden or minimized in the background.
- Fixed an issue where the agent could get stuck in a loop replying to the same inline review comment multiple times instead of moving on.
- Spellcheck is now disabled in comment fields and search inputs, removing false-positive red underlines on code, file paths, and identifiers.
- Syntax highlighting now works correctly for .mjs, .cjs, .mts, and .cts files in the file view.
- Terminal processes (dev servers, scripts) are now properly stopped when a workspace is deleted or archived, preventing orphaned background processes from continuing to run.
- The model selected in the draft composer is now consistently used when starting a new session, including from the command palette and other workspace creation paths.
- When automatic feedback submission fails, the feedback form now offers a prefilled GitHub issue URL as a fallback instead of timing out silently.

## v0.2.8

### Added

- Scheduled workflows now bind to a dedicated workspace (worktree by default). Successive runs reuse the same workspace, and the workflow creation/edit dialog includes a workspace type selector matching the regular session flow.
- Workspace files panel now offers a three-scope dropdown: "All" (working tree vs base), "Branch" (HEAD vs base), and "Uncommitted" (working tree vs HEAD). "All" is the new smart default for git-backed workspaces. Empty states for each scope offer a one-click switch when another scope has changes.

### Changed

- Improved keyboard and screen-reader accessibility on the onboarding theme step: focus now returns to the color-family filter button when its menu closes, and selecting themes via search or the "Feeling lucky" button announces results to screen readers.
- Renamed the "Branch" file scope option to "Committed" in the workspace Files panel dropdown, so it pairs clearly with "Uncommitted".
- The Settings "Add account" flow now uses the device-code authentication experience, matching the sign-in flow for both GitHub.com and GitHub Enterprise Server accounts.

### Fixed

- Browser tabs opened by the agent now correctly appear as shared in the UI.
- Chat sessions now show their title in the back/forward navigation history menu instead of raw URLs or duplicate "Chat" entries.
- Fixed a bug where the model picker displayed one model (e.g. Claude Opus 4.6) but sessions were started with a different model when no model had been explicitly selected or after using "Reset to recommended".
- Fixed a false "Session appears to have been interrupted" banner appearing on app restart for sessions that had ended cleanly.
- Fixed a keychain timeout error on macOS when interacting with the Keychain Allow/Always Allow prompt during sign-in. The timeout has been raised from 5s to 30s to accommodate user interaction with the dialog.
- Fixed a regression syncing the model picker between home and pending sessions.
- Fixed an infinite session recreation loop on startup that could silently replace conversation history with empty sessions when resuming sessions failed.
- Fixed an issue where session resume could fail due to a CLI ping response deserialization mismatch.
- Fixed an issue where the My Work filter preview would re-run aggressively while the autocomplete dropdown was open, causing the list to refilter underneath it.
- Fixed an issue where typing `- ` in the message editor would immediately convert to a list, preventing users from creating task-list items with `- [ ]`.
- Fixed branch label truncation in the workspace branch popover so both the session branch and parent branch shrink proportionally when space is limited, preventing the session branch from being crushed to a sliver.
- Fixed browser preview misalignment in the chat canvas area after the panel finishes animating open
- Fixed diff not refreshing after file edits in branch workspaces on the default branch.
- Fixed emoji shortcode picker not opening when typing a bare `:` in the live markdown editor
- Fixed GHE/Proxima user avatars expiring and falling back to initials by refreshing the stored avatar URL on every connection.
- Fixed incorrect inline review thread statuses where threads could be mislabeled as Error or Answered and status badges could disappear after a page reload.
- Fixed markdown canvas briefly showing a loading spinner when unrelated UI updates occurred (e.g., typing in the composer, browser tab edits).
- Fixed misalignment of the "3. Suggest changes" number in the exit plan prompt.
- Fixed Mona logo anchoring on the home screen when using the rich text composer.
- Fixed Session Rename not triggering reliably
- Fixed silent workspace creation failures on large repositories where git initialization could exceed the previous timeout, causing kickoff prompts to be dropped with no error feedback
- Fixed the canvas markdown editor flashing a loading spinner multiple times during chat session startup.
- Fixed the floating markdown toolbar link button sometimes appearing to do nothing when clicked
- Fixed the integrated browser preview remaining overlaid on the app UI after archiving a session that had it open.
- Git operations no longer override `core.sshCommand`, fixing broken SSH authentication for users with custom SSH setups such as SSH certificate wrappers, 1Password SSH agent, and similar tools.
- Improved keyboard and screen reader accessibility for toggle switches in Settings, including proper focus indicators and correct announcement behavior.
- Improved screen reader navigation across the app shell with proper landmarks and heading hierarchy: the sidebar, main content area, view headers, and key panels now expose semantic landmark elements with accessible names, and each view declares an <h1> so assistive technology users can orient themselves and jump between sections.
- Improved screen reader support on the onboarding theme, repositories, enterprise URL, and authorize steps: each step now exposes its title as a visually-hidden heading that receives focus on mount, so assistive technology announces the new step on navigation.
- On macOS, Ctrl+A in the rich composer now correctly moves the caret to the start of the line instead of selecting all text.
- Recent pull requests and issues now populate immediately when opening the "Create from…" dialog on a GitHub-backed repository, instead of appearing empty until a search query is typed.
- Screen readers now announce onboarding setup progress messages as they appear during the final setup step.
- The "Create From" dialog no longer surfaces archived sessions as existing workspaces, and selecting a branch always creates a new workspace instead of navigating to an existing one.
- The /agent-merge slash command now correctly enables the agent-merge loop, preventing work from stalling on wait states like pending CI or awaiting review.
- Traffic lights no longer dim when focus moves to the browser preview on macOS

## v0.2.7

### Added

- Added a "Pause all sessions" command palette action that suspends every running session at once, enabling clean restarts without triggering interrupted-session banners when resuming.
- Added keyboard shortcuts for adding comments on plan text, with support for rebinding via the command palette.
- Added OAuth Client ID field to the remote MCP server configuration form, and added Slack as a popular MCP server preset.
- Canvas markdown editor now shows a floating formatting toolbar when text is selected, making inline formatting actions available right where you're working.
- Emoji shortcode picker in the message composer: type `:` to search and insert GitHub emoji shortcodes (e.g. `:rocket:` → 🚀). Shortcodes are rendered as emoji while editing and preserved as `:shortcode:` in the exported markdown.
- Git is bundled with the app under a staff-only experiment, paving the way for users to no longer need git installed on their system.
- Health check view now shows a Database section with schema version, latest supported version, and database file path (with copy button)
- Rich Markdown editors now support table editing with row and column insertion, deletion, and column alignment controls.
- Sidebar workspace hover previews now show when a PR has auto-merge or agent merge enabled.

### Changed

- GitHub Enterprise Server onboarding now uses the device-code authentication flow, matching the GitHub.com experience.
- Improved markdown list editing in the rich composer: nested lists now render correctly, indent/outdent actions are available via toolbar buttons and Tab/Shift+Tab (or Cmd/Ctrl+[/]) when the cursor is in a list item, and raw markdown editing mode uses a monospace font.
- Plan review now shows a single unified toolbar when selecting text, combining the comment action and formatting options in one place.
- The artifact file picker now starts collapsed by default when opening a markdown editor from the chat canvas panel, keeping the editor focused on the new document.

### Fixed

- Anchor navigation in the integrated browser now works correctly without disrupting the current page view.
- Cross-session messages (send_session_message / send_chat_message) are now reliably delivered even when the target workspace session is not currently active, instead of silently failing while reporting success.
- File tree folders can now be manually collapsed even when they contain the currently selected file
- Fixed a Linux-only bug where temporary files created during PR comment replies would appear in the repository root and show up in diffs.
- Fixed an issue where clicking "New session" on a pull request or issue could create duplicate workspaces in the sidebar.
- Fixed an issue where creating a new session for a repository that was still cloning would silently create the session in a different, already-cloned repository instead.
- Fixed an issue where navigating away while a merge or review drawer was open would leave the backdrop stuck over the app.
- Fixed an issue where plan canvas comments would disappear the first time a user attached one during exit-plan review.
- Fixed an issue where the model could repeatedly call the session rename tool instead of continuing with the user's task.
- Fixed browser preview layout on Linux where the preview appeared as the bottom half of the window instead of in the right panel.
- Fixed the inline review reply loop and duplicate agent replies that could occur when multiple comments were posted on the same thread in quick succession.
- Improved canvas markdown editor performance during window resize.
- Improved error guidance when app update signature verification fails — users now see a clear message with a link to download and reinstall the latest release.
- Inline review comments from agent reviews no longer get permanently stuck showing an "Investigating" badge.
- PR review comments can now be added to deleted lines (shown in red) in the diff view, not just added or context lines.
- Restored undo/redo (Cmd+Z / Ctrl+Z) functionality in the composer, and fixed an issue where focus could be unexpectedly pulled back into the composer textarea.
- Screen readers now announce the Welcome page heading immediately when the onboarding step appears.
- Status updates during the app authorization flow (code copied, browser opened, waiting for authorization, timeout hint) are now announced to screen readers.

## v0.2.6

### Added

- Added a "Share as secret gist" button to the assistant message hover toolbar, allowing you to save a reply as a secret gist with one click. On success, the gist URL is copied to your clipboard and opened in the browser.
- Multi-select and bulk actions on the My work table — select multiple PRs or issues and act on them all at once via the command palette
- Repository clone deep links (`gh://clone/owner/repo` and `gh://github.com/owner/repo`) now open Quick Open prefilled with the repository URL, routing you into the existing clone/add repository flow.
- Visual Studio installations are now detected and available in the "Open in" IDE list on Windows.

### Changed

- In branch (in-place) workspaces, the agent now routes PR creation to a new worktree-backed session by default instead of opening a PR directly from the local clone. Users can still create a PR from the current session by explicitly asking (e.g. "open the PR from this branch").
- Moved the file folder picker button and tree to the left side of the file view, next to the file path.
- The agent-merge feature now re-checks CI and pull request status every 10 minutes by default, down from 30 minutes, so the agent responds more promptly after CI finishes.
- The command palette now animates smoothly on open, scaling and fading in instead of appearing abruptly.
- The folder tree is now the permanent file navigation experience for workspace files. The experimental settings toggle to disable it has been removed.
- Updated onboarding discovery cards to better clarify that sessions run in their own worktree and that pull requests are created manually when you're ready.

### Fixed

- Added `read:org` scope to OAuth token requests, fixing `gh pr edit` and other org-scoped operations hanging for ~3 minutes before timing out
- Arrow keys now move the cursor correctly when renaming a file inline, instead of being intercepted by tree navigation.
- Bold and italic toolbar formatting in the Markdown editor now visually appears in the editor surface as expected.
- Chart canvases now update live when the agent edits the backing artifact, instead of showing stale content.
- Clicking an artifact pill in group view now navigates to the correct session before opening the artifact.
- Comments and replies on diff lines no longer interrupt the agent mid-task — they are now queued and delivered after the current agent turn completes.
- File viewer (Cmd-P) now refreshes automatically when the underlying file is updated by a tool or other change, instead of showing stale content.
- Fixed a bug where the agent's reply-to-review-comment tool could send duplicate replies to the same review thread in a loop.
- Fixed an issue where editing a saved workflow prompt that starts with a slash command would immediately show the slash suggestions popup, obscuring the edit form.
- Fixed an issue where formatting in the markdown editor could trigger an unnecessary loading spinner during autosave
- Fixed an issue where the diff view would get stuck in an outdated state when a comment composer was opened but abandoned without entering any content
- Fixed broken images in pull request bodies and comments that appeared as broken placeholders in the app.
- Fixed file sort order in the changed-files sidebar to match github.com when directory names share a prefix.
- Fixed markdown editors in the right panel flickering back to a loading state when the agent modified files.
- Fixed Share Feedback from the macOS Help menu not working when the sidebar was collapsed.
- Fixed the agent `create_session` tool failing to create sessions in folder-backed projects. It now creates a folder workspace instead of attempting a git worktree against a non-git directory.
- Forking a pinned session now keeps the fork pinned in the sidebar automatically.
- Markdown images in the PR view now render at their intrinsic size and scale down proportionally when the panel is narrower than the image.
- Merge assistance now correctly handles stacked PRs whose base branch has been auto-retargeted by GitHub, avoiding stale base branch data during merges.
- Pasting a PR URL into Cmd-K for a repository not yet connected to the app now correctly opens that PR after the repository is cloned, instead of falling back to a generic draft session.
- PR check run rows now open the GitHub PR checks page for that run, instead of the provider's external details URL
- Queued messages panel no longer expands wider than the composer when messages contain long content
- Reduced flickering and blank states when switching between Repository and Artifacts in the file-tab folder picker.
- Reduced UI lag when switching between sessions with multiple sessions open
- Session references in markdown now correctly resolve and navigate to the referenced session, including when the session is known through workspace state.
- The file tree filter now stays visible while scrolling through long file lists, so you no longer need to scroll back to the top to filter the tree.
- Windows installers now clean up legacy installs, removing stale shortcuts and registry entries that could cause the old app to launch unexpectedly.
- Workflow prompts now support multi-line input using the Enter key.
- Workflow sessions are now correctly scoped to their project's account, preventing GitHub Enterprise repositories from inheriting the wrong host (github.com) when running project workflows.

## v0.2.5

### Added

- Workflow schedules now support quarter-hour start times (e.g. 12:15 AM), giving more flexibility when configuring daily and weekly automations.

### Changed

- Composer status pills are now hidden while prompt or widget takeover surfaces are active, keeping the focus on the current decision. Pending-decision row numbers also stay aligned when choices wrap to multiple lines.
- Improved accessibility across onboarding, including better keyboard navigation, focus rings, and screen reader support for theme selection, as well as clearer repository-selection semantics.

### Fixed

- App auto-update now retries failed authenticated requests anonymously, fixing update failures for users whose GitHub token is blocked by SAML/SSO enforcement.
- Fixed an issue where workflow creation could get stuck on clean installs due to the model picker showing a default model that wasn't recognized by the workflow dialog.
- Fixed focus ring rendering issues on home composer buttons — including clipping, z-order, WebKit ghost outlines, and pixel misalignments.
- Fixed sidebar navigation snapping back to the active chat when clicking Workflows or other sidebar items while the quick chat composer was focused.
- Fixed the composer send button visibly shifting position when switching between sessions.
- Follow-up messages submitted in the composer while a session is starting are now queued and shown immediately, instead of being blocked until the session is ready.
- In-place (non-worktree) sessions now stay on the current branch by default. The agent will no longer create new branches, switch branches, or commit without being explicitly asked to do so.
- Long branch names in the home screen branch picker no longer overflow their container.
- Nested lists in the markdown editor now render with correct indentation.
- Nested markdown lists now render with correct indentation.
- Restored bottom spacing and muted backdrop on the draft session composer so the project and branch pickers are visually grouped with the composer card.
- Restored live git clone progress updates (e.g. "Receiving objects: 42%") in the workspace cloning indicator
- Session creation no longer fails when a stale git lock file is present — the lock file is now automatically removed and the operation retried.
- The My Work inbox filter panel now remembers whether it was open when navigating away and back.

## v0.2.4

### Added

- Queued follow-up messages are now available by default during active sessions, allowing users to queue prompts while a response is in progress.
- Skills now appear as slash commands in the Quick chat composer, matching the behavior already available in Home and draft workspaces.

### Changed

- Consecutive tool calls are now grouped into a single collapsible panel with a natural-language summary (e.g. "Edited foo.ts and 3 other tool calls"), reducing visual noise in the conversation timeline. The panel shows a live spinner while tools are running, auto-opens during active work, and auto-closes when complete.
- PR number labels now display as "PR #123" instead of bare "#123" in the workspace PR tab and composer PR pill, avoiding potential confusion with issue references.

### Fixed

- Fixed blurry app icon on Windows at all DPI scales
- Fixed fullscreen toggle appearing on the wrong side in split panel layouts
- Restored spinner animation for in-progress todos in the Plan tab
- Fixed sidebar navigation snapping back to the active quick chat when clicking another section (e.g. Workflows) while the chat composer was focused
- Quick chats with unsent composer drafts are no longer discarded when navigating away from the chats view, so typed text isn't lost when switching to another sidebar section

## v0.2.3

### Added

- Right-click context menu (New session / View session, Quick chat, Copy link) is now available in the My Work inbox list view, matching the existing context menu in the table view.
- Session automations are now available as an opt-in experiment in Experimental settings, letting you repeat prompts on a schedule.
- Skills now appear in the slash command picker on the Home screen and in draft workspaces, so you can invoke `/skill-name` before starting a session.

### Changed

- Adding a GitHub repository now opens the command palette repo picker instead of the older dialog.
- The feedback form now shows a notice that submissions will be posted as public GitHub issues, and the submit button is labeled "Share feedback".
- The folder view is now available by default when viewing individual files, and the Changes panel no longer shows an "All files" scope.

### Fixed

- Bot account names (e.g. `github-actions[bot]`) are now displayed without the `[bot]` suffix in issue/PR rows, author cells, assignee avatars, search cards, and other UI surfaces.
- Draft sessions no longer show incorrect setup or worktree state before a prompt is submitted. A loading indicator is shown while a repo is cloning, and the project picker is now available in the draft composer footer.
- Feedback drafts are now preserved when accidentally dismissing the feedback popover (e.g. outside click, Escape, or sidebar collapse), so you no longer lose what you've typed.
- Fixed an issue where the find-in-file search window could render outside the app window when opened near the right edge of the screen.
- Fixed worktree creation timing out with "Timed out fetching the base branch" on large repositories by streaming fetch progress with an idle timeout instead of a fixed wall-clock limit.
- Recent sessions header now shows correctly in the sidebar when no sessions exist yet
- Skill files and MCP configs are now correctly rediscovered when resuming a session, fixing a bug where they were silently lost on resume.
- The Changes pill label in the composer now stays visible at medium session widths, making the diff entry point easier to find.

## v0.2.2

### Added

- Added a context menu to folder tree file rows with options to open the file in a new tab and copy its absolute path.
- Added a folder tree for navigating workspace files, with stable toolbar controls when switching files, search support for markdown files, and automatic reveal of the active file when the tree opens.
- Added column visibility controls to the My Work table view, letting you show or hide individual columns from a new Columns submenu. Reset options for column widths, order, and visibility are now grouped under a Reset submenu.
- Agents can now share and interact with the integrated browser preview — navigating pages, reading content, taking screenshots, and performing clicks and input — when the browser agent tools experiment is enabled.
- Canvas and browser tabs in the chat panel can now be split side by side
- The folder tree view for file navigation is now available as an opt-in experiment in Settings for all users.
- The slash command palette now shows argument autocomplete — enum-argument commands (like `/remote`, `/collect-debug-logs`, `/skills`) keep the palette open with allowed values after you type a space, while freeform-argument commands show a ghost-text hint describing what to type.

### Changed

- Added subtle vertical dividers between right panel tabs for easier visual distinction.
- Clicking an author or assignee avatar in the My Work inbox now opens that user's GitHub profile in your browser.
- Improved accessibility of the repository connection onboarding flow for screen reader and voice control users.
- Polished My work views and table interactions: the new view button now shows a 'New view' tooltip, the reset button is renamed from 'Clear' to 'Reset', deleting a custom view now shows a confirmation dialog with a 'Don't ask again' option, right-clicking an avatar in the inbox table now correctly opens the row context menu, and a separator was added above 'Copy link' in the row context menu.
- Queued follow-up prompts now use a consistent icon across both the submit button (when holding Cmd/Ctrl) and the queued-message pill.
- Redesigned the home screen as a discovery surface — surfaces inbox previews and contextual feature prompts to help you understand what to do next.
- Refined the My work inbox: restyled the filter editor as an inset card, added a split Save menu with "Save to this view" and "Save as new view" options, renamed "Reset to default" to "Clear", added right-click context menus on inbox tabs (Edit, Duplicate, Delete) and on table rows with a new "Quick chat" option to start a chat about the selected pull request or issue.
- Renamed the "View inbox" button to "View all" in the Up next section of the home screen.
- Revamped the default inbox sections: replaced "Needs my attention" with "Active" (issues and PRs assigned to you, plus PRs you authored) and "Review requests" (PRs where you or a team you're on is requested as a reviewer), and fixed the "Done" section so it no longer shows closed-unmerged pull requests.
- Reworked the My work filter editor with two distinct modes: a quick-filter mode (funnel toggle) for query-only edits with an inline Undo button and save/revert menu, and an edit mode for renaming a view and resetting it to its defaults.
- Right-panel tab close button now appears in the leading icon slot instead of as a right-side overlay, providing a more consistent interaction target.
- Sidebar badges and state pills for ready-to-merge and completed workspaces now use green success styling.
- Submitting a prompt on the home page without selecting a project now starts a quick chat instead of silently doing nothing.
- The "new updates" banner in the My work inbox is now displayed as a full-width strip flush against the filter bar, making it easier to spot when new items are available.
- The My Work inbox now remembers your last active tab and returns you to it on next load.

### Fixed

- Arrow keys now move the cursor correctly inside the new workspace search input instead of switching between source tabs.
- Browser preview pages no longer have unexpected DOM mutations (color-scheme attributes, injected style tags, or matchMedia overrides) applied by the app.
- Command palette "Set thinking effort" action now works correctly when no active session has started yet
- Discarding a draft session now shows a dedicated confirmation dialog with appropriate copy, instead of the generic delete dialog.
- Discovery cards on the home page are now automatically dismissed for items completed during onboarding, so already-configured features no longer appear as suggestions after setup.
- File attachment icons in chat messages now match the size used in attachment chips
- Fixed a crash that could occur when loading pull request checks for PRs with large check result pages
- Fixed a crash that could occur when loading pull request details with deeply nested check contexts.
- Fixed a crash that could occur when refreshing PR details with a large number of status checks.
- Fixed a gap between the sidebar and content area when using zoom levels above 1x.
- Fixed an error that could appear in the document navigator when opening files in ephemeral markdown canvases.
- Fixed an issue where adding an empty GitHub repository could cause the first feature branch pushed by a session to become the repo's default branch.
- Fixed an issue where attaching files to a chat could stop working after a draft session was converted into an active session.
- Fixed the add-tab menu alignment so it opens anchored to the trigger button edge instead of centering beneath it.
- Home screen discovery cards now correctly show actionable onboarding cards first, with tip cards as fallback, regardless of onboarding completion status.
- MCP tool calls now display with the correct server label and icon (e.g. "GitHub · Search code") instead of a raw slug like "Github Mcp Server · Search Code".
- Pull requests no longer appear as ready to merge when GitHub's merge requirements are not yet satisfied.
- Selecting a file in the Changes panel's All files tree now keeps the selected row highlighted while its content is displayed.
- Split controls now appear in a pane whenever any tab in that pane can be split, instead of being hidden when the active tab is pinned or otherwise unsplittable.

## v0.2.1

### Added

- Added `/skills reload` slash command in the composer palette to reload skills mid-session, with an inline transcript notice showing the updated skill count.
- Added a hover-to-reveal copy button to inbox item links
- Added an onboarding step for Business, Enterprise, and GHES users that detects when required Copilot preview features are not enabled and guides them to enable the necessary settings.
- Live progress is now shown while cloning a GitHub repository, with per-stage status (receiving objects, resolving deltas) and percentages streamed from git.
- Section editor qualifiers now support comma-separated multi-values (e.g. `repo:a,b,c`, `label:bug,docs`). Typing a comma after a value reopens the autocomplete with already-selected options filtered out.

### Changed

- My Work inbox filter tabs can now be reordered by dragging, and the "All" tab appears first by default.
- The "Archive sessions" button in the sidebar now shows the number of sessions that will be archived (e.g. "Archive 5 sessions" or "Archive 1 session").

### Fixed

- Browser preview theming now uses native OS appearance (macOS webview appearance, isolated Windows WebView2 profiles) instead of injecting scripts into the previewed page, preventing hydration mismatches in frameworks like Next.js. The theme toggle is hidden on Linux where native external theming is unsupported.
- Browser previews now retain their page state (URL, title, favicon) when switching panels or navigating away from a session.
- Fixed a bug where adding a new GitHub repository would briefly show the new workspace then redirect to the home page, hiding clone progress and any error dialogs.
- Fixed an issue on Windows where the app would become unresponsive to screen readers (NVDA) and voice control software after losing window focus.
- Fixed an issue on Windows where the browser preview could appear duplicated due to the native WebView2 surface being out of sync with the React placeholder.
- Fixed sidebar header controls overlapping main content at non-default zoom levels
- Fixed theme toggle not applying correctly in browser preview on Windows
- Fixed update error messages in Settings > General appearing as a second status line below the app version subtitle instead of replacing it
- Git error toasts for failed push, pull, and commit operations now show the actual git error message instead of the raw command arguments.
- Improved alignment and visual consistency across the Settings dialog: switch rows are now vertically centered; the account removal confirmation no longer shows a nested card or double border; MCP server action button spacing is consistent with the rest of the UI.
- Merge and auto-merge availability now correctly reflects GitHub's actual merge permissions, fixing cases where the merge button appeared disabled when it should have been enabled.

## v0.2.0

### Added

- Technical Preview for the GitHub app
