# MCU Architecture Template

Use this reference when creating MCU architecture documents, diagrams, or design reviews.

## Sections

1. Scope and assumptions.
2. Requirement summary and critical constraints.
3. MCU selection matrix and final choice.
4. System block diagram.
5. Power tree and power modes.
6. Clock tree and timing sources.
7. Memory map and storage layout.
8. Pin mux and interface allocation.
9. Firmware layers and module ownership.
10. Runtime modes and state machines.
11. Error handling, diagnostics, and watchdog strategy.
12. Bootloader, update, rollback, and security model.
13. Manufacturing, calibration, and test hooks.
14. Resource budget and margins.
15. Risks, open questions, and ADR links.

## Resource Budget Table

| Resource | Need | Available | Margin | Evidence | Risk |
| --- | --- | --- | --- | --- | --- |
| Flash |  |  |  | map estimate |  |
| RAM |  |  |  | static + stack estimate |  |
| CPU |  |  |  | timing estimate |  |
| Timers |  |  |  | pin/peripheral plan |  |
| DMA |  |  |  | transfer plan |  |
| IRQ priority |  |  |  | latency plan |  |

## Interface Contract

For each interface define:

- Electrical owner and connector or IC.
- Protocol and speed.
- MCU peripheral instance and pins.
- Direction and timing.
- Error detection and recovery.
- Test method and debug access.

## Architecture Review Questions

- Which choices are hard to reverse after PCB release?
- What margin exists for Flash, RAM, CPU, pins, DMA, timers, and interrupts?
- How does the system fail safely when a sensor, actuator, bus, or storage device fails?
- What behavior changes between boot, normal, low-power, fault, service, and update modes?
- How will production and field support identify firmware, hardware revision, and configuration?

## 数据平面契约

记录完整 ISR/DMA 到 PC collector 链路、资源预算、线协议/schema 版本、device/boot/time identity、CRC 与重新同步、queue/backpressure/reconnect、JSONL/SQLite-WAL ownership、replay determinism、correlation IDs、安全边界和证据等级。
