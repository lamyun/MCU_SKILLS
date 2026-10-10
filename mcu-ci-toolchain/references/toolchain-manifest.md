# MCU 工具链清单

固定工具、创建构建清单或准备发布证据时使用本参考。

## 清单字段

```text
项目：
清单版本：
负责人：
支持的主机 OS：
编译器：
编译器版本：
SDK/HAL：
RTOS：
构建系统：
代码生成器：
代码生成器可执行文件/版本：
选中平台/环境状态：
环境发现来源顺序：
环境组件路径/版本/来源：
Keil MDK/μVision/编译器/许可证状态：
Keil target/Pack/scatter/工程 hash：
ESP-IDF framework revision/idf.py/Python/tools 根：
ESP target/sdkconfig/dependency lock：
STM32 firmware package/版本：
CubeMX `.ioc` 路径/SHA-256：
生成参数/manifest SHA-256：
生成输出树摘要：
烧录/调试工具：
Python 或脚本运行时：
静态分析工具：
格式化工具：
板卡目标：
构建配置：
环境变量：
外部包来源：
校验和：
已知不兼容项：
Protocol/payload schema 版本：
PC collector/storage/replay 版本：
Lane/build/evidence 根策略：
```

## 版本固定规则

- 发布构建必须固定编译器、SDK/HAL、RTOS、代码生成器和烧录工具。
- 记录生成代码是提交进仓库，还是在构建时生成。
- 构建脚本不得依赖开发者本机绝对路径。
- 需要可复现时，记录工具下载来源或包哈希。
- 相关第三方包需要记录许可证或出口管制约束。
- 选中平台必须为 `complete`；未选中的 `partial` 环境只保留清单告警。
- Keil 发现阶段许可证记录为 `not-checked`；只有真实批构建才能增加许可证/工具链可用性证据。
- 只有 Espressif 工具而没有 framework 及 framework 自带 `idf.py`，不能判定为可构建 ESP-IDF 环境。

## 制品命名

优先使用能编码身份的信息：

```text
<product>_<board>_<config>_<version>_<source>.<ext>
```

示例：

```text
controller_revB_release_fw-v1.4.2_gabc1234.bin
```

## Size 预算表

| 目标 | 配置 | Flash 限制 | RAM 限制 | 栈策略 | 负责人 |
| --- | --- | --- | --- | --- | --- |

## 发布证据

每个发布归档应包含：

- 清单快照。
- 构建命令。
- 源码版本。
- 制品哈希。
- map 和 size 报告。
- 构建日志。
- 测试报告链接。
