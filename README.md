# loopedin

**Be the shepherd, not the sheep.**

A Claude Code plugin for developers who build with AI and want to understand what they ship.
Claude still writes the code. loopedin keeps you in the loop: you think about the approach,
predict what will happen, and explain the change back in your own words.

It is made for feature work in an existing codebase, not for starting new projects.

## Why

AI makes it easy to click "yes" on every suggestion and ship work you can't explain.
A week later someone asks why a change was made, and you have to dig it up again. loopedin
puts a few short questions in the right places, so the understanding happens while you build.

## How it works

Every session runs in one of two modes. `/loopedin:learn` and `/loopedin:fast` set the mode.
If you start without a command, Claude asks once, at the first real task.

| Mode | What happens |
| --- | --- |
| **Learn & build** | Claude runs the learn loop below. You reason; Claude writes the code. |
| **Build fast** | Normal Claude Code. Decisions and open questions are still written down. |

The learn loop, one short question per step:

1. **Understand**: you explain the task in your own words.
2. **Orient**: you guess where in the code it lives; Claude confirms with file paths.
3. **Approach**: you describe the plan at a high level; Claude checks it against the repo's conventions and earlier decisions.
4. **Predict**: before a plan, test or build runs, you say what you expect.
5. **Build**: Claude writes the code.
6. **Explain back**: `/loopedin:recap`. You write 2–3 sentences on what changed and why; Claude checks them and writes the PR description from them.

When your approach is wrong, Claude does not hand you the answer straight away. It first asks a
question that points at the problem, then where to look, then explains the concept, and only
then gives the answer. Trivial changes skip the loop, and topics you already know get a one-line check.

## What it remembers

Notes live in one private folder on your machine, by default `~/Documents/loopedin-notes/`,
outside every repo. Add it to your editor workspace to read and edit them.

```
learner/profile.md         your preferences, plus topics you know well and topics to work on
learner/learning-log.md    dated evidence per topic
repos/<repo>/map.md        your checked model of how a repo works
repos/<repo>/decisions.md  decisions, with what they assume and when to revisit them
tickets/<id>/notes.md      goal, approach, status, questions for the team, recap
```

The repo name comes from the git remote, so all worktrees of one repo share their notes.
Nothing is sent anywhere. Notes are read into Claude's context, so your normal Claude Code
data settings apply.

## Install

You need [Claude Code](https://code.claude.com/docs) and Python 3.

```text
/plugin marketplace add Ube-VanGrimbergen/loopedin
/plugin install loopedin@loopedin
```

Restart Claude Code, then run `/loopedin:learn` in a repo you work on. The first run asks four
short questions and creates the notes folder.

| Command | What it does |
| --- | --- |
| `/loopedin:learn [task]` | Learn mode for this session; first-run setup if needed |
| `/loopedin:fast [task]` | Fast mode for this session |
| `/loopedin:recap` | Explain back at the end of a ticket |

## Develop

```sh
python3 -B -m unittest discover -s tests -v   # hook tests
claude plugin validate .                      # manifests and skills
claude --plugin-dir .                         # try it without installing
```

The tests check the session hook. They do not check how well Claude teaches; that needs real sessions.

## Credits

Inspired by [vibe-wise](https://github.com/nykooi1/vibe-wise), which does this for new projects.

## License

[MIT](LICENSE)
