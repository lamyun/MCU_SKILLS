---
name: mcu-release-production
description: "嵌入式 MCU 发布量产技能，用于固件与 PC 工具版本冻结、制品管理、protocol/storage 兼容、生产烧录、序列号/校准/配置、工厂测试、Bootloader/OTA/回滚、telemetry/replay 现场诊断和质量闭环。适用于准备 MCU 固件、host collector、schema 或生产资产用于发布、制造、OTA 或现场支持。"
---

# MCU 发布与量产

默认不预设 MCU 厂商、系列、具体型号、封装、开发板或工具链。从用户输入、受控 board profile 和现有项目文件解析目标；缺失时明确标为待确认，示例平台只能按条件选用。

## 概览

使用本技能把工程固件变成可追溯、可生产、可恢复、可维护的发布包。发布必须包含源码、工具链、配置、测试和制品证据。

## 发布流程

1. 冻结范围：需求、缺陷、配置、硬件版本、工具链、目标市场或客户。
2. 清理版本：更新版本号、构建元信息、兼容矩阵、变更记录。
3. 构建制品：bin/hex/elf/map/symbols、配置、签名、哈希、构建日志。
4. 运行发布测试：单元、集成、HIL、长稳、升级/回滚、生产测试抽样。
5. 生成发布包：发布说明、已知问题、烧录说明、回滚说明、证据索引。
6. 建立现场监控：版本分布、故障码、升级成功率、返修和缺陷闭环。

## 量产就绪

量产前确认：

- 烧录工具、脚本、夹具、供电、连接器和工位流程已验证。
- 序列号、密钥、校准参数、区域配置有 owner、格式、备份和追踪。
- 读保护、调试口、Boot 配置、Option Bytes 或熔丝策略已审批。
- 工厂测试能区分硬件故障、烧录故障、校准故障和固件故障。
- 返工、返修、降级和恢复流程已演练。

## OTA 与 Bootloader

涉及现场升级时必须说明：

- 镜像格式、分区布局、版本兼容、签名/校验、断点续传。
- 安装条件：电量、电源、温度、运行模式、业务安全状态。
- A/B、备份区或恢复模式策略。
- 升级失败、掉电、校验失败和启动失败的回滚路径。
- 现场日志和故障码如何帮助远程定位。

## 发布门

发布前输出 yes/no 结论，并列出阻塞项：

- 制品是否可复现。
- 测试是否覆盖发布范围。
- 遗留缺陷是否有风险接受。
- 量产参数是否可追踪。
- 回滚和恢复是否演练通过。

## 数据流发布兼容性

随固件冻结并打包 on-wire protocol schema、payload schema、PC collector、JSONL record schema、SQLite schema/migration、replay tool 和 compatibility matrix。版本与哈希绑定 `project_id`、`change_id`、variant、firmware build 和 release ID。

证明受支持 collector 能读取发布固件，旧 capture 在声明兼容窗口内仍可回放，database migration 使用事务且可恢复，未知 protocol major 会 fail closed 且不破坏证据。Raw/JSONL 证据必须足以重建 SQLite。

禁止从 synthetic/replayed data 声称现场或 HIL 验证；发布证据分别声明 host-verified、target-observed 和受控真实硬件验证范围。

## 现场维护回溯

处理现场问题时不要只给临时修复。必须建立回溯链：

1. 事件归档：事件 ID、现场现象、影响版本、硬件版本、复现条件、日志和故障码。
2. 影响分析：关联需求、设计项、代码模块、测试用例、发布包和生产批次。
3. 根因假设：区分需求遗漏、设计缺陷、实现缺陷、测试逃逸、制造差异、使用环境和配置问题。
4. 处置策略：临时规避、版本回滚、补丁、工厂筛查、现场升级或客户通知。
5. 修复验证：新增回归测试、HIL/长稳/边界测试、发布 gate 和证据路径。
6. 复盘闭环：更新需求、测试、生产说明、支持手册和风险登记。

## 可执行发布门禁

调用 `$mcu-development-lifecycle` 并读取 `references/executable-engineering-gates.md`。生产授权前必须使用 release 专用 v2 profile，执行 `run_engineering_gates`，校验带哈希的真实硬件 HIL manifest、ELF/BIN/MAP/SBOM/签名，并按规定顺序完成安全锁定。禁止只接受 `hil_passed: true`。

## 跑中改进交接

流程执行中出现门禁误通过、可重复故障、反复人工绕行、目录混放或实际工具面与本 Skill 不一致时，调用 `$mcu-continuous-improvement`。项目专有证据保存在 lane 运行目录；只有已复现并有回归保护的通用模式才提升到中央持续改进 Skill。

## 参考资料

## PDF 证据门禁

发布或量产烧录前，对板卡 profile、生产测试、Option Bytes 方案或治具所依赖的每个原理图/手册事实重新运行 `inspect_pdf_evidence`。归档所有通过的 Poppler + Codex PDF manifest；源文件/渲染页哈希变化或仍有差异时阻断发布。

读取 `references/release-checklist.md` 获取发布证据要求；读取 `references/manufacturing-pack.md` 获取生产烧录、校准和工厂测试包结构；读取 `references/field-maintenance-traceability.md` 获取现场事件回溯模板。
