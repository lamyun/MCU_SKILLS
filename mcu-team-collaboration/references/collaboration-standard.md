# MCU Collaboration Standard

Use this reference when standardizing how MCU teams coordinate work, reviews, handoffs, and evidence.

## Single Source Of Truth

Define one canonical location for each artifact. Avoid maintaining the same truth in chat, slides, spreadsheets, and code comments at the same time.

| Artifact | Recommended location | Owner | Update trigger |
| --- | --- | --- | --- |
| Project charter | `docs/project-charter.md` or `docs/governance/` | Project lead | Scope or milestone change |
| RACI | `docs/team/raci.md` | Project lead | Role or team change |
| Requirements | `docs/requirements/` | Product or systems owner | Requirement baseline or change |
| Architecture decisions | `docs/architecture/adr/` | System/firmware lead | Irreversible or cross-team decision |
| Pin mux and interface contract | `docs/architecture/` | System and hardware owners | Hardware or firmware interface change |
| Hardware review findings | `docs/hardware/` | Hardware lead | Schematic PCB BOM review |
| Firmware standards and module contracts | `docs/firmware/` | Firmware lead | Platform or interface change |
| Test plan and traceability | `docs/test/` | Test lead | Requirement or release scope change |
| Safety/security evidence | `docs/safety/` | Risk owner | Risk control or security change |
| Release package and notes | `docs/release/` and `releases/` | Release owner | Release candidate or hotfix |
| Production procedures | `tools/production/` and `docs/release/` | Manufacturing owner | Factory process or firmware package change |

## RACI Rules

- Every major artifact has exactly one accountable owner.
- Responsible contributors can be multiple, but closure authority must be clear.
- Consulted teams must be named for cross-boundary decisions.
- Informed stakeholders receive release-impacting changes and late risk updates.
- Vacant ownership is a blocker, not an administrative detail.

## Review Cadence

Use cadence as a safety net, not as meeting theater:

- Weekly risk review: open risks, blocked evidence, cross-team changes.
- Requirements review: before baseline and after any must-have change.
- Architecture review: before MCU, PCB, storage layout, boot/update, or RTOS commitment.
- Hardware review: before PCB release, after bring-up, and before production hardware freeze.
- Firmware review: for driver, bootloader, storage, RTOS, safety, security, and production-impacting changes.
- Test review: before feature complete, release candidate, and production readiness.
- Release review: before production, OTA, pilot, or customer delivery.
- Post-release review: after field escape, production yield issue, or major support incident.

## Change Classification

Classify every change by blast radius:

| Class | Examples | Required review |
| --- | --- | --- |
| C0 local | Internal implementation with no interface, timing, storage, or production impact | Normal code review |
| C1 module | Module API, driver behavior, diagnostics, or test hook change | Firmware owner and test owner |
| C2 cross-team | Pin mux, interface contract, timing, power, persistent data, build config | Affected hardware firmware test owners |
| C3 release-impacting | Bootloader, OTA, security settings, production script, calibration format, toolchain | Release, production, safety/security as applicable |
| C4 emergency | Field hotfix, production stop, safety/security issue | Incident owner, accountable approver, post-review required |

## Review Finding Closure

A finding is closed only when the reviewer can inspect evidence:

- Code diff, schematic diff, document update, test report, measurement, CI log, or release package.
- Owner and verifier are recorded.
- The same issue is not reopened without root cause.
- If closure is deferred, the exception has expiry and compensating control.

## Handoff Standard

Every handoff package must answer:

- What exact version is handed off?
- What is verified and where is the evidence?
- What is not verified and who accepts the risk?
- What constraints does the next team inherit?
- What tool, fixture, board, script, or config version is required?
- How does the next team report failure back to the owner?

## Decision Hygiene

- Use ADRs for decisions that affect more than one discipline.
- Decisions must include rejected alternatives and consequences.
- Do not bury decisions only in meeting notes or chat.
- Revisit decisions when assumptions fail, requirements change, or defects escape.

## Team Onboarding

A new engineer should find these without private explanation:

- Current board and firmware targets.
- Build and flash commands.
- Pin mux and interface contracts.
- Risk register and open review findings.
- Test strategy and HIL access rules.
- Release and production procedures.
