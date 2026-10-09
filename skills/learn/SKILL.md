---
description: Turn on learn mode for this session. You reason about the approach, Claude builds and explains. Runs a short setup the first time.
argument-hint: "[what you are working on]"
disable-model-invocation: true
---

# loopedin: learn mode

1. Find the notes folder: if `${CLAUDE_PLUGIN_DATA}/config.json` exists, use its `notes_dir`.
   Otherwise use `~/Documents/loopedin-notes`.
2. If `<notes>/learner/profile.md` does not exist, read `${CLAUDE_PLUGIN_ROOT}/guides/setup.md`
   and run the setup first. For its step 4, the plugin data folder is `${CLAUDE_PLUGIN_DATA}`.
3. If the session context names a loopedin session id, write the single word `learn` to
   `<notes>/.state/<session id>`, so the mode survives a restart or compaction.
4. Read `${CLAUDE_PLUGIN_ROOT}/guides/behavior.md` and follow it for the rest of this session,
   until the user runs `/loopedin:fast`.
5. If the user wrote a task after the command, start the learn loop on it. Otherwise ask in one
   line what they are working on.
