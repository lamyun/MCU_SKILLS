# Runtime Learning And Regression Loop

## Checkpoints

Evaluate improvement signals after setup, generation, build, host tests, PDF review, hardware preflight, integration, release gate, recovery, and final handoff. Also evaluate immediately after a false pass, unsafe bypass, data loss, lock race, or migration failure.

## Candidate Lifecycle

1. `observed`: capture behavior, expected result, correlation, environment, and hashed evidence.
2. `reproduced`: reproduce in a clean lane or fixture without relying on prior artifacts.
3. `regression-added`: demonstrate a test that fails before the proposed fix.
4. `implemented`: patch the narrow owning source package.
5. `validated`: run component, contract, and affected cross-stack tests.
6. `promoted`: add a generalized entry to `learned-patterns.md`, record source/install hashes, and install.
7. `blocked` or `rejected`: preserve the reason, evidence, owner, and revisit trigger.

Do not skip directly from observation to promotion.

每次迁移调用 `mcu_mcp.advance_improvement_candidate`，携带当前哈希证据和唯一 `ITR-*` ID。`regression-added` 必须证明回归在修复前失败，`validated` 必须通过受影响跨组件检查，`promoted` 必须带不同工程批准人、approval ID、pattern ID、源码 hash、回滚点和源码/安装一致性。MCP 为每次迁移保存一个不可变事件文件。

## Classification

Classify the owning layer as `project`, `skill`, `mcp`, `agent`, `toolchain`, or `workflow`. Classify the symptom as `false-pass`, `false-block`, `defect`, `missing-capability`, `friction`, `performance`, `migration`, `concurrency`, `documentation`, or `structure`.

Separate:

- generic invariant versus one-project configuration;
- product behavior versus tool behavior;
- environment drift versus source defect;
- software evidence versus target-observed or real-hardware evidence;
- immediate containment versus reusable prevention.

## Promotion Threshold

Promote after two independent occurrences with current evidence. One occurrence is sufficient only for a critical reproducible false pass, integrity/data-loss defect, approval/identity bypass, or destructive-operation safety defect. An engineering owner must still approve the generalized rule.

## Bounded Repair

Allow at most three patch-and-regression attempts for one candidate in a run. Each attempt receives a unique iteration ID and records source hash, changed components, tests, outcome, duration, and rollback point. After three failures, stop, mark blocked, preserve the best reproduction, and hand off.

## Validation Matrix

| Owning layer | Minimum validation |
| --- | --- |
| Project | affected build, unit/integration tests, evidence index |
| Skill | skill validator, 100/500 controls, realistic forward task |
| MCP | syntax/type check, unit tests, stdio tool discovery, negative gate test |
| Agent | setup parity, 100 controls, mode-specific dry run |
| Toolchain | clean build, reproducibility/drift check, artifact hashes |
| Workflow | team audit, lane audit, affected gate tests, rollback rehearsal |

Never modify signed release artifacts, accepted raw evidence, active hardware state, or installed Skills in place during the learning loop.
