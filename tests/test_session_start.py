"""Run the real SessionStart hook with JSON on stdin, in a temporary home folder."""

import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

HOOK = Path(__file__).resolve().parents[1] / "hooks" / "session_start.py"
SESSION = "3f2a9c1e-5b7d-4e8a-9c21-7d4e5f6a8b90"


class SessionStartHook(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.home = Path(self._tmp.name)
        self.notes = self.home / "Documents" / "loopedin-notes"
        self.data = self.home / "plugin-data"
        self.data.mkdir()

    def tearDown(self):
        self._tmp.cleanup()

    def set_up_notes(self, default_mode="ask", notes=None):
        notes = notes or self.notes
        (notes / "learner").mkdir(parents=True)
        (notes / ".state").mkdir()
        (notes / "learner" / "profile.md").write_text(
            f"# Learner profile\n\nDefault mode: {default_mode}\nExperience: Intermediate\n",
            encoding="utf-8",
        )
        return notes

    def run_hook(self, stdin=None, session_id=SESSION):
        if stdin is None:
            stdin = json.dumps({
                "hook_event_name": "SessionStart",
                "session_id": session_id,
                "source": "startup",
                "cwd": str(self.home),
            })
        env = dict(os.environ, HOME=str(self.home), CLAUDE_PLUGIN_DATA=str(self.data))
        result = subprocess.run(
            [sys.executable, str(HOOK)], input=stdin, capture_output=True, text=True, env=env, timeout=10
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        return result.stdout

    def context(self, **kwargs):
        out = self.run_hook(**kwargs)
        self.assertTrue(out, "expected the hook to print context")
        data = json.loads(out)
        self.assertEqual(data["hookSpecificOutput"]["hookEventName"], "SessionStart")
        return data["hookSpecificOutput"]["additionalContext"]

    def test_silent_when_not_set_up(self):
        self.assertEqual(self.run_hook(), "")

    def test_asks_once_by_default(self):
        self.set_up_notes()
        text = self.context()
        self.assertIn("Mode: not chosen yet", text)
        self.assertIn(f"{self.notes}/.state/{SESSION}", text)
        self.assertIn("guides/behavior.md", text)

    def test_restores_learn_chosen_in_session(self):
        self.set_up_notes()
        (self.notes / ".state" / SESSION).write_text("learn\n", encoding="utf-8")
        text = self.context()
        self.assertIn("Mode: learn (chosen earlier in this session)", text)
        self.assertIn("is not approval", text)

    def test_restores_fast_chosen_in_session(self):
        self.set_up_notes()
        (self.notes / ".state" / SESSION).write_text("fast", encoding="utf-8")
        self.assertIn("Mode: fast", self.context())

    def test_profile_default_mode(self):
        self.set_up_notes(default_mode="learn")
        self.assertIn("Mode: learn (default from the learner profile)", self.context())

    def test_session_choice_beats_profile_default(self):
        self.set_up_notes(default_mode="fast")
        (self.notes / ".state" / SESSION).write_text("learn", encoding="utf-8")
        self.assertIn("Mode: learn (chosen earlier", self.context())

    def test_unknown_words_fall_back(self):
        self.set_up_notes(default_mode="sometimes")
        (self.notes / ".state" / SESSION).write_text("yes please", encoding="utf-8")
        self.assertIn("Mode: not chosen yet", self.context())

    def test_custom_notes_folder_from_config(self):
        custom = self.set_up_notes(notes=self.home / "elsewhere" / "notes")
        (self.data / "config.json").write_text(json.dumps({"notes_dir": str(custom)}), encoding="utf-8")
        self.assertIn(f"Notes folder: {custom}.", self.context())

    def test_broken_config_uses_default_folder(self):
        self.set_up_notes()
        (self.data / "config.json").write_text("{not json", encoding="utf-8")
        self.assertIn(f"Notes folder: {self.notes}.", self.context())

    def test_unsafe_session_id_is_not_used_as_a_path(self):
        self.set_up_notes()
        # Would point at learner/profile.md if it were joined to the .state folder.
        text = self.context(session_id="../learner/profile.md")
        self.assertIn("Session id: unknown", text)
        self.assertIn("Mode: not chosen yet", text)
        self.assertNotIn(".state/../", text)

    def test_symlinked_state_file_is_ignored(self):
        self.set_up_notes()
        target = self.home / "outside"
        target.write_text("learn", encoding="utf-8")
        (self.notes / ".state" / SESSION).symlink_to(target)
        self.assertIn("Mode: not chosen yet", self.context())

    def test_invalid_input_stays_silent(self):
        self.set_up_notes()
        self.assertEqual(self.run_hook(stdin="not json"), "")
        self.assertEqual(self.run_hook(stdin=json.dumps({"hook_event_name": "Stop"})), "")

    def test_hook_never_writes(self):
        self.set_up_notes()
        before = sorted(p.relative_to(self.home) for p in self.home.rglob("*"))
        self.context()
        after = sorted(p.relative_to(self.home) for p in self.home.rglob("*"))
        self.assertEqual(before, after)


if __name__ == "__main__":
    unittest.main()
