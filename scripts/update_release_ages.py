#!/usr/bin/env python3
"""Keep exact release-age badges in the organization profile current."""

from __future__ import annotations

import argparse
import json
import os
import re
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

README = Path("profile/README.md")
REPOSITORY_PATTERN = re.compile(
    r"https://img\.shields\.io/github/v/release/quokkify/(?P<repo>[A-Za-z0-9._-]+)"
)
AGE_BADGE_PATTERN = re.compile(
    r"https://img\.shields\.io/(?:"
    r"(?:github/release-date/quokkify/[A-Za-z0-9._-]+|date/\d+)\?label=release%20age"
    r"|badge/release%20age-\d+%20days?-blue"
    r")"
)


def fetch_release_published_at(repository: str) -> datetime:
    request = urllib.request.Request(
        f"https://api.github.com/repos/quokkify/{repository}/releases/latest",
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "quokkify-profile-release-metadata",
            "X-GitHub-Api-Version": "2022-11-28",
        },
    )
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        request.add_header("Authorization", f"Bearer {token}")

    with urllib.request.urlopen(request, timeout=30) as response:
        release = json.load(response)

    published_at = release.get("published_at")
    if not isinstance(published_at, str):
        raise ValueError(f"Latest release for {repository} has no published_at timestamp")

    return datetime.fromisoformat(published_at.replace("Z", "+00:00"))


def update_release_ages(
    markdown: str,
    published_at: dict[str, datetime],
    *,
    now: datetime | None = None,
) -> str:
    current_time = now or datetime.now(timezone.utc)
    if current_time.tzinfo is None:
        raise ValueError("Current time must be timezone-aware")

    updated_lines: list[str] = []
    seen: set[str] = set()

    for line in markdown.splitlines(keepends=True):
        repository_match = REPOSITORY_PATTERN.search(line)
        if not repository_match:
            updated_lines.append(line)
            continue

        repository = repository_match.group("repo")
        if repository not in published_at:
            raise ValueError(f"Missing release timestamp for {repository}")

        release_time = published_at[repository]
        if release_time.tzinfo is None:
            raise ValueError(f"Release timestamp for {repository} must be timezone-aware")
        age_days = max(0, int((current_time - release_time).total_seconds() // 86_400))
        unit = "day" if age_days == 1 else "days"
        badge_url = (
            "https://img.shields.io/badge/release%20age-"
            f"{age_days}%20{unit}-blue"
        )
        line, replacements = AGE_BADGE_PATTERN.subn(badge_url, line)
        if replacements != 1:
            raise ValueError(
                f"Expected exactly one release-age badge for {repository}; found {replacements}"
            )
        seen.add(repository)
        updated_lines.append(line)

    missing = set(published_at) - seen
    if missing:
        raise ValueError(f"Repositories missing from profile: {', '.join(sorted(missing))}")

    return "".join(updated_lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--check",
        action="store_true",
        help="Fail when profile release ages need refreshing",
    )
    args = parser.parse_args()

    markdown = README.read_text(encoding="utf-8")
    repositories = sorted(set(REPOSITORY_PATTERN.findall(markdown)))
    if not repositories:
        raise ValueError("No project release badges found in profile README")

    published_at = {repo: fetch_release_published_at(repo) for repo in repositories}
    updated = update_release_ages(markdown, published_at)

    if updated == markdown:
        print(f"Release ages are current for {len(repositories)} repositories")
        return 0
    if args.check:
        print("Release ages need refreshing")
        return 1

    README.write_text(updated, encoding="utf-8")
    print(f"Updated release ages for {len(repositories)} repositories")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
