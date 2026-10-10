---
name: mcu-firmware-development
description: "厂商与型号无关的嵌入式 MCU 固件开发 Skill，覆盖裸机、RTOS 与轻量框架，并按项目条件支持 STM32CubeMX、Keil MDK、ESP-IDF 等平台，包括环境门禁、代码生成、项目配置治理、生成代码所有权、分层架构、外设、遥测、状态机、错误处理、日志、配置和评审。用于创建、重新生成、重构、评审或标准化 MCU 固件。"
---

# MCU 固件开发

默认不预设 MCU 厂商、系列、具体型号、封装、开发板或工具链。从用户输入、受控 board profile 和现有项目文件解析目标；缺失时明确标为待确认，示例平台只能按条件选用。

## 概览

使用本技能实现可维护、可移植、可测试的 MCU 固件。优先建立清晰边界和可验证行为，再填充外设细节。

## 固件架构

采用分层结构，除非现有工程已经有成熟约定：

- `platform`：启动文件、链接脚本、时钟、系统 tick、芯片级配置。
- `bsp`：板级引脚、电源、时钟源、外部器件实例。
- `drivers`：外设驱动，提供稳定接口，不暴露业务逻辑。
- `middleware`：协议栈、文件系统、日志、参数、升级、诊断。
- `app`：产品业务、状态机、控制策略、用户交互。
- `tests`：host unit tests、target integration tests、mocks/fakes。

## 实现流程

1. 读取需求、引脚表、时钟树、外设约束和现有工程约定。
2. 定义模块契约：输入、输出、状态、错误码、线程/中断上下文、超时。
3. 先实现最小可运行路径：启动、时钟、日志、错误指示、构建。
4. 外设按“初始化、配置、非阻塞传输、错误恢复、诊断计数器”实现。
5. 对状态机使用显式状态、事件、守卫条件和超时处理。
6. 对配置和参数使用版本字段、默认值、校验和迁移策略。
7. 保持硬件相关代码集中在 platform/bsp/drivers，业务层不直接操作寄存器。

## 编码规范

- 使用固定宽度整数类型和明确单位，例如 `uint32_t timeout_ms`。
- 公开 API 返回明确错误码；避免沉默失败。
- ISR 中只做最小工作，把耗时处理推迟到任务或主循环。
- 不在通用驱动中调用业务层。
- 避免动态内存，除非项目明确允许并有碎片监控。
- 所有阻塞等待必须有超时和错误路径。
- 对硬件寄存器、共享变量、中断交互使用 `volatile`、临界区或原子策略，并说明理由。

## 评审检查表

审查固件时优先找这些问题：

- 初始化顺序是否依赖未准备好的时钟、电源或外设。
- 错误路径是否可观测、可恢复、可测试。
- 中断优先级、共享数据和超时是否一致。
- 边界值、溢出、单位换算、环形缓冲区满/空是否处理。
- 编译配置、链接脚本、启动文件和目标芯片是否匹配。
- 低功耗、掉电、复位、看门狗是否有一致策略。

## STM32CubeMX

CubeMX 工作先读取 `references/stm32cubemx-rtos-workflow.md`。选择精确 part/board 前探测本机 CubeMX 和 STM32Cube package；把 `.ioc` 与 generator manifest 作为受控输入，RTOS 仅采用项目声明的 identity/mode，生成到 lane 私有干净目录，隔离应用代码和生成输出，并用 clean regeneration drift 证明结果。

对任一项目所选 STM32 系列，根据 `.ioc` 核对生成的 startup/linker、CPU/FPU、内存和时钟目标；启用 RTOS 时再核对 interrupt/heap/task 设置。工程已生成不等于已编译，UART 可见不等于协议已验证，两者都不等于真实硬件 HIL。

MCU-PC 遥测需调用 `$mcu-rtos-drivers` 并读取 `references/hardware-pc-data-flow-contract.md`。应用数据生产与有边界的 framing/transport 分离，并暴露 drop、queue、DMA、reset 和 protocol counters。

## Keil MDK 与 ESP-IDF

开展 Keil MDK 或 ESP-IDF 工作前调用 `mcu_mcp.detect_embedded_tools`，选择 `keil_mdk` 或 `esp_idf` 并要求环境为 `complete`，然后读取 `references/keil-esp-idf-workflow.md`。具体 target 必须来自项目配置，上层 application/driver 边界不得依赖厂商工程格式。

Keil 固定 `.uvprojx`、target、编译器、CMSIS-Pack 依赖、scatter、defines 和生成/用户代码所有权。维护中的目标优先 ARMCLANG；ARMCC 只保留给明确声明的遗留目标。发现 μVision 不等于许可证或构建通过。

ESP-IDF 固定 framework revision、target、`sdkconfig.defaults`、已审查 `sdkconfig`、组件/依赖锁、分区表和组件所有权。kernel/RTOS 集成由项目所选 framework revision 与 `sdkconfig` 决定；identity 明确后再检查 SMP/core affinity、任务优先级/栈、看门狗、heap capabilities 和 ISR 契约，不能套用 CubeMX 生成规则。

## 可执行工程门禁

涉及目标执行或发布认定时，调用 `$mcu-development-lifecycle` 并读取 `references/executable-engineering-gates.md`。严格按 v2 board profile 构建，保留 ELF/BIN/MAP 哈希，保持旧 direct flash 禁用，并通过私有 OpenOCD sidecar 执行带身份检查的 probe/flash。

禁止把 `run_project_step(upload)` 或 IDE/PlatformIO upload target 当作烧录捷径。通用 project-step runner 只用于 configure、build 和 test；任何目标写入必须经过真实 approval 与 lease 的受控硬件工作流。

## 跑中改进交接

流程执行中出现门禁误通过、可重复故障、反复人工绕行、目录混放或实际工具面与本 Skill 不一致时，调用 `$mcu-continuous-improvement`。项目专有证据保存在 lane 运行目录；只有已复现并有回归保护的通用模式才提升到中央持续改进 Skill。

## 参考资料

## PDF 证据门禁

把 PDF 中的引脚、寄存器、时序限值、极性或电气假设写入代码前，必须有 `$mcu-datasheet-extraction` 通过的 Poppler + Codex PDF manifest。配置或需求中保留 manifest/page 锚点；两条通道不一致时停止实现。

读取 `references/firmware-standard.md` 获取详细项目约定；创建新模块时读取 `references/module-template.md`；读取 `references/stm32cubemx-rtos-workflow.md` 获取 CubeMX、项目所选 STM32 系列、项目声明的可选 RTOS、`.ioc`、所有权和重新生成门禁；Keil MDK 或 ESP-IDF 工作读取 `references/keil-esp-idf-workflow.md`。
