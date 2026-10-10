# MCU 测试计划模板

编写或审计 MCU 固件和板级测试计划时使用本参考。

## 测试计划章节

1. 范围和发布/里程碑。
2. 硬件版本和固件版本。
3. 需求和风险覆盖。
4. 测试层级：unit、integration、HIL、regression、acceptance。
5. 测试环境和设备。
6. 自动化命令和手动步骤。
7. 入口和出口准则。
8. 缺陷处理。
9. 证据存储。
10. 剩余风险和批准。

## 追踪矩阵

| 需求 | 风险 | 设计/模块 | 测试用例 | 层级 | 结果 | 证据 |
| --- | --- | --- | --- | --- | --- | --- |

## 测试用例模板

| 字段 | 值 |
| --- | --- |
| 测试 ID | TC-LEVEL-NNN |
| 需求 ID |  |
| 目的 |  |
| 前置条件 |  |
| 设备 |  |
| 固件/构建 |  |
| 步骤 |  |
| 期望结果 |  |
| 通过/失败阈值 |  |
| 证据 |  |
| 自动化 |  |

## 出口准则

- 所有 must-have 需求都有通过的验证或获批例外。
- 阻塞和严重缺陷已关闭或正式接受。
- 回归套件达到约定通过标准。
- 测试证据已关联固件和板卡版本。
- Flaky 测试已分类，不隐藏在整体通过率里。

## MCU-PC 数据流矩阵

覆盖 valid、partial、concatenated、garbage、bad CRC、oversized、unknown version、duplicate、sequence gap、reset、reconnect、slow consumer 和 storage interruption。验证 bounded memory、明确 drop/gap counter、JSONL rotation/hash manifest、SQLite-WAL recovery/migration 和 deterministic replay hash。

记录 `project_id`、`change_id`、`lane_id`、variant、firmware build/hash、protocol/payload schema、collector/storage/replay version、`run_id`、source capture hash 和证据等级。Host/replay 成功不能通过 target 或 real-HIL 门禁。
