# MCU Safety Analysis

Use this reference for MCU safety reviews, FMEA-like analysis, and reliability controls.

## Safety Item Table

| Item | Function | Failure mode | Cause | Effect | Detection | Mitigation | Verification | Owner |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Hazard Analysis Prompts

- What can the device do that could harm a user, machine, process, product, or environment?
- What if a sensor is stuck high, stuck low, noisy, missing, delayed, or out of range?
- What if an actuator is stuck on, stuck off, reversed, slow, or disconnected?
- What if communication is lost, delayed, replayed, corrupted, or flooded?
- What if storage is corrupted, blank, old, or partially written?
- What if power drops during boot, operation, calibration, or update?
- What if the MCU resets repeatedly or does not reset when needed?

## Safety Controls

Common MCU controls:

- Watchdog based on task progress.
- Brown-out reset and reset-reason logging.
- Plausibility checks for sensors.
- Output safe defaults at reset and fault.
- Fault counters with latching or rate limits.
- Redundant measurement or cross-check where risk justifies it.
- Timeout on every blocking hardware interaction.
- Safe-state transition and recovery policy.
- Manufacturing test for safety-critical I/O.

## Verification Evidence

Use a mix of:

- Unit tests for state transitions and bounds.
- Fault injection for sensor, bus, memory, and power faults.
- HIL tests for actuator safe state and timing.
- Long-run tests for watchdog and resource leaks.
- Review evidence for safety-related code paths.

## Safety Case Summary

```text
Safety goal:
Hazard:
Risk level:
Controls:
Verification:
Residual risk:
Approver:
```
