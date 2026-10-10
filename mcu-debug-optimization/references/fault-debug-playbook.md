# MCU 故障调试手册

诊断崩溃、复位、卡死、内存破坏和现场故障时使用本参考。

## 第一响应

- 固定失败固件版本、硬件版本和测试条件。
- 尽可能在断电前保存日志。
- 记录复位原因、fault 寄存器、栈指针、任务状态和看门狗状态。
- 询问最近变更：代码、编译器、SDK、硬件、电源、环境、负载。

## HardFault 和 CPU Fault

采集：

- PC、LR、SP、xPSR。
- 可用时采集 CFSR、HFSR、DFSR、AFSR、MMFAR、BFAR。
- 当前活动中断号。
- 当前任务和栈高水位。
- 用于地址解析的 map 文件或符号文件。

检查：

- 无效函数指针或返回地址。
- 不支持的非对齐访问。
- 栈溢出。
- NULL 指针或野指针。
- 访问未使能外设或非法内存。
- FPU 上下文或 ABI 不匹配。

## 卡死和看门狗复位

检查：

- 哪个任务停止推进。
- 队列、互斥锁、信号量和事件状态。
- 长临界区或长时间关闭中断。
- 无超时的阻塞 I/O。
- 优先级反转。
- 嵌套锁导致的死锁。

## 内存破坏

检查：

- 栈溢出和任务栈大小。
- DMA 写出缓冲区边界。
- 环形缓冲区满/空逻辑。
- 如果使用动态内存，检查 use-after-free。
- 没有所有权约束的并发写。
- 持久化参数迁移和长度校验。

## 通信故障

检查：

- 电气层和时序。
- 错误计数器和状态寄存器。
- ISR overrun 或环形缓冲区溢出。
- 超时和恢复路径。
- 协议解析器对部分帧、非法帧和突发帧的处理。

## 调试输出

好的调试报告应包含：

- 复现步骤。
- 已采集证据。
- 已验证假设。
- 根因。
- 修复。
- 新增回归测试。
- 剩余风险。

## MCU-PC 数据流分诊

把 firmware build/protocol/schema 和 MCU queue/DMA/drop/reset counter，与 PC connection/parser/quarantine、JSONL、SQLite-WAL、disk/backpressure 和 replay record 关联。先确定第一个失败阶段，并用不可变 capture 复现，再改 target code。报告贯穿 `change_id`、`lane_id` 和 `run_id`。
