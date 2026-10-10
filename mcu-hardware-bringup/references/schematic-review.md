# MCU Schematic Review

Use this reference to review MCU board design before PCB release or prototype build.

## 证据门禁

- 禁止仅依据文本提取结果评审 PDF 原理图。
- 必须让 `$mcu-datasheet-extraction` 的 Poppler + Codex PDF 双验证 manifest 通过。
- 每条发现记录页码/图纸号、可用时的坐标区、位号、引脚、网络名、源 PDF SHA-256 和 manifest 路径。
- 网络名、连接点、交叉线、旋转内容或跨页符号存在歧义时停止定论并登记差异。

## Power

- Verify every MCU supply pin and analog supply pin is connected as required by the datasheet.
- Check voltage range, regulator current, sequencing, brown-out behavior, and power-good/reset interaction.
- Place decoupling capacitors close to supply pins and use values recommended by the vendor.
- Confirm analog reference filtering and measurement range.
- Check current sense, protection, reverse polarity, surge/ESD, and thermal constraints.

## Clock

- Confirm crystal/resonator/load capacitor values and layout constraints.
- Provide fallback plan for internal oscillator where appropriate.
- Check RTC clock source, backup domain, and low-power clock accuracy.
- Ensure clock output or measurement access exists when bring-up risk is high.

## Reset, Boot, And Debug

- Confirm reset pull-up/down, reset supervisor, button or external reset sources.
- Verify boot pins default to the intended mode at power-up.
- Confirm SWD/JTAG pins are not blocked by external circuits at reset.
- Preserve programming connector access, ground reference, reset, and target voltage sense.
- Document option bytes, read protection, and bootloader entry method.

## Pin Mux

- Cross-check each pin against alternate functions, boot behavior, default state, drive strength, and voltage tolerance.
- Avoid assigning critical functions to pins with conflicting boot/debug behavior.
- Add test points for first-spin high-risk signals.
- Confirm unused pins have defined states.

## Interfaces

- UART/CAN/USB/Ethernet: check transceiver power, termination, ESD, polarity, and connector pinout.
- SPI/I2C: check pull-ups, chip-select defaults, bus speed, level shifting, and recovery path.
- ADC: check source impedance, filtering, reference, scaling, and protection.
- PWM/motor/control: check gate drive, dead time needs, fault feedback, and safe defaults.

## Review Output

Produce a table:

| Area | Finding | Impact | Recommendation | Verification |
| --- | --- | --- | --- | --- |
