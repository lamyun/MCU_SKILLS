# MCU Firmware Module Template

Use this reference when creating a new firmware module or reviewing an existing module boundary.

## Module Header

```c
#pragma once

#include <stdint.h>
#include <stdbool.h>

typedef enum {
    MODULE_OK = 0,
    MODULE_ERR_INVALID_ARG,
    MODULE_ERR_BUSY,
    MODULE_ERR_TIMEOUT,
    MODULE_ERR_HW,
} module_status_t;

typedef struct {
    uint32_t timeout_ms;
} module_config_t;

module_status_t module_init(const module_config_t *config);
module_status_t module_start(void);
module_status_t module_stop(void);
module_status_t module_get_status(uint32_t *status_flags);
```

## Required Design Notes

For each module document:

- Purpose and owner.
- Public APIs and expected call order.
- Allowed call context: boot, task, ISR, callback, low-power resume.
- External dependencies.
- Timing and blocking behavior.
- Error codes and recovery.
- Persistent state or configuration.
- Test strategy and mocks/fakes.

## State Machine Template

```text
States:
- INIT
- IDLE
- ACTIVE
- FAULT

Events:
- EVT_START
- EVT_STOP
- EVT_TIMEOUT
- EVT_HW_ERROR

Transitions:
| Current | Event | Guard | Action | Next |
| --- | --- | --- | --- | --- |
```

## Diagnostics

Expose:

- Last error.
- Error counters.
- State.
- Last transition timestamp.
- Queue or buffer high-water mark if relevant.
