# MCU Skills 使用指南

本文档说明这套 MCU skills 如何调用、输入数据如何格式化，以及如何运行随附审计脚本。

说明：文档内容使用中文；命令、路径、skill 名称、脚本参数、C/API 标识符和常见英文缩写保持原样，避免影响调用和执行。

全局约束：所有 MCU skills 默认不选择厂商、系列、具体型号、封装、开发板或工具链。目标必须来自用户输入、受控 board profile、原理图/手册证据或现有项目配置；信息不足时列为待确认，不得用示例型号补位。STM32CubeMX、Keil MDK、ESP-IDF 等只是在目标匹配时加载的条件化工作流。

## 技能地图

按任务选择最小可用 skill：

| 需求 | 调用的 skill |
| --- | --- |
| 产品创意、市场对标、MVP 范围、方案选型 | `$mcu-product-discovery` |
| 端到端规划、阶段门、项目审计 | `$mcu-development-lifecycle` |
| 需求、MCU 选型、系统架构 | `$mcu-requirements-architecture` |
| 芯片手册/参考手册提取、引脚/寄存器/电气事实 | `$mcu-datasheet-extraction` |
| 原理图评审、PCB 评审、板级 Bring-up | `$mcu-hardware-bringup` |
| 裸机固件、模块设计、编码规范 | `$mcu-firmware-development` |
| RTOS 任务、驱动、ISR、DMA、总线 | `$mcu-rtos-drivers` |
| 单元、集成、HIL、回归、验收测试 | `$mcu-verification-test` |
| 故障调试、时序、内存、功耗优化 | `$mcu-debug-optimization` |
| 发布、量产烧录、校准、OTA | `$mcu-release-production` |
| 多厂商环境发现、工具链、构建、CI、制品 | `$mcu-ci-toolchain` |
| 功能安全、网络安全、合规、可靠性控制 | `$mcu-safety-security-compliance` |
| RACI、评审、交接、变更控制、团队协作 | `$mcu-team-collaboration` |

产品或赛道还不清楚时先从 `$mcu-product-discovery` 开始；跨阶段工程治理从 `$mcu-development-lifecycle` 开始。

## 基础调用格式

推荐使用下面的提示词结构：

```text
Use $mcu-development-lifecycle.

目标：
规划 MCU 项目流程并建立阶段门。

项目背景：
- 产品：
- MCU/板卡：
- 当前阶段：
- 团队：
- 约束：

输入资料：
- 需求：
- 架构说明：
- 硬件文件：
- 固件仓库：
- 测试状态：

期望输出：
- 阶段计划
- 风险
- 必需交付物
- 下一步行动
```

## 给 skill 的数据格式

优先使用结构化 Markdown。一个概念写一行，表格一行代表一条记录。

### 项目上下文

```text
项目：
产品：
MCU：
板卡版本：
固件版本：
当前阶段：
目标发布：
风险等级：
团队角色：
已知约束：
```

### 产品发现输入

```text
创意：
目标用户：
使用场景：
现有替代方案：
竞品/对标对象：
MVP 目标：
非目标：
关键假设：
商业/效率/安全价值：
```

### 需求行

```markdown
| ID | 需求 | 优先级 | 验收标准 | 验证方式 | 负责人 | 状态 |
| --- | --- | --- | --- | --- | --- | --- |
| REQ-FUNC-001 |  | must |  | HIL |  | draft |
```

### MCU 选型输入

```markdown
| 候选 MCU | Flash | RAM | CPU | ADC/PWM | 总线 | 功耗 | 安全能力 | 成本 | 风险 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
```

### 芯片手册提取输入

```text
文档：
文档类型：datasheet / reference manual / errata / app note
MCU 精确型号：
封装：
文档版本/日期：
页码或章节：
目标事实：pins / registers / electrical / timing / errata / peripheral limits
下游用途：
输出格式：
```

### 硬件评审输入

```text
MCU：
原理图版本：
PCB 版本：
BOM 版本：
电源轨：
时钟源：
复位/启动/调试：
关键外设：
已知疑点：
希望评审的范围：
```

### 固件模块输入

```text
模块：
层级：platform / bsp / driver / middleware / app
目的：
公开 API：
调用上下文：boot / task / ISR / callback
时序要求：
缓冲区和所有权：
错误处理：
测试：
```

### RTOS 任务输入

```markdown
| 任务 | 职责 | 触发源 | 周期/截止时间 | 优先级 | 栈预算 | 阻塞对象 | 看门狗角色 |
| --- | --- | --- | --- | --- | --- | --- | --- |
```

### 测试用例输入

```text
测试 ID：
关联需求：
层级：unit / integration / HIL / regression / acceptance
前置条件：
步骤：
期望结果：
证据：
自动化命令：
```

### 调试输入

```text
现象：
频率：
固件版本：
板卡版本：
最近变更：
日志：
Fault 寄存器：
复位原因：
复现步骤：
已经尝试：
```

### 发布输入

```text
发布版本：
源码版本：
工具链：
硬件兼容性：
制品：
测试摘要：
已知问题：
生产说明：
回滚说明：
需要的审批：
```

### 维护回溯输入

```text
事件 ID：
现场现象：
影响版本：
硬件版本：
复现条件：
日志/故障码：
关联需求：
关联测试：
关联发布包：
临时处置：
期望回溯范围：
```

### 团队协作输入

```text
交付物：
版本：
负责人：
评审人：
受影响团队：
需要决策：
开放风险：
证据链接：
期望交接：
```

## 常见调用示例

### 启动新 MCU 项目

```text
Use $mcu-product-discovery.
基于下面的创意做市场对标、MVP 范围和方案选型。
请输出竞品矩阵、方案评分、关键假设、PRD 到需求 ID 的初稿和下一阶段 skill。

产品创意：
...
```

```text
Use $mcu-development-lifecycle.
基于下面的产品信息创建端到端 MCU 项目流程。
请输出阶段门、必需交付物、RACI、风险和前两周执行计划。

项目背景：
...
```

### 评审需求

```text
Use $mcu-requirements-architecture.
请评审这些需求是否清晰、可测试，是否缺少边界条件、MCU 资源影响和追踪关系。

需求：
...
```

### 提取芯片手册事实

```text
Use $mcu-datasheet-extraction.
请从下面的 MCU datasheet 和 reference manual 摘录中提取实现事实。
输出源文档清单、引脚/AF 表、寄存器事实、电气/时序限制、errata 风险和下游交接建议。

文档：
...
```

### 评审原理图 Bring-up 风险

```text
Use $mcu-hardware-bringup.
请基于下面的 MCU 硬件摘要，从电源、时钟、复位、启动、调试、引脚复用、ADC、总线和 Bring-up 顺序输出发现。

硬件摘要：
...
```

### 设计固件模块

```text
Use $mcu-firmware-development.
请设计固件模块契约和实现计划。

模块输入：
...
```

### 设计 RTOS 任务和驱动

```text
Use $mcu-rtos-drivers.
请评审任务和驱动设计中的优先级反转、阻塞、ISR/DMA 所有权、队列容量和诊断问题。

设计：
...
```

### 制定测试计划

```text
Use $mcu-verification-test.
请建立需求到测试的策略，覆盖 unit、integration、HIL、regression 和 acceptance。

输入：
...
```

### 分析故障

```text
Use $mcu-debug-optimization.
请分析该 MCU 故障，给出需要收集的证据、可能根因、验证实验和回归测试。

故障数据：
...
```

### 准备发布

```text
Use $mcu-release-production.
请评审发布就绪度，输出阻塞项、所需证据、制造包缺口和回滚风险。

发布数据：
...
```

### 回溯现场问题

```text
Use $mcu-release-production.
请把下面的现场事件回溯到需求、测试、发布包和修复验证。
输出影响范围、可能根因、需要补采的证据、临时处置、修复计划和复盘行动。

维护回溯输入：
...
```

### 标准化团队协作

```text
Use $mcu-team-collaboration.
请为该 MCU 团队建立 RACI、评审节奏、变更分级、交接规则和必需证据。

团队背景：
...
```

## 期望输出格式

可以明确要求输出为下面几类：

```text
期望输出：
- 按严重程度排序的问题
- 必需证据
- 带负责人和截止时间的行动表
- 风险和缓解措施
- 开放问题
```

行动表：

```markdown
| ID | 行动 | 负责人 | 截止时间 | 证据 | 状态 |
| --- | --- | --- | --- | --- | --- |
```

风险表：

```markdown
| ID | 风险 | 影响 | 缓解措施 | 验证方式 | 负责人 | 状态 |
| --- | --- | --- | --- | --- | --- | --- |
```

评审发现：

```markdown
| ID | 发现 | 影响 | 建议 | 负责人 | 验证方式 |
| --- | --- | --- | --- | --- | --- |
```

## 推荐项目目录

```text
project/
  docs/
    governance/
    product/
    datasheets/
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

## 团队协作最小证据

团队标准化建议先建立这些文件：

```text
docs/project-charter.md
docs/team/raci.md
docs/team/review-cadence.md
docs/team/change-control.md
docs/team/handoff-register.md
docs/governance/risk-register.md
docs/architecture/adr/
docs/governance/metrics.md
```

然后运行：

```powershell
& $py D:/Desktop/mcu-skills/mcu-team-collaboration/scripts/check_team_collaboration.py D:/path/to/project
```
