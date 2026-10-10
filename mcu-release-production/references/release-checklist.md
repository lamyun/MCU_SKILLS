# MCU Release Checklist

Use this reference for firmware release candidates, production releases, and field-update packages.

## Release Inputs

- Source revision and clean build status.
- Toolchain version and SDK/HAL/RTOS version.
- Board revisions supported.
- Build configuration and feature flags.
- Linker script, startup file, memory map, boot settings.
- Security settings, option bytes, fuses, readout protection.

## Artifacts

Include as applicable:

- `.bin`, `.hex`, `.elf`, `.map`, symbols, disassembly if needed.
- Artifact hashes.
- Signing metadata.
- Bootloader and application compatibility matrix.
- Release notes.
- Known issues and risk acceptance.
- Test reports.
- Production programming instructions.

## Release Tests

- Build reproducibility or controlled build evidence.
- Unit and integration summary.
- HIL/regression summary.
- Upgrade, rollback, and recovery tests if applicable.
- Long-run or stress tests for high-risk products.
- Factory programming and test dry run.

## Approval Questions

- Can another machine rebuild the same release from documented inputs?
- Can manufacturing program, identify, test, and rework units?
- Can field support identify the running version and collect diagnostics?
- Can users recover from a failed update or interrupted power event?
- Are all residual risks assigned to named approvers?

## MCU-PC 发布输入

- 固定并哈希 protocol/payload schema、PC collector、JSONL schema、SQLite schema/migration、replay tool 和 compatibility matrix。
- 证明 transactional migration/recovery、保留 capture 的 deterministic replay，以及未知 protocol major 的 fail-closed 行为。
- 分别声明 `host-verified`、`target-observed` 和 `real-hardware-hil` 范围。
