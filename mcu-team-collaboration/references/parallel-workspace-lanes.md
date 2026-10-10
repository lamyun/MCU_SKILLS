# 并行工作区 Lane

多个 Codex task、工程师、worktree 或 build job 并发开发同一 MCU 产品时使用本参考。独立软件工作可以并行，代码生成和物理资源必须串行。

## Lane 契约

每个活动 lane 登记：

```yaml
schema_version: 1
lane_id: LANE-firmware-001
project_id: PROJECT-001
change_id: CHG-001
owner: user:firmware-owner
role: firmware
branch: feature/CHG-001-firmware
workspace_root: <governed-worktree-or-workspace>
build_root: <lane-private-build-root>
evidence_root: <lane-private-evidence-root>
owned_paths: [firmware/app, firmware/middleware]
leases: []
heartbeat: <UTC timestamp>
expires: <UTC timestamp>
status: active
```

机器状态使用稳定 ID 和规范绝对根路径，治理记录使用项目相对路径。拒绝路径穿越、没有显式共享 owner 的重叠可写根、已过期 lane，以及被另一个 change 复用的 lane ID。

## 推荐角色

- Coordinator/integrator：负责契约、路由、checkpoint、冲突处理和最终门禁。
- Platform/codegen lane：负责 `.ioc`、生成 HAL/CMSIS/项目声明的可选 RTOS、startup、linker 和 generator manifest。
- Firmware lane：负责应用和非生成 middleware。
- Host lane：负责 protocol tooling、collector、storage、replay 和 host tests。
- Verification lane：负责独立测试、fixture、report 和证据复核。

小项目可以合并角色，但每项制品仍只能有一个 accountable owner，高风险工作保留独立验证。

## 隔离规则

- 每个 lane 使用不同 worktree/workspace、branch、build、temporary、log 和 evidence staging 目录。
- 活动 lane 之间禁止共享 CMake/Ninja/Make 输出、CubeMX 临时输出、Python virtual environment 变更、串口 capture、SQLite 文件或测试结果目录。
- 不可变证据只能追加。由 coordinator 发布已接受的 lane 证据，并带 `lane_id`、`change_id`、源码版本、哈希和 supersession 链接。
- 重要状态不得只留在聊天中；必须更新 lane registry、handoff、decision record 和 checkpoint。

## 所有权与合并规则

- 路径 ownership map 是门禁，不是建议。lane 需要修改其他 owner 的路径时必须请求 handoff 或协同变更所有权。
- 同一 variant 的租约有效时，只有 platform/codegen lane 能修改 `.ioc` 或运行 CubeMX。
- 应用逻辑放在生成路径之外。不可避免的 `USER CODE` 修改必须记录 owner，并证明 clean regeneration 后仍保留。
- 集成前，每个 lane 都基于约定基线完成 rebase/merge，在私有干净目录构建、运行必需测试并发布 handoff。
- `.ioc`、CubeMX 版本、firmware package、generated file、linker 或 startup 变更合入后，integrator 必须执行一次 clean regeneration、generated-drift compare、完整构建和受影响回归。

## 资源租约

以下可变或单 owner 资源使用独占租约：

- 按 project + variant 标识的 `.ioc`/CubeMX generation。
- 按稳定 device identity 标识的 serial/USB port，不能只依赖 `COMx`。
- 按 serial number 标识的 debug probe。
- 按 asset ID 标识的 board、fixture、power supply 和 instrument。
- 按 `operation_id` 标识的 hardware workflow。

每个 lease 包含 resource type/ID、project/change/lane IDs、owner、acquired/heartbeat/expires 时间、预期操作和 release result。获取必须是原子的；第二个 owner 收到 `blocked`，不得尝试共享连接。恢复过期 lease 必须审计，并确认没有进程仍持有资源。

只读源码分析、host test 和隔离构建可以无硬件租约并行。物理 probe、reset、flash、serial capture、fault injection、calibration 和 HIL 必须取得相应租约并满足既有审批门禁。

## 交接与关闭

Lane handoff 包含精确源码版本、changed/owned paths、相关 `.ioc` 和 schema 哈希、build/test 命令、制品、证据路径、开放风险和下一 owner。只有在工作已集成或明确放弃、资源已释放、证据已发布、checkpoint 已记录最终状态后才能关闭 lane。
