# MCU HIL 与回归

设计硬件在环和回归套件时使用本参考。

## HIL 优先级

优先覆盖 host 测试难以证明的内容：

- 真实传感器和执行器时序。
- 掉电、欠压、复位和唤醒。
- 总线故障、设备断开、线路卡死和非法帧。
- Bootloader、升级、回滚和版本兼容。
- 长时间运行、温度或电压边界。
- 生产烧录和校准流程。

## HIL 证据

记录：

- 固件制品和哈希。
- 板卡序列号和硬件版本。
- 治具版本和接线。
- 仪器型号/配置。
- 输入激励和时序。
- 原始日志、trace、截图和结果摘要。

## 回归套件

应包含：

- must-have 需求烟测。
- 每个已修复缺陷的可复现测试。
- 高风险时序、内存、功耗和通信测试。
- 如果存在现场升级，则包含升级和回滚测试。
- 生产烧录和校准 sanity 检查。

## Flaky 测试分类

将 flaky 分类为：

- 产品行为不稳定。
- 测试治具不稳定。
- 测试脚本竞争或超时。
- 仪器/环境噪声。
- 需求或阈值不清晰。

不要在没有保留其覆盖风险的情况下删除 flaky 测试。

## 证据等级边界

Synthetic frame、parser test、JSONL/SQLite 和 replay 只能证明 `host-verified`。已识别 target 的串口 sample 可证明 `target-observed`。只有通过的受控 board/fixture/instrument manifest 和带哈希原始证据才是 `real-hardware-hil`。
