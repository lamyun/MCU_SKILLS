# 多厂商环境工作流

## 发现契约

调用既有 `mcu_mcp.detect_embedded_tools`，读取 `environments.stm32`、`environments.keil_mdk`、`environments.esp_idf`、组件 path/source/version 和 `selection_gate`。发现优先级固定为配置、环境变量、PATH、Windows 注册表、有限常见目录。

`auto` 只用于盘点。构建前显式选择 `stm32`、`keil_mdk` 或 `esp_idf` 并要求 `complete`。`partial` 表示发现了部分软件，但不满足平台构建契约。相邻目录、命令包装器或安装缓存不能替代缺失组件。

## 完整性要求

| 平台 | `complete` 必需项 | 可选清单 |
| --- | --- | --- |
| STM32 | CubeMX、Java、ARM GCC、CMake、Ninja、固件仓库、已配置固件包 | 下载和调试工具 |
| Keil MDK | μVision，以及 ARMCLANG 或明确声明的遗留 ARMCC | Pack 根；具体 Pack 在项目门禁检查 |
| ESP-IDF | Framework、其 `tools/idf.py`、Python、CMake、Ninja、Xtensa/RISC-V 编译器之一 | ESP OpenOCD 和另一编译器族 |

Keil 发现不验证许可证。Espressif 工具存在但缺 ESP-IDF framework 与 `idf.py` 时必须为 `partial`。

## 构建门禁

Keil 固定 `.uvprojx` hash、target、编译器、Pack ID/版本、scatter、defines、include paths、μVision 批构建命令/日志和 AXF/ELF/HEX/MAP hash。IDE 下载选项不能作为构建步骤。

ESP-IDF 固定 framework version/revision、Python 环境、工具版本、target、`sdkconfig.defaults`、最终 `sdkconfig`、组件/依赖锁、分区表、bootloader、应用 ELF/BIN/MAP 和 flash arguments 证据。`set-target`、reconfigure 和 build 只能写 lane 私有目录；通用项目步骤禁止 `flash`、`monitor` 和 erase。

每个 lane 独占 source workspace、build tree、cache、log、evidence 和可写 telemetry store。选中平台不完整返回 `SELECTED_PLATFORM_ENVIRONMENT_INCOMPLETE`；公开控制面缺能力返回 `MCP_CAPABILITY_MISSING`。

环境与构建仍只是软件证据。板卡身份、目标访问、烧录、串口采集、HIL 和发布必须通过各自治理证据。
