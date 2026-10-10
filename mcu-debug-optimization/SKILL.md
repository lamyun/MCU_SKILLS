---
name: mcu-debug-optimization
description: "嵌入式 MCU 调试与优化技能，用于 HardFault/复位/死机/看门狗、内存、时序、通信、MCU-PC 遥测/collector/persistence/replay 故障、功耗、性能、启动、trace 和可靠性。适用于诊断或优化 MCU 固件、host 数据链路、板级行为、时序、内存、功耗或稳定性。"
---

# MCU 调试优化

默认不预设 MCU 厂商、系列、具体型号、封装、开发板或工具链。从用户输入、受控 board profile 和现有项目文件解析目标；缺失时明确标为待确认，示例平台只能按条件选用。

## 概览

使用本技能把“偶现问题”拆成可采集证据、可复现假设和可验证修复。先保护现场和建立观测，再改代码。

## 调试流程

1. 固定问题描述：现象、频率、版本、硬件批次、环境、操作步骤、最近变更。
2. 保留现场：日志、寄存器、fault frame、复位原因、栈、水位、heap、关键计数器。
3. 缩小范围：是否与电源、时钟、温度、外设、负载、并发、特定输入有关。
4. 建立假设并设计最小实验，一次只验证一个变量。
5. 修复后加入回归测试或诊断断言，防止同类问题回归。

## 故障类别

- HardFault/BusFault/UsageFault：解析 PC、LR、xPSR、CFSR/HFSR/MMFAR/BFAR 和栈帧。
- Watchdog reset：确认喂狗 owner、最长临界区、阻塞调用和任务心跳。
- Memory corruption：检查数组越界、DMA buffer、栈溢出、生命周期、并发写。
- Timing jitter：检查中断屏蔽、优先级、DMA、cache、锁竞争、日志阻塞。
- Power issue：确认 sleep entry 条件、唤醒源、外设时钟、GPIO 漏电、调试口影响。
- Communication issue：检查波特率/时序、总线恢复、错误计数器、缓冲区压力。

## 优化流程

1. 定义目标和基线：当前值、目标值、测量方法、误差范围。
2. 找瓶颈，不先猜：profile、trace、GPIO timestamp、cycle counter、功耗仪。
3. 优先优化算法、唤醒次数、总线批处理和阻塞路径，再做微优化。
4. 每次优化记录副作用：代码复杂度、RAM/Flash、实时性、功耗、可靠性。
5. 用回归测试证明功能没有退化。

## 必需证据

- 可复现脚本或步骤。
- 原始日志和时间戳。
- 关键寄存器或 trace 片段。
- 修改前后测量数据。
- 根因、修复、验证、遗留风险。

## MCU-PC 数据流诊断

把 MCU produced/sent/dropped、queue high-water、DMA/overrun、CRC/parser、sequence-gap、reconnect、reset/boot ID 和 watchdog counters，与 PC connection、quarantine、JSONL、SQLite-WAL、migration、disk/backpressure 和 replay log 做关联。证据绑定 firmware build/hash、protocol/schema、collector/storage version、`change_id`、`lane_id` 和 `run_id`。

改固件前先分类失败阶段：source production、RTOS queue、framing、DMA/physical transport、PC parser、persistence、query/index 或 replay。串口可见或偶尔收到有效帧不证明端到端健康。优先用不可变 capture 和 host test 复现 parser/storage 故障；只有剩余假设确实需要时才使用受控硬件。

## 可执行调试门禁

接触目标前调用 `$mcu-development-lifecycle` 并读取 `references/executable-engineering-gates.md`。通过 `run_hardware_workflow` 使用同一个 `operation_id` 完成 probe/故障抓取，再用准确 ELF 符号化 PC/LR/栈地址，并通过 CMSIS-SVD 解码外设值。按 profile 选择 Cortex-M 或 RISC-V；不支持的 RTOS/RTT/SWO/ITM 功能必须报告 `UNAVAILABLE`。

## 跑中改进交接

流程执行中出现门禁误通过、可重复故障、反复人工绕行、目录混放或实际工具面与本 Skill 不一致时，调用 `$mcu-continuous-improvement`。项目专有证据保存在 lane 运行目录；只有已复现并有回归保护的通用模式才提升到中央持续改进 Skill。

## 参考资料

## PDF 证据门禁

使用手册或原理图 PDF 解释故障前，必须由 `$mcu-datasheet-extraction` 生成并通过 Poppler + Codex PDF manifest。缺失或失败的门禁只能记为证据缺口；禁止把无法辨认的网络、引脚、限值或表格单元直接写成根因。

读取 `references/fault-debug-playbook.md` 获取故障定位步骤；读取 `references/optimization-checklist.md` 获取时序、内存和功耗优化提示。
