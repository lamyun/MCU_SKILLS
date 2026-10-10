---
name: mcu-safety-security-compliance
description: "嵌入式 MCU 安全、可靠性、网络安全和合规技能，用于故障安全、FMEA/STPA、看门狗、诊断覆盖、安全启动/升级、调试口、密钥管理、MCU-PC 遥测/命令安全、数据保留、法规准备、EMC/ESD 软件策略和安全追踪。适用于评审或设计 MCU 安全、数据流、合规、可靠性或认证控制。"
---

# MCU 安全、网络安全与合规

默认不预设 MCU 厂商、系列、具体型号、封装、开发板或工具链。从用户输入、受控 board profile 和现有项目文件解析目标；缺失时明确标为待确认，示例平台只能按条件选用。

## 概览

使用本技能把安全、可靠性和合规要求前置到需求、架构、实现、测试和发布。不要把它当成发布前补文档；安全控制必须能追踪到需求、设计、代码、测试和生产配置。

## 功能安全流程

1. 明确危害、失效模式、触发条件、影响等级和可接受风险。
2. 定义安全状态、降级策略、诊断、报警、恢复和人工介入路径。
3. 对高风险功能建立 FMEA 或等效风险表。
4. 将安全需求分配到硬件、固件、测试和生产流程。
5. 对每项控制提供验证证据：故障注入、边界测试、长稳、生产测试或分析。

## 网络安全流程

1. 建立威胁模型：资产、攻击者、接口、攻击路径、影响。
2. 定义安全启动、镜像签名、版本回滚限制、密钥存储和调试口策略。
3. 设计 OTA 或现场升级的认证、完整性、断电恢复和回滚。
4. 最小化调试、日志和生产工具泄露敏感信息的风险。
5. 将安全配置纳入发布和量产证据，不只写在设计文档里。

## 合规流程

- 明确目标标准或客户要求，例如功能安全、信息安全、EMC、无线、医疗、工业或车规相关要求。
- 将法规条款转成项目可执行的需求和测试。
- 保留评审、分析、测试、版本、工具链和生产记录。
- 对第三方库、SDK、协议栈、加密库和许可证做清单管理。
- 对偏离项记录理由、影响、批准人和补偿措施。

## 评审重点

- 故障是否能进入已定义安全状态。
- 看门狗是否检测真实任务进展，而不是无条件喂狗。
- 调试口、读保护、Option Bytes 或熔丝是否与生产策略一致。
- 密钥、序列号、校准和客户配置是否可追踪且不泄露。
- 升级失败、掉电、版本不兼容和回滚限制是否经过测试。
- 安全相关需求是否能追踪到测试和发布证据。

## MCU-PC 安全与网络安全

所有 PC 到 MCU byte stream 都按不可信输入处理。分配内存前执行 framing 和 length bounds，拒绝未知 major version，限制畸形流量速率，把 parser 隔离于 safety-critical/control-loop context，并证明 disconnect/flood/backpressure 不会饿死 watchdog 或控制任务。

CRC 只检测意外损坏，不能认证发送方或防止 replay。命令默认只读；改变状态的命令需要 allowlist、与产品风险相符的授权、范围/速率限制、幂等 request ID 或 anti-replay state、safe-state check 和 audit correlation。

对 JSONL/SQLite 遥测进行 privacy、secret、customer data、retention、redaction、export、deletion 和 access-control 分类。常规遥测禁止包含 key 或不受限制的敏感 memory/register dump。Synthetic/replay/host 证据必须与 identified-target 和 real-HIL 分离。

## 可执行安全门禁

调用 `$mcu-development-lifecycle` 并读取 `references/executable-engineering-gates.md`。不可逆控制前执行生产安全门禁：先 program/verify，再 provision identity、enable secure boot、set readout protection、lock debug，最后 final verification。必须有显式授权、回滚边界、审计关联和真实 HIL；mock 证据不能批准锁定。

## 跑中改进交接

流程执行中出现门禁误通过、可重复故障、反复人工绕行、目录混放或实际工具面与本 Skill 不一致时，调用 `$mcu-continuous-improvement`。项目专有证据保存在 lane 运行目录；只有已复现并有回归保护的通用模式才提升到中央持续改进 Skill。

## 参考资料

## PDF 证据门禁

由 PDF 原理图或手册支撑的安全、网络安全和合规结论必须有 `$mcu-datasheet-extraction` 通过的 Poppler + Codex PDF manifest。pending、哈希失效或存在差异时属于未关闭危险/证据缺口，不得用于证明控制项、诊断覆盖率或生产锁定决策。

读取 `references/safety-analysis.md` 获取安全风险模板；读取 `references/security-compliance.md` 获取网络安全、合规和生产控制提示。
