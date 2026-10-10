#!/usr/bin/env python3
"""Validate the enterprise MCU workflow review assets.

This script verifies that the 500-control enterprise review checklist is
complete and can be used as an audit surface. It also prints a lightweight
project evidence summary when --project-root is provided.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


CHECKLIST_PATH = Path("mcu-development-lifecycle/references/enterprise-review-500.md")
EXPECTED_COUNT = 500

PROJECT_EVIDENCE = {
    "governance": ["docs/project-charter.md", "docs/team/*.md", "docs/*raci*.md"],
    "product_discovery": ["docs/product/*", "docs/product/*benchmark*", "docs/product/*mvp*"],
    "requirements": ["docs/requirements/*"],
    "architecture": ["docs/architecture/*"],
    "hardware": ["docs/hardware/*", "hardware/schematics/*", "hardware/pcb/*"],
    "firmware": ["docs/firmware/*", "firmware/**/*"],
    "toolchain_ci": ["ci/*", "docs/firmware/*toolchain*", "tools/scripts/*"],
    "verification": ["docs/test/*", "tests/**/*"],
    "safety_security": ["docs/safety/*", "docs/architecture/*security*", "docs/architecture/*safety*"],
    "release": ["docs/release/*", "releases/*"],
    "production": ["tools/production/*", "docs/release/*production*", "docs/release/*manufacturing*"],
    "field_maintenance": ["docs/field/*", "docs/field/*incident*", "docs/release/*known*"],
}

REQUIRED_COLLABORATION_ASSETS = [
    "mcu-team-collaboration/references/collaboration-standard.md",
    "mcu-team-collaboration/scripts/check_team_collaboration.py",
]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def parse_controls(path: Path) -> list[dict]:
    pattern = re.compile(r"^(\d{3})\. \[([^\]]+)\] (.+)$")
    controls = []
    for line_no, line in enumerate(read_text(path).splitlines(), start=1):
        match = pattern.match(line)
        if not match:
            continue
        controls.append(
            {
                "id": int(match.group(1)),
                "domain": match.group(2),
                "text": match.group(3),
                "line": line_no,
            }
        )
    return controls


def audit_checklist(root: Path) -> dict:
    path = root / CHECKLIST_PATH
    results = []
    controls = parse_controls(path) if path.exists() else []
    by_id = {item["id"]: item for item in controls}

    for control_id in range(1, EXPECTED_COUNT + 1):
        item = by_id.get(control_id)
        if not item:
            results.append(
                {
                    "id": control_id,
                    "passed": False,
                    "detail": "control missing",
                }
            )
            continue
        words = item["text"].split()
        passed = bool(item["domain"].strip()) and len(words) >= 5
        results.append(
            {
                "id": control_id,
                "domain": item["domain"],
                "passed": passed,
                "detail": "control valid" if passed else "control too short or missing domain",
            }
        )

    duplicates = sorted(
        control_id
        for control_id in {item["id"] for item in controls}
        if sum(1 for item in controls if item["id"] == control_id) > 1
    )
    passed = sum(1 for item in results if item["passed"]) if not duplicates else 0
    return {
        "checklist": str(path),
        "total": EXPECTED_COUNT,
        "parsed": len(controls),
        "passed": passed,
        "failed": EXPECTED_COUNT - passed,
        "duplicates": duplicates,
        "collaboration_assets": {
            item: (root / item).is_file() for item in REQUIRED_COLLABORATION_ASSETS
        },
        "score_percent": round(passed * 100 / EXPECTED_COUNT, 1),
        "results": results,
    }


def has_match(root: Path, patterns: list[str]) -> bool:
    for pattern in patterns:
        if any(root.glob(pattern)):
            return True
    return False


def audit_project(project_root: Path) -> dict:
    domains = {}
    for domain, patterns in PROJECT_EVIDENCE.items():
        domains[domain] = {
            "passed": has_match(project_root, patterns),
            "patterns": patterns,
        }
    passed = sum(1 for item in domains.values() if item["passed"])
    return {
        "project_root": str(project_root),
        "domains_passed": passed,
        "domains_total": len(domains),
        "domains": domains,
    }


def print_text(report: dict) -> None:
    checklist = report["checklist_audit"]
    print(f"Enterprise MCU checklist audit: {checklist['checklist']}")
    print(f"Score: {checklist['passed']}/{checklist['total']} ({checklist['score_percent']}%)")
    if checklist["duplicates"]:
        print(f"Duplicate control IDs: {', '.join(map(str, checklist['duplicates']))}")
    missing_assets = [
        path for path, present in checklist.get("collaboration_assets", {}).items() if not present
    ]
    if missing_assets:
        print("Missing collaboration assets:")
        for path in missing_assets:
            print(f"  - {path}")
    failures = [item for item in checklist["results"] if not item["passed"]]
    if failures:
        print("Failures:")
        for item in failures[:50]:
            print(f"  {item['id']:03d}: {item['detail']}")
        if len(failures) > 50:
            print(f"  ... {len(failures) - 50} more")
    else:
        print("All 500 enterprise controls are present and valid.")

    project = report.get("project_audit")
    if project:
        print()
        print(f"Project evidence summary: {project['project_root']}")
        print(f"Domains: {project['domains_passed']}/{project['domains_total']}")
        for domain, result in project["domains"].items():
            status = "OK" if result["passed"] else "MISSING"
            print(f"  {domain}: {status}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate enterprise MCU workflow audit assets.")
    parser.add_argument("skills_root", nargs="?", default=".", help="Path to MCU skills root")
    parser.add_argument("--project-root", help="Optional MCU project root for evidence summary")
    parser.add_argument("--json", action="store_true", help="Print JSON")
    parser.add_argument("--strict", action="store_true", help="Return nonzero if checklist is incomplete")
    args = parser.parse_args()

    root = Path(args.skills_root).resolve()
    if not root.is_dir():
        parser.error(f"not a directory: {root}")

    report = {"checklist_audit": audit_checklist(root)}
    if args.project_root:
        project_root = Path(args.project_root).resolve()
        if not project_root.is_dir():
            parser.error(f"project root is not a directory: {project_root}")
        report["project_audit"] = audit_project(project_root)

    if args.json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        print_text(report)

    missing_assets = [
        present
        for present in report["checklist_audit"].get("collaboration_assets", {}).values()
        if not present
    ]
    failed = (
        report["checklist_audit"]["failed"]
        or report["checklist_audit"]["duplicates"]
        or missing_assets
    )
    return 1 if args.strict and failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
