---
name: mcu-hardware-bringup
description: "嵌入式 MCU 硬件协同与板级 Bring-up 技能，用于原理图/PCB 评审、供电/时钟/复位/启动/调试接口检查、外设和 MCU-PC 传输链路核对、首板上电、测量记录、硬件问题定位和软硬件联调准备。适用于 MCU 硬件评审、UART/USB/VCP 链路验证、板级 Bring-up 或故障隔离。"
---

# MCU 硬件 Bring-up

默认不预设 MCU 厂商、系列、具体型号、封装、开发板或工具链。从用户输入、受控 board profile 和现有项目文件解析目标；缺失时明确标为待确认，示例平台只能按条件选用。

## 概览

使用本技能把硬件风险前置到原理图、PCB 和首板上电阶段，避免固件阶段才发现电源、时钟、启动脚、下载口或外设连接问题。

## 评审流程

1. 确认 MCU 型号、封装、供电域、启动模式、调试接口和关键外设。
2. 对 PDF 原理图调用 `$mcu-datasheet-extraction`，读取其 `references/pdf-dual-verification.md`；Poppler + Codex PDF 双验证 manifest 未通过时，不接受连接关系为确定事实。
3. 按电源、时钟、复位、启动、调试、存储、通信、模拟、保护分块审查。
4. 对每个关键引脚核对：原理图连接、复用功能、默认电平、上拉/下拉、测试点。
5. 检查 PCB：退耦距离、晶振走线、模拟/数字地、电流回路、高速/敏感线、SWD/JTAG 可达性。
6. 输出风险表：问题、影响、验证方式、硬件修改或固件规避方案。

## Bring-up 顺序

按低风险到高风险推进：

1. 空板/未焊关键负载检查：短路、电源阻抗、焊接方向。
2. 限流上电：记录输入电流、各电源轨电压、纹波、温升。
3. 时钟和复位：验证复位释放、晶振起振、时钟输出或内部时钟 fallback。
4. 连接调试器：确认 SWD/JTAG、读芯片 ID、擦写 Flash、单步运行。
5. 最小固件：GPIO 翻转、串口日志、系统 tick、错误指示。
6. 分外设验证：传感器、执行器、通信、存储、ADC/PWM。
7. 边界测试：电压、温度、插拔、异常外设、掉电恢复。

## 需要采集的证据

- 原理图/PCB 版本、BOM 版本、样板编号。
- PDF SHA-256、选中页、双验证 manifest、gate 结果及尚未解决的视觉/文本差异。
- 电源轨测量表、示波器截图、逻辑分析仪记录。
- 下载/启动日志、芯片 ID、Option Bytes 或熔丝配置。
- 外设验证结果、缺陷编号、返板建议。

## MCU-PC 物理链路

从 MCU 引脚到 PC 连接器追踪完整 UART/USB/USB-UART/VCP 链路。核对复用功能、逻辑电平、共地或隔离、transceiver 供电、ESD/保护、极性、连接器 pinout、波特率/时钟容差、使用时的 RTS/CTS，以及板载调试器是否提供稳定 virtual COM interface。默认保留目标器件实际支持的调试接口、reset 和 target-voltage sense，除非存在已审批设计决策。

记录用于绑定端口的物理身份：board serial、probe/VCP serial、USB VID/PID/interface 和当前 OS port name。仅看到 `COMx` 不能证明是预期板卡、固件、帧协议或 HIL。把已确认 transport、pin/DMA/IRQ 约束和实测错误行为交接给 `$mcu-rtos-drivers` 的版本化数据流契约。

## 与固件协同

为固件提供：

- 确认后的引脚表和复用功能。
- 电源/时钟/复位约束。
- 外设地址、片选、IRQ、DMA、校准参数。
- 硬件异常需要软件检测或规避的列表。
- 向 OpenOCD 交接时附带已通过的证据 manifest；必要时在板卡 profile 中配置 `hardware_evidence_manifest` 和 `require_verified_hardware_evidence=true`。

## 可执行 Bring-up 门禁

调用 `$mcu-development-lifecycle` 并读取 `references/executable-engineering-gates.md`。MCU/封装/PCB/BOM、target name、IDCODE、内存映射和原理图证据确认前，bring-up 与 release 两类 v2 profile 都保持禁用。bring-up profile 可不要求既有 HIL，避免循环依赖；release profile 必须要求真实硬件 HIL。

## 跑中改进交接

流程执行中出现门禁误通过、可重复故障、反复人工绕行、目录混放或实际工具面与本 Skill 不一致时，调用 `$mcu-continuous-improvement`。项目专有证据保存在 lane 运行目录；只有已复现并有回归保护的通用模式才提升到中央持续改进 Skill。

## 参考资料

读取 `references/schematic-review.md` 获取设计评审提示；读取 `references/bringup-checklist.md` 获取首次上电和外设验证检查表。
