#!/usr/bin/env python3
"""Run a maturity audit over the MCU skill library."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


REQUIRED_SKILLS = [
    "mcu-development-lifecycle",
    "mcu-product-discovery",
    "mcu-requirements-architecture",
    "mcu-datasheet-extraction",
    "mcu-hardware-bringup",
    "mcu-firmware-development",
    "mcu-rtos-drivers",
    "mcu-verification-test",
    "mcu-debug-optimization",
    "mcu-release-production",
    "mcu-ci-toolchain",
    "mcu-continuous-improvement",
    "mcu-safety-security-compliance",
    "mcu-team-collaboration",
]

REFERENCE_MINIMUMS = {
    "mcu-development-lifecycle": 8,
    "mcu-ci-toolchain": 2,
}

CORE_CHECKS = {
    "mcu-development-lifecycle": [
        ("Phase Gate", ["Phase Gate", "阶段门"]),
        ("Project Structure", ["Project Structure", "项目结构"]),
    ],
    "mcu-product-discovery": [
        ("Market Benchmark", ["Market Benchmark", "市场对标"]),
        ("MVP Scope", ["MVP Scope", "MVP 范围"]),
    ],
    "mcu-requirements-architecture": [
        ("MCU Selection", ["MCU Selection", "MCU 选型"]),
        ("Requirements Workflow", ["Requirements Workflow", "需求流程"]),
    ],
    "mcu-datasheet-extraction": [
        ("Pin Alternate Function", ["Pin", "Alternate Function", "引脚", "复用"]),
        ("Register Field Capture", ["Register", "Bitfield", "寄存器", "位域"]),
    ],
    "mcu-hardware-bringup": [
        ("Bring-up Sequence", ["Bring-up Sequence", "Bring-up 顺序"]),
        ("Evidence", ["Evidence", "证据"]),
    ],
    "mcu-firmware-development": [
        ("Coding Standard", ["Coding Standard", "编码规范"]),
        ("Review Checklist", ["Review Checklist", "评审检查表"]),
    ],
    "mcu-rtos-drivers": [
        ("ISR And DMA", ["ISR And DMA", "ISR 与 DMA"]),
        ("Driver Contract", ["Driver Contract", "驱动契约"]),
    ],
    "mcu-verification-test": [
        ("HIL Guidance", ["HIL Guidance", "HIL 指导"]),
        ("Test Case Fields", ["Test Case Fields", "测试用例字段"]),
    ],
    "mcu-debug-optimization": [
        ("Fault Classes", ["Fault Classes", "故障分类", "故障类别"]),
        ("Optimization Workflow", ["Optimization Workflow", "优化流程"]),
    ],
    "mcu-release-production": [
        ("Production Readiness", ["Production Readiness", "量产就绪"]),
        ("OTA And Bootloader", ["OTA And Bootloader", "OTA 与 Bootloader"]),
    ],
    "mcu-ci-toolchain": [
        ("CI Workflow", ["CI Workflow", "CI 流程"]),
        ("Required Checks", ["Required Checks", "必需检查"]),
    ],
    "mcu-continuous-improvement": [
        ("Project Directory Contract", ["project-directory-contract.md"]),
        ("Bounded Repair", ["three", "三轮"]),
    ],
    "mcu-safety-security-compliance": [
        ("Safety Workflow", ["Safety Workflow", "功能安全流程"]),
        ("Security Workflow", ["Security Workflow", "网络安全流程"]),
    ],
    "mcu-team-collaboration": [
        ("Handoff Workflow", ["Handoff Workflow", "交接流程"]),
    ],
}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def skill_dir(root: Path, skill: str) -> Path:
    return root / skill


def frontmatter_valid(path: Path, expected_name: str) -> tuple[bool, str]:
    if not path.exists():
        return False, "SKILL.md missing"
    text = read_text(path)
    match = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not match:
        return False, "frontmatter missing"
    fm = match.group(1)
    if f"name: {expected_name}" not in fm:
        return False, "name mismatch"
    if "description:" not in fm:
        return False, "description missing"
    return True, "frontmatter valid"


def contains(path: Path, needle: str) -> tuple[bool, str]:
    if not path.exists():
        return False, f"{path.name} missing"
    text = read_text(path)
    return (needle in text, f"contains {needle!r}" if needle in text else f"missing {needle!r}")


def contains_any(path: Path, aliases: list[str]) -> tuple[bool, str]:
    if not path.exists():
        return False, f"{path.name} missing"
    text = read_text(path)
    for alias in aliases:
        if alias in text:
            return True, f"contains {alias!r}"
    return False, f"missing any of {', '.join(repr(alias) for alias in aliases)}"


def no_todo(path: Path) -> tuple[bool, str]:
    if not path.exists():
        return False, f"{path.name} missing"
    text = read_text(path)
    markers = ["TO" + "DO", "[" + "TO" + "DO", "Structuring This " + "Skill"]
    found = [marker for marker in markers if marker in text]
    return (not found, "no template placeholders" if not found else f"found {', '.join(found)}")


def reference_count(root: Path, skill: str) -> tuple[bool, str]:
    minimum = REFERENCE_MINIMUMS.get(skill, 2)
    refs = list((skill_dir(root, skill) / "references").glob("*.md"))
    return (len(refs) >= minimum, f"{len(refs)} reference files, expected >= {minimum}")


def build_checks(root: Path) -> list[dict]:
    checks: list[dict] = []

    for skill in REQUIRED_SKILLS:
        base = skill_dir(root, skill)
        checks.extend(
            [
                {
                    "category": "skill-structure",
                    "name": f"{skill} directory exists",
                    "run": lambda base=base: (base.is_dir(), "directory present" if base.is_dir() else "directory missing"),
                },
                {
                    "category": "skill-structure",
                    "name": f"{skill} SKILL.md exists",
                    "run": lambda base=base: ((base / "SKILL.md").is_file(), "SKILL.md present" if (base / "SKILL.md").is_file() else "SKILL.md missing"),
                },
                {
                    "category": "skill-structure",
                    "name": f"{skill} agents/openai.yaml exists",
                    "run": lambda base=base: ((base / "agents" / "openai.yaml").is_file(), "openai.yaml present" if (base / "agents" / "openai.yaml").is_file() else "openai.yaml missing"),
                },
                {
                    "category": "frontmatter",
                    "name": f"{skill} frontmatter valid",
                    "run": lambda base=base, skill=skill: frontmatter_valid(base / "SKILL.md", skill),
                },
                {
                    "category": "template-cleanup",
                    "name": f"{skill} has no template placeholders",
                    "run": lambda base=base: no_todo(base / "SKILL.md"),
                },
            ]
        )

    for skill in REQUIRED_SKILLS:
        checks.append(
            {
                "category": "references",
                "name": f"{skill} has enough references",
                "run": lambda skill=skill: reference_count(root, skill),
            }
        )

    lifecycle = root / "mcu-development-lifecycle" / "SKILL.md"
    for skill in REQUIRED_SKILLS:
        if skill == "mcu-development-lifecycle":
            continue
        checks.append(
            {
                "category": "routing",
                "name": f"lifecycle routes to {skill}",
                "run": lambda skill=skill: contains(lifecycle, f"${skill}"),
            }
        )

    for skill, checks_for_skill in CORE_CHECKS.items():
        path = root / skill / "SKILL.md"
        for concept, aliases in checks_for_skill:
            checks.append(
                {
                    "category": "core-workflow",
                    "name": f"{skill} covers {concept}",
                    "run": lambda path=path, aliases=aliases: contains_any(path, aliases),
                }
            )

    checks.extend(
        [
            {
                "category": "maturity",
                "name": "100-point maturity reference exists",
                "run": lambda: ((root / "mcu-development-lifecycle" / "references" / "maturity-review-100.md").is_file(), "maturity review present"),
            },
            {
                "category": "team-workspace",
                "name": "team workspace contract exists",
                "run": lambda: ((root / "mcu-development-lifecycle" / "references" / "team-workspace-contract.md").is_file(), "team workspace contract present"),
            },
            {
                "category": "change-control",
                "name": "team collaboration requires a change id",
                "run": lambda: contains(root / "mcu-team-collaboration" / "SKILL.md", "change_id"),
            },
            {
                "category": "provenance",
                "name": "CI binds evidence to change and variant",
                "run": lambda: contains(root / "mcu-ci-toolchain" / "SKILL.md", "配置摘要"),
            },
            {
                "category": "automation",
                "name": "project structure checker exists",
                "run": lambda: ((root / "mcu-development-lifecycle" / "scripts" / "check_mcu_project.py").is_file(), "project checker present"),
            },
            {
                "category": "automation",
                "name": "audit script suite exists",
                "run": lambda: (
                    all(
                        (root / path).is_file()
                        for path in [
                            "mcu-development-lifecycle/scripts/check_mcu_project.py",
                            "mcu-development-lifecycle/scripts/check_skill_maturity.py",
                            "mcu-development-lifecycle/scripts/check_enterprise_pipeline.py",
                            "mcu-ci-toolchain/scripts/check_build_artifacts.py",
                            "mcu-team-collaboration/scripts/check_team_collaboration.py",
                        ]
                    ),
                    "audit script suite present",
                ),
            },
        ]
    )

    if len(checks) < 100:
        raise RuntimeError(f"internal audit definition must contain at least 100 checks, found {len(checks)}")
    return checks


def run_audit(root: Path) -> dict:
    results = []
    for index, check in enumerate(build_checks(root), start=1):
        passed, detail = check["run"]()
        results.append(
            {
                "id": index,
                "category": check["category"],
                "name": check["name"],
                "passed": bool(passed),
                "detail": detail,
            }
        )
    passed = sum(1 for item in results if item["passed"])
    return {
        "root": str(root),
        "total": len(results),
        "passed": passed,
        "failed": len(results) - passed,
        "score_percent": round(passed * 100 / len(results), 1),
        "results": results,
    }


def print_text(report: dict) -> None:
    print(f"MCU skill maturity audit: {report['root']}")
    print(f"Score: {report['passed']}/{report['total']} ({report['score_percent']}%)")
    failures = [item for item in report["results"] if not item["passed"]]
    if not failures:
        print("All checks passed.")
        return
    print()
    print("Failures:")
    for item in failures:
        print(f"  {item['id']:03d}. [{item['category']}] {item['name']}: {item['detail']}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit the MCU skill library with maturity checks.")
    parser.add_argument("skills_root", nargs="?", default=".", help="Path to the skill library root")
    parser.add_argument("--json", action="store_true", help="Print JSON")
    parser.add_argument("--strict", action="store_true", help="Return nonzero if any check fails")
    args = parser.parse_args()

    root = Path(args.skills_root).resolve()
    if not root.is_dir():
        parser.error(f"not a directory: {root}")

    report = run_audit(root)
    if args.json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        print_text(report)
    return 1 if args.strict and report["failed"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
