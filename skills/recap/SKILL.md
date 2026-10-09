---
description: Explain back at the end of a ticket. You write 2–3 sentences on what changed and why; Claude checks them and writes the PR description from them.
disable-model-invocation: true
---

# loopedin: recap

Notes folder: `config.json` in `${CLAUDE_PLUGIN_DATA}` (its `notes_dir`), else `~/Documents/loopedin-notes`.
Find the repo name and ticket id as in `${CLAUDE_PLUGIN_ROOT}/guides/behavior.md` ("Before the first task").

1. **Their words first.** Ask, in the checkpoint format from behavior.md:

   ---
   **✦ Explain back: <ticket title>**

   In 2–3 sentences: what changed, and why?

   ---

   Wait for their answer. Do not write a draft for them. If they are stuck, name the 2–3 most
   important changed files with one line each, and ask again.
2. **Check.** Compare their sentences with the diff against the base branch and with the ticket
   notes. Reply with at most three bullets: what is wrong, what is missing. If nothing is wrong,
   say so in one line. If something important is wrong, ask them to fix only that part, once.
   After that, correct it yourself and record the topic as Developing (behavior.md, Notes).
3. **Write the PR description** from their sentences:
   - Use the repo's pull request template and conventions if there are any (for example
     `.github/pull_request_template.md`, `CLAUDE.md`, `CONTRIBUTING.md`).
   - Otherwise use: Summary (their sentences), Why, What changed (bullets per area), How it was tested.
   - Keep their wording in the summary; fix only grammar and facts.
   Save it as `tickets/<id>/pr-description.md` in the notes folder and show it.
4. **Update the notes.** Their final sentences go under `## Recap` in the ticket notes, and the
   `Status:` line becomes `done`. Update `learning-log.md` and `profile.md` as the Notes table in
   behavior.md says. List any open "Ask the team" items in one line.

Pushing and opening the pull request stay with the user.
