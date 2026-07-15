#!/usr/bin/env python3
"""Append GitHub's rolling traffic window to a durable ledger.

GitHub keeps 14 days of traffic and then discards it, with no error and no warning.
This script is the only reason the discovery experiment has a record at all; see
meta/discovery-preregistration.md.

Stdlib only, on purpose: it must run before (and without) the project venv.

Usage:  GITHUB_TOKEN=... GITHUB_REPOSITORY=owner/name python meta/traffic_snapshot.py

The token must have push access to the repository (the traffic API requires it) and
must belong to the repository's own account -- see the pre-registration.
"""

from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

API = "https://api.github.com"
LEDGER = Path(__file__).parent / "traffic" / "ledger.json"


def fail(message: str) -> None:
    print(f"traffic_snapshot: {message}", file=sys.stderr)
    sys.exit(1)


def get(path: str, token: str) -> dict:
    request = urllib.request.Request(
        f"{API}{path}",
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "noether-walk-traffic-snapshot",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return json.load(response)
    except urllib.error.HTTPError as error:
        body = error.read().decode("utf-8", "replace")[:200]
        if error.code in (401, 403):
            # Silent failure here would look identical to "nobody visited": loud exit.
            fail(
                f"{error.code} on {path} -- the token lacks push access to this "
                f"repository, so the traffic API refuses it. The ledger is NOT being "
                f"written. See meta/discovery-preregistration.md. Response: {body}"
            )
        fail(f"HTTP {error.code} on {path}: {body}")
    except urllib.error.URLError as error:
        fail(f"network error on {path}: {error.reason}")


def day_of(timestamp: str) -> str:
    return timestamp[:10]


def load_ledger(repository: str) -> dict:
    if not LEDGER.exists():
        return {"repository": repository, "days": {}, "snapshots": []}
    ledger = json.loads(LEDGER.read_text())
    if ledger.get("repository") != repository:
        fail(f"ledger belongs to {ledger.get('repository')!r}, refusing to mix in {repository!r}")
    return ledger


def main() -> None:
    token = os.environ.get("GITHUB_TOKEN") or ""
    repository = os.environ.get("GITHUB_REPOSITORY") or ""
    if not token:
        fail("GITHUB_TOKEN is empty")
    if "/" not in repository:
        fail("GITHUB_REPOSITORY must be 'owner/name'")

    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    today = now[:10]

    views = get(f"/repos/{repository}/traffic/views", token)
    clones = get(f"/repos/{repository}/traffic/clones", token)
    referrers = get(f"/repos/{repository}/traffic/popular/referrers", token)
    paths = get(f"/repos/{repository}/traffic/popular/paths", token)
    repo = get(f"/repos/{repository}", token)

    ledger = load_ledger(repository)
    days = ledger["days"]

    # Days inside the 14-day window are authoritative -- overwrite. Days that have
    # aged out keep whatever we captured while they were still visible.
    for entry in views.get("views", []):
        day = days.setdefault(day_of(entry["timestamp"]), {})
        day["views"] = entry["count"]
        day["view_uniques"] = entry["uniques"]
    for entry in clones.get("clones", []):
        day = days.setdefault(day_of(entry["timestamp"]), {})
        day["clones"] = entry["count"]
        day["clone_uniques"] = entry["uniques"]

    snapshot = {
        "taken_at": now,
        "stars": repo.get("stargazers_count"),
        "forks": repo.get("forks_count"),
        "watchers": repo.get("subscribers_count"),
        "open_issues": repo.get("open_issues_count"),
        # The referrer is the result the experiment is actually after.
        "referrers": [
            {"source": r["referrer"], "count": r["count"], "uniques": r["uniques"]}
            for r in referrers
        ],
        "paths": [
            {"path": p["path"], "count": p["count"], "uniques": p["uniques"]}
            for p in paths
        ],
    }

    ledger["snapshots"] = [s for s in ledger["snapshots"] if s["taken_at"][:10] != today]
    ledger["snapshots"].append(snapshot)
    ledger["snapshots"].sort(key=lambda s: s["taken_at"])
    ledger["days"] = dict(sorted(days.items()))
    ledger["updated_at"] = now

    LEDGER.parent.mkdir(parents=True, exist_ok=True)
    LEDGER.write_text(json.dumps(ledger, indent=2, sort_keys=False) + "\n")

    total_views = sum(d.get("views", 0) for d in days.values())
    print(
        f"traffic_snapshot: {repository} | {len(days)} days on record | "
        f"{total_views} views total | {snapshot['stars']} stars | "
        f"{len(snapshot['referrers'])} referrers | -> {LEDGER}"
    )
    for referrer in snapshot["referrers"]:
        print(f"  referrer: {referrer['source']} ({referrer['uniques']} uniques)")


if __name__ == "__main__":
    main()
