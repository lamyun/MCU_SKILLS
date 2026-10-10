# MCU Enterprise Workflow

Use this reference when an MCU project needs enterprise-grade governance, repeatable delivery, and audit-ready evidence.

## Operating Principles

- One source of truth for requirements, architecture, pin tables, interfaces, risks, defects, tests, releases, and production records.
- Evidence over status: a gate passes because linked artifacts prove readiness.
- Changes are classified by blast radius, not by who requested them.
- CI and HIL are treated as production systems with ownership, observability, and recovery.
- Release packages are reproducible, traceable, supportable, and recoverable.
- Escaped defects update requirements, tests, diagnostics, automation, and standards.

## Enterprise Pipeline

1. Intake: capture scope, business goal, stakeholders, constraints, and product risk class.
2. Planning: create RACI, milestone plan, risk register, review schedule, and evidence map.
3. Requirements: baseline measurable requirements and verification strategy.
4. Architecture: approve MCU selection, resource budgets, interfaces, state modes, safety/security controls.
5. Hardware design: review schematic, PCB, BOM, debug access, test points, and bring-up plan.
6. Toolchain baseline: pin compiler, SDK/HAL, RTOS, code generator, build scripts, and programmer tools.
7. Firmware implementation: build layered firmware with module contracts, diagnostics, and test hooks.
8. CI automation: run matrix builds, warning checks, static analysis, host tests, and size budgets.
9. Board bring-up: capture power, clock, reset, debug, boot, and peripheral evidence.
10. Verification: run unit, integration, HIL, regression, stress, fault-injection, and acceptance tests.
11. Stabilization: debug faults, optimize timing/power/memory, and close reliability risks.
12. Release readiness: freeze scope, build artifacts, hashes, release notes, known issues, and approvals.
13. Production readiness: validate programming, calibration, factory test, serialization, security lock, and rework.
14. Field readiness: validate update, rollback, diagnostics, version query, fault codes, and support workflow.
15. Post-release learning: analyze production/field signals and update standards, tests, and skills.

## Gate Evidence Model

Every enterprise gate should include:

- Artifact version reviewed.
- Required evidence links.
- Open findings.
- Accepted risks.
- Exceptions and expiry.
- Owner and approver.
- Next gate dependencies.

## Exception Management

Use exceptions sparingly and make them visible:

- Exception ID.
- Requirement or gate being bypassed.
- Reason and impact.
- Compensating control.
- Expiry date or release limit.
- Approver.
- Verification plan to close it.

## Audit Trail

Keep records for:

- Requirement baselines and changes.
- Architecture decisions.
- Review findings and closure evidence.
- Toolchain manifests.
- CI/HIL logs.
- Release artifacts and hashes.
- Production programming and test results.
- Field issues and corrective actions.

## Enterprise Metrics

Track leading and lagging indicators:

- Requirements without tests.
- Resource margin trend.
- CI pass rate and warning trend.
- Static analysis findings by age.
- HIL pass rate and flaky tests.
- Defects by phase introduced and phase found.
- Release blockers by category.
- Production yield and rework causes.
- OTA/update success rate.
- Field failure rate and repeat root causes.
