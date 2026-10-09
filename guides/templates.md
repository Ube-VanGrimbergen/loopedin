# loopedin: note templates

Create a file from its template the first time you need to write to it. Replace `<...>` with
real values or "Not known yet". Never overwrite an existing file with a fresh template.

Folder layout inside the notes folder:

```
learner/profile.md         who the learner is, preferences, Strong / Developing topics
learner/learning-log.md    dated evidence per topic
repos/<repo>/map.md        the learner's checked model of how the repo works
repos/<repo>/decisions.md  decisions that matter beyond one ticket
tickets/<id>/notes.md      one ticket: goal, approach, status, ask the team, recap
tickets/<id>/*.md          drafts, for example a PR description
.state/<session-id>        one word, `learn` or `fast`: the mode of that session
```

## learner/profile.md

Keep the first lines exactly in this form; the session hook reads `Default mode:`.

```markdown
# Learner profile

Default mode: ask
Experience: <Beginner / Intermediate / Advanced>
Explanations: <Plain and short / Normal / Detailed>
Notes: <anything else, for example "English is my second language">

## Strong
None yet.

## Developing
None yet.
```

A topic line under Strong or Developing:
`- <topic>: seen <n>x, last <YYYY-MM-DD>. Example: <one line>`

## learner/learning-log.md

```markdown
# Learning log

## <topic>
- <YYYY-MM-DD> <repo> <ticket>: <what happened, one line>
```

## repos/<repo>/map.md

Only write what you checked in the code. Mark guesses with `(?)`.

```markdown
# <repo> map

## Purpose
<what this repo does, 1–2 sentences>

## Main parts
- <part>: <path>. <one line on what it does>

## Main flows
- <flow name>: <step> -> <step> -> <step>

## Conventions
- <convention>: <where it is written down, or an example file>

## Unknowns
- <what is not clear yet>
```

## repos/<repo>/decisions.md

```markdown
# <repo> decisions

## <decision, as a short sentence>
Decided: <YYYY-MM-DD> · Ticket: <id>
Why: <one or two lines>
Assumes: <what must stay true>
Revisit if: <the event that should reopen it>
```

## tickets/<id>/notes.md

```markdown
# <id>: <short title>

Repos: <repo names>
Status: <step> — <what we wait for>

## Goal (in the learner's words)

## Approach

## Decisions (this ticket only)

## Ask the team
- [ ] <question> (who could know: <name or role>)

## Predictions
- <YYYY-MM-DD> expected: <...> / actual: <...>

## Recap
```
