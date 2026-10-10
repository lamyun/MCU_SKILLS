# MCU Phase Gates

Use this reference when planning, auditing, or reporting MCU project progress.

## Gate Format

Each gate should include:

- Phase name and gate ID.
- Entry criteria.
- Required evidence.
- Exit criteria.
- Open risks and accepted risks.
- Owner and approver.
- Next-phase blockers.

## G0 Concept

Entry:

- Product intent, business reason, and rough constraints exist.
- Target users, environment, and cost range are known or explicitly unknown.

Evidence:

- Product brief.
- Initial risk list.
- Candidate architecture notes.

Exit:

- Project scope and non-goals are clear.
- Major unknowns have owners.

## G1 Requirements Baseline

Entry:

- Product scenarios and stakeholders are identified.
- Hardware, firmware, manufacturing, and test stakeholders can review.

Evidence:

- Requirements table with stable IDs.
- Acceptance criteria for must-have requirements.
- Initial requirement-to-test traceability.

Exit:

- Must-have requirements are measurable.
- Ambiguous requirements are either resolved or tracked as risks.

## G2 Architecture And MCU Selection

Entry:

- Requirements baseline exists.
- Key interfaces and performance constraints are known.

Evidence:

- MCU selection matrix.
- Datasheet fact packet with exact device/package, source revision, and high-risk constraints.
- Resource budget.
- System block diagram.
- Interface contracts.
- Architecture decision records.

Exit:

- Selected MCU and critical external ICs are justified.
- Resource margin is acceptable or explicitly risk-accepted.

## G3 Hardware Design Review

Entry:

- Schematic and preliminary PCB constraints exist.
- Pinout, clock, power, boot, reset, and debug choices are available.

Evidence:

- Schematic review checklist.
- Source-anchored pin mux table.
- Power tree.
- Clock tree.
- BOM risk review.

Exit:

- Critical hardware risks are closed or mitigated.
- Bring-up test points and debug access are preserved.

## G4 Board Bring-up

Entry:

- Prototype boards, BOM, and schematic/PCB versions are recorded.
- Bring-up plan and measurement equipment are ready.

Evidence:

- Power rail measurements.
- Clock/reset/debug validation.
- Minimal firmware logs.
- Peripheral smoke test results.

Exit:

- Board can boot, be programmed, and run minimal diagnostics.
- Hardware issues have workaround or re-spin decisions.

## G5 Firmware Feature Complete

Entry:

- Board baseline is usable.
- Firmware architecture and coding rules are agreed.

Evidence:

- Implemented feature list.
- Module interfaces.
- Build logs.
- Static analysis or review results.
- Integration test results.

Exit:

- Required features are implemented.
- Known defects are triaged.
- Test team can run release-candidate validation.

## G6 Verification Complete

Entry:

- Release candidate is built reproducibly.
- Test plan and traceability matrix are current.

Evidence:

- Unit, integration, HIL, regression, and acceptance reports.
- Defect summary.
- Coverage notes for high-risk requirements.
- Long-run and fault-injection records where applicable.

Exit:

- Blocking defects are closed.
- Residual risks are accepted by the right owner.

## G7 Release And Production Readiness

Entry:

- Release candidate passed verification.
- Manufacturing process and tooling are ready.

Evidence:

- Release package with firmware images, hashes, map/elf/symbols, build logs.
- Programming and calibration instructions.
- Factory test procedure.
- OTA or field update evidence, if applicable.

Exit:

- Production can program, test, identify, and recover units.
- Field support has version, diagnostic, and rollback guidance.

## G8 Post-release Learning

Entry:

- Product has shipped to production, pilot, field trial, or customer validation.
- Production and field feedback channels are active.

Evidence:

- Field defects, production yield, update success rate, support cases, and returned-unit analysis.
- CI/test gaps linked to escaped defects.
- Updated requirements, diagnostics, tests, release notes, or production procedures.

Exit:

- Escaped defects have root cause and preventive action.
- Standards, skills, templates, or scripts are updated where the escape revealed a process gap.
