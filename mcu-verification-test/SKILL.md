---
name: mcu-verification-test
description: "嵌入式 MCU 验证测试技能，用于需求追踪、单元/集成/HIL/回归、CubeMX 重新生成、版本化遥测、PC collector、JSONL/SQLite 持久化、回放、边界/异常、长稳、缺陷闭环和发布证据。适用于设计、实现、审计或改进 MCU 固件、host 数据链路和板级验证。"
---

# MCU 验证测试

默认不预设 MCU 厂商、系列、具体型号、封装、开发板或工具链。从用户输入、受控 board profile 和现有项目文件解析目标；缺失时明确标为待确认，示例平台只能按条件选用。

## 概览

使用本技能建立从需求到测试再到发布证据的闭环。测试目标不是“跑过一次”，而是让关键行为可重复验证、缺陷可复现、发布风险可解释。

## 测试策略

按风险选择测试层级：

- Host unit tests：算法、协议解析、状态机、参数校验、边界条件。
- Target integration tests：驱动、外设、RTOS 任务、存储、启动和复位。
- HIL tests：真实板卡、治具、仪器、传感/执行闭环、掉电/异常注入。
- Regression tests：缺陷复现用例、发布前必跑集、长稳和压力场景。
- Acceptance tests：产品需求级验收、制造测试、现场升级和回滚验证。

## 工作流程

1. 建立需求追踪矩阵：requirement -> design -> implementation -> test -> result。
2. 对每条高风险需求定义正常路径、边界路径、异常路径和恢复路径。
3. 为缺陷创建最小复现测试，并加入回归集合。
4. 自动化能自动化的部分；不能自动化的测试也要有步骤、仪器、判定标准和记录模板。
5. 发布前输出测试摘要：范围、版本、环境、通过率、遗留缺陷、风险接受。

## 测试用例字段

每个测试用例至少包含：

- Test ID、关联需求 ID、风险等级、测试层级。
- 前置条件、设备/固件版本、配置、输入刺激。
- 步骤、期望结果、判定阈值、日志和仪器记录。
- 自动化命令或手动操作说明。
- 失败后的数据保留要求。

## HIL 指导

- 优先覆盖人工容易漏掉的时序、掉电、通信异常、边界输入和长时间运行。
- HIL 脚本必须记录固件版本、板卡编号、治具版本、仪器配置。
- 对 flaky 测试区分产品不稳定、治具不稳定、脚本不稳定和环境不稳定。
- 对安全相关行为保留原始日志，不只保留摘要。

## 数据流与并行验证

读取 `$mcu-rtos-drivers` 的 `references/hardware-pc-data-flow-contract.md`。测试 valid、partial、concatenated、garbage、bad CRC、oversized、unknown version、duplicate、out-of-order、sequence gap、reset 和 timestamp wrap。覆盖 cable loss、reconnect、slow host/disk、bounded queue overflow、SQLite-WAL 中断/恢复、JSONL rotation/hash manifest、schema migration 和 deterministic replay。

在 lane 私有工作区无硬件运行 host verification。并发 lane 需要证明 build/evidence/database 隔离，并验证第二个 `.ioc`、serial port、probe 或 board lease 会被阻断。集成后重新执行 clean CubeMX generation、generated-drift comparison、完整构建和受影响回归。

证据等级保持分离：generation、build 和 host/replay 可以通过，而 target observation 或 real HIL 仍为 `blocked`。

## 可执行验证门禁

调用 `$mcu-development-lifecycle` 并读取 `references/executable-engineering-gates.md`。从 manifest 校验真实 HIL 的板卡序列号/版本、精确固件哈希、治具、仪器、pass 测试和带哈希原始证据；增加 mock mode、哈希漂移、profile/版本不符、缺少原始证据和上游 gate 失败的负向测试。

## 跑中改进交接

流程执行中出现门禁误通过、可重复故障、反复人工绕行、目录混放或实际工具面与本 Skill 不一致时，调用 `$mcu-continuous-improvement`。项目专有证据保存在 lane 运行目录；只有已复现并有回归保护的通用模式才提升到中央持续改进 Skill。

## 参考资料

## PDF 证据门禁

把每个来自 PDF 的验收限值、引脚/网络断言和硬件前置条件写入追踪矩阵，并附 `$mcu-datasheet-extraction` manifest 和页码锚点。执行前要求 `inspect_pdf_evidence` 通过；增加负向测试，证明哈希失效、漏复核页面或未解决差异会阻断验收。

读取 `references/test-plan-template.md` 获取测试计划结构；读取 `references/hil-regression.md` 获取 HIL 和回归设计细节。
