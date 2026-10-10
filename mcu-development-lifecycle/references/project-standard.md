# MCU Project Standard

Use this reference to standardize repository layout, naming, reviews, and lifecycle evidence.

## Repository Layout

Prefer this structure unless an existing project has a clear established convention:

```text
project/
  docs/
    governance/
    requirements/
    architecture/
    hardware/
    firmware/
    test/
    safety/
    team/
    release/
  hardware/
    schematics/
    pcb/
    bom/
    bringup/
  firmware/
    app/
    bsp/
    drivers/
    middleware/
    platform/
    include/
    tests/
  tools/
    scripts/
    production/
  tests/
    unit/
    integration/
    hil/
    regression/
  ci/
  releases/
```

## Naming

- Requirements: `REQ-<DOMAIN>-NNN`, for example `REQ-PWR-001`.
- Architecture decisions: `ADR-NNN-brief-title.md`.
- Risks: `RISK-NNN`.
- Test cases: `TC-<LEVEL>-NNN`, for example `TC-HIL-012`.
- Defects: use the team's tracker ID; include firmware version and board revision.
- Review findings: `REV-<AREA>-NNN`, for example `REV-HW-004`.
- Safety/security risks: `SAFE-NNN` and `SEC-NNN`.
- Enterprise exceptions: `EXC-NNN`.
- Release tags: prefer `fw-vMAJOR.MINOR.PATCH` plus hardware compatibility notes.

## Document Rules

- Every document must state scope, version, owner, and last review date.
- Every critical decision must include alternatives considered and rollback conditions.
- Every test report must include firmware version, board revision, equipment or environment, and raw evidence location.
- Every release package must include reproducibility data: source revision, toolchain, build config, generated artifacts, and hashes.
- Every handoff must include version, owner, verified evidence, unverified risk, and next-team constraints.
- Every safety/security control must trace to a requirement, implementation, verification evidence, and release or production setting.
- Every enterprise exception must include reason, blast radius, compensating control, approver, and expiry.

## Review Discipline

Use reviews to find integration risk, not just formatting issues:

- Requirements review: ambiguity, measurability, missing fault paths.
- Architecture review: resource margin, irreversible choices, manufacturability.
- Hardware review: power, clock, reset, boot, debug, pin mux, test points.
- Firmware review: concurrency, error paths, blocking calls, ownership boundaries.
- Test review: coverage of high-risk requirements and defects.
- CI/toolchain review: reproducibility, matrix coverage, warnings, size budget, artifact evidence.
- Safety/security review: hazards, threat model, debug lock, update integrity, risk acceptance.
- Release review: reproducibility, factory readiness, rollback, traceability.
- Team handoff review: owner, input quality, known gaps, and closure evidence.
- Enterprise gate review: evidence completeness, exception age, metric trend, and post-release feedback.

## Configuration Management

- Treat generated firmware images, linker scripts, boot settings, option bytes, calibration formats, and production scripts as controlled release inputs.
- Do not change compiler, linker, RTOS, SDK, HAL, or code generation settings without recording release impact.
- Keep board revision compatibility explicit in firmware configuration.
- Require explicit review for persistent data format, storage layout, bootloader, OTA, debug protection, and factory script changes.

## Quality Metrics

Track a small set consistently:

- Requirement coverage by test level.
- Defect escape rate and reopened defects.
- Firmware Flash/RAM usage and margin.
- Worst-case stack high watermarks.
- Boot time, key latency, and power-mode current.
- HIL pass rate and flaky test count.
- Production programming/test yield.
- CI pass rate, warning count, size trend, and build reproducibility failures.
- Open risks by age and owner.
- Exception count, exception age, and expired exceptions.
