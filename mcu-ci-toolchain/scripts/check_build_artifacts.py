#!/usr/bin/env python3
"""Inspect MCU build or release directories for expected artifacts."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


ARTIFACT_EXTS = {
    ".elf": "debug_symbols",
    ".map": "linker_map",
    ".bin": "binary_image",
    ".hex": "hex_image",
}

EVIDENCE_NAMES = [
    "build.log",
    "size.txt",
    "size-report.txt",
    "hashes.txt",
    "manifest.txt",
    "manifest.json",
    "release-notes.md",
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def inspect(root: Path) -> dict:
    files = [p for p in root.rglob("*") if p.is_file()]
    artifacts = {}
    for ext, label in ARTIFACT_EXTS.items():
        matched = sorted(str(p.relative_to(root)) for p in files if p.suffix.lower() == ext)
        artifacts[label] = matched

    evidence = {
        name: sorted(str(p.relative_to(root)) for p in files if p.name.lower() == name)
        for name in EVIDENCE_NAMES
    }
    missing_artifacts = [label for label, matched in artifacts.items() if not matched]
    missing_evidence = [name for name, matched in evidence.items() if not matched]

    image_hashes = {
        str(p.relative_to(root)): sha256(p)
        for p in files
        if p.suffix.lower() in {".bin", ".hex"}
    }

    return {
        "root": str(root),
        "artifacts": artifacts,
        "evidence": evidence,
        "image_hashes": image_hashes,
        "missing_artifacts": missing_artifacts,
        "missing_evidence": missing_evidence,
        "release_ready": not missing_artifacts and not missing_evidence,
    }


def print_text(result: dict) -> None:
    print(f"MCU build artifact audit: {result['root']}")
    print()
    print("Artifacts:")
    for label, files in result["artifacts"].items():
        print(f"  {label}: {len(files)}")
        for file in files[:5]:
            print(f"    - {file}")
    print()
    if result["missing_artifacts"]:
        print("Missing artifact classes:")
        for item in result["missing_artifacts"]:
            print(f"  - {item}")
    else:
        print("Artifact classes: OK")
    print()
    if result["missing_evidence"]:
        print("Missing evidence files:")
        for item in result["missing_evidence"]:
            print(f"  - {item}")
    else:
        print("Evidence files: OK")
    if result["image_hashes"]:
        print()
        print("Image hashes:")
        for name, digest in result["image_hashes"].items():
            print(f"  {name}: {digest}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit MCU build/release artifacts.")
    parser.add_argument("root", help="Build or release directory")
    parser.add_argument("--json", action="store_true", help="Print JSON output")
    parser.add_argument("--strict", action="store_true", help="Return nonzero if not release-ready")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    if not root.is_dir():
        parser.error(f"not a directory: {root}")

    result = inspect(root)
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print_text(result)

    if args.strict and not result["release_ready"]:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
