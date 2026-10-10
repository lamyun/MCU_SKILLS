---
name: mcu-datasheet-extraction
description: "嵌入式 MCU 芯片手册与参考手册提取技能，用于把 PDF/手册章节、引脚表、复用功能、寄存器、电气参数、时序图、勘误和封装数据转换成有证据来源的工程事实。适用于 MCU 选型、引脚复用、驱动开发、硬件评审、寄存器配置、时序预算或需求交接前的数据提取、审计和规范化。"
---

# MCU 芯片手册提取

默认不预设 MCU 厂商、系列、具体型号、封装、开发板或工具链。从用户输入、受控 board profile 和现有项目文件解析目标；缺失时明确标为待确认，示例平台只能按条件选用。

## 概览

使用本技能从 MCU datasheet、reference manual、errata、封装文档和应用笔记中提取可直接用于工程实现的事实。每个关键事实都必须带来源证据，避免硬件、固件、需求和测试后续依赖猜测。

## 工作流

1. 确认源文档：MCU 精确型号、封装、文档标题、版本、发布日期、页码范围和使用章节。
2. 确认提取目标：MCU 选型、引脚复用、外设配置、寄存器配置、电气预算、时序预算、启动/调试行为或 errata 风险。
3. 对每份 PDF 执行 `references/pdf-dual-verification.md` 中的 Poppler + Codex PDF 门禁；`inspect_pdf_evidence` 未返回 `passed=true` 前，不得提取为确定事实。
4. 用表格提取事实：章节、页码、表/图编号、适用条件、原始值、归一化值、单位、适用范围和置信度。
5. 区分直接事实和工程解释。推断结论标为 `推断`，并写清假设。
6. 交叉检查变体相关事实：封装脚数、温度等级、电压范围、存储容量、外设实例、复用功能和硅版本。
7. 生成下游交接包：需求和选型交给 `$mcu-requirements-architecture`；原理图和引脚风险交给 `$mcu-hardware-bringup`；寄存器和驱动细节交给 `$mcu-firmware-development` 或 `$mcu-rtos-drivers`；时序和测试限值交给 `$mcu-verification-test`。

## 提取范围

只提取当前任务需要的事实，但完成前至少检查这些类别：

- 器件身份：型号、封装、存储容量、温度等级、文档版本。
- 电源和复位：电压范围、电源轨、复位阈值、掉电行为、启动模式、调试引脚。
- 时钟：振荡器选项、PLL 限制、时钟树约束、外设时钟上限。
- 引脚和复用：引脚名、封装脚号、GPIO 端口、复用功能、模拟能力、启动/调试冲突、默认状态。
- 外设能力：实例名、通道映射、DMA 请求线、中断、定时器、ADC/PWM/UART/SPI/I2C/CAN/USB/Ethernet 约束。
- 寄存器和位域：地址、复位值、访问类型、字段宽度、合法取值、副作用、写 1 清零等行为。
- 电气和时序限制：min/typ/max、工作条件、单位、负载、温度、电压、采样假设。
- 勘误和限制：硅版本、受影响模块、规避措施、验证影响。

## 证据规则

- 每个非显然数值都记录页码、章节、表/图编号和文档版本。
- 保留 `min`、`typ`、`max`，不要合并成单一数值。
- 保留 VDD、温度、时钟源、负载、采样时间、模式等工作条件。
- 不混用不同封装。封装未知时，把引脚事实标为封装相关。
- 不把 datasheet 和 reference manual 的事实混在一起，必须标明每个值来自哪份文档。
- 多份文档冲突时报告冲突；只有版本链明确时才优先采用最新官方版本。
- 如果输入是 PDF 截图或局部摘录，明确标出缺页或上下文不确定。
- 每份 PDF 事实包都记录双验证 manifest 路径和 gate 状态。
- 禁止仅依据文字提取结果推断原理图连接关系。

## 输出

按任务返回最小但可用的交付包：

- 源文档清单和置信度说明。
- 带证据锚点的事实表。
- 实现影响和风险。
- 待确认问题或缺失章节。
- 建议继续调用的下游 skill。

## 可执行工程门禁

事实将进入 board profile、硬件流程或发布时，调用 `$mcu-development-lifecycle` 并读取 `references/executable-engineering-gates.md`。双验证 manifest 通过且精确 MCU/封装/PCB/BOM 得到独立确认前，不得启用 v2 board profile。

## 跑中改进交接

流程执行中出现门禁误通过、可重复故障、反复人工绕行、目录混放或实际工具面与本 Skill 不一致时，调用 `$mcu-continuous-improvement`。项目专有证据保存在 lane 运行目录；只有已复现并有回归保护的通用模式才提升到中央持续改进 Skill。

## 参考资料

处理任何 PDF 时读取 `references/pdf-dual-verification.md`。构建提取交付包时读取 `references/datasheet-fact-template.md`。提取寄存器映射或位域时读取 `references/register-field-capture.md`。
