# MCU Bring-up Checklist

Use this reference for first power, board smoke tests, and hardware/firmware integration.

## Before Power

- Record board ID, PCB revision, BOM revision, assembly notes, and visible defects.
- Inspect polarity-sensitive parts, solder bridges, missing parts, connectors, and jumpers.
- Measure resistance from each power rail to ground.
- Set bench supply current limit.
- Decide which loads or jumpers stay disconnected for first power.

## First Power

- Apply power with current limit.
- Record input current and each rail voltage.
- Check regulator enable pins, reset line, boot pins, and temperature.
- Capture ripple or startup waveform for critical rails.
- Stop if current exceeds expectation or a device heats unexpectedly.

## MCU Access

- Connect debugger with target voltage sense and reset.
- Read chip ID.
- Mass erase or unlock if safe.
- Program a minimal image.
- Verify reset, halt, step, and run.
- Record option bytes or security configuration.

## Minimal Firmware

- Toggle a known GPIO.
- Print UART or SWO log if available.
- Read reset reason.
- Start system tick.
- Exercise watchdog in a controlled way.
- Save build version in output logs.

## Peripheral Bring-up

For each peripheral record:

| Peripheral | Pins | Test firmware | Expected | Result | Evidence | Issue |
| --- | --- | --- | --- | --- | --- | --- |

## Stop Conditions

- Unexplained high current or overheating.
- Unstable reset or power rail.
- Debug interface cannot reliably connect.
- Boot mode cannot be controlled.
- External device pulls MCU pins beyond allowed range.

## PC 传输检查

- 核对完整 UART/USB/VCP 电气路径、复用、逻辑电平、共地/隔离、保护、clock/baud 容差和 connector pinout。
- 记录 board/probe/VCP serial、USB VID/PID/interface、OS port、pins、DMA/IRQ 和实测 error counter。
- 保留目标器件支持的调试接口，按稳定物理 identity 绑定设备，不能只信任 `COMx`。
