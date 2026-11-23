"""Read-only report of remote branches that may be safe to remove."""

from __future__ import annotations

import json
import os
import re
from datetime import datetime, timezone
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode, urlsplit
from urllib.request import Request, urlopen

PROTECTED_BRANCHES = frozenset({"main", "test", "development"})
INACTIVITY_DAYS = (30, 60)


def _request_json(url: str, token: str) -> tuple[object, str | None]:
    request = Request(
        url,
        method="GET",
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "User-Agent": "t0003-branch-audit",
            "X-GitHub-Api-Version": "2022-11-28",
        },
    )
    try:
        with urlopen(request, timeout=20) as response:
            return json.load(response), _next_link(response.headers.get("Link", ""))
    except HTTPError as error:
        raise RuntimeError(f"GitHub API returned HTTP {error.code} for {url}") from error
    except URLError as error:
        raise RuntimeError(f"GitHub API request failed for {url}: {error.reason}") from error


def _next_link(header: str) -> str | None:
    for item in header.split(","):
        parts = item.split(";")
        if len(parts) < 2 or 'rel="next"' not in parts[1]:
            continue
        link = parts[0].strip()
        if link.startswith("<") and link.endswith(">"):
            return link[1:-1]
    return None


def _pages(url: str, token: str):
    initial = urlsplit(url)
    origin = (initial.scheme.lower(), initial.netloc.lower())
    while url:
        payload, next_url = _request_json(url, token)
        if not isinstance(payload, list):
            raise RuntimeError("GitHub API returned an unexpected list response")
        if next_url:
            next_page = urlsplit(next_url)
            if (next_page.scheme.lower(), next_page.netloc.lower()) != origin:
                raise RuntimeError("GitHub API pagination link changed origin")
        yield from payload
        url = next_url


def _parse_date(value: str | None) -> datetime | None:
    if not value:
        return None
    result = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if result.tzinfo is None:
        raise ValueError("GitHub returned a commit date without a timezone")
    return result.astimezone(timezone.utc)


def _expected_target(branch: str) -> str | None:
    if branch.startswith("feature/"):
        return "development"
    if branch == "development":
        return "test"
    if branch == "test":
        return "main"
    return None


def _is_release_or_hotfix(branch: str) -> bool:
    return branch.startswith(("release/", "hotfix/"))


def _associated_prs(pull_requests: list[dict], branch: str, repository: str) -> list[dict]:
    return [
        pr for pr in pull_requests
        if pr.get("head", {}).get("ref") == branch
        and pr.get("head", {}).get("repo", {}).get("full_name", "").lower() == repository.lower()
    ]


def classify_branch(
    branch: dict,
    pull_requests: list[dict],
    repository: str,
    now: datetime | None = None,
) -> dict[str, object]:
    name = branch["name"]
    sha = branch.get("commit", {}).get("sha")
    commit = branch.get("commit", {}).get("commit", {})
    commit_data = commit.get("committer") or commit.get("author") or {}
    committed_at = _parse_date(commit_data.get("date"))
    current_time = (now or datetime.now(timezone.utc)).astimezone(timezone.utc)
    inactivity = max(0, (current_time - committed_at).days) if committed_at else None
    prs = _associated_prs(pull_requests, name, repository)
    open_prs = [pr for pr in prs if pr.get("state") == "open"]
    merged_prs = [pr for pr in prs if pr.get("merged_at")]
    target = _expected_target(name)

    report: dict[str, object] = {
        "branch": name,
        "last_commit": committed_at.strftime("%Y-%m-%d %H:%M UTC") if committed_at else "unbekannt",
        "inactive_days": inactivity,
        "merge_status": "kein zugehöriger PR",
        "pull_request": "–",
        "recommendation": "Behalten",
        "reason": "",
    }

    if prs:
        selected = open_prs[0] if open_prs else prs[0]
        state = "offen" if selected.get("state") == "open" else (
            "gemergt" if selected.get("merged_at") else "geschlossen, nicht gemergt"
        )
        report["pull_request"] = f"#{selected['number']} ({state})"
        report["merge_status"] = state

    if name in PROTECTED_BRANCHES or branch.get("protected", False):
        report["reason"] = "geschützter Standard-Branch"
    elif open_prs:
        report["reason"] = "mindestens ein offener Pull Request"
    elif _is_release_or_hotfix(name):
        report["reason"] = "Release-/Hotfix-Branch wird vorsorglich nicht zur Löschung empfohlen"
    elif any(not pr.get("merged_at") for pr in prs):
        report["recommendation"] = "Manuelle Prüfung empfohlen"
        report["reason"] = "mindestens ein zugehöriger Pull Request wurde ohne Merge geschlossen"
    elif merged_prs:
        merged = merged_prs[0]
        report["pull_request"] = f"#{merged['number']} (gemergt)"
        report["merge_status"] = f"gemergt nach {merged.get('base', {}).get('ref', 'unbekannt')}"
        same_tip = merged.get("head", {}).get("sha") == sha
        expected_target = target or merged.get("base", {}).get("ref")
        correct_target = merged.get("base", {}).get("ref") == expected_target
        if same_tip and correct_target:
            report["recommendation"] = "Löschung empfohlen"
            report["reason"] = f"Branch-Spitze ist vollständig nach {expected_target} integriert"
        else:
            report["recommendation"] = "Manuelle Prüfung empfohlen"
            report["reason"] = (
                "Branch-Spitze oder vorgesehenes Ziel weicht vom gemergten Pull Request ab"
            )
    elif inactivity is None:
        report["recommendation"] = "Manuelle Prüfung empfohlen"
        report["reason"] = "Commit-Datum ist nicht verfügbar"
    elif inactivity > INACTIVITY_DAYS[0]:
        report["recommendation"] = "Manuelle Prüfung empfohlen"
        threshold = INACTIVITY_DAYS[1] if inactivity > INACTIVITY_DAYS[1] else INACTIVITY_DAYS[0]
        report["reason"] = f"kein zugehöriger Pull Request; seit mehr als {threshold} Tagen inaktiv"
    else:
        report["reason"] = f"zuletzt vor {inactivity} Tagen geändert; keine abgeschlossene Integration"

    return report


def audit(repository: str, token: str, api_url: str = "https://api.github.com") -> list[dict[str, object]]:
    if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repository):
        raise ValueError("Repository muss das Format owner/name haben")
    if urlsplit(api_url).scheme.lower() != "https":
        raise ValueError("GitHub API muss über HTTPS angesprochen werden")

    owner, name = repository.split("/")
    root = f"{api_url.rstrip('/')}/repos/{owner}/{name}"
    branches_url = f"{root}/branches?{urlencode({'per_page': 100})}"
    reports = []
    for branch in _pages(branches_url, token):
        if not isinstance(branch, dict) or not isinstance(branch.get("name"), str):
            raise RuntimeError("GitHub API returned an unexpected branch response")
        parameters = {
            "state": "all",
            "head": f"{owner}:{branch['name']}",
            "per_page": 100,
        }
        prs_url = f"{root}/pulls?{urlencode(parameters)}"
        pull_requests = list(_pages(prs_url, token))
        reports.append(classify_branch(branch, pull_requests, repository))
    return reports


def render_report(reports: list[dict[str, object]]) -> str:
    counts = {
        label: sum(report["recommendation"] == label for report in reports)
        for label in ("Löschung empfohlen", "Manuelle Prüfung empfohlen", "Behalten")
    }
    lines = [
        "## Branch-Bereinigung: Prüfbericht",
        "",
        f"Geprüfte Branches: **{len(reports)}** · "
        f"Löschung empfohlen: **{counts['Löschung empfohlen']}** · "
        f"Manuelle Prüfung: **{counts['Manuelle Prüfung empfohlen']}** · "
        f"Behalten: **{counts['Behalten']}**",
        "",
        "| Branch | Letzter Commit | Inaktivität | Merge-Status | Zugehöriger PR | Empfehlung und Begründung |",
        "|---|---|---:|---|---|---|",
    ]
    for report in reports:
        days = "unbekannt" if report["inactive_days"] is None else f"{report['inactive_days']} Tage"
        values = (
            report["branch"], report["last_commit"], days, report["merge_status"],
            report["pull_request"], f"{report['recommendation']}: {report['reason']}",
        )
        lines.append("| " + " | ".join(str(value).replace("|", "\\|").replace("\n", " ") for value in values) + " |")
    return "\n".join(lines) + "\n"


def main() -> int:
    repository = os.environ.get("GITHUB_REPOSITORY")
    token = os.environ.get("GITHUB_TOKEN")
    if not repository or not token:
        raise SystemExit("GITHUB_REPOSITORY und GITHUB_TOKEN müssen gesetzt sein")
    reports = audit(repository, token, os.environ.get("GITHUB_API_URL", "https://api.github.com"))
    summary = render_report(reports)
    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_path:
        with open(summary_path, "a", encoding="utf-8") as output:
            output.write(summary)
    print(summary, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
