# MCU Firmware Standard

Use this reference when creating, refactoring, or reviewing MCU firmware.

## Layers

- `platform`: startup, linker script, interrupt vector, clock tree, system tick, chip-level configuration.
- `bsp`: board revision, pin map, board power controls, external device instances.
- `drivers`: peripheral and device drivers with stable APIs.
- `middleware`: protocols, logging, parameters, diagnostics, file systems, update support.
- `app`: product states, control logic, user workflows, policy decisions.

Keep dependencies one-way: `app -> middleware -> drivers -> bsp/platform`. Lower layers must not call product-specific app code.

## Module API Rules

- Use clear init/config/start/stop/read/write/status functions.
- Return typed status or error codes from public APIs.
- State which APIs are callable from ISR context.
- State ownership of buffers passed into asynchronous functions.
- Every blocking API must take timeout or document why it cannot block.
- Every module should expose enough status for diagnostics.

## Error Handling

- Distinguish invalid argument, busy, timeout, hardware fault, protocol error, and unsupported operation.
- Count recurring errors in diagnostic counters.
- Provide recovery actions for external-device and bus errors.
- Avoid silent retries without a limit or observable counter.
- Preserve root-cause data before resetting.

## Configuration

- Store product configuration separately from compile-time hardware constants.
- Version persistent parameters and define migration behavior.
- Validate configuration with range checks and checksum or signature where appropriate.
- Define factory defaults and safe fallback defaults.

## Build And Toolchain

- Record compiler, SDK/HAL, RTOS, linker script, board target, and optimization level.
- Make build outputs include version, git revision or source ID, board target, and build timestamp if allowed by reproducibility rules.
- Treat warnings as actionable; document any suppressed warning.
- Keep generated code isolated and do not mix hand edits into generated regions.
- STM32CubeMX 工程把 `.ioc`、CubeMX/STM32 package 版本、生成参数和输出树摘要作为受控输入。
- 生成文件只允许在已声明 `USER CODE` 区域修改；应用/协议逻辑放在生成目录之外。
- 每个 project variant 只有一个 codegen owner/lease；`.ioc` 或生成器变化后执行 clean-regeneration comparison。

## Code Review Focus

- Unit consistency: ms/us/ticks, bytes/words, ADC counts/volts.
- Integer overflow and signed/unsigned conversion.
- Buffer bounds and ring buffer full/empty handling.
- ISR/task shared data and memory barriers.
- Initialization order and deinitialization paths.
- Low-power transitions and peripheral resume.
- Watchdog responsibility and fault containment.
