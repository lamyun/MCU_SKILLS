# Keil MDK 与 ESP-IDF 固件工作流

## 统一入口门禁

调用 `mcu_mcp.detect_embedded_tools`。选中的 `keil_mdk` 或 `esp_idf` 必须为 `complete`；遇到 `SELECTED_PLATFORM_ENVIRONMENT_INCOMPLETE` 立即停止。运行上下文保留发现 path、source、version 和缺失项。环境发现只证明本机软件存在。

产品行为放在 `app`，稳定外设契约放在 `drivers`，板级实例放在 `bsp`，芯片/framework 细节放在 `platform` 或 middleware。IDE 工程文件或 ESP-IDF component registration 不能替代应用架构。

## Keil MDK

- 固定 `.uvprojx`、target、MCU/device、编译器、语言选项、defines、include paths、source groups、scatter/linker 输入、输出命名和 CMSIS-Pack ID/版本。
- `.uvoptx` 默认属于开发者状态，除非项目明确治理其中字段。不得依赖 GUI 上次选中的 target 或本地 Pack 替代。
- 优先 ARMCLANG。需要 ARMCC 时记录遗留原因、版本、迁移负责人、语言限制和最后支持版本。
- 生成的 device/startup/CMSIS 与用户模块分离；审查重新生成差异，拒绝用户区丢失、启动向量、内存映射、FPU/ABI 或中断定义异常变化。
- 使用 μVision 批构建形成软件证据，哈希工程、target manifest、scatter、AXF/ELF、HEX/BIN、MAP 和完整日志。真实构建成功才能补充许可证/工具链可用性证据。
- 禁止用 μVision 下载/调试动作绕过受控烧录。

## ESP-IDF

- 固定 framework revision、ESP target、`CMakeLists.txt`、component manifest、`idf_component.yml`、`sdkconfig.defaults`、已审查 `sdkconfig`、`dependencies.lock`、分区 CSV/BIN、bootloader，以及适用的 secure boot/flash encryption 配置。
- `idf.py set-target` 只能在 lane 私有 workspace 执行并审查其配置变更；build 与 component cache 也必须 lane 私有。
- ESP-IDF 的 RTOS/kernel identity 属于项目 framework 与 `sdkconfig` 证据。identity 明确后，针对精确 target 检查任务优先级、栈单位、core affinity/SMP、ISR 到任务交接、tick、watchdog、heap capability、PSRAM 和 shutdown/reset。
- 应用协议/数据生产与 UART/USB/Wi-Fi/BLE transport 分离，保留 bounded queue、reconnect/backpressure、drop/reset counters、固件身份和可 replay framing。
- `idf.py build` 后哈希应用 ELF/BIN/MAP、bootloader、分区表、sdkconfig、dependency lock、framework revision、project description 和 flash arguments。
- 通用 project step 禁止 `flash`、`monitor`、`erase-flash` 以及 partition/bootloader 上传目标。

两个平台的目标执行都需要精确启用的 board profile、匹配制品 hash、批准、资源 lease 和 `run_hardware_workflow`。构建通过仍只是软件证据。
