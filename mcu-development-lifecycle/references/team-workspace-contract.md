# MCU 团队工作区契约

本契约用于多人 MCU 工程。工作目录是一条数字主线，不是文档堆积：每项受控变更都必须连接目标、产品变体、实现、验证、审批、硬件执行、发布和现场闭环。

## 标准目录

```text
project/
  governance/
    project-contract.yaml
    variant-matrix.yaml
    raci.yaml
    risks.yaml
    exceptions.yaml
    changes/
    approvals/
    decisions/
    lanes/
  requirements/
  architecture/
  hardware/{schematics,pcb,bom,bringup}/
  firmware/{app,bsp,drivers,middleware,platform,include,tests}/
  host/{protocol,collector,storage,replay,tests}/
  configuration/{boards,products,toolchains,cubemx,protocols}/
  tests/{unit,integration,sil,hil,regression,stress}/
  lab/{assets,reservations,calibration,runs}/
  manufacturing/{programming,calibration,test-limits,provisioning}/
  field/{releases,incidents,telemetry,capa}/
  evidence/{pdf,builds,tests,hardware,dataflow,releases}/
  evidence/index.jsonl
  ci/
  tools/
  reports/
  .mcu-mcp/{project_state.yaml,handoff.md,decision_log.md,run_history.jsonl,machine_index.json}
```

已有项目如果具备同等的所有权和追溯能力，不应为了匹配目录而搬迁；应在 `governance/project-contract.yaml` 中记录映射。

## 项目和变体契约

项目契约至少包含 `schema_version`、不可变 `project_id`、产品/工程/安全负责人、事实源、生命周期等级、支持变体、必经门禁、证据保留策略和发布权限。身份应使用组织账号或稳定 ID，不使用显示名称。

每个变体必须绑定 board profile、板卡/PCB/BOM 版本、MCU/封装、Bootloader/应用布局、工具链摘要、功能配置摘要、原理图 PDF manifest、SVD 版本、测试计划、生产限值和发布兼容性。CubeMX/数据流变体还要绑定 `.ioc` SHA-256、CubeMX 与 STM32 firmware package 版本、generator manifest 摘要、项目声明的 RTOS identity/mode/version、protocol/payload schema、PC collector、storage schema/migration 版本和兼容窗口。发布证据禁止使用 `latest`、未固定工具链或生成器。

## 变更契约

每项受控变更创建 `governance/changes/CHG-*.yaml`，包含变更 ID、请求人、责任人、风险、影响文件/变体、负责的 `lane_id`、需求/接口/安全/软硬件/测试/生产/发布/现场影响、所需 Skill、关闭证据、回滚、迁移计划、期限和独立审批。

高风险、目标硬件、发布、生产和安全锁定变更不得由请求人自批。一个 `change_id` 必须贯穿构建、测试、HIL、`operation_id`、审批、例外、发布和现场问题。

## 变更驱动路由

- 产品/需求变更：产品、需求架构、验证和发布影响。
- 原理图/BOM/PCB/MCU/封装/引脚/时钟/电源变更：数据手册、Bring-up、固件/驱动、HIL、安全、发布和制造。
- 固件/驱动/RTOS/链接脚本/启动代码：固件、RTOS、CI、验证、调试，并按风险加入安全。
- `.ioc`/CubeMX/firmware package/generated-code：固件、CI、硬件/引脚、项目声明的 RTOS/驱动影响、clean regeneration、generated-drift comparison 和回归。
- Host protocol/collector/storage/replay：需求/架构、RTOS/驱动、CI、验证、安全/隐私、发布兼容和现场追踪。
- Lane/ownership/lease：团队协作与 CI 隔离评审；可写路径或资源换 owner 后重跑受影响集成门禁。
- 工具链/SDK/HAL/RTOS/生成器：CI、固件、验证、发布可复现性及许可/安全审查。
- 测试/夹具/仪器/限值：验证、团队协作、发布和生产；保留校准和原始数据。
- Bootloader/OTA/密钥/Option Byte/调试锁：需求架构、安全、发布、生产、真实 HIL 和双人审批。
- 仅文档变更：必须证明未改变受控事实或执行输入，否则重新分类。

仅在首次基线、重大架构变更、里程碑和发布认证时运行全部生命周期 Skill；日常变更执行最小充分路由，并记录明确跳过的阶段。

## 证据、审批与实验室

向 `evidence/index.jsonl` 追加不可变记录：证据 ID/类型、`change_id`、`lane_id`、适用时的 `run_id`、变体、源码版本、工具/运行时/schema 版本、路径、SHA-256、生成者、时间、上游输入、证据等级、门禁结果、保留等级和替代记录。禁止覆盖证据来制造通过结果。

高风险变更应分离请求人、实现人、验证人和发布授权人。生产锁定、密钥注入、禁用回滚或破坏性批量操作要求两个不同受控身份。审批只对指定变更、变体、产物/配置哈希和有效期成立；过期例外直接阻断。

硬件运行前预约板卡、夹具、探针和仪器，记录资产 ID、校准状态、夹具版本、供电限制、操作者、起止时间、固件哈希、profile、`change_id` 和 `operation_id`。身份不匹配或故障资产进入隔离；Mock 仅证明编排。

门禁只使用 `pass`、`fail`、`blocked`，并列出控制项、缺失证据、例外、责任人、下一步和稳定报告哈希。

## 并行 Lane 与资源租约

每个活动工作 lane 在 `governance/lanes/` 保存一份契约，包含稳定 `lane_id`、`project_id`、`change_id`、owner、role、branch/workspace、私有 build/evidence 根、owned paths、heartbeat、expiry 和 status。只有可变根不重叠时，build 和 host-test lane 才能并发。

`.ioc`/CubeMX generation、serial/USB port、debug probe、board、fixture 和 instrument 使用原子独占 lease。Lease 绑定 project/change/lane ID 和稳定资源身份，不能只依赖临时 `COMx`；第二个申请者为 `blocked`。集成后执行一次 clean regeneration、generated-drift comparison、完整构建和受影响回归，再关闭 lane。
