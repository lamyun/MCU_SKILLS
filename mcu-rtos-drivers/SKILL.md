---
name: mcu-rtos-drivers
description: "嵌入式 MCU RTOS 与驱动框架技能，用于项目声明 RTOS 的身份路由、任务划分、优先级设计、栈/堆预算、ISR/DMA、同步原语、总线驱动、并发安全、低功耗和版本化 MCU-PC 遥测。适用于设计、实现、评审或排查裸机或任意 RTOS 驱动、UART/USB 协议、PC collector、持久化或回放链路。"
---

# MCU RTOS 与驱动

默认不预设 MCU 厂商、系列、具体型号、封装、开发板或工具链。从用户输入、受控 board profile 和现有项目文件解析目标；缺失时明确标为待确认，示例平台只能按条件选用。

默认也不选择 RTOS。RTOS identity 只能来自项目 manifest、生成器配置、依赖锁或显式用户输入；来源冲突或缺失时保持 `unconfigured`，不得根据 MCU、SDK 或示例工程猜测。

## 概览

使用本技能处理 MCU 固件中最容易失控的并发、驱动、ISR、DMA 和总线资源问题。目标是让驱动行为可预测、上下文边界清晰、故障可恢复。

## RTOS 设计流程

1. 列出所有周期任务、事件任务、后台任务和中断源。
2. 为每个任务定义职责、触发源、周期/截止时间、优先级、栈预算、看门狗喂狗策略。
3. 避免任务间直接共享可变状态；优先使用消息、队列、事件和单 owner 模型。
4. 为每条阻塞路径定义超时、取消、错误恢复和诊断计数器。
5. 建立系统负载预算：CPU 使用率、最坏中断延迟、峰值队列深度、栈高水位。

## 驱动契约

每个驱动都要说明：

- 支持的调用上下文：task、ISR、boot、low-power resume。
- 同步模型：阻塞、异步、回调、future/event、polling。
- 资源 owner：外设实例、DMA channel、IRQ、GPIO、bus lock。
- 错误模型：超时、总线错误、校验失败、设备不在线、忙状态。
- 生命周期：init、open、configure、transfer、cancel、close、deinit。
- 诊断：计数器、最后错误、状态快照、trace hook。

## ISR 与 DMA 规则

- ISR 中只清标志、搬运最小数据、投递事件或释放同步对象。
- ISR 与 task 共享缓冲区时明确 cache、memory barrier、临界区和 ownership。
- DMA buffer 定义对齐、生命周期、缓存一致性、半传输/全传输处理。
- 回调不得调用可能阻塞的 API，除非 RTOS 和驱动明确允许。
- 中断优先级必须兼容 RTOS syscall 限制。

## 总线模式

- I2C/SPI 总线使用 bus manager 统一仲裁片选、速率、模式、超时和恢复。
- CAN/UART 使用 ring buffer 或消息队列隔离 ISR 和解析任务。
- 对共享总线设备提供设备级 transaction API，避免业务层直接拼接底层时序。
- 总线错误恢复必须覆盖 NACK、仲裁丢失、卡死低电平、超时和外设复位。

## 评审检查表

- 是否有优先级反转、无界等待、队列溢出或栈溢出风险。
- 是否把复杂业务放进 ISR 或驱动回调。
- 是否所有 transfer 都能 cancel 或 timeout。
- 是否有统一的设备状态和错误观测入口。
- 是否有并发测试、压力测试和异常注入测试。

## MCU-PC 运行契约

实现遥测或命令前读取 `references/hardware-pc-data-flow-contract.md`。使用单一 owner 的有边界链路：ISR/DMA capture -> telemetry task -> UART/USB DMA -> incremental PC parser -> append-only JSONL -> SQLite-WAL query index -> deterministic replay。

每个帧都要版本化并限制长度，支持重新同步、CRC 损坏检测、sequence/reset identity、timestamp、兼容协商、重连、背压策略和诊断计数器。CRC 不能认证改变状态的 PC 命令。host 缺失、变慢、断开或恶意输入时仍要保证 control loop 和 watchdog 健康。

校验 project/change/lane/variant、device/board 和 firmware identity 后，live evidence 只能写入已登记 lane/run 的私有 raw/JSONL 与 SQLite 路径。调用方指定的共享数据库、未知 lane 或 synthetic capture 必须保持隔离的软件证据。

## 可执行调试门禁

目标侧诊断时，调用 `$mcu-development-lifecycle` 并读取 `references/executable-engineering-gates.md`。检查线程或 trace 前先保留关联故障快照；只有 target/OpenOCD 配置支持时才使用 `rtos_threads` 和白名单 RTT/SWO/ITM 控制，不可用时报告 `UNAVAILABLE`，禁止编造线程或 trace 证据。

## 跑中改进交接

流程执行中出现门禁误通过、可重复故障、反复人工绕行、目录混放或实际工具面与本 Skill 不一致时，调用 `$mcu-continuous-improvement`。项目专有证据保存在 lane 运行目录；只有已复现并有回归保护的通用模式才提升到中央持续改进 Skill。

## 参考资料

## PDF 证据门禁

实现来自 PDF 的 IRQ、DMA、寄存器、总线时序、极性或引脚事实前，必须有 `$mcu-datasheet-extraction` 通过的 Poppler + Codex PDF manifest。在驱动契约中引用 manifest/page 锚点；视觉与文本通道冲突时停止实现。

读取 `references/rtos-design.md` 获取任务设计模板；读取 `references/driver-contract.md` 获取驱动 API 评审字段；读取 `references/hardware-pc-data-flow-contract.md` 获取线协议、运行所有权、collector、持久化、回放、关联标识和证据等级契约。
