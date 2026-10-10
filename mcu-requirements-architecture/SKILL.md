---
name: mcu-requirements-architecture
description: "嵌入式单片机 MCU 需求工程与系统架构技能，用于产品需求澄清、需求拆解、MCU 选型、资源预算、接口定义、状态机设计、架构权衡、风险识别和需求到设计追踪。适用于把产品目标转换成可实现的 MCU 需求、架构决策、接口契约、选型准则，或版本化 MCU-PC 遥测与 host 数据需求。"
---

# MCU 需求与架构

默认不预设 MCU 厂商、系列、具体型号、封装、开发板或工具链。从用户输入、受控 board profile 和现有项目文件解析目标；缺失时明确标为待确认，示例平台只能按条件选用。

## 概览

使用本技能把模糊产品目标转换成可实现、可验证、可追踪的 MCU 系统方案。输出优先服务后续硬件、固件、测试和量产阶段。

## 输入信息

先收集或推断以下信息；缺失项标记为待确认，不要编造：

- 产品场景、用户动作、关键成功指标。
- 供电方式、功耗目标、工作温度、寿命和可靠性目标。
- 外设接口：GPIO、ADC、PWM、UART、SPI、I2C、CAN、USB、Ethernet、无线模块等。
- 实时性：采样周期、控制环、通信延迟、启动时间、故障响应时间。
- 存储：Flash/RAM/EEPROM/外部存储、日志、参数、升级空间。
- 安全与维护：调试口策略、加密、认证、OTA、现场诊断。
- 制造约束：成本、封装、供应链、烧录、校准、测试治具。

## 需求流程

1. 将用户目标拆成功能需求、非功能需求、约束需求和验收标准。
2. 给每条需求分配稳定 ID，例如 `REQ-FUNC-001`、`REQ-PWR-001`。
3. 为每条需求定义可测量指标、测试方法、边界条件和失败处理。
4. 标记优先级：must、should、could、defer。
5. 建立需求追踪字段：设计项、代码模块、测试用例、结果、缺陷链接。

## 架构流程

1. 画出功能分解：传感、执行、通信、存储、UI、安全、诊断、升级。
2. 建立资源预算：CPU 负载、RAM、Flash、外设通道、DMA、定时器、中断优先级。
3. 定义硬件/固件边界：哪些功能依赖外部 IC，哪些由 MCU 软件实现。
4. 定义运行模式：boot、init、normal、low-power、fault、service、update。
5. 定义关键状态机和数据流，尤其是异常恢复路径。
6. 记录架构决策和放弃方案，避免后续重复争论。

## MCU 选型

比较 MCU 时输出表格，不只给结论：

- 架构/频率/FPU/DSP/TrustZone 或安全能力。
- Flash/RAM/EEPROM/缓存/外部存储接口。
- ADC/DAC/PWM/定时器/比较器/运放等模拟和控制资源。
- 通信接口、DMA 能力、中断数量和优先级能力。
- 功耗模式、唤醒源、启动时间。
- 封装、温度等级、供货风险、生态、调试工具、认证经验。
- Bootloader、加密、读保护、量产烧录和现场升级支持。

## MCU-PC 数据契约

产品数据从硬件进入 PC 软件时，先定义端到端契约，再选择实现。明确 source/sample 语义、单位、速率与突发上限、延迟/抖动/丢失预算、最大离线时长、背压、设备复位身份、host OS/runtime、保留期、回放保真度、隐私和兼容窗口。

线协议、payload schema、PC collector 和 storage schema 都要有稳定版本。为 UART/USB bandwidth、DMA、queue、RAM、CPU、disk 和 database 建立预算。需求和验收证据贯穿 `project_id`、`change_id`、`lane_id`、variant、firmware build、protocol/schema、collector/storage 和 `run_id`。

冻结 framing、CRC、reconnect、SQLite-WAL、JSONL 或 replay 行为前，调用 `$mcu-rtos-drivers` 并读取 `references/hardware-pc-data-flow-contract.md`。Host test、replay、target observation 和真实硬件 HIL 必须作为不同证据等级。

## 交付物

- 需求规格草案或审查意见。
- MCU 选型矩阵和推荐结论。
- 系统架构说明、模块边界、接口契约、运行模式。
- 风险清单和待确认问题。
- 需求到设计/测试追踪初版。

## 可执行工程门禁

冻结目标架构前，调用 `$mcu-development-lifecycle` 并读取 `references/executable-engineering-gates.md`。把精确 MCU/封装/board/PCB/BOM、target name、IDCODE、内存范围、probe/transport、证据要求、制品哈希、擦除策略和 Option Bytes 策略写入规范 v2 profile；存在 `UNCONFIRMED` 时阻断下游门禁。

## 跑中改进交接

流程执行中出现门禁误通过、可重复故障、反复人工绕行、目录混放或实际工具面与本 Skill 不一致时，调用 `$mcu-continuous-improvement`。项目专有证据保存在 lane 运行目录；只有已复现并有回归保护的通用模式才提升到中央持续改进 Skill。

## 参考资料

## PDF 证据门禁

芯片手册、参考手册或原理图 PDF 中的事实必须路由到 `$mcu-datasheet-extraction`。只有通过的 Poppler + Codex PDF manifest 才能支撑冻结需求、MCU 选型评分、接口预算或架构决策；否则只能记录为假设和开放风险。

读取 `references/requirements-template.md` 获取需求表字段；读取 `references/architecture-template.md` 获取架构章节和评审提示。
