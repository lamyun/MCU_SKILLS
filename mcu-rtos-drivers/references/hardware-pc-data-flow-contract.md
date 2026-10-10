# MCU 到 PC 数据流契约

UART、USB CDC 或其他 byte stream 上建立可观测、可回放 MCU-PC 链路时使用本参考。线协议、collector schema、storage schema 和 replay 行为必须协同版本化。

## 端到端链路

每一段都定义明确所有权：

```text
sensor/control source -> ISR/DMA capture -> bounded queue -> telemetry task
-> bounded TX/ring buffer -> UART/USB DMA -> PC reader -> frame validator
-> append-only JSONL/raw archive -> SQLite-WAL index -> replay/analysis
```

控制环不得等待遥测、host 连接、存储或日志。实现前先定义队列容量、最大帧/载荷、速率预算、丢弃策略、重试、超时和诊断计数器。

## 线协议帧

新 byte-stream 协议优先使用 COBS 编码和 `0x00` 分隔符，使接收端能从半帧或损坏数据重新同步。解码后的帧必须声明字节序并至少包含：

| 字段 | 最小用途 |
| --- | --- |
| `magic` | 排除无关流量 |
| `protocol_major`, `protocol_minor` | 兼容性判定 |
| `message_type`, `flags` | 载荷解释 |
| `header_length`, `payload_length` | 严格边界检查 |
| `sequence` | 检出丢包、重复和乱序 |
| `boot_id` 或 session ID | 区分设备重启 |
| `device_time_us` | 设备单调时间戳 |
| payload | 版本化消息数据 |
| CRC-32 | 检测解码后 header + payload 的意外损坏 |

在 protocol schema 中固定字段宽度、字节序、最大解码长度、CRC polynomial/init/reflection 规则和精确覆盖范围。CRC 只检测传输损坏，不等于身份认证。

每次连接先发送 `HELLO`/`DEVICE_INFO`，携带支持的协议范围、device/board identity、firmware build ID/hash、reset/boot ID、schema IDs、能力和最大载荷。未知 major version 必须拒绝或隔离；只有兼容 major version 内才能协商可选行为。

## MCU 运行规则

- 接收和发送缓冲区采用静态分配或有边界内存池。
- ISR/DMA callback 只做最小采集，组帧和发送由单一 owner task 完成。
- 不得无限等待 host flow control；明确使用 drop-oldest、drop-newest、aggregate 或 reduce-rate 等策略。
- 暴露 produced、sent、dropped、queue high-water、DMA error、CRC/parser error、reconnect、sequence gap 和 device reset 计数器。
- 电缆断开、host 变慢或持续输入畸形数据时，仍要保证 watchdog 和 control loop 健康。
- PC 到 MCU 命令默认只读；任何改变状态的命令都需要显式授权、范围/速率限制、幂等 request ID 和审计记录。

## PC Collector

Collector 必须：

1. 接收数据前绑定预期 device 和 protocol contract。
2. 增量读取，按分隔符重新同步，并在解析载荷前限制全部内存分配。
3. 附加 host UTC 接收时间和 host monotonic time，但不得覆盖设备时间戳。
4. 使用有边界 exponential backoff 重连；新连接创建新记录，不得合并不同 `boot_id`。
5. 策略允许时，把被拒绝帧和原因写入有边界 quarantine stream。
6. 改变状态的命令必须在记录提交后才确认完成。

使用 append-only JSONL 作为可移植证据日志。每条记录包含 schema version、raw frame 编码/hash、解码字段、校验状态、device/build identity、connection ID 和 correlation IDs。按大小/时间轮转并生成索引与 SHA-256 manifest；禁止改写旧证据来使门禁通过。

使用 SQLite 作为查询/索引层，启用 WAL，固定 schema version，使用事务，对 `(device_id, boot_id, sequence, message_type)` 等稳定 event key 建立唯一约束，并保留 migration journal。JSONL/raw evidence 保持权威，以便重建数据库和验证迁移。

## 回放契约

Replay 消费不可变 capture，以及固定的 protocol schema、collector version 和 storage schema，并必须：

- 相同输入重复运行时产生相同规范化事件和稳定结果哈希。
- 保留设备顺序、gap、duplicate、reset、validation failure 和原始时间戳。
- 支持 real-time、accelerated 和 step 模式，但不得改变解码内容。
- 除非另有显式批准模式，否则不得打开物理串口或向 MCU 发命令。
- 使用新的 `run_id` 写 replay 输出，禁止与真实硬件证据混合。

## 关联标识和证据等级

贯穿 `project_id`、`change_id`、`lane_id`、variant、firmware build ID/hash、protocol/schema version、collector/storage version、`run_id`、device ID、可用时的 board serial，以及受控硬件会话的 `operation_id`。

准确报告证据等级：

- `generated`：存在 CubeMX/配置产物。
- `built`：固件/host 软件已编译并记录哈希。
- `host-verified`：parser、collector、persistence、migration 和 replay 通过合成或既有记录测试。
- `target-observed`：从已识别 target 捕获到数据，但可能仍不满足完整 HIL。
- `real-hardware-hil`：受控 board/fixture/instrument manifest 和原始证据通过全部硬件门禁。

禁止把 mock、synthetic、replay、仅串口可见或 host test 升级为 `real-hardware-hil`。
