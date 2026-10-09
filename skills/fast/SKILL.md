---
description: Switch to fast mode for this session. Normal Claude Code without teaching; loopedin still keeps decisions and open questions.
argument-hint: "[what you are working on]"
disable-model-invocation: true
---

# loopedin: fast mode

1. Find the notes folder: if `${CLAUDE_PLUGIN_DATA}/config.json` exists, use its `notes_dir`.
   Otherwise use `~/Documents/loopedin-notes`.
2. If `<notes>/learner/profile.md` does not exist, say in one line that loopedin is not set up
   yet and that `/loopedin:learn` sets it up. Then continue with the task as normal Claude Code.
3. If the session context names a loopedin session id, write the single word `fast` to
   `<notes>/.state/<session id>`.
4. Read `${CLAUDE_PLUGIN_ROOT}/guides/fast.md` and follow it for the rest of this session.
   Say in one line: "Fast mode on. `/loopedin:learn` switches back."
5. If the user wrote a task after the command, start on it.
