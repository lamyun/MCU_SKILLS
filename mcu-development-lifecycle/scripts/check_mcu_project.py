#!/usr/bin/env python3
"""Audit an MCU project against the lifecycle baseline.

The checker is intentionally conservative: missing items are warnings by
default so teams can adopt the standard incrementally. Use --strict in CI when
the baseline should be enforced.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Iterable


REQUIRED_DIRS = [
    "governance",
    "governance/changes",
    "governance/approvals",
    "governance/decisions",
    "governance/lanes",
    "docs",
    "docs/governance",
    "docs/product",
    "docs/requirements",
    "docs/architecture",
    "docs/hardware",
    "docs/firmware",
    "docs/test",
    "docs/safety",
    "docs/team",
    "docs/release",
    "docs/field",
    "hardware",
    "hardware/schematics",
    "hardware/pcb",
    "hardware/bom",
    "hardware/bringup",
    "firmware",
    "firmware/app",
    "firmware/bsp",
    "firmware/drivers",
    "firmware/middleware",
    "firmware/platform",
    "firmware/include",
    "firmware/tests",
    "host",
    "host/protocol",
    "host/collector",
    "host/storage",
    "host/replay",
    "host/tests",
    "tools",
    "tools/scripts",
    "tools/production",
    "tests",
    "tests/unit",
    "tests/integration",
    "tests/sil",
    "tests/hil",
    "tests/regression",
    "tests/stress",
    "configuration",
    "configuration/boards",
    "configuration/products",
    "configuration/toolchains",
    "configuration/cubemx",
    "configuration/protocols",
    "lab",
    "lab/assets",
    "lab/reservations",
    "lab/calibration",
    "lab/runs",
    "manufacturing",
    "manufacturing/programming",
    "manufacturing/calibration",
    "manufacturing/test-limits",
    "manufacturing/provisioning",
    "field",
    "field/releases",
    "field/incidents",
    "field/telemetry",
    "field/capa",
    "evidence",
    "evidence/pdf",
    "evidence/builds",
    "evidence/tests",
    "evidence/hardware",
    "evidence/dataflow",
    "evidence/releases",
    "reports",
    ".mcu-mcp",
    "ci",
    "releases",
]


EVIDENCE_PATTERNS = {
    "product_discovery": [
        "docs/product/*.md",
        "docs/product/*.csv",
        "docs/product/*.xlsx",
        "docs/product/*benchmark*",
        "docs/product/*mvp*",
    ],
    "governance": [
        "governance/project-contract.yaml",
        "governance/variant-matrix.yaml",
        "governance/raci.yaml",
        "docs/project-charter.md",
        "docs/governance/*.md",
        "docs/team/*raci*",
        "docs/*raci*.md",
    ],
    "requirements": [
        "docs/requirements/*.md",
        "docs/requirements/*.xlsx",
        "docs/requirements/*.csv",
    ],
    "architecture": [
        "docs/architecture/*.md",
        "docs/architecture/*adr*.md",
        "docs/architecture/adr/*.md",
    ],
    "hardware_review": [
        "docs/hardware/*review*.md",
        "hardware/bringup/*.md",
        "hardware/bom/*",
    ],
    "firmware_standard": [
        "docs/firmware/*.md",
        "firmware/*/README.md",
    ],
    "test_plan": [
        "docs/test/*.md",
        "tests/**/*.md",
        "tests/**/*.py",
        "host/tests/*.py",
        "host/tests/**/*.py",
    ],
    "ci_toolchain": [
        "ci/*",
        ".github/workflows/*",
        "CMakePresets.json",
        "docs/firmware/*toolchain*.md",
        "docs/firmware/*ci*.md",
        "tools/*.ps1",
        "tools/scripts/*",
    ],
    "safety_security": [
        "docs/safety/*.md",
        "docs/safety/*.csv",
        "docs/safety/*.xlsx",
        "docs/architecture/*security*.md",
        "docs/architecture/*safety*.md",
    ],
    "team_collaboration": [
        "governance/raci.yaml",
        "docs/team/*.md",
        "docs/team/*.csv",
        "docs/team/*.xlsx",
        "docs/*raci*.md",
    ],
    "team_raci": [
        "governance/raci.yaml",
        "docs/team/*raci*",
        "docs/*raci*",
    ],
    "team_handoffs": [
        "docs/team/*handoff*",
        "docs/release/*handoff*",
    ],
    "change_control": [
        "governance/changes/*.yaml",
        "docs/governance/*change*",
        "docs/team/*change*",
    ],
    "release_package": [
        "docs/release/*.md",
        "releases/*",
    ],
    "field_maintenance": [
        "docs/field/*.md",
        "docs/field/*incident*",
        "docs/field/*support*",
        "docs/release/*known*",
    ],
    "enterprise_metrics": [
        "docs/governance/*metric*.md",
        "docs/governance/*dashboard*.md",
        "docs/team/*retro*.md",
        "docs/release/*post*.md",
    ],
    "evidence_index": ["evidence/index.jsonl"],
    "lab_governance": ["lab/assets/*", "lab/calibration/*", "lab/reservations/*"],
    "cubemx_generation": ["*.ioc", "firmware/**/*.ioc", "configuration/cubemx/*"],
    "host_dataflow": [
        "host/protocol/*",
        "host/collector/*",
        "host/storage/*",
        "host/replay/*",
        "host/*protocol*.py",
        "host/*collector*.py",
        "host/*store*.py",
        "host/*replay*.py",
    ],
    "protocol_contract": [
        "configuration/protocols/*",
        "configuration/telemetry/*contract*",
        "host/protocol/*schema*",
        "host/protocol/*contract*",
        "host/*protocol*.py",
    ],
    "parallel_lanes": ["governance/lanes/*.yaml", "governance/lanes/*.yml"],
    "dataflow_evidence": [
        "evidence/dataflow/*",
        "evidence/lanes/*/*/telemetry*.jsonl",
        "evidence/lanes/*/*/replay*.jsonl",
    ],
}


def has_match(root: Path, patterns: Iterable[str]) -> bool:
    for pattern in patterns:
        if any(root.glob(pattern)):
            return True
    return False


def audit_project(root: Path) -> dict:
    missing_dirs = [path for path in REQUIRED_DIRS if not (root / path).is_dir()]
    missing_evidence = [
        name for name, patterns in EVIDENCE_PATTERNS.items() if not has_match(root, patterns)
    ]

    warnings = []
    if not any((root / name).exists() for name in ["README.md", "docs/project-charter.md"]):
        warnings.append("Add a project charter or README with scope, owners, and board targets.")
    if not has_match(root, EVIDENCE_PATTERNS["governance"]):
        warnings.append("No governance evidence found; add gate, exception, metric, or decision records.")
    if not any(root.glob("docs/product/*")):
        warnings.append("No product discovery evidence found; add market benchmark, MVP scope, or option scorecard.")
    build_patterns = ("CMakeLists.txt", "Makefile", "*.uvprojx", "firmware/**/CMakeLists.txt", "firmware/**/*.uvprojx")
    if not has_match(root, build_patterns):
        warnings.append("No common firmware build project file found at the project root or under firmware/.")
    if not has_match(root, EVIDENCE_PATTERNS["ci_toolchain"]):
        warnings.append("No CI directory content found; build and test automation may not be reproducible.")
    if not has_match(root, EVIDENCE_PATTERNS["team_collaboration"]):
        warnings.append("No team collaboration evidence found; add RACI, review, or handoff records.")
    if not any(root.glob("docs/field/*")):
        warnings.append("No field maintenance evidence found; add incident, support, or traceback records.")
    if not any(root.glob("docs/safety/*")):
        warnings.append("No safety/security evidence found; add hazard, threat, or compliance records when product risk requires it.")
    if not any(root.glob("**/.gitignore")):
        warnings.append("No .gitignore found; generated build artifacts may pollute reviews.")
    if not has_match(root, ("*.ioc", "firmware/**/*.ioc", "configuration/cubemx/*")):
        warnings.append("未发现 CubeMX .ioc；请记录生成真源，或明确标记 CubeMX 不适用。")
    if not has_match(root, ("host/collector/*", "host/*collector*.py")):
        warnings.append("未发现 PC collector 证据；请补充 MCU-PC 数据链路或显式豁免。")
    if not any(root.glob("governance/lanes/*")):
        warnings.append("未发现 lane 契约；并行开发必须保持禁用或显式映射。")

    return {
        "root": str(root),
        "missing_dirs": missing_dirs,
        "missing_evidence": missing_evidence,
        "warnings": warnings,
        "ok": not missing_dirs and not missing_evidence,
    }


def print_text(result: dict) -> None:
    print(f"MCU project audit: {result['root']}")
    print()
    if result["missing_dirs"]:
        print("Missing baseline directories:")
        for item in result["missing_dirs"]:
            print(f"  - {item}")
    else:
        print("Baseline directories: OK")

    print()
    if result["missing_evidence"]:
        print("Missing lifecycle evidence:")
        for item in result["missing_evidence"]:
            print(f"  - {item}")
    else:
        print("Lifecycle evidence: OK")

    if result["warnings"]:
        print()
        print("Review prompts:")
        for warning in result["warnings"]:
            print(f"  - {warning}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit an MCU project structure.")
    parser.add_argument("project_root", help="Path to the MCU project root")
    parser.add_argument("--json", action="store_true", help="Print machine-readable JSON")
    parser.add_argument("--strict", action="store_true", help="Return nonzero when items are missing")
    args = parser.parse_args()

    root = Path(args.project_root).resolve()
    if not root.exists() or not root.is_dir():
        parser.error(f"project root does not exist or is not a directory: {root}")

    result = audit_project(root)
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print_text(result)

    if args.strict and not result["ok"]:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
