# MCU CI 流水线

创建、评审或改进 MCU CI 流水线时使用本参考。

## 流水线阶段

1. 环境检查：验证编译器、SDK、RTOS、Python、构建工具和脚本版本。
2. 源码卫生：格式化、lint、生成代码漂移、禁用文件、必要的许可证头。
3. 快速构建：编译主板卡的 debug 和 release 目标。
4. 矩阵构建：编译支持的板卡、bootloader/application 组合和特性配置。
5. 静态分析：运行配置好的分析器，并导出机器可读结果。
6. Host 测试：在无硬件环境运行单元测试、解析器测试、算法测试和状态机测试。
7. Size 分析：将 Flash/RAM/section 使用量与预算和历史基线比较。
8. 制品打包：收集 elf、bin、hex、map、符号、哈希、日志和版本元数据。
9. 目标烟测：可选运行仿真器、模拟器或单板烟测。
10. HIL/回归：对发布分支、夜间构建或高风险变更执行受控阶段。
11. CubeMX 可复现：在 lane 私有干净树按固定 `.ioc` 重新生成并比较规范化输出。
12. Host 数据流：测试 framing/CRC/version bounds、reconnect/backpressure、JSONL、SQLite-WAL migration 和 deterministic replay。

## 失败输出

每个失败阶段应展示：

- 精确命令。
- 工作目录。
- 工具链和 SDK 版本。
- 目标和配置。
- 第一条有用错误和完整日志位置。
- 已生成的制品或证据路径。

## 分支策略

- 功能分支：格式化、编译受影响目标、host 测试。
- 主分支：完整编译矩阵、静态分析、host 测试、size 检查、制品打包。
- 发布分支：主分支检查加 HIL/回归、发布包、可复现证据。
- 热修分支：受影响目标加覆盖该缺陷的回归测试。

## 硬件资源控制

CI 使用真实板卡时：

- 按序列号或治具 ID 使用板卡锁。
- 每次测试前都上电复位或复位到已知状态。
- 保存串口日志、调试器输出、固件版本、板卡 ID 和治具 ID。
- 设置硬超时和恢复步骤。
- 隔离反复产生 flaky 失败的板卡或治具。
- 按稳定 board、port、probe、fixture、instrument identity 原子获取一个 lease，并关联 project/change/lane/operation ID。
- 即使 firmware、host、verification lane 并行构建和测试，硬件 job 仍必须串行。

## 完成定义

流水线达到团队可用时应满足：

- 新开发者可以在本地复现 CI 命令。
- CI 制品足以支持调试，不需要重新运行 job。
- size 和 warning 回归可见。
- 发布制品能关联源码版本、目标和工具链。
- HIL 失败能为固件、硬件和测试团队保留足够证据。
