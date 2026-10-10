# MCU Driver Contract

Use this reference when creating or reviewing a driver API.

## Driver Contract Table

| Field | Description |
| --- | --- |
| Device | Peripheral or external IC |
| Owner | Module or task owning the instance |
| Context | boot / task / ISR / callback |
| Sync model | blocking / async / polling / callback |
| Buffers | ownership, alignment, lifetime, DMA/cache rules |
| Timeout | per operation or global default |
| Errors | status codes and recovery action |
| Power | sleep entry and resume behavior |
| Diagnostics | counters, last error, state snapshot |
| Tests | unit, integration, HIL, fault injection |

## API Checklist

- `init` can be called once or has documented reinit behavior.
- `deinit` leaves pins, clocks, IRQs, and DMA in a known state.
- `configure` validates unsupported options.
- `transfer` behavior is clear when the device is busy.
- `cancel` exists for async or long blocking operations.
- ISR and callback APIs are clearly marked.
- Driver does not call application policy code.

## DMA Checklist

- Buffer alignment is specified.
- Buffer lifetime extends until completion callback.
- Cache maintenance is handled or explicitly not needed.
- Half-transfer and full-transfer behavior is documented.
- Error interrupt and abort path are tested.

## Bus Recovery

For I2C/SPI/UART/CAN-like buses, define:

- Timeout threshold.
- Peripheral reset path.
- GPIO bit-bang or clock-pulse recovery if needed.
- Device reinitialization order.
- Diagnostics after recovery.
