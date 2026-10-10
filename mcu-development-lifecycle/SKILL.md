---
name: mcu-development-lifecycle
description: "厂商、芯片型号与 RTOS 无关的端到端嵌入式 MCU 生命周期 Skill，用于需求、架构、硬件、平台选择、项目声明 RTOS/驱动、MCU-PC 数据流、隔离并行 lane、验证、调试、发布和量产，并按项目证据路由条件化平台工作流。适用于项目规划、环境门禁、阶段门、交付物标准化、团队工作区、generated-code 治理、质量追踪和跨团队协同。"
---

# MCU Development Lifecycle

默认不预设 MCU 厂商、系列、具体型号、封装、开发板或工具链。从用户输入、受控 board profile 和现有项目文件解析目标；缺失时明确标为待确认，示例平台只能按条件选用。

## 概览

使用本技能把 MCU 项目拆成可管理的阶段、交付物、检查项、质量门和团队协作机制。任务只涉及单一阶段时，优先跳转到对应阶段技能；任务跨阶段或需要标准化管理时，先用本技能建立总控框架。

## 技能路由

按任务意图选择最小足够技能：

- 产品创意、市场对标、目标用户、MVP 范围、方案选型：调用 `$mcu-product-discovery`。
- 需求、选型、系统架构、接口预算：调用 `$mcu-requirements-architecture`。
- 芯片手册、参考手册、引脚表、复用功能、寄存器、电气和时序限制：调用 `$mcu-datasheet-extraction`。
- 原理图、PCB、上电、时钟、复位、下载口、外设硬件验证：调用 `$mcu-hardware-bringup`。
- 裸机固件、目录结构、编码规范、构建、外设初始化：调用 `$mcu-firmware-development`。
- RTOS、驱动框架、ISR、DMA、总线、并发、低功耗状态机：调用 `$mcu-rtos-drivers`。
- 单元测试、集成测试、HIL、回归、验收、追踪矩阵：调用 `$mcu-verification-test`。
- HardFault、死机、时序、内存、功耗、性能、可靠性优化：调用 `$mcu-debug-optimization`。
- 版本发布、量产烧录、校准、OTA、现场维护、变更控制：调用 `$mcu-release-production`。
- 构建系统、工具链、CI、静态分析、制品和自动化：调用 `$mcu-ci-toolchain`。
- 功能安全、网络安全、合规、认证、故障安全和生产锁定：调用 `$mcu-safety-security-compliance`。
- 团队角色、RACI、评审、交接、变更控制和协作治理：调用 `$mcu-team-collaboration`。
- STM32CubeMX `.ioc`、项目所选 STM32 系列、可选 RTOS 生成和 generated drift：调用 `$mcu-firmware-development` 与 `$mcu-ci-toolchain`。
- Keil MDK 或 ESP-IDF 环境/bootstrap：先调用 `$mcu-ci-toolchain` 并要求选中平台完整，再调用 `$mcu-firmware-development`。
- 版本化 MCU-PC 遥测、PC collector/persistence/replay：调用 `$mcu-requirements-architecture`、`$mcu-rtos-drivers`、`$mcu-verification-test`，并按风险调用 `$mcu-safety-security-compliance`。
- 并行 Codex/worktree、lane ownership 和资源租约：调用 `$mcu-team-collaboration` 与 `$mcu-ci-toolchain`。
- 运行中失败、重复绕行、目录分层、回归学习或跨项目模式提升：调用 `$mcu-continuous-improvement`。

## 生命周期流程

1. 完成产品发现：用户场景、市场对标、MVP 范围、方案评分、非目标和关键假设。
2. 建立项目章程：产品目标、边界、风险等级、约束、里程碑、负责人。
3. 固化需求基线：功能、性能、环境、安全、法规、制造、维护、可测试性。
4. 提取芯片手册事实：精确型号/封装、引脚复用、外设限制、寄存器、电气约束、时序限制和 errata。
5. 形成系统架构：MCU 选型、时钟/电源/存储/通信/安全/升级架构、接口预算。
6. 完成硬件协同：原理图评审、PCB 约束、BOM 风险、Bring-up 计划。
7. 搭建固件和工具链工程：目录、构建、CI、代码规范、配置管理、日志和错误处理。
8. 实现驱动和业务：分层接口、RTOS 任务、ISR/DMA、状态机、异常恢复。
9. 建立安全、合规和可靠性控制：故障安全、威胁模型、调试口策略、升级安全、证据追踪。
10. 建立验证闭环：需求追踪、测试计划、自动化、HIL、回归、缺陷管理。
11. 优化和稳定化：时序、内存、功耗、EMC 相关软件策略、长稳测试。
12. 发布和量产：版本冻结、制品签名、烧录/校准、生产测试、现场升级和回滚。
13. 维护和回溯：现场缺陷、生产良率、测试逃逸、CI 波动、版本影响分析和标准更新。

## 标准输出

每次输出尽量落到可执行项：

- 阶段目标、入口条件、退出条件、责任人、证据物。
- 风险清单：风险、影响、触发条件、缓解措施、验证方式、当前状态。
- 决策记录：背景、备选方案、选择、理由、影响、回滚条件。
- 产品发现包：市场对标、MVP 范围、非目标、方案评分、关键假设和验证实验。
- 芯片手册事实包：源文档版本、精确器件/封装、引脚复用表、外设/寄存器事实、电气和时序限制、errata 风险。
- 需求到测试追踪：需求 ID、设计项、实现模块、测试用例、结果、缺陷链接。
- 发布证据包：源码版本、工具链版本、配置、构建日志、测试报告、制品哈希。
- 团队协作包：RACI、评审记录、交接清单、变更记录、风险接受。
- 安全合规包：安全/威胁分析、控制项、验证证据、生产锁定记录。
- 上下文恢复包：`project_state.yaml`、`handoff.md`、`decision_log.md`、`run_history.jsonl`、`machine_index.json`。
- 维护回溯包：现场事件、影响版本、需求/测试/发布链接、根因、修复验证和复盘行动。
- 数据流证据包：protocol/collector/storage schema、JSONL/raw manifest、SQLite migration journal、replay hash、计数器和准确证据等级。
- 并行工作包：lane registry、路径所有权、租约、每 lane 构建/测试证据、集成重新生成和关闭交接。

## 项目结构基线

建议先按此结构落地，再根据项目裁剪：

```text
project/
  docs/
    product/
    requirements/
    architecture/
    hardware/
    firmware/
    test/
    safety/
    team/
    release/
    field/
  hardware/
    schematics/
    pcb/
    bom/
    bringup/
  firmware/
    app/
    bsp/
    drivers/
    middleware/
    platform/
    include/
    tests/
  host/
    protocol/
    collector/
    storage/
    replay/
    tests/
  configuration/
    boards/
    products/
    toolchains/
    cubemx/
    protocols/
  tools/
    scripts/
    production/
  tests/
    unit/
    integration/
    hil/
    regression/
  ci/
  releases/
```

## 平台环境、数据流与并行 Lane

把 `.ioc`、CubeMX/项目所选 STM32 firmware package 版本、可选 RTOS 设置、protocol/storage schema 和 lane registry 作为受控 variant 输入。任一变化都触发 impact routing、clean regeneration、generated-drift comparison、隔离重建、host regression 和下游证据刷新。

Keil 还要治理 `.uvprojx`、target、编译器、CMSIS-Pack、scatter 和批构建证据；ESP-IDF 治理 framework revision、`idf.py`、target、sdkconfig、dependency lock、partition/bootloader/application 制品和 lane 私有配置/构建输出。选中的 `stm32`、`keil_mdk` 或 `esp_idf` 环境必须为 `complete`，环境发现仍只是软件证据。

每个 build、test、capture、persistence、replay 和 hardware record 都携带 `project_id`、`change_id`、`lane_id`、variant、source/build/schema version、`run_id` 和 hash。物理操作额外保留 `approval_id` 和 `operation_id`。软件 lane 可以并行；`.ioc` generation 和 board/port/probe/fixture/instrument 必须只有一个未过期独占 lease。

使用证据阶梯 `generated -> built -> host-verified -> target-observed -> real-hardware-hil`，通过前一级绝不代表后一级通过。

## 公开控制面不变量

- `mcu_mcp` 保持唯一公开 MCU 控制面；只能通过受控硬件工作流访问私有 OpenOCD sidecar。
- `run_project_step` 只用于不接触目标的 configure/build/test，禁止 `upload`；目标烧录必须使用 `run_hardware_workflow`。
- 目标操作前校验真实 change、variant、带 scope 的 approval、独立审批人、有效期、artifact hash、team audit 和独占资源 lease；非空 ID 字符串不是证据。
- build、telemetry ingest 或发布证据前校验已登记 lane 和全部关联字段。共享可变源码根的非 Git lane 只能只读/构建，不能算隔离写入 lane。
- build、evidence、raw/JSONL、SQLite 和临时路径必须 lane 私有；拒绝调用方指定的共享 store 或属于其他 lane/change 的制品。

## 阶段门规则

不要让阶段门只成为会议结论。每个 gate 必须能回答：

- 已确认什么事实？
- 哪些证据支撑这些事实？
- 哪些风险被接受，谁接受，为什么可以接受？
- 下阶段如果失败，如何定位到责任交付物？

来源于 PDF 的硬件和器件事实只有在 `$mcu-datasheet-extraction` 将本地 Poppler 提取/渲染与 Codex PDF 视觉复核记录到未变更且通过的 `mcu-pdf-dual-verification` manifest 后，才可通过阶段门。pending、fail、不完整或哈希失效的证据必须保留为开放风险，不能升级为基线事实。

## 跑中改进交接

流程执行中出现门禁误通过、可重复故障、反复人工绕行、目录混放或实际工具面与本 Skill 不一致时，调用 `$mcu-continuous-improvement`。项目专有证据保存在 lane 运行目录；只有已复现并有回归保护的通用模式才提升到中央持续改进 Skill。

## 参考资料

按需要读取：

- `references/phase-gates.md`：完整阶段门、入口/出口、证据物。
- `references/project-standard.md`：项目目录、命名、文档、版本、评审规范。
- `references/artifact-templates.md`：需求、架构、风险、决策、测试、发布模板。
- `references/maturity-review-100.md`：100 项 MCU 全流程成熟度审查清单。
- `references/enterprise-workflow.md`：企业级 MCU 工作流水线、质量门、例外和审计证据模型。
- `references/team-workspace-contract.md`：团队标准目录、项目/变更/变体契约、职责分离、证据索引和变更驱动路由。
- `references/enterprise-review-500.md`：500 项企业级 MCU 流水线审查控制点。
- `references/executable-engineering-gates.md`：规范 `mcu-mcp` 控制面、board v2、PDF/HIL 门禁、sidecar 硬件流程、发布/安全门禁和调试证据。任何影响目标或认定发布合格的工作开始前必须读取。

实现细节还需读取 `$mcu-firmware-development` 的 `references/stm32cubemx-rtos-workflow.md`、`$mcu-rtos-drivers` 的 `references/hardware-pc-data-flow-contract.md` 和 `$mcu-team-collaboration` 的 `references/parallel-workspace-lanes.md`。

## 脚本

使用 `scripts/check_mcu_project.py <project-root>` 按基线目录和生命周期证据审计项目仓库。默认把缺项视为评审提示，而不是自动失败。

使用 `scripts/check_skill_maturity.py <skills-root>` 对本 skill 库执行 100 项结构和生命周期覆盖审计。

使用 `scripts/check_enterprise_pipeline.py <skills-root> --project-root <project-root>` 校验 500 项企业级清单，并汇总项目证据覆盖情况。
