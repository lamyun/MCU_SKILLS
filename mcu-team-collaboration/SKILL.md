---
name: mcu-team-collaboration
description: "嵌入式 MCU 团队协作与工程治理技能，用于角色/RACI、隔离并行工作区、lane 与 generated-code ownership、资源租约、评审、需求/设计/代码/测试/发布追踪、变更控制、交接和跨硬件/固件/host/测试/生产团队协同。适用于组织 MCU 多 Agent 开发、评审、所有权、租约、追踪和交接。"
---

# MCU 团队协作

默认不预设 MCU 厂商、系列、具体型号、封装、开发板或工具链。从用户输入、受控 board profile 和现有项目文件解析目标；缺失时明确标为待确认，示例平台只能按条件选用。

## 概览

使用本技能把 MCU 开发从“靠个人记忆推进”变成“团队可交接、可追踪、可复盘”。重点不是增加流程，而是减少反复沟通、遗漏和返工。

## 协作模型

每个项目至少建立：

- RACI：需求、架构、硬件、固件、测试、生产、发布、现场支持的 owner。
- 单一事实源：需求、引脚表、接口契约、风险、缺陷、发布证据分别放在哪里。
- 评审节奏：需求评审、架构评审、硬件评审、代码评审、测试评审、发布评审。
- 变更控制：哪些变更必须走评审，哪些可以快速合入。
- 交接规则：硬件给固件、固件给测试、测试给发布、发布给生产和现场支持。
- 单一事实源：每类协作证据的存放位置、owner、更新触发条件。

## 评审流程

1. 明确评审对象和版本，不评审口头状态。
2. 先看影响面：需求、硬件、固件、测试、生产、现场。
3. 对每个发现写成可执行项：问题、影响、建议、owner、截止时间、验证方式。
4. 决策必须记录备选方案和接受的风险。
5. 关闭项必须附证据，不只写“已处理”。
6. 如果无法按期关闭，必须创建带过期时间的例外，而不是让问题沉没。

## 交接流程

每次跨团队交接都要回答：

- 当前版本是什么？
- 已验证什么，证据在哪里？
- 尚未验证什么，风险是什么？
- 对下一团队的输入、限制、工具和注意事项是什么？
- 如果失败，回到谁那里定位？

## 变更控制

这些变更必须显式审查：

- MCU 型号、封装、时钟、电源、boot、debug、存储布局。
- 引脚复用、外设实例、DMA、IRQ、RTOS 优先级。
- bootloader、OTA、安全配置、读保护、生产烧录脚本。
- 持久化参数格式、校准格式、序列号或密钥策略。
- 发布分支、工具链、SDK/HAL/RTOS 或编译优化级别。

## 并行开发

开启并行 Codex task、worktree 或 job 前读取 `references/parallel-workspace-lanes.md`。登记 coordinator，以及有边界的 firmware/platform、host 和 verification lane；记录 `project_id`、`change_id`、`lane_id`、owner、branch/workspace、私有 build/evidence 根、owned paths、heartbeat、expiry 和 status。

隔离源码分析、构建和 host test 可以并发。`.ioc`/CubeMX generation 以及每个物理 port、probe、board、fixture、instrument 都通过原子独占 lease 串行。两个 lane 不得写同一 generated tree、build directory、SQLite database 或 evidence staging path。集成后必须 clean regenerate 并运行受影响回归。

可写 lane 必须有独立可变 worktree/workspace。指向共享项目源码的非 Git `hash-snapshot` lane 在获得带基线 hash 的独立复制工作区前只能只读/构建。只检查 build/evidence 目录唯一性的 lane audit 不充分。

## 可执行协作门禁

涉及目标操作时，调用 `$mcu-development-lifecycle` 并读取 `references/executable-engineering-gates.md`。为规范 board profile、PDF 差异关闭、固件哈希、治具/仪器、发布批准和生产锁定指定负责人；用同一个 `operation_id` 串联 sidecar 审计和证据，任何身份或证据门禁阻断时禁止交接。

所有跨团队变更从生命周期 Skill 的 `team-workspace-contract.md` 开始。必须记录唯一 `change_id`、影响分级、请求人、责任人、独立评审人、影响变体、关闭证据和有期限的例外。高风险、目标硬件、生产、发布或安全锁定工作禁止请求人自批。

硬件操作前校验持久化 approval record、scope、variant/configuration/artifact hash、独立身份和有效期，并要求 team audit 与 board/port/probe/fixture/instrument lease 通过。按每个目标 workflow 单独计算独立审批 quorum，不得跨 workflow 拼接审批人数；flash 和 telemetry-capture 的全部批准必须对同一固件 SHA-256 达成一致。非空 `change_id` 或 `approval_id` 字符串不代表已批准。

## 跑中改进交接

流程执行中出现门禁误通过、可重复故障、反复人工绕行、目录混放或实际工具面与本 Skill 不一致时，调用 `$mcu-continuous-improvement`。项目专有证据保存在 lane 运行目录；只有已复现并有回归保护的通用模式才提升到中央持续改进 Skill。

## 参考资料

读取 `references/collaboration-standard.md` 获取单一事实源、RACI、节奏、变更分级和关闭规则。

读取 `references/team-operating-model.md` 获取角色、协作节奏和 RACI；读取 `references/review-handoff-templates.md` 获取评审和交接模板；读取 `references/parallel-workspace-lanes.md` 获取 lane 隔离、所有权、租约、合并和关闭规则。

## 脚本

## PDF 证据门禁

把每个 `mcu-pdf-dual-verification` manifest 作为 PDF 来源 MCU 事实的单一评审记录。明确 Poppler 提取、Codex PDF 视觉复核、差异关闭和下游批准负责人；gate 为 pending、fail 或哈希失效时禁止交接。

使用 `scripts/check_team_collaboration.py <project-root>` 审计团队协作证据，例如 RACI、决策记录、评审发现、交接、变更控制、度量和复盘。
