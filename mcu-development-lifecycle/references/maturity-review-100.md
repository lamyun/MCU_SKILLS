# MCU 100-Point Maturity Review

Use this reference to review whether the MCU skill set and a project workflow have moved from usable to team-ready. Score each item as `0` missing, `1` partial, or `2` strong evidence.

## Lifecycle Governance

1. Project scope, non-goals, owners, and milestones are documented.
2. Phase gates have entry criteria, exit criteria, and evidence requirements.
3. Risks have owners, mitigation, verification, and acceptance rules.
4. Architecture decisions record context, alternatives, impact, and rollback.
5. Requirements, design, code, test, and release evidence are traceable.
6. Hardware, firmware, test, production, and field support handoffs are defined.
7. Toolchain, SDK, HAL, RTOS, and build scripts are controlled inputs.
8. Release candidates have reproducible build evidence.
9. Lessons from defects feed back into tests and standards.
10. Team metrics expose blockers, escapes, flaky tests, and late changes.

## Requirements And Architecture

11. Product goals are converted into measurable requirements.
12. Functional and non-functional requirements are separated and prioritized.
13. Real-time, power, storage, communication, safety, and manufacturing constraints are explicit.
14. Each must-have requirement has acceptance criteria.
15. MCU selection uses a comparison matrix, not only preference.
16. Flash, RAM, CPU, timer, DMA, IRQ, and pin margins are estimated from source-anchored device facts.
17. Runtime modes include boot, init, normal, low-power, fault, service, and update.
18. Interface contracts define electrical, protocol, timing, ownership, and recovery behavior.
19. Persistent data formats are versioned and migration is planned.
20. Architecture risks are reviewed before PCB and firmware commitments.

## Hardware And Bring-up

21. Power tree, sequencing, brown-out, and reset interactions are reviewed.
22. Clock tree, oscillator layout, RTC, and fallback clock behavior are reviewed.
23. Boot pins, debug pins, option bytes, and programming access are verified.
24. Pin mux choices avoid reset, boot, and debug conflicts and cite the relevant datasheet or reference-manual source.
25. Analog references, ADC ranges, filtering, and source impedance are reviewed.
26. Communication interfaces include termination, pull-ups, ESD, polarity, and recovery plans.
27. Test points and measurement access exist for high-risk signals.
28. First-power procedure includes current limits and stop conditions.
29. Bring-up records board ID, BOM, measurements, firmware version, and evidence.
30. Hardware issues are linked to firmware workarounds or re-spin decisions.

## Firmware Architecture

31. Firmware layers separate platform, BSP, drivers, middleware, and application logic.
32. Lower layers do not call product-specific application policy.
33. Public module APIs define lifecycle, context, timing, errors, and ownership.
34. All blocking operations have timeout and failure paths.
35. Error handling preserves root-cause data before reset or recovery.
36. Configuration and calibration data have defaults, validation, and versioning.
37. Watchdog strategy checks real progress, not only a timer tick.
38. Build metadata identifies target, version, configuration, and source.
39. Code review focuses on initialization, concurrency, overflow, bounds, and low-power behavior.
40. New features include diagnostics and test hooks appropriate to risk.

## RTOS And Drivers

41. Every task has responsibility, trigger, priority, stack budget, and watchdog role.
42. Task priorities are based on timing and resource ownership.
43. Shared mutable state has a clear owner or synchronization rule.
44. Queues, events, mutexes, and critical sections have bounded behavior.
45. ISR code is minimal and compatible with RTOS priority rules.
46. DMA buffers define alignment, lifetime, cache behavior, and completion ownership.
47. Bus drivers centralize arbitration, timeout, and recovery.
48. Driver APIs state task/ISR/callback safety.
49. Driver diagnostics expose state, last error, and counters.
50. Stress tests cover queue overflow, timeout, cancel, and bus fault recovery.

## Verification And Test

51. Test strategy maps requirements to unit, integration, HIL, regression, and acceptance levels.
52. High-risk behavior has normal, boundary, fault, and recovery test cases.
53. Unit tests cover algorithms, parsers, state machines, and parameter validation.
54. Integration tests cover drivers, RTOS interactions, boot, storage, and reset.
55. HIL tests record firmware, board, fixture, instrument, and raw evidence.
56. Every fixed defect adds a regression test or documented equivalent.
57. Flaky tests are classified instead of hidden.
58. Release test reports list scope, environment, pass/fail, gaps, and residual risk.
59. Production tests distinguish programming, hardware, calibration, and firmware failures.
60. Test evidence is retained by firmware version and board revision.

## Debug And Optimization

61. Fault handlers capture PC, LR, SP, xPSR, fault registers, and active context where possible.
62. Reset reason and post-reset breadcrumbs are available.
63. Hangs and watchdog resets can identify task progress and blocking resources.
64. Memory corruption checks include stack, DMA, buffers, persistence, and concurrent writers.
65. Communication failures collect electrical, protocol, timeout, and buffer evidence.
66. Optimization starts with baseline metrics and repeatable measurement.
67. Timing paths use trace, GPIO timestamp, cycle counter, or analyzer evidence.
68. Power measurements separate boot, active, idle, sleep, and wake behavior.
69. Flash, RAM, stack, heap, and section sizes are tracked over time.
70. Optimizations include regression evidence and documented tradeoffs.

## CI, Toolchain, And Automation

71. Toolchain manifest pins compiler, SDK/HAL, RTOS, code generator, and programmer tools.
72. Build scripts do not depend on developer-specific absolute paths.
73. CI has fast branch checks and deeper release/nightly checks.
74. Build matrix covers supported boards, configs, and bootloader/application variants.
75. Static analysis, formatting, warnings, and generated-code drift are checked.
76. Size budgets detect Flash/RAM regressions.
77. Host tests run without hardware.
78. HIL jobs have board locks, timeouts, reset/power control, and evidence capture.
79. Build artifacts include elf, map, bin/hex, logs, hashes, and manifest.
80. CI failures show exact commands, versions, target, config, and log paths.

## Safety, Security, And Compliance

81. Safety hazards and failure modes are documented.
82. Safety state, degraded behavior, recovery, and user/service intervention are defined.
83. Safety controls are linked to requirements, design, implementation, and tests.
84. Watchdog, brown-out, plausibility checks, and safe outputs are tested.
85. Threat model identifies assets, interfaces, threats, impact, controls, and verification.
86. Secure boot or image verification is considered for updateable products.
87. Debug access, readout protection, option bytes, and lock-down order are controlled.
88. Keys, serial numbers, calibration, and customer configuration have traceable handling.
89. OTA/update covers authentication, integrity, power loss, compatibility, and rollback.
90. Compliance evidence includes traceability, reviews, tests, tools, dependencies, and production records.

## Team Collaboration And Release

91. RACI assigns responsible and accountable owners for each major deliverable.
92. Review findings include impact, owner, due date, verification, and evidence.
93. Hardware-to-firmware handoff includes pin mux, power, clocks, reset, debug, and known issues.
94. Firmware-to-test handoff includes version, requirements, diagnostics, test hooks, and risk areas.
95. Test-to-release handoff includes scope, failures, flaky tests, untested risks, and recommendation.
96. Release-to-production handoff includes artifacts, hashes, programming, calibration, security, and recovery.
97. Change control covers MCU, pins, clocks, storage layout, bootloader, security, persistent data, and toolchain.
98. Production scripts, factory limits, and calibration formats are reviewed and versioned.
99. Field support can query version, hardware revision, serial number, config, and fault codes.
100. Post-release issues are triaged back into requirements, tests, diagnostics, CI, and release notes.
