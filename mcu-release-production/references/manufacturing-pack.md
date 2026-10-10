# MCU Manufacturing Pack

Use this reference when preparing production programming, calibration, factory test, and field support material.

## Package Structure

```text
manufacturing-pack/
  firmware/
    app.bin
    app.hex
    app.elf
    app.map
    hashes.txt
  programming/
    program.ps1 or program.sh
    programmer-config/
    option-bytes/
  calibration/
    calibration-procedure.md
    parameter-format.md
  factory-test/
    test-procedure.md
    test-scripts/
    limits/
  labels-and-identity/
    serial-number-format.md
    version-query.md
  recovery/
    unbrick.md
    rollback.md
  release-notes.md
```

## Programming Flow

1. Identify board revision and product variant.
2. Connect programmer and verify target voltage.
3. Erase or unlock as required.
4. Program bootloader, application, parameters, and security settings in the approved order.
5. Verify hash or readback where allowed.
6. Program serial number, keys, region, or calibration placeholders.
7. Lock debug/readout settings only after verification.
8. Run factory test and save result against serial number.

## Calibration

Define:

- Parameter names, units, ranges, defaults, and storage address.
- Calibration equipment and fixtures.
- Calculation method.
- Acceptance limits.
- Recalibration or field reset behavior.
- Data backup and traceability.

## Factory Test

Factory tests should separate:

- Programming failure.
- Power or hardware assembly failure.
- Sensor/actuator failure.
- Calibration failure.
- Firmware functional failure.

## Field Support

Provide:

- How to query firmware version, hardware revision, serial number, and configuration.
- Fault code table and log extraction steps.
- Recovery, rollback, and safe-mode entry.
- Compatibility rules for replacing boards or modules.
