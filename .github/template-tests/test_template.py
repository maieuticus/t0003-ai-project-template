"""Template regression and practical tests.

Practical tests copy the template exactly like "Use this template" would (tracked and
untracked files, no .git history) into a temporary project and run it there.
Set TEMPLATE_TEST_OFFLINE=1 to skip tests that download Spec Kit or OpenSpec.
"""

import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
import projectcfg  # noqa: E402

OFFLINE = os.environ.get("TEMPLATE_TEST_OFFLINE") == "1"
# Maintenance-only file that must be moved out of the template before the first release.
EXCLUDE = {"IMPLEMENTIERUNGSVORGABE.md"}
FORBIDDEN_NEUTRAL = (".specify", "openspec", ".devcontainer", "templates", "profiles", "src")


def git(cwd: Path, *args: str) -> str:
    result = subprocess.run(["git", "-c", "user.email=t@t", "-c", "user.name=t", *args],
                            cwd=cwd, capture_output=True, text=True, check=True)
    return result.stdout


def copy_template(destination: Path) -> Path:
    listing = git(ROOT, "ls-files", "-co", "--exclude-standard", "-z").split("\0")
    for name in filter(None, listing):
        if name in EXCLUDE or not (ROOT / name).is_file():
            continue
        target = destination / name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(ROOT / name, target)
    git(destination, "init", "-q")
    git(destination, "add", "-A")
    git(destination, "commit", "-qm", "initial")
    return destination


def run(project: Path, *args: str, check: bool = False):
    result = subprocess.run([sys.executable, *args], cwd=project, capture_output=True, text=True,
                            encoding="utf-8", errors="replace")
    if check and result.returncode:
        raise AssertionError(f"{args} failed:\n{result.stdout}\n{result.stderr}")
    return result


class ProjectConfig(unittest.TestCase):
    TEXT = ("project:\n  name: \"\"\nsdd:\n  tool: null  # comment\n  version: null\n"
            "checks:\n  - [\"python\", \"-c\", \"print(1)\"]\n")

    def test_get_and_set_preserve_other_lines(self):
        self.assertIsNone(projectcfg.get(self.TEXT, "sdd", "tool"))
        updated = projectcfg.set_value(self.TEXT, "sdd", "tool", "openspec")
        self.assertEqual(projectcfg.get(updated, "sdd", "tool"), "openspec")
        self.assertIn("version: null", updated)
        self.assertEqual(projectcfg.checks(updated), [["python", "-c", "print(1)"]])

    def test_invalid_check_entry_is_rejected(self):
        with self.assertRaises(ValueError):
            projectcfg.checks("checks:\n  - not-a-list\n")


class NeutralProject(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory()
        cls.project = copy_template(Path(cls.temp.name) / "project")

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    def test_contains_no_profiles_generator_or_forced_sdd(self):
        for name in FORBIDDEN_NEUTRAL:
            self.assertFalse((self.project / name).exists(), name)
        config = projectcfg.read_text(self.project / "config/project.yaml")
        self.assertIsNone(projectcfg.get(config, "sdd", "tool"))

    def test_no_agent_installer_or_privilege_escalation(self):
        for path in self.project.rglob("*"):
            if (path.is_file() and ".git" not in path.parts and "template-tests" not in path.parts
                    and path.suffix in {".sh", ".py", ".json", ".yml", ".yaml"}):
                text = path.read_text(encoding="utf-8", errors="ignore")
                for needle in ("curl ", "| sudo", "sudo "):
                    self.assertNotIn(needle, text, f"{path.name}: {needle}")

    def test_check_and_status_work_without_generator(self):
        run(self.project, "scripts/check.py", check=True)
        status = run(self.project, "scripts/status.py", check=True).stdout
        self.assertIn("Aktueller Stand", status)
        self.assertIn("noch nicht gewählt", status)

    def test_check_detects_broken_link_and_missing_file(self):
        broken = copy_template(Path(self.temp.name) / "broken")
        (broken / "docs/PROJECT_HANDOFF.md").write_text("# x\n[kaputt](gibt-es-nicht.md)\n", encoding="utf-8")
        (broken / "docs/QUICKSTART.md").unlink()
        result = run(broken, "scripts/check.py")
        self.assertEqual(result.returncode, 1)
        self.assertIn("Linkziel fehlt", result.stderr)
        self.assertIn("Pflichtdatei fehlt", result.stderr)
        self.assertIn("Abschnitt '## Aktueller Stand' fehlt", result.stderr)

    def test_project_checks_run_and_failures_are_reported(self):
        failing = copy_template(Path(self.temp.name) / "failing")
        config = failing / "config/project.yaml"
        config.write_text(config.read_text(encoding="utf-8").replace(
            "checks: []", 'checks:\n  - ["python", "-c", "raise SystemExit(3)"]'), encoding="utf-8")
        self.assertEqual(run(failing, "scripts/check.py").returncode, 1)

    def test_openspec_tool_rejects_invalid_pin(self):
        pinned = copy_template(Path(self.temp.name) / "pin")
        (pinned / ".openspec-version").write_text("latest\n", encoding="utf-8")
        result = run(pinned, "scripts/openspec_tool.py", "--version")
        self.assertEqual(result.returncode, 1)
        self.assertIn("MAJOR.MINOR.PATCH", result.stderr)


class UpdateCheck(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        base = Path(self.temp.name)
        self.upstream = base / "upstream"
        self.upstream.mkdir()
        git(self.upstream, "init", "-q")
        (self.upstream / "f").write_text("x", encoding="utf-8")
        git(self.upstream, "add", "-A")
        git(self.upstream, "commit", "-qm", "c")
        for tag in ("v0.1.0", "v0.2.0"):
            git(self.upstream, "tag", tag)
        self.project = copy_template(base / "project")

    def tearDown(self):
        self.temp.cleanup()

    def configure(self, source: str, release: str):
        path = self.project / "config/project.yaml"
        text = projectcfg.set_value(path.read_text(encoding="utf-8"), "template", "source", source)
        path.write_text(projectcfg.set_value(text, "template", "release", release), encoding="utf-8")

    def check(self):
        before = (self.project / "config/project.yaml").read_bytes()
        result = run(self.project, "scripts/update_check.py", check=True)
        self.assertEqual((self.project / "config/project.yaml").read_bytes(), before)
        return result.stdout

    def test_current_outdated_and_unreachable(self):
        self.configure(self.upstream.as_posix(), "0.2.0")
        self.assertIn("keine neue Version", self.check())
        self.configure(self.upstream.as_posix(), "0.1.0")
        self.assertIn("neue Version v0.2.0 verfügbar", self.check())
        self.configure((Path(self.temp.name) / "gibt-es-nicht").as_posix(), "0.1.0")
        self.assertIn("nicht geprüft", self.check())


@unittest.skipIf(OFFLINE, "benötigt Netzwerk (Spec Kit/OpenSpec-Download)")
class SelectSdd(unittest.TestCase):
    def select(self, tool: str, *extra: str):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        project = copy_template(Path(temp.name) / "project")
        protected = {name: (project / name).read_bytes() for name in
                     ("AGENTS.md", ".github/copilot-instructions.md", "README.md")}
        run(project, "scripts/sdd.py", "select", tool, *extra, check=True)
        for name, content in protected.items():
            self.assertEqual((project / name).read_bytes(), content, f"{name} wurde überschrieben")
        config = projectcfg.read_text(project / "config/project.yaml")
        self.assertEqual(projectcfg.get(config, "sdd", "tool"), tool)
        run(project, "scripts/check.py", check=True)
        return project

    def test_speckit(self):
        project = self.select("speckit")
        self.assertTrue((project / ".specify/integration.json").is_file())
        self.assertTrue((project / ".specify/workflows/project-sdd/workflow.yml").is_file())
        self.assertFalse((project / "openspec").exists())
        self.assertEqual(projectcfg.get(projectcfg.read_text(project / "config/project.yaml"), "sdd", "version"),
                         (ROOT / ".specify-version").read_text().strip())
        again = run(project, "scripts/sdd.py", "select", "speckit")
        self.assertEqual(again.returncode, 1)
        switch = run(project, "scripts/sdd.py", "select", "openspec")
        self.assertEqual(switch.returncode, 1)
        self.assertIn("Migrationsplan", switch.stderr)
        self.assertFalse((project / "openspec").exists())

    def test_openspec(self):
        project = self.select("openspec")
        self.assertTrue((project / "openspec/config.yaml").is_file())
        self.assertFalse((project / ".specify").exists())
        self.assertEqual(projectcfg.get(projectcfg.read_text(project / "config/project.yaml"), "sdd", "version"),
                         (ROOT / ".openspec-version").read_text().strip())
        switch = run(project, "scripts/sdd.py", "select", "speckit")
        self.assertEqual(switch.returncode, 1)
        self.assertFalse((project / ".specify").exists())

    def test_existing_file_is_protected(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        project = copy_template(Path(temp.name) / "project")
        target = project / ".github/copilot-instructions.md"
        target.write_text("EIGENE ANPASSUNG\n", encoding="utf-8")
        run(project, "scripts/sdd.py", "select", "openspec", "--integration", "codex", check=True)
        self.assertEqual(target.read_text(encoding="utf-8"), "EIGENE ANPASSUNG\n")


if __name__ == "__main__":
    unittest.main()
