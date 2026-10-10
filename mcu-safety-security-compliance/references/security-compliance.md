# MCU Security And Compliance

Use this reference for threat modeling, secure update, production lock-down, and compliance preparation.

## Threat Model

| Asset | Interface | Threat | Impact | Control | Verification |
| --- | --- | --- | --- | --- | --- |

Common assets:

- Firmware image.
- Bootloader and update process.
- Keys and certificates.
- Calibration and serial number data.
- Customer configuration.
- Debug and production tools.
- Diagnostic logs.

## Security Controls

- Secure boot or verified boot for products that need image authenticity.
- Signed update packages and integrity checks.
- Anti-rollback if older firmware can reintroduce risk.
- Debug port lock or controlled unlock in production.
- Readout protection and option-byte policy.
- Key injection and storage process with traceability.
- Sensitive log redaction.
- Dependency and license inventory.

## OTA And Field Update

Review:

- Authentication and integrity.
- Power-loss behavior.
- Storage layout and free space.
- Rollback or recovery mode.
- Version compatibility.
- Update progress reporting.
- Failure telemetry.
- Factory reset and safe-mode interaction.

## Compliance Evidence

Keep:

- Requirement traceability.
- Architecture and threat model.
- Risk acceptance records.
- Static analysis and review results.
- Test reports and raw logs.
- Toolchain and dependency manifests.
- Production programming and lock-down records.

## Production Security Checklist

- Debug access policy approved.
- Readout protection set at the correct production step.
- Keys are not present in source control or logs.
- Programming scripts do not expose secrets in command history.
- Failed units can be reworked without weakening shipped-unit security.
- Field support can diagnose without unlocking unnecessary access.

## 遥测与 PC 命令控制

- 分配内存前对每帧限长和版本校验；畸形或不兼容流量不能饿死 control/watchdog task。
- CRC 仅检测损坏。改变状态的命令需要认证、授权、rate limit、审计，并按风险增加幂等或 anti-replay。
- 分类 JSONL/SQLite 内容，redact secret，控制 retention/access/export/deletion，并分离 replay/host 与真实硬件证据。
