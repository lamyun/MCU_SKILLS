---
name: mcu-continuous-improvement
description: "基于证据的 MCU 持续改进 Skill，用于划分项目和运行目录、在流程执行中登记问题、把重复故障或工程摩擦转成回归测试，并将验证后的通用改进提升到 MCU Skills、MCP、Agent、模板或项目标准。适用于 STM32CubeMX、Keil MDK、ESP-IDF、固件、上位机遥测、并行 lane、构建、测试、硬件、HIL、发布、迁移、环境发现和故障处置流程，避免代码、分析、证据和报告混放，也不降低任何门禁。"
---

# MCU 持续改进

默认不预设 MCU 厂商、系列、具体型号、封装、开发板或工具链。从用户输入、受控 board profile 和现有项目文件解析目标；缺失时明确标为待确认，示例平台只能按条件选用。

所有 MCU 运行学习统一使用一个有上限的证据闭环。项目专有内容留在项目运行目录；只有已复现、已有回归保护且可泛化的规则，才进入本 Skill 的 `references/learned-patterns.md`。

## 建立运行目录

1. 在产生分析或证据前，使用五个关联 ID 和 lane owner 调用 `mcu_mcp.initialize_run_workspace`。
2. 遵循 `references/project-directory-contract.md`，分别存放产品分析、硬件分析、固件代码、上位机代码、构建输出、测试、原始证据、报告和改进候选。
3. 保留现有工程布局，不自动移动 CubeMX 生成的 `Core`、`Drivers`、`Middlewares`、startup、linker 或 `.ioc`。
4. 每个可写 lane 使用独立 workspace 和 run root；改进目录不得充当源码树、构建目录、遥测数据库或发布暂存区。

## 跑中观察

出现以下信号时调用 `mcu_mcp.record_improvement_candidate`：误通过、误阻断、缺失门禁、哈希校验缺口、不安全旁路、重复人工绕行、交接不清、能力缺失、可复现的构建/生成/协议/迁移/并发/锁恢复故障、性能退化、文档与真实公开工具面不一致，或厂商环境在缺必需 framework/compiler 时被误判为 complete、安装布局变化导致错误 `not-found`。

候选必须绑定当前关联信息、复现方法和带 SHA-256 的证据，并写明预期行为、影响层、拟增加回归和回滚方式。不得从 Mock、回放、编译结果或未确认板卡中学习硬件事实。

## 评审与提升

在阶段检查点和运行结束时读取 `references/runtime-learning-loop.md`，调用 `mcu_mcp.review_improvement_candidates`。每次进入 reproduced、regression-added、implemented、validated、promoted、blocked 或 rejected 时调用 `mcu_mcp.advance_improvement_candidate`，只追加迁移事件，不重写不可变候选。

只有满足以下条件才提升：证据哈希仍有效；问题可在隔离夹具复现；已排除项目配置和本机环境原因；修复前有失败回归、修复后通过；受影响的 MCP/Skills/Agent/项目兼容检查全部通过；没有降低审批、身份、PDF、租约、HIL、发布或证据边界；已记录 owner 和回滚点。

可复现的严重误通过可单次进入回归阶段；其他模式至少需要两次独立发生或工程评审。单个候选每次运行最多自动修复三轮，之后保留为 `blocked` 并交接，不得无限自循环。

## 单一沉淀入口

`references/learned-patterns.md` 是唯一已审核模式索引，按治理、CubeMX、固件、RTOS、上位机数据流、构建 CI、验证、硬件、安全、发布和协作分类。

不得把原始日志、客户代码、板卡秘密、绝对本机路径或单项目事实写入 Skill。提升条目只保留触发条件、工程不变量、回归、适用范围、受影响组件和候选/运行来源 ID。

## 跨组件规则

只修改源包，不直接改 Codex 安装副本。MCP 改动必须增加 MCP 回归和 stdio 工具发现检查；Agent 改动必须更新对应参考和 100 项控制；领域 Skill 只保留最短路由和不变量，完整学习索引仍集中在本 Skill。全部验证通过且源码/安装哈希一致后才安装。

## 参考

- 初始化或整理目录前读取 `references/project-directory-contract.md`。
- 评审或提升候选前读取 `references/runtime-learning-loop.md`。
- 检查是否已有通用方案时读取 `references/learned-patterns.md`。

MCP 不可用时，使用 `assets/project-directory-policy.yaml` 和 `assets/improvement-candidate.yaml`。
