# MCU Artifact Templates

Use these compact templates when creating project documents or review outputs.

## Requirement Row

| Field | Value |
| --- | --- |
| ID | REQ-DOMAIN-NNN |
| Statement | The system shall... |
| Rationale | Why this matters |
| Priority | must / should / could / defer |
| Acceptance | Measurable pass/fail criteria |
| Verification | inspection / analysis / unit / integration / HIL / acceptance |
| Owner | Person or team |
| Status | draft / reviewed / baseline / changed |

## Architecture Decision Record

```text
ADR-NNN: Title
Status: proposed / accepted / superseded
Context:
Decision:
Alternatives:
Consequences:
Rollback or migration:
Evidence:
```

## Risk Row

| Field | Value |
| --- | --- |
| ID | RISK-NNN |
| Risk | What may happen |
| Cause | Why it may happen |
| Impact | Cost, schedule, safety, quality, production |
| Probability | low / medium / high |
| Mitigation | Preventive action |
| Contingency | Recovery action |
| Verification | How mitigation is proven |
| Owner | Person or team |
| Status | open / watching / mitigated / accepted / closed |

## Datasheet Fact Row

| Field | Value |
| --- | --- |
| Fact ID | DS-NNN |
| Source document | Datasheet / reference manual / errata title and revision |
| Page / section / table | Evidence anchor |
| Device / package | Exact applicability |
| Raw value | Value exactly as stated |
| Normalized value | Engineering-ready value and unit |
| Conditions | Voltage, temperature, clock, load, mode, or silicon revision |
| Impact | Requirement, hardware, firmware, timing, test, or production implication |
| Confidence | high / medium / low |

## Test Case

```text
Test ID:
Linked requirements:
Level: unit / integration / HIL / regression / acceptance
Risk covered:
Preconditions:
Steps:
Expected result:
Pass/fail threshold:
Evidence to save:
Automation command:
```

## Release Summary

```text
Release:
Source revision:
Toolchain:
Hardware compatibility:
Build configuration:
Artifacts and hashes:
Tests run:
Known issues:
Production notes:
Rollback notes:
Approvals:
```

## RACI Row

| Deliverable | Responsible | Accountable | Consulted | Informed |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## Review Finding

```text
Finding ID:
Review area:
Artifact/version reviewed:
Finding:
Impact:
Recommendation:
Owner:
Due:
Verification evidence:
Status:
```

## Handoff Summary

```text
From team:
To team:
Artifact/version:
Verified evidence:
Known gaps:
Risks transferred:
Constraints for next team:
Fallback contact:
```

## Safety Or Security Control

| Control ID | Requirement | Risk/threat | Design control | Implementation | Verification | Release/production evidence |
| --- | --- | --- | --- | --- | --- | --- |
