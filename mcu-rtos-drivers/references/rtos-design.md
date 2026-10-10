# MCU RTOS Design

Use this reference when designing or reviewing an RTOS-based MCU application.

## Task Table

| Task | Responsibility | Trigger | Period/deadline | Priority | Stack budget | Blocks on | Watchdog role |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Priority Rules

- Assign priority from timing need, not perceived importance.
- Keep fast hardware service tasks above slow business tasks.
- Avoid long-running work in high-priority tasks.
- Identify priority inversion risks where a high-priority task waits on a low-priority owner.
- Confirm interrupt priorities are compatible with RTOS API restrictions.

## Communication Patterns

- Use queues for ownership transfer.
- Use event flags for state notification without payload.
- Use mutexes only around short critical sections.
- Prefer a single owner task for each peripheral, bus, or mutable subsystem state.
- Avoid global flags without ownership and memory ordering notes.

## Timing Budget

Capture:

- Worst-case interrupt latency.
- Longest critical section.
- Longest scheduler lock or interrupt disable time.
- Task execution time and jitter.
- Queue depth under peak load.
- Stack high-water mark after stress tests.

## Watchdog Strategy

- Do not feed watchdog from a timer ISR that ignores task health.
- Use per-task heartbeats or progress counters for critical tasks.
- Define what data is saved before watchdog reset.
- Test intentional deadlock or starvation scenarios.

## Low Power

- Define which task owns sleep entry.
- Check all locks, DMA transfers, bus operations, and wake sources before sleep.
- Define resume order for clocks, GPIO, drivers, sensors, and communication links.
- Measure current with debugger detached when possible.
