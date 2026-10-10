---
name: mcu-ci-toolchain
description: "厂商与型号无关的 MCU CI、工具链与自动化 Skill，覆盖环境自动发现、标准化交叉编译、CMake/Make/IDE 工程、SDK/HAL/RTOS 版本、生成漂移、并行 lane 隔离、Host 遥测测试、固件制品、HIL 触发、发布证据和团队可复现构建，并按项目条件路由 STM32CubeMX、Keil MDK、ESP-IDF 等平台工作流。用于创建、审计、优化或排查 MCU 构建系统、CI、工具链清单和自动化流程。"
---

# MCU CI 工具链

默认不预设 MCU 厂商、系列、具体型号、封装、开发板或工具链。从用户输入、受控 board profile 和现有项目文件解析目标；缺失时明确标为待确认，示例平台只能按条件选用。

## 概览

使用本技能把“个人电脑能编过”升级为“团队和 CI 都可复现”。优先固定工具链、构建入口、检查项、制品命名和失败诊断。

## 构建基线

每个 MCU 项目至少明确：

- 编译器、链接器、SDK/HAL、RTOS、代码生成器、烧录工具版本。
- 支持的 board target、MCU 型号、硬件版本和构建配置。
- 唯一推荐构建入口，例如 `cmake --build`、`make`、`west build` 或团队脚本。
- 输出制品：`elf`、`bin`、`hex`、`map`、符号、size 报告、构建日志。
- 可复现构建要求：输入版本、配置、环境变量、生成代码策略。

## CI 流程

1. 先跑快反馈：格式、lint、编译、size budget、host unit tests。
2. 再跑目标相关检查：静态分析、target integration、仿真或硬件烟测。
3. 对关键分支跑 HIL、回归、发布包生成和证据归档。
4. 每个失败都输出可定位信息：命令、target、工具版本、日志路径、制品路径。
5. 把构建、测试和发布证据连接到提交、需求或缺陷。

## 必需检查

- Build matrix 覆盖支持的 board、bootloader/app、debug/release、安全配置。
- 编译 warning 策略明确；新增 warning 不能被静默吞掉。
- Flash/RAM/stack/heap 或 section size 有阈值和趋势记录。
- 生成代码、配置文件、链接脚本、启动文件变更会触发审查。
- Unit tests 和 host tests 能在无硬件环境运行。
- HIL tests 有硬件资源锁、超时、日志和失败保全。

## CubeMX、Host 与 Lane 门禁

- 选择平台前调用 `mcu_mcp.detect_embedded_tools`。选中的 `stm32`、`keil_mdk` 或 `esp_idf` 必须为 `complete`；未选择平台的不完整环境只作为清单告警。
- 在工具链 manifest 中保留组件 path、version、discovery source、环境状态和缺失项。软件发现不等于许可证、构建、目标板、烧录、HIL 或发布证据。
- Keil 至少需要 μVision 与 ARMCLANG，或明确声明的遗留 ARMCC；固定 target、Pack、工程/scatter 输入、批构建日志和 AXF/HEX/MAP 输出。发现阶段许可证保持 `not-checked`，直到真实批构建成功。
- ESP-IDF 需要 framework、`tools/idf.py`、Python、CMake、Ninja，以及 Xtensa/RISC-V 编译器之一。只有工具没有 framework 时必须是 `partial`。固定 framework revision、target、sdkconfig、dependency lock、bootloader/partition/app 制品，并禁止 flash/monitor 上传目标。

- 固定 CubeMX、项目所选 STM32 firmware package、`.ioc`、生成参数、target/variant、可选 RTOS 模式和输出树摘要；在 lane 私有临时树 clean regenerate，无法解释的 generated drift 必须失败。
- 每个 lane 使用独立 source worktree/workspace、build、temporary、log、evidence、SQLite 和 test-result 路径；并发 job 禁止复用可变 build directory。
- 快速门禁在无硬件环境运行 protocol parser、malformed-frame、reconnect/backpressure、JSONL、SQLite-WAL migration 和 deterministic replay 测试。
- 制品贯穿 `project_id`、`change_id`、`lane_id`、variant、build/run ID、tool/schema version 和 hash；硬件 job 额外需要独占 board/port/probe lease 和受控 operation correlation。
- 分别报告 `generated`、`built`、`host-verified`、`target-observed` 和 `real-hardware-hil`；禁止提升 mock/replay/serial smoke test。
- configure/build/ingest 前解析并校验已登记 lane；拒绝未知 lane、change/variant/workspace 不一致、共享可写源码根、共享数据库和 lane 契约外的调用方自选输出。
- `run_project_step` 仅用于不接触目标的步骤，所有 profile 都拒绝 `upload`；只有真实 approval、板卡身份、artifact hash、team audit 和资源 lease 通过后，才能经 `run_hardware_workflow` 烧录。

## 自动化风格

- 用脚本封装复杂命令，但保留底层命令可见性。
- 脚本参数必须显式：target、config、toolchain、output、clean。
- CI 不依赖开发者本机绝对路径。
- 下载 SDK 或工具链时记录 checksum 或版本来源。
- 生产和发布脚本比开发脚本更保守，默认 dry-run 或明确确认。

## 可执行工程门禁

涉及硬件或发布时，调用 `$mcu-development-lifecycle` 并读取 `references/executable-engineering-gates.md`。把 `run_engineering_gates` 设为 CI 必需任务，归档 JSON 报告和哈希；只接受校验通过的真实硬件 HIL manifest，mock sidecar 结果只能验证编排。

把生命周期 Skill 的 `team-workspace-contract.md` 作为 CI 策略输入。构建前解析活动变更和产品变体，记录工具链摘要、源码版本、配置摘要、产物哈希、测试范围、例外、请求人、独立审批和来源证明；拒绝未声明变体、无负责人或过期例外、可变工具链引用，以及属于其他变更的证据。

## 跑中改进交接

流程执行中出现门禁误通过、可重复故障、反复人工绕行、目录混放或实际工具面与本 Skill 不一致时，调用 `$mcu-continuous-improvement`。项目专有证据保存在 lane 运行目录；只有已复现并有回归保护的通用模式才提升到中央持续改进 Skill。

## 参考资料

## PDF 证据门禁

CI 或发布输入依赖原理图/手册 PDF 时，必须存在由 `$mcu-datasheet-extraction` 生成且通过的 `mcu-pdf-dual-verification` manifest。门禁中重新调用 `inspect_pdf_evidence`，归档 manifest；哈希失效、Codex PDF 页覆盖不全或存在未解决差异时必须失败。

读取 `references/ci-pipeline.md` 了解流水线结构；读取 `references/toolchain-manifest.md` 了解环境和发布可复现字段。选择 STM32、Keil MDK 或 ESP-IDF 前读取 `references/multi-vendor-environment-workflow.md`。CubeMX 或数据流变更还要读取 `$mcu-firmware-development` 的 `references/stm32cubemx-rtos-workflow.md`、`$mcu-rtos-drivers` 的 `references/hardware-pc-data-flow-contract.md` 和 `$mcu-team-collaboration` 的 `references/parallel-workspace-lanes.md`。

## 脚本

使用 `scripts/check_build_artifacts.py <build-or-release-dir>` 检查 MCU 构建输出、哈希、map/size 证据和发布就绪提示。
