# Changelog

## v1.0.14

### Highlights

- Added an /init slash command to generate or improve a repository's Copilot instructions file.
- You can now type & in the composer to mention and reference another session by name.
- The home screen now shows prompt cards with suggested tasks that fill the composer when clicked.
- Added /model and /models slash commands to open the model picker or select a model by name or ID.
- AI credit usage warnings now appear above the chat composer with a next step when you run low or out.

### Added

- Added /clear and /reset slash commands to reset the current chat session transcript while staying in the same workspace or chat context.
- Added /model and /models slash commands to the prompt composer to open the model picker or select a model by name or ID.
- Added a /rename slash command to rename the current session or chat directly from the composer.
- Added a `/chronicle reindex` slash command to rebuild the Chronicle session index.
- Added a `/init` slash command to generate or improve a repository's Copilot instructions file.
- AI credit usage warnings now appear above the chat composer, with a plan-aware next step when you run low or run out.
- In the diff view, you can now open a file directly from its header, and right-click a file header to copy its file path or relative path, or open the file in a new tab or your browser.
- Session ID is now shown in the workspace and chat title popovers with a one-click copy button, making it easy to reference a session when working across multiple chats.
- The home screen now shows prompt cards below the composer with suggested tasks to try. Clicking a card fills the composer with the suggested prompt using a typewriter animation.
- You can now type & in the composer to mention and reference another session by name.

### Changed

- In repository settings, the trust actions (Accept, Revoke, Keep local, and Create config file) now show a spinner and become non-interactive while the request is in flight, so it's clear the action was registered.
- Refactored the repository configuration section of project settings into a reusable, presentational `RepositoryConfigFileSettings` component, with Storybook coverage now backed by the real component. No change to behavior.
- Shift+Tab in the chat composer now moves focus backward as expected for keyboard and screen-reader users, instead of cycling the session mode. Change modes from the mode menu or with ⌘/Ctrl+Shift+M (remappable in Settings → Keyboard Shortcuts).

### Fixed

- Agent merge check-in prompts no longer clutter the composer's prompt history.
- Closed pull requests that were previously drafts now show the closed icon in the sidebar instead of the draft icon.
- Fixed an error that could prevent bring-your-own-key models from working in project and workspace sessions.
- Fixed keyboard focus returning to the wrong place after closing the "Add from GitHub" repository picker during onboarding, so keyboard and screen-reader users can navigate correctly.
- Fixed lag when switching between chat sessions, especially very large conversations.
- Fixed pull request and issue lists, pull request details, and creating or updating pull requests/issues breaking after a repository was renamed or transferred on GitHub.
- Fixed the coding agent auto-merging a pull request before GitHub's own merge checks (e.g. required status checks) were satisfied.
- Fixed the composer's Changes pill not appearing on WSL workspaces when a session had uncommitted edits.
- Fixed the Impeccable design skill leaving behind stray cache files and git exclude entries in repos where no design issues were found.
- Fixed third-party MCP servers requiring OAuth getting stuck on an endless "authenticating" spinner instead of prompting to sign in.
- In project settings, the repository configuration file row is now hidden until a `.github/github-app.yml` config actually exists, instead of appearing before you've created one.
- Local automations now use your Settings and per-project instructions, matching interactive sessions.
- Widened the scrollbar thumb on Windows and Linux and fixed the dark theme hover color so the thumb is brighter on hover as expected.

## v1.0.13

### Highlights

- Chats can now be archived instead of only deleted, hiding them from the sidebar without losing history and letting you restore them later.
- A full-screen Present mode for canvas, diff, and file panels hides app chrome for a clean, distraction-free view.
- A new /compact slash command lets you manually compact a workspace or chat conversation on demand to reduce token usage.
- Selecting an HTML file in the Files panel now shows a globe button to open it directly in the integrated browser.
- You can now right-click an image in a pull request, issue, or comment to copy it, matching existing chat behavior.

### Added

- Added a "Show Copilot CLI Session" setting in Settings → Sessions that controls whether sessions created by the Copilot CLI appear in the sidebar and, if so, how far back to surface them. The setting defaults to Off, so CLI sessions are hidden until you opt in.
- Added a full-screen Present mode for canvas, diff, and file panels: an Enter full screen button in the panel tab bar hides the app chrome and window header for a clean, full-bleed view, and can be exited with the button, Esc, or the OS fullscreen toggle.
- Chats can now be archived instead of only deleted. Archive a chat from its sidebar context menu to hide it from the sidebar without losing its history, and restore it later from Manage sessions.
- New /compact slash command lets you manually compact a workspace or chat conversation to reduce token usage, with optional focus instructions. Compaction already happens automatically when a conversation grows large; this lets you trigger it on demand.
- Selecting an HTML file in the Files panel now shows a globe button in the header that opens the file in the integrated browser.
- Session spend now shows a separate "Agent merge" line when background agent merge activity contributed to the total, making it easier to see how your credits were used.
- You can now right-click an image in a pull request, issue, or comment to copy it, matching the existing behavior for images in chat.

### Changed

- Clicking an issue or pull request reference — in a conversation message or the prompt composer — now opens it in the in-app viewer instead of the browser when a workspace is active. Cmd/Ctrl-click still opens it in the browser.
- Copying an assistant response now pastes as formatted rich text (headings, bold, lists, tables, code) into apps like Teams, Outlook, and Word, instead of raw markdown.
- Improved rendering performance while assistant and reasoning messages are streaming in: completed parts of the message no longer get re-parsed on every update, making long streaming responses smoother.
- Pull requests in a merge queue now show a "Queued" status across all PR status surfaces, including badges, sidebar icons, tray menu labels, and the MyWork list, instead of appearing as open or merge-ready.
- Reworked the Add filter dropdown to show common filters first, with an "All filters" option to reveal the full grouped list and search across all filters.
- Screen readers now announce the number of matching results when filtering repositories and other item pickers.
- The branch name shown in the pull request view now includes a built-in copy button, merged into a single pill instead of a separate icon next to it.

### Fixed

- Automated agent check-in prompts no longer show up as ticks on the conversation timeline scrubber, and clicking the last tick now scrolls to its actual message instead of overshooting to a trailing automated exchange.
- Cloud automations now let you choose a model and reasoning effort, and remember your choice when you edit the automation later. Previously the model selection was ignored and reasoning effort couldn't be changed.
- Fixed a doubled border at the bottom of the merge summary card when a pull request is ready to merge
- Fixed an issue where messages sent while the agent was working could get stuck showing as pending, and could cause the earlier message to appear to disappear from the conversation.
- Fixed incorrect ARIA roles on segmented controls throughout the app so screen readers now correctly identify single-choice settings (theme mode, filter mode, plugin/skill/shortcut filters, etc.) as radio groups rather than tab controls, and added missing panel labels to the genuine tab controls (markdown editor, MCP settings).
- Fixed keyboard and screen-reader navigation order in the onboarding steps — on wide screens, the Continue/Finish button is now reached after the choices it applies to, matching the visual and expected reading order.
- Fixed screen readers announcing the Mode and Terminal theme options in Settings > Themes as tabs instead of radio buttons, and added missing group labels and descriptions.
- Fixed the sidebar session status spinner sometimes staying stuck on "working" after a session went idle.
- Hid the redundant scrollbar in the conversation view when the timeline is visible.
- In repository settings, the "Trusted" status label now appears to the left of the "Revoke" button, following the expected state-then-action order.
- Opening a new terminal from the add-tab menu or command palette now focuses the terminal immediately instead of leaving focus on the button you clicked.
- Screen readers now announce each control's name and description when navigating the Sessions settings panel.
- Screen readers now announce the empty-selection hint in the onboarding Repositories step when no repositories are selected.
- Screen readers now announce the field name and description when focusing the Mode and Font dropdowns in Settings > Themes.
- Screen readers now hear the sign-in code copy confirmation before the browser opens during device-code sign-in, so users are no longer dropped into the browser with no context of what happened.
- The attention badge dot on the Windows and Linux system tray icon is now amber instead of black, making it visible on dark taskbars.
- Toggling merge settings (like "Merge pull request") for a workspace with agent merge enabled now takes effect immediately instead of waiting up to 10 minutes for the next automatic check.

## v1.0.12

### Highlights

- Added an agent picker to the chat composer toolbar so you can select a custom agent before or during a session, including sessions opened from issues and pull requests.
- HTML files can now be opened in the integrated browser directly from the editor header, file tree, and inline chat references.
- Draft pull requests now open the full PR panel, giving access to agent-merge options and a "Ready for review" action.
- When creating GitHub issues, the agent now follows the repository's issue templates, preserving headings, sections, and comments.
- Fixed a bug where renaming a repository's default branch on the remote caused the diff view to show a large phantom diff of hundreds of files.

### Added

- Added an agent picker to the chat composer toolbar, letting you select a custom agent before or during a session. The selected agent is also applied to sessions spawned from issues, pull requests, and other entry points.
- HTML files can now be opened in the integrated browser directly from the file editor header, the file tree context menu, and inline file references in chat messages. File browser tabs also now show the file name instead of a blank label when opening local files. Build-step apps (for example Vite or React projects) that reference ES modules or server-root assets can't render from a local file, so the browser panel now shows a short "run a dev server" explanation instead of a blank page. Global agent discovery now degrades gracefully on CLIs that do not implement `agents.discover`.
- Right-clicking a chat image now shows a "Copy image" option that copies the image to your clipboard, available on both inline thumbnails and in the image viewer.

### Changed

- Draft pull requests now open the full PR panel, giving access to agent-merge options and a "Ready for review" action from the same place as other PR states.
- Quote in reply now appends quoted text to the end of your existing draft, preserves inline code and formatting, supports a keyboard shortcut (Cmd+Shift+'), and places the cursor on the line after the quote.
- The theme picker in Settings > Appearance is now fully keyboard and screen-reader accessible: arrow keys navigate between theme cards, Enter or Space applies a theme, Escape resets to the default GitHub theme, and selecting a theme announces its name to assistive technology.
- When creating GitHub issues, the agent now checks for and follows the repository's issue templates, preserving headings, sections, and HTML comments.

### Fixed

- Fixed a bug where renaming a repository's default branch (e.g. master → main) on the remote would cause the diff view to show a large phantom diff of hundreds of files even though the working tree was clean.
- Fixed keyboard focus loss on Windows after Alt+Tab — the chat composer now correctly regains focus when switching back to the app.
- Fixed panel scrollbars being unclickable on Windows because resize handles were overlapping them.
- In Project Settings, the "Open on GitHub" link for the config file is now hidden when the file has not yet been committed to the default branch. A "Reveal in file manager" button is shown instead so the file can still be found locally.
- Navigating to a Settings section via the in-dialog search or contextual buttons now moves keyboard focus to that section's heading, so keyboard and screen-reader users land directly on the destination content instead of the dialog container.
- On Windows, the tray now uses the main app icon so it keeps enough contrast in both light and dark taskbar modes.
- Opening a Markdown file in the editor canvas no longer silently rewrites its contents (e.g. escaping underscores or changing fenced-code indentation) when an external no-op file refresh occurs.

## v1.0.11

### Highlights

- Local automations now support custom CRON expressions, letting you schedule workflows at any cadence using a segmented expression editor with inline validation and a human-readable preview.
- Screen readers now announce agent activity in Sessions and Quick Chats — including replies, tool calls, and CLI commands — with new per-category announcement toggles in Settings > Accessibility.
- The Manage Sessions filter bar now supports "is not" exclusion on all four filters, and the State filter offers distinct values (Open, Draft, Merged, Closed, No pull request) instead of a two-bucket grouping.
- Fixed workflows failing to run when configured with a local or custom provider model (e.g. Ollama or Foundry) — scheduled and manual runs now correctly route to the selected model.
- Added a folder icon button next to the session path in the workspace dropdown to reveal the session folder in your native file manager.

### Added

- Added a folder icon button next to the session path in the workspace dropdown to reveal the session folder in the native file manager (Finder, Explorer, or Files).
- Local automations now support custom CRON expressions, letting you schedule a workflow at any cadence (e.g. "every 15 minutes on weekdays") using a segmented expression editor with inline validation and a human-readable preview.
- Screen readers now announce agent activity in Sessions and Quick Chats — including replies, tool calls, CLI commands, and a loading heartbeat — so non-sighted users get real-time feedback without leaving the prompt field. New per-category announcement toggles are available in Settings > Accessibility.

### Changed

- Plugin marketplace groups in Settings > Plugins are now collapsed by default, reducing visual clutter when opening the page.
- The "Open in" app list in session context menus is now collapsed into a single "Open in…" submenu, keeping the menus more compact when multiple apps are configured.
- The issue timeline now shows a reference card (status icon, title, and issue number) when a sub-issue or parent issue is added or removed, instead of a bare action line.
- The Manage Sessions filter bar now supports "is not" exclusion on all four filters (Status, State, Repository, Environment), and the State filter now offers distinct values — Open, Draft, Merged, Closed, and No pull request — instead of the previous two-bucket Open/Closed grouping.
- The prompt composer's borders, focus rings, and send button now consistently reflect the active mode color — neutral for interactive, blue for plan, green for autopilot, and orange for shell.

### Fixed

- Editing an automation's project now saves correctly even after the automation has run at least once.
- Fixed an issue where the fork button disappeared after a model change, skills reload, or agent switch notice appeared in the conversation.
- Fixed an issue where the scrollbar in the conversation timeline area was nearly impossible to grab when timeline markers were visible.
- Fixed an issue where typing an org name in the sidebar clone search could skip repos that belong to that org.
- Fixed missing Changes pill, command palette session actions, and side-panel toggle for existing sessions when the right panel started closed.
- Fixed the horizontal scrollbar in Manage sessions: it now scrolls to reveal all columns when they overflow, and disappears when all columns fit.
- Fixed workflows failing to run when configured with a local or custom provider model (e.g. Ollama, Foundry, or custom OpenAI-compatible). Scheduled and manual workflow runs now correctly route to the selected provider model instead of returning "model not available".
- Forking a session that had been idle for ~10 minutes no longer fails with a "not found" error.
- Page Up and Page Down now scroll the conversation transcript when focus is on the conversation area.
- Scrolling the slash-command and mention menus no longer dismisses the menu on Windows — dragging the scrollbar now scrolls as expected.
- The checks panel now shows a "Checks are starting" pending state instead of the neutral "No checks have run yet" message when GitHub has queued checks that haven't reported individual results yet, preventing the empty state from being misleadingly reassuring.

## v1.0.10

### Highlights

- Orchestrator sessions can now approve or redirect a child session's plan while it's paused in plan mode, instead of waiting for a human.
- "Share extension as gist" now appears in the command palette whenever a shareable extension is installed, and automatically opens the new gist in your browser.
- On macOS, the native menu bar now reflects your current keyboard shortcut bindings, and the View menu item has been renamed from "Open Search" to "Command Palette".
- On Windows, tools installed to the user-level PATH (such as winget or nuget) are now correctly found when running agent sessions or the integrated terminal.
- When a project is linked to the wrong GitHub account, the app now detects the correct account and prompts to re-authorize instead of silently failing.

### Added

- Orchestrator sessions can now approve or redirect a child session's plan while it's paused in plan mode, instead of the child waiting for a human. Plan-ready children notify their creator, the plan is surfaced via get_session, and the new respond_to_session_plan tool resolves it.

### Changed

- "Share extension as gist…" now appears in the command palette whenever a workspace session has a shareable extension installed, not only when an extension canvas is open. Sharing an extension now also opens the new gist in your browser so the result is obvious.
- Nested folders in workspace file trees now use a smaller indent step so deeply nested folder hierarchies are more compact and easier to read.
- Renamed "Quick Chat" / "Quick Chats" to "Chat" / "Chats" throughout the app (sidebar, tray menu, workflows, project picker, and menus).

### Fixed

- Automation run detail header no longer overlaps at narrow window widths — run status hides and action buttons compact to icon-only before the toolbar can crowd.
- Conversation scroll position is now correctly restored when switching between session tabs.
- Conversation scroll position is now preserved when switching back to a previously visited session.
- Fixed a crash that prevented the app from launching on macOS when a repository's configuration file contained a quoted YAML value with 16 or more consecutive spaces.
- Fixed a doubled border line appearing between adjacent file headers in the diff view when files are collapsed or when a sticky header slides into view.
- Fixed a wide empty gap in the GitHub authentication banner on wide windows — the message and action buttons now sit flush together instead of being separated by dead space.
- Fixed an issue on Windows where browser-based features could fail when the app was launched using Windows application compatibility settings.
- Fixed sidebar toggle button being unclickable when the sidebar is collapsed on the home view
- Fixed the spinner on the Merge when ready button freezing instead of animating in WebKit.
- On macOS, the native menu bar now reflects your current keyboard shortcut bindings — remapped shortcuts appear correctly in the menu. The View menu item has also been renamed from "Open Search" to "Command Palette", and the keyboard shortcuts settings search now shows only your active bindings.
- On Windows, tools installed to the user-level PATH (such as winget, nuget, or any per-user tool install) are now correctly found when running agent sessions or the integrated terminal.
- Onboarding now correctly shows badges for all selected GitHub repositories, including those found via search.
- Slash command and mention suggestion popovers in the chat input now span the full width of the composer.
- The Add files and Add folder dialogs now open in the active workspace directory instead of an arbitrary OS default location.
- The Plan pill no longer shows a shimmer animation or count when a background agent is running but no plan exists.
- The Quick chats sidebar section now shows a "No quick chats yet" message when empty, instead of a blank area.
- The search query no longer resets when selecting repositories in multi-select mode.
- Timeline navigation now smoothly animates when jumping to conversation history items that are offscreen, and clicking the expanded timeline lane correctly selects the hovered item.
- When a project is linked to the wrong GitHub account, the app now detects the correct account and prompts to re-authorize it, instead of silently failing with errors on repository actions, pull request creation, and pull request polling.

## v1.0.9

### Highlights

- Quick chats now support tool-approval commands (/yolo, /allow-all-tools, /reset-allowed-tools) and session forking, bringing them to feature parity with code sessions.
- The Settings → Usage & Plan page now shows your active Copilot plan name directly beneath the Plan heading, so you no longer need to visit GitHub.com to see which plan you are on.
- Sessions awaiting your input now display a question-mark icon in the sidebar instead of a small dot, making the needs-input state easier to recognize at a glance.
- Fixed orphaned git fsmonitor daemon processes accumulating after each app quit — daemons are now stopped on worktree removal and when the app exits.
- Fixed the Windows tray icon disappearing against the taskbar when using a dark system theme — the icon now uses a theme-appropriate asset and updates automatically.

### Added

- Quick chats now support tool-approval commands (/yolo, /allow-all-tools, /reset-allowed-tools) and session forking, bringing them to feature parity with code sessions.
- Searching or filtering in Settings (Themes, MCP servers, Skills, Experimental, and Plugins) now announces the number of matching results to screen readers.
- The Settings → Usage & Plan page now shows your active Copilot plan name (e.g. Copilot Max, Copilot Pro+, Copilot Business) directly beneath the Plan heading, so you no longer need to visit GitHub.com to see which plan you are on.

### Changed

- Folder rows in the Files and Changes trees now show only a chevron (no redundant folder icon), and changed-file status icons align with the folder gutter — matching VS Code's file-tree style.
- Improved the empty states in the automations view when search or filters return no results: the runs list now shows a title, description, and a "Clear filters" button consistent with the gallery section.
- Removed the inline Split down and Split right buttons from the tab bar. Splitting is still available via the tab right-click context menu, drag-and-drop to a pane edge, and keyboard shortcuts.
- Sessions awaiting your input now display a question-mark icon in the sidebar instead of a small dot, making the needs-input state easier to recognize at a glance.
- The model-change notice in the conversation now displays the long-context window as a dot-separated suffix (e.g. "Claude Opus 4.8 · 1M") and renders the reasoning effort label with proper spacing, matching the model picker's style.

### Fixed

- Clicking an attachment label in the overflow menu no longer accidentally removes the attachment — removal now requires clicking the explicit X button.
- Clicking an attachment row in the composer overflow menu now opens or previews the attachment, matching the behavior of clicking the visible attachment pill.
- Column resizing in table views (such as manage sessions) now works reliably when dragging.
- Fixed orphaned git fsmonitor daemon processes accumulating after each app quit. Daemons are now stopped on worktree removal and when the app exits.
- Fixed the repository visibility selector (Public/Private) in the Create new repository and Publish to GitHub dialogs to use correct radio-group semantics, so screen readers now properly announce the selected option and its description.
- Fixed the Windows tray icon disappearing against the taskbar when using a dark system theme. The tray icon now uses a theme-appropriate asset and updates automatically when the system theme changes.
- Keyboard focus now moves correctly when adding or removing environment variable and header rows in the MCP server settings editor.
- Screen readers now announce the keyboard shortcut when focusing the Search button in the sidebar (e.g. "Search, Command + K" on macOS, "Search, Ctrl + K" on Windows/Linux).
- The "Feeling lucky" button in the theme picker now announces the number of new themes and the name of the theme it applied to screen readers, replacing an inaccurate theme count.

## v1.0.8

### Highlights

- Sessions now automatically remember your last model, reasoning effort, and long-context state — no more configuring a default model in settings.
- Screen-reader users can navigate the chat transcript message-by-message using heading navigation, with each message announced as 'You said:' or 'Copilot said:'.
- The issue pill in the composer now shows a color-coded status icon (open, completed, not planned), matching pull request pill behavior.
- The Changes panel file list now always displays as a tree view, with a file count and diff stat shown in the toolbar.
- Closing a Terminal tab now prompts for confirmation before ending the session, with a 'Don't ask again' option for future closes.

### Changed

- Canvas tool calls in the conversation now show the canvas icon instead of a generic tools icon, making them easier to recognize at a glance.
- Closing a Terminal tab in the right panel now shows a confirmation dialog before ending the session. A "Don't ask again" checkbox lets you skip the prompt for future closes.
- Merged pull requests now display the merge icon instead of the pull request icon, making merged state easier to recognize at a glance.
- Screen-reader users can now navigate the chat transcript message-by-message using heading navigation — each message is announced as "You said:" or "Copilot said:" followed by a preview of the text.
- The Changes panel file list now always displays as a tree view (the flat/tree toggle has been removed), the toolbar shows a file count and diff stat, file header names use lighter typography, and a doubled border under the toolbar is fixed.
- The issue pill in the composer now shows a color-coded status icon (open, completed, not planned) matching the existing pull request pill behavior.

### Fixed

- Fixed microphone test playback in Settings → Voice playing only in the left ear on Linux when using multi-channel audio interfaces.
- Fixed the selected file scope label in the Files panel toolbar (e.g. "Committed") showing in muted text instead of the default color, making the active selection easier to read.
- In the Last updated sidebar view, session groups with recent child activity now correctly float to the top and land in the right date bucket (e.g. "Recent sessions") instead of staying pinned to the parent session's older timestamp.
- Opening the Changes tab with the mouse no longer leaves a stuck focus ring on the file list.
- The 'Created session' tool call row in conversations now shows the correct icon instead of a generic wrench.
- The main composer is now hidden while an "Ask Question" prompt is open, preventing accidental messages from being sent instead of answering the prompt.

### Removed

- Removed the "Default model" section from Sessions settings. New sessions now automatically start with the model, reasoning effort, and long-context state from your last selection in the session model picker.

## v1.0.7

### Highlights

- Added a "Quick chat" option to the home screen project picker, letting you start a chat session directly without selecting a repository.
- Automation runs now show token, context, and AI-credit usage in the run details popover, matching what chat sessions already display.
- The model picker now widens to fit long custom model names, and custom model providers show their own brand icons in the picker.
- macOS traffic light buttons are now native controls, restoring accessibility support and the green button long-press window management menu.
- Fixed agent-merge incorrectly declining to merge pull requests that the user has permission to merge.

### Added

- Added a "Quick chat" option to the home screen project picker, letting you start a chat session directly without selecting a repository.
- Automation runs now show token, context, and AI-credit usage in the run details popover, matching what chat sessions already display. Reopening a past run shows the spend from that run.

### Changed

- macOS traffic light buttons are now native controls, restoring accessibility support and the green button long-press window management menu.
- The model picker now widens to fit long custom model names, and custom model providers show their own brand icons (Ollama, Azure, Microsoft Foundry, Foundry Local) in the picker and the "Model changed" message. The "Custom" badge on custom models now flows inline with the model name.
- Updated the top-level fuzzy-matchable slash commands for the Impeccable design skill. The promoted shortcuts are now `/impeccable audit`, `/impeccable critique`, `/impeccable live`, `/impeccable polish`, and `/impeccable distill`.

### Fixed

- Closed issues now show the correct status indicator everywhere, including the inbox: purple for completed, and grey with a circle-slash icon for issues closed as not planned or duplicate (instead of red or a generic closed badge).
- Fixed a crash in the tray menu that could occur on startup when store data arrived while the menu was being built.
- Fixed agent-merge incorrectly declining to merge pull requests that the user has permission to merge.
- Fixed clipped border corners on settings textareas (e.g. the Instructions field) caused by the horizontal scrollbar gutter.
- Sidebar tooltips now dismiss immediately when the sidebar is collapsed, instead of remaining visible and floating disconnected from their triggers.

## v1.0.6

### Highlights

- Type @ in any comment or description composer to get autocomplete suggestions for mentionable users and org teams in the current repository.
- Manage sessions now supports pill-style filters, a bulk-select toolbar, and bulk archive or delete with a confirmation step.
- The Automations screen now has a unified search that filters both automation cards and runs simultaneously, with matched text highlighted.
- Opening a background agent's activity tab now scrolls to the latest output and shows a live progress indicator while the agent is working.
- Manually renamed sessions and workspaces are no longer overwritten by the agent's automatic rename.

### Added

- Images in the canvas editor markdown preview now render for all users.
- Type @ in any comment or description composer to get autocomplete suggestions for mentionable users and org teams in the current repository.

### Changed

- Composer status pills that don't fit on one row now collapse into a circular "…" button; clicking it opens a menu listing the overflowed items instead of wrapping onto a second line.
- Conversation image attachments now preserve their natural aspect ratio instead of being cropped to a square, and multiple images are displayed in a balanced grid layout.
- Conversation transcript polish: long ask-user questions can now be expanded and collapsed with a chevron disclosure (keyboard accessible), while short questions that already fit stay as a plain row; the timeline picker only selects when you click an actual tick (not surrounding whitespace) and only reveals near the bars; the native scrollbar is no longer hidden when the timeline picker is showing; Cmd+K in the terminal now clears the buffer instead of opening the command palette; and the New Window shortcut is hidden unless multi-window support is enabled.
- Manage sessions now uses pill-style filters to narrow the list, a bottom toolbar to select and bulk-archive or bulk-delete sessions, and a confirmation step for all bulk actions.
- Opening a background agent's activity tab now scrolls to the latest output and shows a live progress indicator while the agent is working.
- Renamed the sidebar "Group by" time option from "Updated" to "Last updated" for clarity.
- Routine agent actions (internal memory bookkeeping, read-only session/workspace lookups, and session/workspace renames) are no longer shown as individual rows in the conversation timeline, reducing clutter. Completed thinking and activity blocks now start collapsed by default.
- The "Manage sessions" view now shows two separate disk usage columns — "Files (Disk)" for the session's working files and "Chat (Disk)" for the chat history — instead of a single combined column. Both columns are sortable.
- The Automations screen now has a unified search input that filters both automation cards and runs simultaneously, with matched text highlighted. A filter icon inside the search bar provides access to Project, Status, and 'Runs of' filters. No-match states now show a proper empty state with a 'Clear filters' button.

### Fixed

- Action buttons in the home page "Up next" list are now visible when focused via keyboard, not only on mouse hover.
- Ctrl+Z (undo) and Ctrl+Shift+Z / Ctrl+Y (redo) now work in the chat composer on Linux, where WebKitGTK doesn't bind those keystrokes to native editing by default.
- Fixed a Windows resource leak where tray menu rebuilds could accumulate USER objects over time, potentially causing the app to malfunction after many session changes.
- Fixed an issue where the "This project's GitHub account was removed" banner could stay stuck even though the correct account was still connected.
- Fixed empty system sounds picker on Linux in notification settings
- Fixed image preview bounding box being wider than the image for wide (e.g. panoramic) images in conversations.
- Fixed the chat composer floating in the middle of the screen instead of staying pinned to the bottom when there are only a few messages.
- Fixed the in-app pull request view failing to load on GHES and GHE.com (data residency) hosts, where it previously showed a GraphQL schema error.
- Manually renamed sessions and workspaces are no longer overwritten by the agent's automatic rename.
- Running a script now focuses its terminal tab, so the command starts and streams output immediately instead of waiting until you click into the tab.
- Screen readers now correctly announce punctuation and arrow-key shortcuts in the command palette (e.g. "Command + Comma" for the Go to Settings shortcut), instead of silently dropping them.
- Slash command menu now filters more accurately and no longer surfaces unrelated commands when nothing matches the typed query. Keyboard shortcut glyphs in menus are now sized to match the surrounding text.
- The sidebar resize handle now shows a visible hover stripe when you drag to resize, making it easier to discover; Swift files now display syntax highlighting in the file viewer.
- The terminal now shows a clear, actionable error when your $SHELL points to a path that no longer exists, instead of a raw system error.
- When viewing a referenced pull request in the session panel, the Overview and Changes tabs are now shown so you can browse the PR diff.

## v1.0.5

### Added

- Model Providers configuration — connect your own API keys from OpenAI, Anthropic, Azure, and others — is now available to all users in Settings.

### Fixed

- Fixed a sidebar status flicker where merging a pull request briefly bounced between "Ready to merge" and "Done" before settling.

## v1.0.4

### Highlights

- Fixed a bug where backslashes (e.g. in Windows paths, LaTeX, or regex) were doubled on every save in the markdown editor, progressively corrupting files.
- Fixed multi-second freezes when opening the right-click context menu, command palette, and merge drawer while content was loading — open times now stay consistently fast.
- After an Autopilot task finishes, the session mode now automatically reverts to Interactive so your next prompt isn't silently run in Autopilot.
- The /impeccable design skill's subcommands are now discoverable and selectable directly in the slash-command palette.
- Fixed a frame-rate drop to ~5fps when typing in the composer while the agent streams a response.

### Added

- Added a `ghapp://automations/new` deep link that opens the new automation dialog with name, prompt, and trigger schedule pre-filled — the workflow is not created until the user clicks Create.
- Added an "Automatically check for updates" toggle in General settings. When turned off, the app no longer runs background update checks on launch or hourly; the manual "Check for updates" action still works.
- After the agent finishes an Autopilot task, the session mode now automatically reverts to Interactive so your next prompt is not silently run in Autopilot.
- The /impeccable design skill's subcommands (shape, craft, critique, polish, and more) are now discoverable and selectable directly in the slash-command palette.
- When the Impeccable design skill is enabled, the design hook now fires automatically after each file edit, giving the agent immediate design feedback to incorporate into its next step.

### Changed

- Internal: Desktop's Copilot CLI sessions can enable memory through typed copilot-sdk session configuration when the Session memory experiment is enabled.
- Renamed the "Recent sessions" menu item and view title to "Manage sessions" to better reflect that it supports search, bulk archive, and delete — not just a list of recent activity.
- Running a script now opens the run output as a regular tab instead of forcing a bottom split, so your current view stays undisturbed when the panel is already open.
- Settings tabs now preserve their state (search queries, expanded rows, and scroll position) when switching between sections, and switching back to a previously visited tab is instant.
- The Auto model row in the model picker now shows an info popover explaining that Auto selects the best model for your request and that usage through Auto is billed at a 10% discount.
- When the agent views multiple images in a single batch, they now collapse into a single "View N images" tool call that expands into a row of clickable thumbnails when clicked.

### Fixed

- Fixed a bug in the markdown editor canvas where backslashes (e.g. in Windows paths, LaTeX, or regex) were doubled on every save, progressively corrupting the file.
- Fixed a frame-rate drop (down to ~5fps) when typing in the composer while the agent is streaming a response, caused by an ungated per-row ResizeObserver in the conversation list.
- Fixed a remaining cause of multi-second freezes when opening the right-click context menu, command palette, and merge drawer while a diff, checks, or conversation was loading — open times now stay consistently fast.
- Fixed background agent duration showing an inflated time (e.g. "67h 8m") in the composer pill after resuming a session.
- Fixed image drag-and-drop onto the prompt composer being silently ignored on macOS Retina displays.
- Fixed the bulk selection toolbar in My Work wrapping the item count onto two lines when many items are selected.
- In multi-account setups, the avatar shown on ask_user prompt answers now correctly reflects the account linked to the session's repository instead of always showing the default account.
- Issue type indicators in the issue detail toolbar now show as hollow rings instead of filled circles, matching the style used elsewhere in the app and on GitHub.com.
- Keyboard users can now navigate the PR comment reaction picker using arrow keys, with Home/End to jump to the first or last emoji.
- Links in rendered markdown content now show a pointer cursor on hover, making them feel correctly interactive.
- Question and answer text in ask_user conversation rows is now selectable and copyable.
- The My Work detail panel now shows a proper empty state with a close button when no item is selected, so the panel is no longer a dead end.
- When an agent creates a sub-session via the `create_session` tool and specifies a custom agent in the kickoff parameters, the child session now correctly loads that agent instead of inheriting the parent session's agent.
- When multiple local clones of the same repository are open, the project picker now shows distinct labels (e.g. "work/webapp" and "personal/webapp") instead of identical names.

## v1.0.3

### Highlights

- Fixed a critical bug where an in-app update could silently wipe all workspaces and session history — the app now automatically recovers from a backup if the database is found empty or corrupt at startup.
- Daily scheduled workflows now support selecting multiple hours, so the same automation can run at several times per day without writing a custom cron expression.
- Settings now has a dedicated Sessions tab grouping session-related options — default model, custom instructions, auto-approve, agent merge attribution, remote access, and session lifecycle.
- The session info popover now shows a complete context window breakdown — system prompt, tools, MCP tools, messages, free space, and buffer — at any time, not just during an active turn.
- Fixed a progressive slowdown when opening the right-click context menu, command palette, and merge drawer after extended use — open times now stay consistently fast.

### Added

- Daily scheduled workflows now support selecting multiple hours, so the same automation can run at several times per day without writing a custom cron expression.
- Deep links now support opening a specific cloud automation or cloud automation run directly in the app (e.g. from a notification or the GitHub automations page).
- You can now customize project groups in the sidebar with a display name and color — right-click a project group and choose Customize to personalize it.

### Changed

- Bash command rows now show a live elapsed timer while a command is running, making it easy to tell how long a command has been going.
- Failed workflow run errors now show an inline copy button on hover, making it easy to copy exact error text without interfering with clicking the row.
- Merged pull requests now display the same pull request icon as open pull requests, distinguished by color, for a more consistent appearance everywhere they're shown.
- Pull request descriptions that fail to load now show a clear error with a Try again button instead of an empty description.
- Settings now has a dedicated "Sessions" tab grouping session-related options (default model, custom instructions, auto-approve, agent merge attribution, remote access, and session lifecycle) separately from general app settings.
- The send button in the prompt composer now changes color to match the active session mode — blue for Plan mode and green for Autopilot mode.
- The session info popover now shows a complete context window breakdown — system prompt, tools, MCP tools, messages, free space, and buffer — at any time, not just during an active turn.
- The Submit review and Cancel buttons in the PR review panel are now right-aligned, with Cancel to the left of Submit review, matching standard dialog conventions.

### Fixed

- Agent autocomplete now reflects newly installed or removed plugin-provided agents without requiring a restart.
- Changing reasoning effort without switching models now shows the correct notice (e.g. "Reasoning effort changed from Medium to High.") instead of incorrectly saying the model changed.
- Fixed a bug where an in-app update could silently wipe all workspaces and session history on the next launch. The app now automatically recovers from a backup if the database is found empty or corrupt at startup.
- Fixed an issue where the PR button always used "main" as the target branch even when a different base branch was selected, especially when clicking the button quickly before changes had loaded.
- Fixed conversation messages overlapping a long first prompt when scrolling through the chat history.
- Fixed file drag-and-drop missing the drop target on high-DPI displays.
- Fixed near-black hue colors in the Monochrome theme in light mode — colored elements now render as distinct, visible hues instead of collapsing to near-black.
- Fixed progressive slowdown when opening the right-click context menu, command palette, and merge drawer after extended app use — open times could grow from milliseconds to several seconds and now stay consistently fast.
- Fixed the breadcrumb in the pull request detail view being hidden behind macOS window controls when the sidebar is collapsed.
- In the sidebar's group-by-status view, a session tree now surfaces in its most urgent group, so a ready-to-merge or needs-input child session bubbles the whole tree up instead of being hidden under the root session's group.
- Issues that were transferred between repositories no longer get stuck on "Loading..." when opened, whether from the inbox or inside a session.
- Pull requests that have automatic merge enabled but with the 'Merge pull request' action turned off now correctly appear as ready to merge in the sidebar.
- The auto-merge button in the pull request merge drawer no longer flashes back to its previous state while the request is in flight — enabling or disabling auto-merge now immediately reflects the new state.
- Voice dictation no longer prevents the Linux app from launching on PipeWire or bare ALSA systems without PulseAudio client libraries installed.

## v1.0.2

### Highlights

- Session forking is now available to all users: fork a session from a completed agent response to explore an alternative approach, then merge the forked work back to the parent session.
- Pull request creation now automatically creates or reuses forks for public repositories when you don't have push access to the upstream.
- Start a Copilot session in any repository directly from an issue's context menu in My Work, not just the repository the issue was filed in.
- Weekly automations can now be scheduled to run on multiple days of the week.
- Remote sessions are easier to find: the sidebar's new-project menu includes a 'Resume remote session…' option, and the command palette groups remote sessions by repository.

### Added

- Added a "New session in repository..." option to the issue context menu in My work, letting you start a session in a different repository than the one the issue was filed in. The bulk Actions picker can also start individual sessions in a chosen repository.
- Pull request creation can now automatically create or reuse forks for public repositories when the current user cannot push to the upstream repository.
- Session forking is now available to all users: fork a session from a completed agent response to explore an alternative approach, then merge the forked work back to the parent session.
- Weekly automations can now be scheduled to run on multiple days of the week. Select multiple weekday checkboxes when creating or editing a weekly automation; the trigger displays a compact summary (e.g. "3 days selected") and the selected days are restored when you reopen the automation.

### Changed

- Clicking a GitHub issue link in chat or a canvas opens the issue in the app's side panel instead of the system browser. Right-click the link to open it in your default browser or copy it; in a canvas, Cmd/Ctrl-click also opens it in your browser.
- In the sidebar, sessions with an open pull request now appear above sessions that are still actively running.
- Remote sessions are now easier to find: the sidebar's new-project menu includes a 'Resume remote session…' option, and the command palette groups remote sessions by repository with pull-request or branch icons.
- Search and grep tool results are now grouped by file, showing each file path once as a header with a line-number gutter, making results easier to scan.
- Sessions whose PR is ready to merge now appear under a dedicated "Ready to merge" group in the grouped sidebar view, instead of being mixed into "Needs input".
- Settings sidebar navigation is now organized into logical groups, labels use consistent sentence case ("MCP servers", "Model providers"), and Model providers has a new icon.
- The composer now shows a dedicated Plan pill and a separate Background agents pill again, instead of a single combined Tasks pill.
- The default branch prefix now uses a dash separator (e.g. `username-my-feature`) instead of a slash (e.g. `username/my-feature`) for newly generated branch names.

### Fixed

- An error message now appears under the repository name input in the create repository dialog when the name contains disallowed characters, instead of the Create button silently staying disabled.
- Fixed a file-watcher leak that could accumulate while opening, archiving, and deleting workspaces over a long session, eventually exhausting the app's file watchers and causing it to stop detecting file changes until restart.
- Fixed an issue where editing the interval of a workspace-bound automation workflow (e.g., manual → hourly) would silently revert to the previous value after saving.
- Fixed an issue where the composer pills (Changes, PR, Plan, Tasks) would briefly stack vertically when closing an expanded panel.
- My Work list rows now stay highlighted while their context menu is open, making it clear which item the menu applies to.
- Opening the Automations view via a deep link on cold start no longer intermittently shows a blank screen.
- Repository name input no longer auto-capitalizes the first letter — the exact casing you type is now preserved.
- The add-tab (+) button in the right-panel tab bar now sits immediately after the last tab instead of floating at the far right edge of the bar.
- The changed-files count no longer resets to zero when a file-watcher error occurs; the last known file list is preserved until a successful update arrives.
- User, plugin, and remote agents are now shown in the /agent command when working inside a project, not just project-scoped agents.

## v1.0.1

### Highlights

- Added configurable branch prefix settings — set an app-wide default and a per-project override for the prefix used when generating worktree branches.
- External links can now open the app and pre-fill the plugin install form via deep links, letting plugin marketplace READMEs link directly into Settings → Plugins.
- Sketch is now available as a recommended MCP server in Settings, letting you connect Copilot to your Sketch designs.
- GitHub issue and pull request links now open in-app by default, showing them in right-panel tabs or the My Work detail view instead of the system browser.
- The "Default model" option has been removed from General Settings — your model, reasoning effort, and context tier selections in the composer are now automatically used for new sessions.

### Added

- Added configurable branch prefix settings — set an app-wide default and a per-project override for the prefix used when generating worktree branches.
- External links can now open the app and pre-fill the plugin install or add-marketplace form via deep links, letting plugin marketplace READMEs link directly into Settings → Plugins.
- Sketch is now available as a recommended MCP server in Settings, letting you connect Copilot to your Sketch designs.

### Changed

- GitHub issue and pull request links now open in-app by default across markdown and timeline cross-reference surfaces. In workspace sessions they open in right-panel issue/PR tabs, and in My Work they navigate to the corresponding detail view. Right-click on these links shows a consistent Open link and Copy link menu, where Open link and Cmd/Ctrl-click still open the system browser.
- In the composer Tasks panel, group headers ("To-dos" / "Background agents") are now hidden when only one group is present, reducing visual clutter.
- MCP settings now groups servers into categories — 'On this device', 'Plugins', and 'Built-in' — making it easier to see which servers come from plugins versus your own configuration.
- The "My work" filter bar now shows only your active filters instead of listing all available filters as placeholder pills. Adding a filter and then clearing its value keeps the picker open so you can choose a new value, and closing the picker with no value removes the pill. Filters showing "Any" now appear visually muted.
- The feature tip on new-session and quick-chat empty states is now stable for the duration of a session. The auto-rotating behavior and the "Show another tip" button have been removed.
- The sidebar's 'Filter sessions' dropdown (Sort by, Projects) has been replaced with a single toggle button to switch between grouped and flat session views.
- Updated slash command descriptions to use "session" instead of "workspace".
- When the agent asks you a question, your answer now shows your GitHub avatar and a curved connector linking the question to your response.

### Fixed

- Fixed an intermittent error ('Cannot rebase onto multiple branches') that occurred when running git rebase or git pull --rebase in a workspace while the app was open and polling for sync status in the background.
- Fixed the focus ring not appearing on the Keyboard Shortcuts settings heading when navigating to it via deep link on macOS.
- Keyboard focus ring now appears correctly when navigating the server-type selector in Settings → MCP Servers → Add server using arrow keys on macOS.
- Label color dots in the pull request and issue metadata toolbar now match the colors shown in the labels dropdown.
- macOS: pressing `Home` or `End` on an external keyboard no longer inserts an invalid `.notdef` box character (U+F729 / U+F72B) into the chat composer, home-screen prompt, or other text inputs.
- On Windows, the app no longer becomes unresponsive to NVDA and Windows Voice Access after the window loses focus or is covered by another window.
- On Windows, the Open dialog now shows the correct icon for PowerShell (Core / 7+) and correctly labels the legacy entry as "Windows PowerShell".
- Opening a dialog (such as Settings) now closes any open menu instead of leaving it visible on screen.
- Opening a non-text binary file (e.g. a font or other binary file) in the workspace file viewer now shows the "This file can't be previewed" placeholder instead of a "Failed to load workspace file." error banner.
- Restored the separate "Show another tip" button on the empty-state rotating tips, so the tip text is read as content instead of being hidden inside the button's accessible name.
- Right-clicking an item in My Work and choosing "New session" from the context menu now opens the session composer (where you can choose a model and write a prompt) instead of immediately starting an automatic review.
- Screen readers now announce the number of matching shortcuts (e.g. "3 shortcuts found" or "No shortcuts found") when filtering the keyboard shortcuts list in Settings → Accessibility.
- Text in extension canvases (editor preview, browser, terminal, and others) now renders with the same font smoothing as the rest of the app.
- The in-app terminal now correctly reports its terminal type as xterm-256color regardless of how the app was launched, fixing broken colors and missing capabilities in shells and TUI programs when the app was started from tmux, screen, or the macOS dock.
- Users on unlimited plans now see an infinity icon and a 'No usage limit' label in the prompt composer usage gauge instead of a blank space.
- Videos attached to a pull request or issue now play in the detail panel instead of showing a blank area.
- When editing an existing cloud automation, the "Run in the cloud" switch now correctly shows as enabled and disabled (read-only) instead of being hidden, and clicking the label text no longer accidentally toggles the switch.
- When opening the Keyboard Shortcuts settings section via the command palette, the section heading is now focused and scrolled into view.

### Removed

- The "Default model" option has been removed from General Settings. Your model, reasoning effort, and context tier selections in the composer are now automatically used when creating new sessions.

## v1.0.0

### Highlights

- The Recent sessions view now supports bulk actions — select multiple sessions and archive or delete them at once, with new sortable Branch and Created columns.
- The composer now shows a dedicated Tasks pill combining to-dos and background agents, plus a separate Plan pill that opens the plan document.
- In Local mode, the session composer now includes a branch picker so you can choose which branch to start a session on.
- Business, Enterprise, and GHES users whose organization had 'Editor preview features' disabled are no longer blocked from accessing the app during sign-in.
- Your local repository vs. new worktree preference for new sessions now carries across projects, defaulting to the type you last chose.

### Added

- Added an About dialog (accessible via the GitHub menu) that includes a License and Open Source Notices section listing third-party dependency licenses.
- Added an AI disclaimer — "GitHub Copilot uses AI. Check for mistakes." — at the bottom of the home view.
- In Local mode, the session composer now shows a branch picker so you can choose which branch to start a session on instead of always using the current branch.
- The Recent sessions view now supports bulk actions: select multiple sessions via checkboxes and archive or delete them at once. The view also gains sortable Branch and Created columns and a header actions menu with options to reset column widths or delete all archived sessions.

### Changed

- The composer now shows a dedicated Tasks pill that combines to-dos and background agents in one panel, plus a separate Plan pill that opens the plan document. The right-panel Plan tab is reserved for plan.md content and no longer appears for to-do-only sessions.

### Fixed

- Business, Enterprise, and GHES users whose organization had "Editor preview features" disabled are no longer blocked from accessing the app during sign-in.
- Enlarged the checkbox hit target in the My work and Recent sessions tables so the full cell area toggles selection, not just the small checkbox box.
- Fixed accessibility issues when customizing keyboard shortcuts in Settings: focus is now properly managed when entering capture mode, screen readers now announce shortcut recording state and results, and conflict resolution buttons are reachable by keyboard.
- The local repository vs. new worktree choice for new sessions now carries across projects — opening a project you haven't configured before defaults to the type you last chose, instead of always resetting to a new worktree.

## v0.2.34

### Highlights

- Added a Plugins tab in Settings to install, manage, and browse Copilot plugins from marketplaces, with enable/disable toggles, update, and uninstall.
- Pull request and issue detail views now show a metadata toolbar below the title with one-click editing for reviewers, assignees, and labels.
- You can now select and copy text from the diff view, with selections preserved as you scroll.
- New session screens display rotating feature tips covering slash commands, file references, modes, and more.
- Clicking a choice in an ask-user prompt now confirms it immediately, removing the need for a second Continue click.

### Added

- Added a Plugins tab in Settings to install, manage, and browse Copilot plugins from marketplaces, including enable/disable toggles, update, and uninstall.
- Added an "Open in default browser" option to the right-click context menu on links in chat messages.
- New session screens now display rotating feature tips — covering slash commands, file references, modes, and more — so you can discover what Copilot can do while you think about your first message.
- Pull request and issue detail views now show a metadata toolbar directly below the title with pill-shaped buttons for reviewers, assignees, and labels — each editable in one click.
- You can now select and copy text from the diff view, with selections preserved as you scroll through virtualized content.

### Changed

- Clicking a choice in an ask-user prompt now confirms it immediately, removing the need to click Continue as a second step.
- The rotating tip in the empty states is now more accessible: its shuffle control names the action in its accessible name ("Show another tip"), and a newly shuffled tip is announced to screen readers.
- You can now scroll the mouse wheel over the right-panel tab bar to reveal tabs that don't fit on screen, in addition to using the overflow menu.

### Fixed

- Fixed a horizontal scrollbar appearing in the Settings dialog at high browser zoom levels.
- In the keyboard shortcuts help dialog, screen readers now read each shortcut as a structured list that pairs the action with its keys, and announce punctuation keys such as comma, brackets, and backtick by name instead of skipping them.
- Long single-word pull request and issue titles (such as test method names) now wrap correctly instead of overflowing the container in both the full-screen and sidebar panel views.
- On Linux, middle-click paste no longer unexpectedly attaches a clipboard image to the message composer.
- Screen readers now announce the correct last-updated time for sidebar workspace rows instead of always saying '2 minutes ago'.
- Screen readers now announce which item is active in the Settings navigation panel, making it easier to orient within the Settings dialog without leaving the navigation list.
- Screen readers now correctly announce "Settings" (instead of "Projects") when the Settings dialog opens.
- The 'No GitHub repositories yet' empty-state heading in My Work is now a real heading, allowing screen-reader users to reach it via heading navigation.
- The Settings dialog page title is now properly announced as a heading by screen readers, improving navigation for assistive technology users.
- VoiceOver now announces Skills settings rows correctly — the disclosure reads only the skill name instead of including the action buttons' labels in the announcement.

## v0.2.33

### Highlights

- Added a /orchestrate composer command for coordinating multi-session and multi-repo work, letting the agent delegate tasks across child sessions.
- Added /context and /usage slash commands to view your session's token usage and AI credit spend, or your plan's usage and rate limits.
- The agent can now create cloud sessions on your behalf when using the create_session tool, in addition to local sessions.
- MCP App UI panels can no longer send chat messages or invoke tools without a user gesture, closing a security vulnerability where a server-authored panel could act automatically on load.
- Mermaid diagrams now render using the improved Beautiful Mermaid renderer by default, with automatic fallback for unsupported syntax.

### Added

- Added /context and /usage slash commands in the chat composer. /context opens the session usage summary (token count, context window, and AI credit spend); /usage opens your plan's usage and rate limits.
- Added a /orchestrate composer command for coordinating multi-session and multi-repo work, letting the agent delegate tasks across child sessions instead of working inline.
- File paths mentioned in assistant messages that point to generated artifacts are now rendered as clickable links that open the file in the right panel.
- The agent can now create cloud sessions on your behalf when using the create_session tool, in addition to local sessions.

### Changed

- Error toasts now show up to 4 lines of text, stay visible for 10 seconds, and include a "Copy error" button for messages with dynamic content so you can easily capture error details for bug reports.
- File paths mentioned in agent responses are now always clickable, opening the file directly in the editor.
- Images in conversations and pull requests now load lazily and use less memory.
- Improved accessibility of the Share feedback dialog: the topic menu now announces its current selection, the feedback textarea has a proper label, the submit button stays focusable and is announced as unavailable when empty, the mood picker uses correct radio button semantics with arrow-key navigation, and Tab no longer dismisses the dialog when focus is on the last control.
- Improved the command palette's session actions: added an "Open in panel..." item to open a terminal, browser, or other panel without leaving the keyboard; removed the now-redundant individual "Open terminal" and "Open browser" items; reordered thinking controls so "Set thinking effort" appears before the reasoning toggle; moved share and extension items to the bottom; and hid "Create PR" when the session has no changes. Also added a keyboard-shortcut tooltip to the right panel's "+" add-tab button.
- Mermaid diagrams now render using the improved Beautiful Mermaid renderer by default, with automatic fallback to the legacy renderer for unsupported syntax.
- The Azure DevOps popular MCP server preset now uses the hosted remote endpoint instead of a local npx command, so adding it no longer requires a local Node.js install.
- The find dialog (Cmd+F) is now unified across the conversation, diff view, and Home — one consistent experience with shared scope toggles wherever you search.

### Fixed

- Agent merge no longer silently enables on draft pull requests. Previously, a sticky per-project default could inherit onto a new draft PR and queue GitHub auto-merge without the user's knowledge.
- Binary and non-text files (e.g. .xlsx) now show a helpful empty state with "Show in Finder" and "Open file" actions instead of a raw error message. "Show in Finder/Explorer/File Manager" is also available in the file tree context menu and in the artifact editor toolbar.
- Copy, share, and bookmark actions now reliably appear on assistant responses in conversations that include tool use, task completions, or resumed historical sessions.
- Creating a session from a pull request no longer silently fails when the project's linked GitHub account is missing. The link is automatically restored if possible, and if not, an actionable error message is shown with the option to reassign the account in Project Settings.
- Dismissing the auto-cleanup prompt (via the X button, Escape, or swipe) now permanently suppresses it instead of allowing it to reappear on every app launch or every 6 hours.
- Fixed a bug where a new empty chat was created in the sidebar on every app launch.
- Fixed extra spacing on the Changes tab when no diff stats are present, so all workspace tabs now have consistent padding.
- Fixed the "GitHub authorization needed" banner flashing on and off during normal use.
- MCP App UI panels can no longer send chat messages or invoke tools on behalf of the user without a user gesture, closing a security vulnerability where a server-authored panel could do so automatically on load.
- Pasting rich content into the composer now imports supported formatting without inserting raw HTML markup. Cmd/Ctrl+Shift+V (paste as plain text) reliably inserts literal text without applying markdown formatting or link wrapping.
- Pending message bubbles now display a clearly visible dashed outline instead of a faint one.
- Pending user messages now show a "Pending" label on hover instead of a misleading timestamp.
- Quick chats are now automatically renamed by the agent based on the conversation content, matching the behavior of project sessions.
- Screen readers now announce correct item counts, keyboard shortcut names, and external-link affordances in app menus.
- Selecting a session from the Cmd-K palette now focuses the prompt composer on arrival, so you can start typing immediately without an extra click.
- The "Create from…" dialog now shows "Matching pull requests" and "Matching issues" instead of "Cached pull requests" and "Cached issues" when searching.
- The command palette now shows 'User extension' or 'Project extension' next to identically named extensions, making it easy to tell them apart when both scopes are installed.
- The sidebar toggle is now visible and usable while a workspace panel is maximized, so you can show or hide the sidebar without leaving panel focus mode.
- Toggle switches now maintain clear visual contrast across all themes, including custom and monochrome themes in both light and dark mode.
- Tooltips in the bottom pane of a split layout now display correctly instead of being hidden behind a browser preview pane.
- Voice mode mic test playback no longer hijacks the system play/pause media key.

### Removed

- Agent merge no longer remembers the last selection per project. This sticky default could enable agent merge on PRs the user never explicitly opted in for; agent merge is now always opt-in per PR.

## v0.2.32

### Added

- Export markdown content as a secret GitHub Gist from the workspace plan canvas, markdown file editor, and assistant reply actions.
- Free Copilot plan users now see an upgrade prompt in Account settings highlighting higher usage limits, premium models, and AI reviews.
- Use the /agent slash command in the prompt composer to select a custom agent for your session. The active agent is shown in the branch popover and persists across app restarts.

### Changed

- Creating a new session is now significantly faster — model data is preloaded in the background while the workspace is being set up, reducing cold-start time by ~900ms.
- Inline-code file paths in the markdown file viewer are now rendered as clickable pills that open the file directly, matching the behavior already present in chat messages and tool-call results. Newly created files also become clickable immediately without requiring a reload.
- The label filter picker in the work filter bar now renders GitHub emoji shortcodes (e.g. :bug:) as emoji glyphs instead of raw text.
- When a project's startup script fails, the error notification now shows a tail of the captured script output inline, along with a "View logs" action to see the full output and an "Edit script" action to jump directly to the project's script settings.

### Fixed

- Browser preview and extension canvas panels now correctly reflect the app zoom level instead of staying at a stale zoom when the zoom setting is changed.
- Centered dialogs no longer overflow off-screen or hide their footer and close button when the viewport is short or the user has zoomed in.
- Fixed a bug where toggling a state filter value off in the My work filter bar would have no effect when the view was saved with a legacy state qualifier (e.g. built-in views like Active), leaving the selection permanently stuck.
- On Linux, selecting a .desktop application from the "Open in..." custom app picker now correctly launches the app and displays its icon.
- Pressing ArrowDown from the newest prompt history entry now restores the saved draft and closes the history popover, instead of leaving the composer stuck at the most recent history item.
- Sleep prevention (keep awake) now works on Linux via systemd-logind D-Bus inhibit; the settings toggle is also visible on Linux.

## v0.2.31

### Added

- A new Background agents pill above the composer lists active background tasks; clicking a task opens its output in a side panel. In-chat subagent rows now also open task output in a side panel and show agent-type icons.
- Added a per-row actions menu to the pull request checks panel, letting you re-run failed checks, cancel pending checks, and open check logs without leaving the workspace.
- Agent merge now remembers your last choice per project. When you create a pull request, the agent-merge selection you last used in that project is reapplied automatically, so you don't have to re-enable it every time.
- GitHub Projects URLs pasted into the chat composer now render as styled reference pills (with the project name and icon), matching the existing behavior for Issues and Pull Requests.
- Quick chat now shows an empty state with a GitHub mark and rotating tips when no messages have been sent yet, helping users discover available commands and features.
- Right-clicking a GitHub-backed project in the sidebar now shows an "Open on GitHub" option that opens the repository in the browser.
- Right-clicking selected text in a conversation reply now shows a context menu with options to copy the selection or quote it as a follow-up in the composer.

### Changed

- Active tabs now use medium font weight instead of semibold, giving tab strips a lighter, more balanced appearance across the app.
- Git operations (such as status and diff) are now significantly faster when working with large repositories.
- The onboarding screen for users without access now directs them to explore Copilot subscription plans instead of joining a waitlist.

### Fixed

- Agent merge now starts its first check promptly after a pull request is created instead of waiting up to a minute.
- Clicking the scrollbar or padding in the slash command, skill mention, and file reference menus no longer closes the menu before you can scroll.
- Diff comments containing bare GitHub URLs no longer render clipped or invisible after their link metadata loads.
- Fix the Linux clipboard via the native backend: images now paste when the webview doesn't expose them, and copy buttons work on wlroots Wayland compositors (such as Hyprland).
- Fixed a 2–3 second UI freeze on macOS when enabling voice dictation for the first time and the microphone permission prompt appeared.
- Fixed a security issue where agent-generated links using dangerous URL schemes (javascript:, data:, vbscript:) could execute code in the app.
- Fixed git operations failing with "terminal prompts disabled" when working in repositories with non-GitHub remotes (Azure DevOps, GitLab, Bitbucket, etc.)
- Fixed high GPU usage and fan spin-up on macOS while the app is idle, particularly noticeable on high-refresh-rate (120 Hz ProMotion) displays.
- Fixed intermittent server errors when performing pull request actions (such as queuing, toggling auto-merge, and adding reactions) by automatically retrying transient failures.
- Fixed the merge panel incorrectly showing "Merge blocked" when a pull request is in the merge queue; it now correctly shows "Queued to merge".
- Fixed the Update branch button in the merge drawer incorrectly triggering the conflict-resolution agent flow when the branch was simply behind the base branch with no merge conflicts.
- Links and avatars in the inbox, pull request view, and prompt URL chips now correctly point to the right host when connected to a GitHub Enterprise Cloud Data Residency instance.
- Mention, issue, and commit autolinks in pull request and comment bodies now resolve to the correct host when connected to a GitHub Enterprise Cloud Data Residency instance.
- On macOS and Linux, the app now restricts the local database file (which may contain an auth token) to owner-only permissions (0600), and repairs existing installations on the next launch.
- Opening Settings is now faster.
- Opening the command palette (⌘K) is now faster and feels instant: it no longer triggers redundant network subscriptions on every open (which could cause multi-second delays for users with many pull requests), renders its overlay through a dedicated portal to avoid expensive whole-window style recalculation, and appears immediately instead of animating in.
- Project attachment pills in the composer now show the correct project icon and project name instead of the GitHub owner avatar and a user-like label.
- Screen readers now announce the actual key combination when focusing a keyboard shortcut chip in Settings › Accessibility › Keyboard shortcuts, instead of only reading the command name.
- The app now attempts to bring itself to the foreground when opened via a deep link from the browser, including when the app window is on a different macOS Space.
- The auto-merge agent no longer blocks on or attempts to fix optional (non-required) CI checks; only checks required by branch protection are considered when determining whether a PR is mergeable.

## v0.2.30

### Added

- Added a "Remote sessions" setting in General settings that lets you choose the default remote behavior for new sessions: Off, Export (transcript only), or Remote control.
- Added a new "Agent merge reply attribution" toggle in Settings > General (on by default). When enabled, agent merge appends a short attribution line to the replies it posts when resolving pull request review threads, indicating the reply was made automatically by the GitHub Copilot app.
- Quick Chat now includes an integrated terminal in its right panel, so you can run commands without leaving the chat.
- You can now paste or drag-and-drop images directly into GitHub comment boxes (issues, pull requests, reviews, and the create issue dialog) — the image uploads automatically and the hosted link is inserted into the comment.

### Changed

- Agent questions now appear as a card above the composer instead of replacing it. Clicking a choice or pressing its number key highlights it; pressing Enter or clicking Continue confirms. Pressing Escape or sending a normal message dismisses the prompt.
- Anthropic model names now display in full (e.g. "Claude Opus 4.8", "Claude Sonnet 4.6") in the model picker and model-change messages, matching how GPT and Gemini models are already shown.
- Clicking Run now opens the run-script terminal in a bottom split of the right panel instead of taking over the main tab group, so the diff or files surface stays visible above the run output.
- The command palette placeholder now mentions sessions, making it easier to discover that you can search for active sessions from the same entry point.
- The pull request inbox now loads initial results faster; diff stats and check status badges appear shortly after in a follow-up update.

### Fixed

- (Windows/Linux) Deep-links now route to the focused app instance when multiple instances are running, and closing one instance no longer breaks deep-link handling in others.
- API errors (billing misconfiguration, bad credentials, server errors, connection failures) now display as readable messages in the conversation instead of raw JSON or HTTP response text.
- Canvas tabs (extension, editor, and browser canvases) no longer reappear after restarting a session when the user had previously closed them.
- Closing a terminal canvas now persists across session switches — it no longer reappears when reselecting a session.
- Enabling remote control now shows a clear error when the session is unavailable (e.g. blocked by enterprise policy) instead of a false success notification with non-functional actions.
- Fixed a bug in the Rich view editor where saving a markdown file containing snake_case identifiers in tables caused backslashes to double on every save, ballooning the file size and freezing the session.
- Fixed a false "Copilot CLI failed to start" error that could appear on busy machines even when the CLI was healthy.
- Fixed a performance issue where opening multiple workspaces could pin a CPU core at 100% and cause the app to drop to near-zero frames per second.
- Fixed an error when opening an installed extension canvas from the "+" menu that caused a "Failed to open canvas" error for extensions with longer names.
- Fixed an error where USB microphones reporting 24-bit or 32-bit audio formats (such as the Jabra Link 380 on Windows) failed with "Unsupported microphone sample format" in Voice mode.
- Fixed an issue on macOS and Linux where Git Credential Manager would repeatedly display a "GitHub Sign in" dialog during background git operations, causing a loop of prompts that could not be permanently dismissed.
- Fixed an issue where clicking "Re-run" in the pull request Checks panel would open duplicate browser tabs instead of re-running the check.
- Fixed an issue where reopening a pull request with an already-provisioned workspace would stall the UI indefinitely on "Preparing project..."
- Fixed an issue where the GitHub re-authentication banner would appear repeatedly during transient GitHub API outages, even when the account token was still valid.
- Fixed deep-link callbacks on Linux opening a new instance instead of routing to the running one.
- Fixed Linux updates so deb and rpm installs show release-page guidance instead of failing to self-update, while AppImage installs can self-update again.
- Fixed markdown rendering: footnotes now appear as smaller muted text with a dividing line, task-list checkboxes stay vertically centered at all text sizes, and GitHub issue/PR reference links wrap correctly inside task lists.
- Fixed unreadable word-level diff highlights in the GitHub Light High Contrast theme, where changed words appeared as dark text on a dark background.
- Inbox search results now respect the requested sort order instead of always being sorted by most recently updated.
- Model provider icons in the model picker now correctly reflect the active light/dark theme tone, including on first paint.
- Pasting multiline text inside a blockquote now keeps all lines within the quote instead of only the first line escaping into unquoted text.
- Project pickers in the automation dialog and new-session view now label each entry by its unique project name, so multiple worktrees or folders of the same repository are distinguishable.
- Sessions are now correctly renamed by the agent when the first-prompt auto-generated name contained punctuation or mixed casing that differed from its stored form.
- Switching to a model that does not support reasoning effort (such as Auto or MAI Code 1 Flash) no longer causes session creation to fail when a reasoning effort was previously configured.
- Unsaved filter refinements in the My work inbox are now preserved when navigating away and back within the app.

## v0.2.29

### Changed

- Bare GitHub PR and issue URLs in markdown now render as compact references (owner/repo#123, or #123 for same-repo links); in list items, they also include a state-aware icon and title to match github.com rich reference behavior.
- Clicking a linked issue from the pull request body or the issue system-prompt card now opens the issue directly in the right panel instead of navigating to an external browser tab or displaying generic system prompt.

### Fixed

- Fixed automations failing to run after switching to a model that does not support reasoning.
- Fixed terminal failing to launch on Windows when PowerShell 7 was installed from the Microsoft Store.
- Fixed the timeline picker's collapsed hover area so it no longer accidentally intercepts mouse events on nearby controls in narrow viewports
- Restoring an archived session no longer fails when the session's local git branch has been deleted (e.g. after a pull request is merged and its branch auto-deleted).
- The "working" activity indicator (sidebar Working badge and the in-conversation loading row) now keeps animating when the OS has Reduce Motion enabled, instead of freezing into a static shape that looked stuck.

## v0.2.28

### Added

- Press Cmd+F (Ctrl+F on Windows/Linux) inside a conversation to search for text, with match-case and match-whole-word toggles, navigation between matches, and a configurable dialog corner in General settings.
- Quick chats now show token usage, context window, and AI credit spend in the chat title menu, matching the detail already available in regular sessions.
- When starting a session from an issue, a new "New session in repository..." option in the start menu lets you pick which of your project repositories the session opens in.

### Changed

- Comments in the pull request and merge drawers now render their content progressively as you scroll, reducing load time when opening pull requests with many comments.
- Issue pills above the composer now show the entity type in the label (for example 'Issue #1234'), matching the existing pattern used for pull request pills ('PR #6483').
- Pasting a GitHub URL (e.g. github.com/org/repo/pull/123) into the "Add GitHub repository" search now automatically extracts the repository and searches for it instead of treating the full URL as a query.
- Scheduled session automations now show a badge in the sidebar and display the next scheduled run time in the hover preview.
- The banner shown during an in-progress merge, rebase, cherry-pick, or revert now reads "Resolving …" instead of "… paused", more accurately reflecting that the operation is actively being handled by the agent.
- The conversation timeline is now always shown by default — no setting required. Timeline navigation and bookmarks are available whenever there is enough conversation history.
- The deep link URL for the Inbox view has changed from `ghapp://inbox` to `ghapp://mywork`.

### Fixed

- Collapsing a session in the sidebar now correctly hides all of its descendants, even when they belong to different repository groups.
- Fixed a soft-lock during onboarding where the "Sign in to GitHub" button never appeared for users with the system Reduce Motion accessibility setting enabled, or when the headline text was empty.
- Fixed blank terminal tab and scripts not executing when running commands on Windows with Command Prompt (cmd.exe) as the default shell.
- Fixed the Plan pill in the composer being taller and misaligned compared to other pills.
- Unlimited plans no longer show incorrect exhausted-quota indicators, and session AI-credit spend is now shown consistently in the usage gauge and workspace info popover.

## v0.2.27

### Fixed

- Fixed task-list checkboxes overflowing outside the card boundary in the pull request drawer, and enabled interactive checkbox toggling in that view.
- The "Read documentation" link on the home screen now opens the GitHub Copilot app-specific getting started guide instead of the generic Copilot documentation page.

## v0.2.26

### Added

- Added support for toggling task list checkboxes (`- [ ]` / `- [x]`) directly in the embedded pull request and issue descriptions. Changes are saved back to GitHub.
- F6 and Shift+F6 now cycle keyboard focus through major regions of the app, making it faster for keyboard and screen-reader users to navigate between the sidebar, conversation area, composer, and other landmarks.

### Changed

- Reduced worktree session startup time by roughly half, from ~6 seconds to ~3.5 seconds.
- The token usage section in the workspace branch popover now shows cached tokens and reasoning tokens in addition to input and output token counts.

### Fixed

- Conversation no longer replays a long catch-up scroll when returning to a session after display sleep, App Nap, or extended window occlusion.
- Fixed @mentions, EMU usernames, and commit SHA links not rendering correctly in pull request descriptions containing raw HTML (e.g. <details> blocks).
- Fixed an issue where delegated sessions using `notify_on_idle: "always"` would send a flood of repeated desktop notifications with no new content.
- Fixed an issue where deleting a worktree session could force-delete the local branch even when it contained local commits that were never pushed, causing data loss.
- Fixed an issue where the model picker would revert to the session's previous model when switching back to an existing session, discarding any model selection the user made.
- Fixed inline images in private-repository issues, pull requests, and comments failing to load with an HTTP 404 error once the page had been open for a few minutes. These images now refresh their short-lived signed URLs on demand.
- Fixed several keyboard navigation issues in the sidebar chat list: Tab now correctly exits the list instead of getting trapped, activating "Show more" moves focus to the first newly revealed item, and pressing Space no longer accidentally activates a chat row while typing a search.
- Fixed the end-of-response actions toolbar (copy, share, bookmark, fork) appearing on an assistant message while the response was still in progress. The toolbar now stays hidden across the whole in-flight response and only surfaces once the turn genuinely ends.
- Removed spurious "No comments yet." placeholder from the pull request conversation area and review draft panel when there are no comments.
- Settings dropdowns now immediately reflect the chosen archive and delete windows after accepting the auto-cleanup prompt, instead of showing "Disabled" until the next app restart.
- Show a loading spinner in the diff view when file changes are still loading, preventing a blank white area with no visual feedback.
- The branch sync indicator now correctly shows when a workspace branch is both diverged from its upstream and behind the PR base, instead of silently dropping the behind-base count and showing a misleading status.

## v0.2.25

### Fixed

- The app now restores your last viewed page after a reload (such as waking your Mac from sleep), instead of returning you to the home screen.

## v0.2.24

### Fixed

- In worktree sessions, the agent now correctly anchors file paths to the worktree's own checkout instead of the project's main checkout, preventing edits from silently landing on the wrong branch.

## v0.2.23

### Fixed

- Fixed automatic sync incorrectly resetting local branch checkouts, which could silently discard local commits or move the branch behind its expected position.
- Fixed canvas panels disappearing while a modal overlay (such as the command palette or settings dialog) was open; the canvas now stays visible beneath the overlay.

## v0.2.22

### Fixed

- Fixed slash commands (e.g. /chronicle) being incorrectly displayed as incoming cross-session messages instead of normal user messages.
- Fixed the app becoming slow and unresponsive when opening a pull request or workspace with a very large diff.

## v0.2.21

### Added

- Added a long context toggle in the model picker for models that support extended context windows, with the active tier shown in the model picker button.
- Added support for a `gh://session/new` deep link that opens the app and starts a new session for a given repository, pull request, or branch — with optional prompt and mode query parameters.
- Several experiments are now on for all users: canvases, MCP apps, the inbox tray menu, the channels view, cli sessions, browser-agent tools, the workspace uncommitted scope, the invertocat minigame, and editing files by selecting lines. Cloud workflows are also always on, and cloud sessions remain user-toggleable but default on for everyone. Voice dictation is now opt-in for everyone from Settings → Experimental.
- The agent can now read back the rendered output from a terminal after running a command, enabling it to see and act on command results in the terminal.

### Changed

- Copilot Pro, Pro+, and Max subscribers are now taken directly to the repository selection step after sign-in, bypassing the waitlist.
- The copy button next to PR and issue references is now always visible instead of only appearing on hover.
- The remove-project and delete-session dialogs now accurately explain that session worktrees are force-deleted, that uncommitted work is snapshotted to a recovery ref, and that recovering that work is a manual git step.

### Fixed

- Automation run timeline now displays older runs above newer runs, matching the order used in the session timeline picker.
- Command Palette now shows "Go to My work" (with the correct icon) instead of the outdated "Go to Inbox" label.
- External links clicked inside the browser preview now show a confirmation dialog offering to open the URL in your default browser, instead of being silently blocked.
- Fixed a bug where clicking "Update branch" after a local branch diverged from its upstream remote would send Copilot to merge or rebase the wrong target branch instead of the correct remote tracking branch.
- Fixed a spurious scrollbar appearing in the inline diff comment textarea on macOS when "Always show scrollbars" is enabled.
- Fixed app sluggishness (slow typing, slow session switching) when multiple concurrent sessions are streaming responses at the same time.
- Fixed images embedded in issue timelines failing to load due to an HTTP 400 error on signed attachment URLs.
- Fixed the !cmd shell shortcut when triggered from the home screen or an empty/new session — it now correctly bootstraps a workspace and opens a terminal tab in the session worktree directory instead of failing or running in the wrong location.
- Pasting a pull request URL into the quick-open palette (cmd-k) now opens the session that created that PR instead of offering to start a duplicate. Sessions are also now findable by the PR title or URL even when the session name differs.
- Quota usage percentages now display as whole numbers, consistent with the Copilot CLI.
- Removed the floating "No comments or activity yet." text that appeared visually in the pull request and issue detail view when there was no activity.
- Restored the hidden octocat minigame on the home screen, which had stopped appearing after a recent update.
- Restored the message composer during active automation runs, allowing users to respond to prompts and permission requests without first opening the session separately.
- Searching for "high contrast" in Settings now surfaces the Mode section where the High Contrast option lives.
- The model picker and session info popover now correctly show the context window size when long context is enabled.
- Uncommitted and untracked files are now preserved in a recoverable git ref before archiving or deleting a session, preventing silent data loss when removing worktrees.

## v0.2.20

### Added

- Added a long context toggle in the model picker for models that support extended context windows, with the active tier shown in the model picker button.
- Added support for a `gh://session/new` deep link that opens the app and starts a new session for a given repository, pull request, or branch — with optional prompt and mode query parameters.
- Several experiments are now on for all users: canvases, MCP apps, the inbox tray menu, the channels view, cli sessions, browser-agent tools, the workspace uncommitted scope, the invertocat minigame, and editing files by selecting lines. Cloud workflows are also always on, and cloud sessions remain user-toggleable but default on for everyone. Voice dictation is now opt-in for everyone from Settings → Experimental.
- The agent can now read back the rendered output from a terminal after running a command, enabling it to see and act on command results in the terminal.

### Changed

- Copilot Pro, Pro+, and Max subscribers are now taken directly to the repository selection step after sign-in, bypassing the waitlist.
- The copy button next to PR and issue references is now always visible instead of only appearing on hover.
- The remove-project and delete-session dialogs now accurately explain that session worktrees are force-deleted, that uncommitted work is snapshotted to a recovery ref, and that recovering that work is a manual git step.

### Fixed

- Automation run timeline now displays older runs above newer runs, matching the order used in the session timeline picker.
- Command Palette now shows "Go to My work" (with the correct icon) instead of the outdated "Go to Inbox" label.
- External links clicked inside the browser preview now show a confirmation dialog offering to open the URL in your default browser, instead of being silently blocked.
- Fixed a bug where clicking "Update branch" after a local branch diverged from its upstream remote would send Copilot to merge or rebase the wrong target branch instead of the correct remote tracking branch.
- Fixed a spurious scrollbar appearing in the inline diff comment textarea on macOS when "Always show scrollbars" is enabled.
- Fixed app sluggishness (slow typing, slow session switching) when multiple concurrent sessions are streaming responses at the same time.
- Fixed the !cmd shell shortcut when triggered from the home screen or an empty/new session — it now correctly bootstraps a workspace and opens a terminal tab in the session worktree directory instead of failing or running in the wrong location.
- Pasting a pull request URL into the quick-open palette (cmd-k) now opens the session that created that PR instead of offering to start a duplicate. Sessions are also now findable by the PR title or URL even when the session name differs.
- Quota usage percentages now display as whole numbers, consistent with the Copilot CLI.
- Removed the floating "No comments or activity yet." text that appeared visually in the pull request and issue detail view when there was no activity.
- Searching for "high contrast" in Settings now surfaces the Mode section where the High Contrast option lives.
- The model picker and session info popover now correctly show the context window size when long context is enabled.
- Uncommitted and untracked files are now preserved in a recoverable git ref before archiving or deleting a session, preventing silent data loss when removing worktrees.

## v0.2.19

### Fixed

- Extension permission dialogs no longer disappear when the agent finishes a turn, preventing the extension from becoming permanently blocked waiting for approval.
- Fixed an issue where the extension-permission dialog could appear on session start even when "auto-approve all tools" was enabled.
- Fixed the session hover card appearing in the wrong position (top-left corner) when hovering over a pinned workspace in the sidebar.

## v0.2.18

### Changed

- The files panel toolbar no longer shows redundant insertion/deletion counts when the active scope's stats match the Changes tab total (e.g. the "All changes" scope, or "Committed" with a clean working tree).

### Fixed

- Cross-session messages and workspace kickoffs now show the clean message text across all clients instead of the verbose internal wrapper, while the desktop still shows the sender attribution banner.
- Fixed an issue where leaving an active streaming session with the display asleep caused the entire session to replay character-by-character on wake, with heavy repainting and blocked session switching.
- Spell-check squiggles no longer appear in the freeform answer text box when responding to agent prompts.
- The README toggle in the new repository dialog now shows a visible label and description, making the option clearer for sighted users.
- When Git is not installed, the error shown during repository cloning now clearly states that Git is required and prompts you to install it, instead of showing a confusing system-level error message.

## v0.2.17

### Added

- Extensions can now be installed from a GitHub repository folder URL (e.g. `https://github.com/{owner}/{repo}/tree/{ref}/{path}`), in addition to gist URLs.
- The agent can now edit GitHub Actions workflow files (`.github/workflows/`) directly using its OAuth token, without requiring separate local Git credentials or the `gh` CLI.

### Changed

- Workflow tool calls (such as renaming sessions, running SQL queries, storing memory, and navigating) are now visible in the conversation timeline instead of being hidden, so you can see more of what the agent is doing.

### Fixed

- Clicking the plan.md filename link in a Create/Edit tool-call card now opens the Plan tab instead of doing nothing.
- Decision prompts (questions, plans, permission requests) no longer steal focus when they appear, preventing accidental option selection or dismissal while typing.
- Fixed a floating "Loading conversation…" label that was incorrectly visible while pull request comments were loading; the text is now hidden visually but still announced to screen readers.
- Model picker tooltip now correctly shows context window size and pricing details when connected to a cloud session.

## v0.2.16

### Added

- Sessions created by another session are now shown nested under their parent session in the sidebar.

### Changed

- Automation runs no longer flicker as placeholder sessions in the sidebar. Starting a run now immediately shows a 'Preparing automation' progress state. The 'Open session' button is promoted to a primary action in the run view. The Automations sidebar item now shows green/red counts of succeeded and failed runs instead of a single status dot.
- The pull request detail view in My Work now displays branch labels with an arrow instead of verbose merge text, and the split-pane view now shows the PR title, status badge, and labels in a compact inline row.

### Fixed

- "Always allow for this project" permission approvals now persist correctly across sessions when using git worktrees — the approval dialog no longer re-prompts on every new worktree-backed session.
- Fixed EGL_BAD_PARAMETER crashes on Wayland systems (Arch, Fedora 42) when launching the Linux AppImage
- Fixed the "Last commit" diff scope incorrectly showing an empty "No changes to compare" state and a nonsense branch label when the tip commit had changes.
- The context window size shown in the workspace header now displays the correct default tier value instead of the maximum long-context window. AI credit usage is also preserved when resuming a previous session.

## v0.2.15

### Changed

- Branch (in-place) workspace sessions now create pull requests in-place by default instead of redirecting the agent to spawn a parallel worktree session. Picking a branch workspace is treated as the signal that work belongs in the local clone, and repo-specific guidance in AGENTS.md / CLAUDE.md takes precedence over the app's general advice. The `create_pull_request` soft gate that previously refused on branch workspaces without `allow_in_place: true` has been removed.

### Fixed

- Reduced UI lag in the system tray menu during workspace switching and streaming

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

- Added experimental Voice dictation that lets you capture speech locally and insert transcripts into the composer using a configurable shortcut, with support for push-to-talk or toggle mode, microphone device selection, and local transcription model management.

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
