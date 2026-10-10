# MCU Requirements Template

Use this reference when drafting, cleaning, or reviewing MCU requirements.

## Requirement Categories

- Functional: product behavior visible to users or other systems.
- Performance: latency, sampling rate, control-loop timing, boot time, throughput.
- Power: active, idle, sleep, shutdown, wake source, battery life.
- Environmental: temperature, humidity, vibration, EMC-related behavior.
- Interface: electrical and protocol-level requirements.
- Safety/reliability: fault detection, fallback, watchdog, safe state.
- Security: debug access, authentication, encryption, secure boot, update trust.
- Manufacturing: programming, calibration, serial number, factory test.
- Service: diagnostics, logs, field update, configuration.

## Requirement Quality Rules

- Use one requirement per row.
- Make the statement measurable or pair it with measurable acceptance criteria.
- Avoid vague terms such as fast, low power, robust, stable, or user-friendly unless quantified.
- Include boundary and failure behavior for external inputs, sensors, communications, and storage.
- Assign priority and verification method before baselining.
- Link each must-have requirement to at least one test strategy.

## Requirement Table

| ID | Requirement | Rationale | Priority | Acceptance criteria | Verification | Owner | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| REQ-FUNC-001 |  |  | must |  | HIL |  | draft |

## Review Questions

- Can firmware and test teams implement and verify this without asking what it means?
- Does this requirement imply hardware resources that are not budgeted?
- Does the requirement define startup, shutdown, low-power, fault, and recovery behavior?
- Is calibration or manufacturing data required?
- Is the requirement still valid across supported hardware revisions?

## MCU-PC 需求字段

每条硬件到 PC 数据需求增加 source semantics/units、nominal/burst rate、latency/jitter/loss、queue/backpressure、disconnect/reconnect、protocol/schema 兼容窗口、host/storage/replay 行为、retention/privacy 分类和验收证据等级。
