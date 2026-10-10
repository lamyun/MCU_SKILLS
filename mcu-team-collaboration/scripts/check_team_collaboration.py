#!/usr/bin/env python3
"""Audit MCU project collaboration evidence."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import yaml


CHECKS = {
    "project_charter": ["docs/project-charter.md", "docs/governance/project-charter.md"],
    "raci": ["docs/team/*raci*", "docs/*raci*"],
    "decision_records": ["docs/architecture/adr/*.md", "docs/architecture/*adr*.md"],
    "risk_register": ["docs/governance/*risk*", "docs/*risk*"],
    "review_findings": ["docs/team/*review*", "docs/hardware/*review*", "docs/firmware/*review*"],
    "handoffs": ["docs/team/*handoff*", "docs/release/*handoff*"],
    "change_control": ["docs/governance/*change*", "docs/team/*change*"],
    "meeting_cadence": ["docs/team/*meeting*", "docs/team/*cadence*", "docs/governance/*cadence*"],
    "metrics": ["docs/governance/*metric*", "docs/team/*metric*", "docs/governance/*dashboard*"],
    "post_release_learning": ["docs/release/*post*", "docs/team/*retro*", "docs/governance/*lesson*"],
    "parallel_lanes": ["governance/lanes/*.yaml", "governance/lanes/*.yml"],
    "resource_leases": ["governance/lanes/*lease*", "lab/reservations/*", ".mcu-mcp/*lease*"],
    "generated_code_ownership": ["configuration/cubemx/*ownership*", "docs/firmware/*generated*", "governance/lanes/*codegen*"],
    "host_dataflow_handoff": ["docs/team/*dataflow*", "docs/team/*telemetry*", "host/*handoff*"],
}


SEMANTIC_CHECKS = {
    "project_charter": [
        ("governance/project-contract.yaml", ("project_id", "owners"), {"contract_type": "mcu-team-project"}),
    ],
    "raci": [
        ("governance/raci.yaml", ("roles",), {}),
    ],
    "risk_register": [
        ("governance/risks.yaml", ("risks",), {}),
    ],
    "change_control": [
        ("governance/changes/*.yaml", ("change_id", "requester"), {}),
        ("governance/changes/*.yml", ("change_id", "requester"), {}),
    ],
    "parallel_lanes": [
        ("governance/lanes/*.yaml", ("lane_id", "owner", "change_id", "workspace_id"), {}),
        ("governance/lanes/*.yml", ("lane_id", "owner", "change_id", "workspace_id"), {}),
    ],
    "resource_leases": [
        ("governance/lanes/*lease*.yaml", ("lease_id", "resource_type", "resource_id", "lane_id", "expires_at"), {}),
        ("governance/lanes/*lease*.yaml", ("lease_id", "resource_type", "resource_id", "lane_id", "expires_utc"), {}),
        ("lab/reservations/*.yaml", ("lease_id", "resource_type", "resource_id", "lane_id", "expires_at"), {}),
        ("lab/reservations/*.yaml", ("lease_id", "resource_type", "resource_id", "lane_id", "expires_utc"), {}),
        (".mcu-mcp/locks/resources/*.yaml", ("lease_id", "resource_type", "resource_id", "lane_id", "expires_at"), {}),
        (".mcu-mcp/locks/resources/*.yaml", ("lease_id", "resource_type", "resource_id", "lane_id", "expires_utc"), {}),
    ],
    "generated_code_ownership": [
        ("governance/generated-code-ownership.yaml", ("source_of_truth", "generated_roots", "codegen_owner_role"), {"contract_type": "mcu-generated-code-ownership"}),
    ],
    "host_dataflow_handoff": [
        ("configuration/telemetry/*contract*.yaml", ("transport", "protocol", "storage", "correlation"), {"contract_type": "mcu-hardware-pc-data-flow"}),
    ],
}

SEMANTIC_ONLY_CHECKS = {"parallel_lanes", "resource_leases"}
PLACEHOLDER_TOKENS = ("TEMPLATE", "REPLACE", "UNCONFIRMED", "<", ">")


def has_match(root: Path, patterns: list[str]) -> bool:
    return any(any(root.glob(pattern)) for pattern in patterns)


def contains_placeholder(value: object) -> bool:
    if isinstance(value, str):
        upper = value.upper()
        return any(token in upper for token in PLACEHOLDER_TOKENS)
    if isinstance(value, dict):
        return any(contains_placeholder(item) for item in value.values())
    if isinstance(value, list):
        return any(contains_placeholder(item) for item in value)
    return False


def has_semantic_contract(root: Path, check_name: str) -> bool:
    for pattern, required_keys, expected in SEMANTIC_CHECKS.get(check_name, []):
        for path in root.glob(pattern):
            try:
                value = yaml.safe_load(path.read_text(encoding="utf-8"))
            except (OSError, UnicodeError, yaml.YAMLError):
                continue
            if not isinstance(value, dict):
                continue
            if not all(key in value and value[key] not in (None, "") for key in required_keys):
                continue
            if contains_placeholder(value):
                continue
            if all(value.get(key) == expected_value for key, expected_value in expected.items()):
                return True
    return False


def audit(root: Path) -> dict:
    results = {}
    for name, patterns in CHECKS.items():
        pattern_match = has_match(root, patterns)
        semantic_match = has_semantic_contract(root, name)
        results[name] = {
            "passed": semantic_match if name in SEMANTIC_ONLY_CHECKS else pattern_match or semantic_match,
            "patterns": patterns,
            "pattern_match": pattern_match,
            "semantic_contract_match": semantic_match,
        }
    passed = sum(1 for item in results.values() if item["passed"])
    return {
        "root": str(root),
        "passed": passed,
        "total": len(results),
        "score_percent": round(passed * 100 / len(results), 1),
        "results": results,
    }


def print_text(report: dict) -> None:
    print(f"MCU team collaboration audit: {report['root']}")
    print(f"Score: {report['passed']}/{report['total']} ({report['score_percent']}%)")
    for name, item in report["results"].items():
        status = "OK" if item["passed"] else "MISSING"
        print(f"  {name}: {status}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit MCU collaboration evidence.")
    parser.add_argument("project_root", help="MCU project root")
    parser.add_argument("--json", action="store_true", help="Print JSON")
    parser.add_argument("--strict", action="store_true", help="Return nonzero if any check fails")
    args = parser.parse_args()

    root = Path(args.project_root).resolve()
    if not root.is_dir():
        parser.error(f"not a directory: {root}")

    report = audit(root)
    if args.json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        print_text(report)
    return 1 if args.strict and report["passed"] != report["total"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
