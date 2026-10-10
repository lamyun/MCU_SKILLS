# Project And Run Directory Contract

## Purpose

Separate mutable code, generated code, analysis, evidence, reports, and reusable learning so concurrent lanes do not overwrite one another and release evidence is not confused with working notes.

## Project-Level Layout

```text
project/
  analysis/
    00-intake/
    10-requirements/
    20-architecture/
    30-hardware/
    40-firmware/
    50-host-dataflow/
    60-verification/
    70-safety-security/
    80-release/
    90-retrospective/
  firmware/                 # for projects already using this wrapper layout
  host/
  tools/
  tests/
  configuration/
  governance/
  evidence/
    builds/
    host/
    telemetry/
    pdf/
    hardware/
    hil/
    release/
  reports/
  .mcu-mcp/
    lanes/
    locks/
    runs/
    improvements/
```

Keep native CubeMX flat-root trees in place when already established. In that case `Core`, `Drivers`, `Middlewares`, `.ioc`, startup, linker, and generated build descriptors remain firmware sources; do not wrap or move them without a separately reviewed migration.

## Per-Run Layout

```text
.mcu-mcp/runs/<run_id>/
  context/          # immutable IDs, inputs, versions, hashes
  analysis/         # run-local reasoning by domain, no source code
  build/            # manifests and links to lane-private build outputs
  tests/            # machine results and logs
  telemetry/        # capture/replay references, not shared databases
  hardware/         # governed operation references only
  evidence/         # hash manifests and indexes
  reports/          # gate and closure reports
  improvements/     # candidates originating in this run
  handoff/          # next action and unresolved blockers
  run-manifest.json
```

## Ownership Rules

- `analysis/` contains notes and derived findings, never compilable source or authoritative raw evidence.
- Firmware and host source live in their source trees or isolated lane workspace, never under `reports/` or `evidence/`.
- Build products live in a lane-private build directory; the run tree stores manifests and references.
- Raw captures are immutable and live under lane-private evidence. SQLite is a rebuildable index, not the only evidence.
- Reports are derived and can be regenerated. They never replace raw logs or manifests.
- Improvement candidates link to evidence by path and SHA-256. They do not duplicate raw logs.
- A release package consumes passing gate inputs and immutable artifacts only; it never includes unreviewed analysis notes as authority.

## Migration Rule

Create missing directories additively. First generate a proposed move map and hash inventory. Move existing content only through a governed change with owners, path compatibility checks, clean rebuild, replay, and rollback evidence.
