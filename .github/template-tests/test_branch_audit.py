"""Regression tests for the read-only remote branch audit."""

from datetime import datetime, timedelta, timezone
from pathlib import Path
import sys
import unittest
from unittest import mock

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
import branch_audit  # noqa: E402


NOW = datetime(2026, 11, 23, 12, 0, tzinfo=timezone.utc)
REPOSITORY = "owner/project"


def branch(name="feature/example", *, days_old=5, protected=False, sha="tip"):
    committed = NOW - timedelta(days=days_old)
    return {
        "name": name,
        "protected": protected,
        "commit": {
            "sha": sha,
            "commit": {"committer": {"date": committed.isoformat()}},
        },
    }


def pull_request(
    *, number=12, branch_name="feature/example", state="closed", merged=True,
    base="development", head_sha="tip",
):
    return {
        "number": number,
        "state": state,
        "merged_at": "2026-11-20T12:00:00Z" if merged else None,
        "base": {"ref": base},
        "head": {
            "ref": branch_name,
            "sha": head_sha,
            "repo": {"full_name": REPOSITORY},
        },
    }


class BranchAudit(unittest.TestCase):
    def test_standard_and_api_protected_branches_are_never_recommended_for_deletion(self):
        for name in ("main", "test", "development"):
            with self.subTest(name=name):
                result = branch_audit.classify_branch(
                    branch(name),
                    [pull_request(branch_name=name, base="main")],
                    REPOSITORY,
                    NOW,
                )
                self.assertEqual(result["recommendation"], "Behalten")
                self.assertEqual(result["reason"], "geschützter Standard-Branch")

        result = branch_audit.classify_branch(
            branch(protected=True), [pull_request()], REPOSITORY, NOW
        )
        self.assertEqual(result["recommendation"], "Behalten")

    def test_active_branches_and_open_pull_requests_are_never_recommended_for_deletion(self):
        active_release = branch_audit.classify_branch(
            branch("release/1.2", days_old=90), [], REPOSITORY, NOW
        )
        self.assertEqual(active_release["recommendation"], "Behalten")
        active_hotfix = branch_audit.classify_branch(
            branch("hotfix/security", days_old=90), [], REPOSITORY, NOW
        )
        self.assertEqual(active_hotfix["recommendation"], "Behalten")

        open_pr = branch_audit.classify_branch(
            branch(days_old=90),
            [pull_request(state="open", merged=False)],
            REPOSITORY,
            NOW,
        )
        self.assertEqual(open_pr["recommendation"], "Behalten")
        self.assertIn("offener Pull Request", open_pr["reason"])

    def test_only_merged_tip_into_the_expected_target_is_recommended(self):
        merged = branch_audit.classify_branch(
            branch(), [pull_request()], REPOSITORY, NOW
        )
        self.assertEqual(merged["recommendation"], "Löschung empfohlen")
        self.assertIn("vollständig", merged["reason"])

        wrong_target = branch_audit.classify_branch(
            branch(), [pull_request(base="main")], REPOSITORY, NOW
        )
        self.assertEqual(wrong_target["recommendation"], "Manuelle Prüfung empfohlen")

        changed_tip = branch_audit.classify_branch(
            branch(sha="newer-tip"), [pull_request()], REPOSITORY, NOW
        )
        self.assertEqual(changed_tip["recommendation"], "Manuelle Prüfung empfohlen")

    def test_closed_unmerged_and_stale_unassociated_branches_require_manual_review(self):
        closed = branch_audit.classify_branch(
            branch(), [pull_request(merged=False)], REPOSITORY, NOW
        )
        self.assertEqual(closed["recommendation"], "Manuelle Prüfung empfohlen")

        mixed = branch_audit.classify_branch(
            branch(),
            [pull_request(), pull_request(number=13, merged=False)],
            REPOSITORY,
            NOW,
        )
        self.assertEqual(mixed["recommendation"], "Manuelle Prüfung empfohlen")

        for age in (31, 61):
            with self.subTest(age=age):
                stale = branch_audit.classify_branch(
                    branch(days_old=age), [], REPOSITORY, NOW
                )
                self.assertEqual(stale["recommendation"], "Manuelle Prüfung empfohlen")
                self.assertEqual(stale["inactive_days"], age)
                self.assertIn("30 Tagen" if age == 31 else "60 Tagen", stale["reason"])

    def test_recent_unmerged_branch_is_kept_and_summary_counts_recommendations(self):
        recent = branch_audit.classify_branch(branch(days_old=30), [], REPOSITORY, NOW)
        self.assertEqual(recent["recommendation"], "Behalten")

        report = branch_audit.render_report([
            recent,
            branch_audit.classify_branch(branch(), [pull_request()], REPOSITORY, NOW),
        ])
        self.assertIn("Geprüfte Branches: **2**", report)
        self.assertIn("Löschung empfohlen: **1**", report)
        self.assertIn("Letzter Commit", report)
        self.assertIn("Zugehöriger PR", report)

    def test_audit_rejects_malformed_repository_names(self):
        with self.assertRaises(ValueError):
            branch_audit.audit("owner/../repo", "token")

    def test_audit_queries_branches_and_pull_requests_read_only(self):
        with mock.patch.object(
            branch_audit, "_request_json",
            side_effect=[([branch()], None), ([pull_request()], None)],
        ) as request:
            reports = branch_audit.audit(REPOSITORY, "test-token")

        self.assertEqual(reports[0]["recommendation"], "Löschung empfohlen")
        self.assertIn("/repos/owner/project/branches?", request.call_args_list[0].args[0])
        self.assertIn("head=owner%3Afeature%2Fexample", request.call_args_list[1].args[0])

    def test_workflow_is_scheduled_manual_and_read_only(self):
        workflow = (ROOT / ".github/workflows/branch-audit.yml").read_text(encoding="utf-8")
        self.assertIn('cron: "17 6 * * 1"', workflow)
        self.assertIn("workflow_dispatch:", workflow)
        self.assertIn("release:", workflow)
        self.assertIn("contents: read", workflow)
        self.assertIn("pull-requests: read", workflow)
        self.assertNotIn("contents: write", workflow)
        self.assertNotIn("pull-requests: write", workflow)


if __name__ == "__main__":
    unittest.main()
