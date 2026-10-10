# MCU Review And Handoff Templates

Use this reference for cross-team reviews, handoffs, and closure evidence.

## Review Finding

```text
Finding ID:
Review:
Version reviewed:
Area:
Finding:
Impact:
Recommendation:
Owner:
Due:
Verification:
Status:
Evidence:
Verifier:
Closure date:
```

## Decision Record

```text
Decision ID:
Context:
Options considered:
Decision:
Reason:
Impact:
Risk accepted:
Rollback condition:
Owner:
Date:
```

## Change Request

```text
Change ID:
Class: C0 / C1 / C2 / C3 / C4
Requester:
Affected artifacts:
Affected teams:
Reason:
Risk:
Required reviews:
Test impact:
Release impact:
Decision:
Evidence:
```

## 并行 Lane 交接

```text
Lane ID:
Project/change ID:
Owner and role:
Branch/workspace:
Owned and changed paths:
Private build/evidence roots:
Source、.ioc、generator、schema 和 artifact hashes:
Commands and test results:
Leases held/released:
Open risks and next owner:
Integration/regeneration required:
```

## Exception Record

```text
Exception ID:
Gate or rule:
Reason:
Impact:
Compensating control:
Owner:
Approver:
Expiry:
Closure evidence:
```

## Hardware To Firmware Handoff

```text
Board revision:
Schematic/PCB/BOM version:
MCU and external ICs:
Power rails:
Clock sources:
Reset and boot settings:
Debug connector:
Pin mux table:
Known hardware issues:
Bring-up evidence:
Firmware constraints:
```

## Firmware To Test Handoff

```text
Firmware version:
Source revision:
Board target:
Implemented requirements:
Known limitations:
Build artifacts:
Configuration:
Diagnostics/logging:
Test hooks:
Risk areas:
```

## Test To Release Handoff

```text
Release candidate:
Test scope:
Environment:
Passed tests:
Failed tests:
Flaky tests:
Untested risks:
Defects:
Evidence links:
Release recommendation:
```

## Release To Production Handoff

```text
Release version:
Artifacts and hashes:
Supported hardware:
Programming procedure:
Calibration procedure:
Factory test:
Security/lock settings:
Rollback/rework:
Known issues:
Support notes:
```

## Post-release Learning

```text
Issue:
Detected by:
Escaped from phase:
Root cause:
Missing control:
Updated requirement:
Updated test:
Updated diagnostic:
Updated process or skill:
Owner:
Due:
Evidence:
```
