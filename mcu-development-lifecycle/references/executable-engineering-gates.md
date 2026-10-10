# MCU 可执行工程门禁

当任务跨越文档、固件制品、调试目标、HIL、发布或生产安全时，使用本流程。`mcu-mcp` 是唯一公开 MCP 控制面；它把 `openocd-mcp` 作为私有目标执行 sidecar 启动。不要同时把两个服务配置为 Codex 公开 MCP。

## 控制顺序

1. 调用 `board_profiles`，选择 v2 规范板卡 profile。profile 被禁用、精确 MCU/封装/PCB/BOM 为 `UNCONFIRMED`、缺少目标名/IDCODE 或内存映射未确认时停止。
2. 所有来自 PDF 的硬件事实都必须执行 `$mcu-datasheet-extraction` 的 Poppler + Codex PDF 流程并调用 `inspect_pdf_evidence`。pending、fail、哈希失效或仍有差异时阻断。
3. 构建固件并保留 `.elf`、`.bin`、`.map`、构建配置、工具链身份、SBOM、签名元数据和 SHA-256。
4. 调用 `run_engineering_gates`，传入项目内的需求追踪、版本一致性、发布和生产安全输入文件。禁止用一个 HIL 布尔值替代真实 manifest。
5. 占用硬件前调用 `run_hardware_workflow(workflow="preflight")`。目标操作使用同一个 `operation_id` 串联 probe、flash、故障抓取、audit 和最终证据记录。
6. 首次连接使用 bring-up profile，只做读优先身份检查；发布使用独立 release profile，并强制 PDF 与真实 HIL 双门禁。精确身份字段确认前，两类 profile 都不得启用。
7. 调用 `run_hardware_workflow(workflow="probe", board_profile=..., confirm=true)`，烧录前比对 target name 和 IDCODE。flash 必须传 `project_path`、`artifact` 和预期固件 SHA-256，强制 verify，并显式决定 reset。
8. 故障后先保全原始寄存器和 trace。用准确且有哈希的 ELF 调用 `symbolize_firmware_addresses`，再用 `inspect_svd_register` 结构化解码外设、寄存器和位域。根据 profile 架构选择 Cortex-M 或 RISC-V snapshot。RTOS/RTT/SWO/ITM 不可用时记录 `UNAVAILABLE`，禁止伪造成通过证据。
9. 归档 audit/evidence。源码、生成代码、链接脚本、board profile、PDF、固件、治具、仪器、Option Bytes 或锁定方案变化后，重新执行全部受影响门禁。

## 真实 HIL Manifest

release 输入必须包含 `workspace_root` 内的 `hil_evidence.manifest`，并可固定其 SHA-256。被引用 manifest 必须使用：

```yaml
schema_version: 1
evidence_type: mcu-hil-verification
execution_mode: real-hardware
board:
  profile: board-release
  board_id: BOARD-ID
  pcb_revision: A
  bom_revision: 1
  serial_number: BOARD-0001
firmware:
  file: project/build/firmware.bin
  sha256: <64位小写十六进制>
fixture:
  id: fixture-id
  revision: 1
instruments:
  - id: scope-1
    model: model-name
tests:
  - id: HIL-001
    status: pass
    raw_evidence:
      - file: project/test-results/HIL-001.log
        sha256: <64位小写十六进制>
gate:
  status: pass
  passed: true
  reasons: []
```

校验器必须重算固件和原始证据哈希，并核对 profile、board ID、PCB revision、BOM revision 和序列号。Mock/仿真/MIL/SIL/PIL、摘要布尔值、没有哈希原始证据的截图或失效 manifest 都不能算真实 HIL。

## 必需门禁输入

- 需求追踪：每条需求含风险、设计、实现、验收准则、关联测试、状态及哈希固定证据。
- 版本一致性：项目 board ID、PCB/BOM、MCU 型号和封装与规范 profile 完全一致，且不含 `UNCONFIRMED`。
- 发布：`.elf`、`.bin`、`.map`、SBOM、已验证签名元数据、测试和 `hil_evidence` 齐全且哈希有效。
- 安全锁定：program、verify、provision identity、enable secure boot、set readout protection、lock debug、final verify 必须按该顺序出现，并包含负责人、命令、验证、回滚边界、状态和显式生产授权。

## 能力边界

`OPENOCD_MCP_MOCK=1` 只允许验证协议、编排、负向门禁和审计路径。输出必须标记为 `mock`，不得用来启用板卡 profile、通过 HIL、声称已连接探针/MCU、批准生产锁定或认定发布合格。保持 direct `flash_firmware` 和 `run_openocd_action` 禁用；它们只是兼容入口，不具备完整 sidecar 身份、哈希、硬件锁、证据和操作关联契约。
