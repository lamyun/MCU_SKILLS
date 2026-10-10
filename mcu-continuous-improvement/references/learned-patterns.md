# Curated MCU Learned Patterns

Only regression-verified, generalized patterns belong here. Project evidence remains in its project run tree.

## Governance

Pattern ID: `PAT-GOV-APPROVAL-CONSENSUS-001`
Trigger: 目标操作的全局审批人数满足要求，但审批分别覆盖不同 workflow，或 flash/telemetry 审批绑定不同固件。
Invariant: 独立身份 quorum 必须按同一目标 workflow 分别计算；flash 和 telemetry-capture 的批准必须对同一规范化固件 SHA-256 达成一致。
Regression: 拆分 workflow 的双人审批和不同制品哈希都必须使团队审计 blocked；同一 workflow、同一制品且满足独立身份数量时才可通过此控制。
Affected components: `mcu-mcp` 团队审计、协作 Skill、全生命周期 Agent。
Applicability: 所有目标硬件、flash、真实遥测、生产和发布审批；不改变请求人分离、有效期、variant、board profile 或 configuration hash 门禁。
Candidate and run IDs: `IMP-APPROVAL-CONSENSUS-001`, `RUN-G4-FINAL-003`.
Promoted source hash: `9f1576f0c0819b02a4732adda2cdbb68539002dec28fca408c8ce9640c09ca6d`.

## CubeMX

## Firmware

## RTOS

## Host Dataflow

## Build And CI

Pattern ID: `PAT-BUILD-MULTI-VENDOR-ENV-COMPLETENESS-001`
Trigger: 扁平可执行文件扫描发现部分厂商工具后，把 Keil MDK 或 ESP-IDF 误判为可构建环境，或本机安装布局不在 PATH 时错误报告未安装。
Invariant: 按配置、环境变量、PATH、Windows 注册表和有限常见目录的固定优先级发现组件；选中平台只有满足其完整组件集合时才为 `complete`。Keil 至少需要 μVision 和 ARMCLANG/ARMCC；ESP-IDF 必须同时有 framework、framework `tools/idf.py`、Python、CMake、Ninja 和 Xtensa/RISC-V 编译器之一。`auto` 只盘点，不完整的选中平台必须 blocked。
Regression: 隔离夹具分别覆盖完整 Keil、完整 ESP-IDF、仅 Espressif 工具但缺 framework 的 `partial`、配置优先级，以及选中不完整平台的 `SELECTED_PLATFORM_ENVIRONMENT_INCOMPLETE`。
Affected components: `mcu-mcp` 环境发现、CI/固件/持续改进 Skills、全生命周期 Agent 与 Codex 安装校验。
Applicability: STM32、Keil MDK、ESP-IDF 本机软件发现与可复现构建入口；软件存在不能提升为许可证、构建、板卡、烧录、串口、HIL 或发布证据。
Candidate and run IDs: `IMP-MULTI-VENDOR-ENV-DISCOVERY-001`, `RUN-G4-FINAL-003`.
Promoted source hash: `3f7fd5f68d5d702930d8431bdf10250d1bd5cb812b97e44b2f77132de155bf52`.

## Verification

## Hardware

## Safety And Security

## Release

## Collaboration

## Entry Format

```text
Pattern ID:
Trigger:
Invariant:
Regression:
Affected components:
Applicability:
Candidate and run IDs:
Promoted source hash:
```
