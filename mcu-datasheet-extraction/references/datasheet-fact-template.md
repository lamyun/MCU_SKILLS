# 芯片手册事实提取模板

使用本模板规范化 MCU datasheet 和 reference manual 中的工程事实。

## 源文档清单

| Source ID | 文档标题 | 文档类型 | 版本/日期 | 页码范围 | PDF SHA-256 | 双验证 manifest/gate | 置信度 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-001 |  | datasheet / reference manual / errata / schematic / app note |  |  |  | 路径 / pass, pending, fail | high / medium / low |

## 器件身份

| 字段 | 提取值 | 来源 | 备注 |
| --- | --- | --- | --- |
| 精确型号 |  |  |  |
| 封装 |  |  |  |
| Flash/RAM |  |  |  |
| 温度等级 |  |  |  |
| 工作电压 |  |  |  |
| 硅版本 |  |  |  |

## 引脚和复用事实

| Pin | 封装脚号 | GPIO | 功能 / AF | 电气模式 | 复位/默认状态 | 冲突/风险 | 来源 |
| --- | --- | --- | --- | --- | --- | --- | --- |

## 外设能力事实

| 外设 | 实例/通道 | 能力 | 限制或条件 | DMA/IRQ | 实现提示 | 来源 |
| --- | --- | --- | --- | --- | --- | --- |

## 电气和时序事实

| 参数 | Min | Typ | Max | 单位 | 条件 | 设计影响 | 来源 |
| --- | --- | --- | --- | --- | --- | --- | --- |

## 勘误和限制

| ID | 受影响模块 | 条件 | 影响 | 规避措施 | 需要验证 | 来源 |
| --- | --- | --- | --- | --- | --- | --- |

## 交接

| 下游领域 | 需要交接的事实 | 建议 skill |
| --- | --- | --- |
| 需求 / MCU 选型 |  | `$mcu-requirements-architecture` |
| 硬件 / 引脚复用 |  | `$mcu-hardware-bringup` |
| 固件 / 寄存器 |  | `$mcu-firmware-development` |
| RTOS / DMA / ISR |  | `$mcu-rtos-drivers` |
| 测试 / 时序限值 |  | `$mcu-verification-test` |
