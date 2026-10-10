# MCU Team Operating Model

Use this reference to establish team roles, review rhythms, and ownership for MCU projects.

## Core Roles

| Area | Typical owner | Key responsibilities |
| --- | --- | --- |
| Product/requirements | Product or systems owner | Scope, priorities, acceptance criteria |
| System architecture | System/firmware lead | MCU selection, interfaces, resource budgets |
| Hardware | EE lead | Schematic, PCB, BOM, bring-up evidence |
| Firmware platform | Firmware lead | Build, BSP, drivers, RTOS, coding standard |
| Application firmware | Feature owner | Product logic, state machines, diagnostics |
| Test/HIL | Test lead | Traceability, automation, HIL, regression |
| CI/tooling | Tools owner | Build reproducibility, CI, artifacts |
| Production | Manufacturing owner | Programming, calibration, factory tests |
| Safety/security | Risk owner | Safety case, threat model, compliance evidence |
| Release | Release owner | Version freeze, package, approvals, field notes |

## RACI Template

| Deliverable | Responsible | Accountable | Consulted | Informed |
| --- | --- | --- | --- | --- |
| Project charter |  |  |  |  |
| Requirements baseline |  |  |  |  |
| MCU selection |  |  |  |  |
| Schematic review |  |  |  |  |
| Pin mux and interface contract |  |  |  |  |
| Firmware architecture |  |  |  |  |
| Toolchain manifest |  |  |  |  |
| Test plan |  |  |  |  |
| Safety/security evidence |  |  |  |  |
| Release package |  |  |  |  |
| Manufacturing pack |  |  |  |  |
| Field support notes |  |  |  |  |

## Meeting Rhythm

- Weekly technical risk review: open risks, blockers, cross-team changes.
- Requirements/architecture review at baseline changes.
- Hardware review before PCB release and after bring-up.
- Firmware review for driver, boot, storage, safety, and concurrency changes.
- Test review before feature complete and release candidate.
- Release readiness review before production or field update.
- Post-release learning review after production escape, field incident, or repeated support issue.

## Team Metrics

Track:

- Open risks by age and owner.
- Requirements without tests.
- Defects without reproduction steps.
- CI pass rate and flaky tests.
- Review findings reopened.
- Release blockers and late requirement changes.
- Change requests by class and closure time.
- Handoff defects found by receiving team.

## Collaboration Rules

- Prefer decision records over repeated chat decisions.
- Keep pin tables, interface contracts, and resource budgets in versioned files.
- Require evidence for closing review findings.
- Keep production-impacting scripts under review.
- Treat handoff packages as inputs to the next team, not as archive paperwork.
- Treat missing ownership as a blocker.
- Close review findings only with inspectable evidence.
- Use explicit change classes for cross-team and release-impacting changes.
