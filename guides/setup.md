# loopedin: first-run setup

Run this once, when the notes folder has no `learner/profile.md`. Keep it short.

1. Say in three sentences: loopedin keeps you in the loop while Claude builds. In learn mode you
   reason about the approach and Claude writes the code. Notes stay on this machine, in a folder
   outside your repos, and are never pushed anywhere.
2. Ask these four questions in one AskUserQuestion call:
   - **Notes** (where to keep notes): `~/Documents/loopedin-notes (Recommended)` ("Easy to find in
     Finder and VS Code") / `Somewhere else` ("You type the path next").
   - **Experience**: `Beginner` / `Intermediate` / `Advanced`.
   - **Explanations**: `Plain and short` ("Simple words, short sentences") / `Normal` / `Detailed`.
   - **Default mode** (when you start without `/loopedin:learn` or `/loopedin:fast`):
     `Ask once per session (Recommended)` / `Always learn` / `Always fast`.
   If they chose "Somewhere else", ask for the path in chat.
3. Create the notes folder with `learner/`, `repos/`, `tickets/` and `.state/`. Create
   `learner/profile.md` and `learner/learning-log.md` from `templates.md` next to this file
   with their answers (`Default mode:` is `ask`, `learn` or `fast`). If they mentioned anything else
   about how they learn, put it on the `Notes:` line.
4. Only if the path is not `~/Documents/loopedin-notes`: write `config.json` in the plugin data folder (the command that started setup names it)
   with `{"notes_dir": "<absolute path>"}`, so the session hook finds it.
5. Tell them two things, and offer to do the first one:
   - To stop permission prompts for notes, add the folder to `permissions.additionalDirectories`
     in `~/.claude/settings.json`. Edit that file only after they say yes.
   - To see the notes in VS Code: File > Add Folder to Workspace, then save the workspace.
6. Continue with the command that started setup.
