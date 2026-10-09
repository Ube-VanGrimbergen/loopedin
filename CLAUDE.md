# CLAUDE.md

loopedin is a Claude Code plugin: markdown instructions plus one read-only SessionStart hook.
No backend, no packages.

## Layout

- `skills/{learn,fast,recap}/SKILL.md`: the slash commands. `${CLAUDE_PLUGIN_ROOT}` and
  `${CLAUDE_PLUGIN_DATA}` are filled in here, and only here.
- `guides/*.md`: read by Claude with the Read tool, so placeholders are NOT filled in. Refer to
  other files as "next to this file" or with a relative path.
- `hooks/session_start.py`: finds the notes folder and prints the session's mode as
  `additionalContext`. It must stay read-only and silent on any error.

## Checks before committing

```sh
python3 -B -m unittest discover -s tests -v
claude plugin validate .
```

## Rules

- Keep the plugin generic: no employer, client or project names in examples.
- Plain, short English in every guide; the readers include people for whom English is a second language.
- Commit messages: short imperative subject. No AI co-author trailers.
