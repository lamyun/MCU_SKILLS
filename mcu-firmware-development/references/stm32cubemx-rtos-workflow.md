# STM32CubeMX 与可选 RTOS 工作流

创建或重新生成任一受 CubeMX 支持的 STM32 工程时使用本参考。默认不选择 RTOS；仅当 `.ioc`、项目 manifest、受控 variant 或显式用户输入声明 RTOS identity 时，才加载对应 RTOS adapter。把代码生成当作可复现构建步骤，不得作为一次性交互操作。

## 选型前先探测

创建工程前记录实际探测值：

- STM32CubeMX 可执行文件路径、产品版本及该版本支持的命令行模式。
- 项目所需 STM32Cube firmware package 路径、精确版本和可用时的 package 校验和。
- 从本机 CubeMX 数据库选出的精确 STM32 型号/封装或板卡；系列由项目输入决定。
- 生成工程使用的编译器、构建系统及版本。
- 项目声明的 RTOS identity、mode、kernel/wrapper 版本；裸机项目明确记录 `rtos: none`。
- 调试传输、SWD 引脚、控制台/遥测外设、引脚、波特率、DMA 和 IRQ 分配。

请求的目标不可用时，禁止用相近型号、板卡、封装、firmware package 或示例工程替代；把缺失输入记录为 `blocked`。

## 受控输入

下列输入必须进入版本控制或治理证据索引：

- 作为 CubeMX 配置唯一真源的 `.ioc` 文件。
- 生成器 manifest：CubeMX 路径/版本、项目所选 STM32Cube package/版本、精确 MCU/封装/板卡、工程类型、生成参数、host OS 和哈希。
- board profile、链接布局、项目声明的 RTOS 配置、协议 schema 和生成代码 ownership policy。
- 可复现生成命令；如果已安装版本没有可用 CLI，则记录精确 GUI 步骤和最终 `.ioc` 哈希。

禁止手写 HAL/CMSIS 工程并把它描述成 CubeMX 生成证据。GUI 生成仅在输入/输出均有记录且后续能进行 clean regeneration 对比时有效。

## 生成顺序

1. 探测工具并选择项目要求的精确已安装 STM32 目标；除非存在已审批硬件决策，否则保留该目标支持的调试接口。
2. 在 `.ioc` 中配置时钟、GPIO、项目所需传输、DMA/IRQ、可选 RTOS、内存、任务和构建选项；裸机项目不得被自动补入 RTOS。
3. 保存并哈希 `.ioc`，在生成前固化 generator manifest。
4. 使用已探测的 CubeMX 接口生成到 lane 独立的干净目录，保留 stdout、stderr、退出码和输出树哈希。
5. 应用、协议、PC 存储接口和可测试逻辑放在生成目录之外；不可避免的生成文件修改只能放进供应商 `USER CODE` 区域。
6. 通过团队唯一构建入口构建，归档 ELF/BIN/HEX/MAP、size、日志、哈希和工具版本。
7. 在第二个干净目录再次生成并比较规范化文件树；无法解释的差异必须把门禁标为 `fail`。

## 目标相关评审

- 根据 `.ioc` 和构建结果核对精确型号/封装、CPU/FPU、Flash/RAM、startup、linker、vector table 和系统时钟；不得套用其他系列参数。
- 保留 SWD 引脚，确认遥测引脚不与 debug、boot、oscillator、motor-control、ADC、comparator、op-amp 或 timer 冲突。
- RTOS 已声明时，记录 kernel/wrapper 版本、tick source、内存策略、静态/动态分配策略、中断优先级边界、任务表、栈预算和队列深度；具体检查器由 RTOS identity 路由。
- 高频遥测不得在控制环 ISR 内完成；把组帧和传输移到有边界的 task/DMA 路径。
- CubeMX 生成成功只证明配置产物已生成，不证明编译、目标运行、电气行为或 HIL。

## 生成代码所有权

至少维护以下 ownership map：

| 路径或制品 | Owner | 允许写入方 | 评审 |
| --- | --- | --- | --- |
| `.ioc` | 平台 owner | 活动 codegen lane | 固件 + 硬件 |
| 生成的 HAL/CMSIS/可选 RTOS 文件 | 平台 owner | 固定版本 CubeMX 与对应 RTOS adapter | generated-drift gate |
| 供应商 `USER CODE` 区域 | 模块 owner | 已声明固件 lane | 代码评审 + 重新生成 |
| 应用和协议模块 | feature owner | 对应 lane | 常规代码评审 |
| linker/startup 输出 | 平台 owner | generator 或已声明 override | 内存映射评审 |

同一个 `.ioc` 和 variant 只能存在一个未过期代码生成租约。不同 lane 可以并行构建和测试，但不得并发重新生成同一目标。

## 漂移门禁

以下任一条件成立时门禁失败：

- `.ioc`、CubeMX 版本、项目所选 STM32Cube package、目标或生成参数未固定。
- 生成文件在获批 `USER CODE` 区域之外存在无法解释的修改。
- 未修改受控输入时，clean regeneration 仍产生差异。
- 生成过程触碰其他 lane 的构建/证据目录或项目根外文件。
- 生成目标、startup、linker、RTOS identity/mode 或调试配置与批准 variant 不一致。

每次接受生成都记录 `project_id`、`change_id`、`lane_id`、variant、源码版本、`.ioc` SHA-256、generator manifest SHA-256、输出树摘要、build ID 和证据路径。
