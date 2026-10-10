# MCU Enterprise Review 500

Use this checklist for enterprise-grade MCU workflow audits. Each control is intentionally short so it can be assigned, scored, and linked to evidence. Score each item as missing, partial, complete, or exception-approved.

## Governance And Intake

001. [Governance] Project charter defines scope owners milestones and success criteria.
002. [Governance] Product risk class is documented before technical planning starts.
003. [Governance] Stakeholder map includes hardware firmware test production support.
004. [Governance] Non goals are documented to prevent uncontrolled scope growth.
005. [Governance] Business constraints are linked to technical tradeoff decisions.
006. [Governance] Project assumptions have owners validation dates and evidence.
007. [Governance] Milestone plan includes phase gates and review windows.
008. [Governance] Gate owners are named for every delivery phase.
009. [Governance] Gate evidence requirements are known before gate review.
010. [Governance] Risk register exists before architecture choices are frozen.
011. [Governance] Decision records include alternatives impact and rollback conditions.
012. [Governance] Exception process records reason impact approver and expiry.
013. [Governance] Escalation path exists for cross team technical blockers.
014. [Governance] Program status separates evidence facts from optimistic forecasts.
015. [Governance] Critical dependencies have owners backup plans and dates.
016. [Governance] Supplier and component risks are tracked with mitigation actions.
017. [Governance] Project baseline records supported hardware and firmware variants.
018. [Governance] Review calendar covers requirements architecture hardware firmware tests.
019. [Governance] Audit trail retains approvals findings and closure evidence.
020. [Governance] Post release learning updates standards scripts and skills.

## Portfolio And Product Planning

021. [Portfolio] Product variants are identified with shared and unique requirements.
022. [Portfolio] Hardware revision strategy is linked to firmware compatibility rules.
023. [Portfolio] Feature roadmap identifies dependencies on MCU resources.
024. [Portfolio] Cost targets include MCU external components testing and production.
025. [Portfolio] Schedule plan accounts for PCB spins and bringup uncertainty.
026. [Portfolio] Make buy reuse decisions are documented with maintainability impact.
027. [Portfolio] Platform reuse strategy defines what must remain generic.
028. [Portfolio] Legacy compatibility requirements are explicit and testable.
029. [Portfolio] Customer commitments are traceable to technical acceptance criteria.
030. [Portfolio] Regulatory or market constraints are captured before design freeze.
031. [Portfolio] End of life component risk has replacement or redesign plan.
032. [Portfolio] Pilot production scope is separated from mass production scope.
033. [Portfolio] Field support model is defined before release planning.
034. [Portfolio] Warranty risk informs diagnostics and production test depth.
035. [Portfolio] Product telemetry needs are reviewed against privacy constraints.
036. [Portfolio] Service tooling requirements are captured with security controls.
037. [Portfolio] Documentation ownership is assigned for customer facing materials.
038. [Portfolio] Localization or regional configuration impacts firmware design.
039. [Portfolio] Product lifecycle plan includes maintenance and update policy.
040. [Portfolio] Portfolio decisions are revisited after major escaped defects.

## Requirements Engineering

041. [Requirements] Requirements use stable identifiers and controlled status values.
042. [Requirements] Each requirement contains one measurable product behavior.
043. [Requirements] Functional and nonfunctional requirements are clearly separated.
044. [Requirements] Acceptance criteria define observable pass fail thresholds.
045. [Requirements] Power requirements cover active idle sleep and wake cases.
046. [Requirements] Timing requirements cover sampling latency jitter and deadlines.
047. [Requirements] Environmental requirements cover temperature voltage and stress.
048. [Requirements] Interface requirements define protocol speed levels and faults.
049. [Requirements] Manufacturing requirements include programming calibration and test.
050. [Requirements] Service requirements include diagnostics logs and version query.
051. [Requirements] Security requirements cover debug access updates and secrets.
052. [Requirements] Safety requirements define hazards mitigations and safe states.
053. [Requirements] Must have requirements have verification method assigned.
054. [Requirements] Ambiguous wording is replaced with quantified criteria.
055. [Requirements] Requirements changes include impact analysis and approver.
056. [Requirements] Requirements traceability links design implementation and tests.
057. [Requirements] Deferred requirements have release or backlog disposition.
058. [Requirements] Customer acceptance requirements map to validation evidence.
059. [Requirements] Requirements baseline is reviewed by all affected disciplines.
060. [Requirements] Requirements gaps are tracked as risks not hidden assumptions.

## System Architecture

061. [Architecture] System block diagram shows sensors actuators MCU and interfaces.
062. [Architecture] Runtime modes include boot normal fault service update sleep.
063. [Architecture] State machines define events guards actions and recovery paths.
064. [Architecture] Hardware firmware boundaries are documented for each function.
065. [Architecture] Resource budget covers CPU Flash RAM timers DMA IRQ pins.
066. [Architecture] Resource margins are justified by risk and growth forecast.
067. [Architecture] Memory map includes bootloader application parameters and logs.
068. [Architecture] Storage layout handles corruption versioning and migration.
069. [Architecture] Power architecture defines rails modes wake sources and sequencing.
070. [Architecture] Clock architecture defines sources accuracy fallback and measurement.
071. [Architecture] Communication architecture defines bus ownership and recovery.
072. [Architecture] Diagnostic architecture defines errors counters logs and retrieval.
073. [Architecture] Watchdog architecture ties feeding to real task progress.
074. [Architecture] Boot architecture defines startup order validation and rollback.
075. [Architecture] Update architecture defines image format verification and recovery.
076. [Architecture] Architecture decisions record rejected alternatives and impact.
077. [Architecture] Architecture review checks irreversible PCB and MCU choices.
078. [Architecture] Architecture diagrams are versioned with reviewed artifacts.
079. [Architecture] Architecture risks are closed before feature implementation accelerates.
080. [Architecture] Architecture supports production test and field service needs.

## MCU Selection And Resource Budget

081. [MCUSelection] Candidate MCUs are compared using documented selection criteria.
082. [MCUSelection] Flash capacity includes bootloader logs parameters and growth.
083. [MCUSelection] RAM capacity includes stacks heaps buffers DMA and margins.
084. [MCUSelection] CPU capacity includes worst case timing and future features.
085. [MCUSelection] FPU DSP or accelerator needs are justified by workload.
086. [MCUSelection] ADC resolution speed reference and channel count are adequate.
087. [MCUSelection] Timer and PWM resources cover control and measurement needs.
088. [MCUSelection] Communication peripherals cover required speed concurrency and DMA.
089. [MCUSelection] Interrupt priority depth supports RTOS and latency needs.
090. [MCUSelection] Low power modes meet wake source and current requirements.
091. [MCUSelection] Package pinout supports layout debug and manufacturing constraints.
092. [MCUSelection] Temperature grade matches environment and derating requirements.
093. [MCUSelection] Security features support boot update and read protection needs.
094. [MCUSelection] Vendor SDK maturity and errata are reviewed before selection.
095. [MCUSelection] Toolchain debugger and programmer support are available.
096. [MCUSelection] Supply chain availability and alternates are reviewed.
097. [MCUSelection] Unit cost includes external components and testing impact.
098. [MCUSelection] Selection matrix includes evidence not only final preference.
099. [MCUSelection] Chosen MCU risks have mitigation or accepted owner.
100. [MCUSelection] MCU selection is revisited after major requirement changes.

## Hardware Design

101. [Hardware] Power tree covers all MCU analog digital and backup domains.
102. [Hardware] Regulator current thermal and transient capacity are reviewed.
103. [Hardware] Brownout reset behavior matches firmware recovery assumptions.
104. [Hardware] Decoupling strategy follows vendor and layout recommendations.
105. [Hardware] Analog reference filtering and accuracy are reviewed.
106. [Hardware] Clock source components match required accuracy and startup time.
107. [Hardware] Crystal layout constraints are visible in PCB review.
108. [Hardware] Reset circuit supports external reset debugger and supervisor needs.
109. [Hardware] Boot pins default to intended production startup mode.
110. [Hardware] Debug pins remain accessible during reset and first bringup.
111. [Hardware] Programming connector includes power sense reset ground and signals.
112. [Hardware] Pin mux table matches schematic PCB and firmware configuration.
113. [Hardware] Unused pins have defined electrical states and rationale.
114. [Hardware] ADC inputs include range scaling filtering and protection review.
115. [Hardware] PWM actuator outputs fail to safe state at reset.
116. [Hardware] Communication transceivers include termination polarity and protection.
117. [Hardware] External memories include write protect power and timing review.
118. [Hardware] Test points exist for high risk power clock and bus signals.
119. [Hardware] Hardware review findings include owner and closure evidence.
120. [Hardware] Hardware design releases preserve bringup and production needs.

## PCB BOM And Manufacturing Design

121. [PCB] PCB stackup supports signal integrity power and manufacturing constraints.
122. [PCB] Critical current loops are reviewed for noise and heating.
123. [PCB] Analog and digital layout interactions are reviewed explicitly.
124. [PCB] Clock traces follow length shielding and placement recommendations.
125. [PCB] High speed interfaces follow impedance and return path rules.
126. [PCB] Reset boot and debug nets avoid unwanted loading or conflicts.
127. [PCB] ESD protection placement supports connector exposure and return paths.
128. [PCB] Thermal design considers regulators drivers and enclosed operation.
129. [PCB] Test fixture access is included before layout release.
130. [PCB] Silkscreen and orientation markers reduce assembly mistakes.
131. [BOM] BOM marks lifecycle availability alternates and approved manufacturers.
132. [BOM] Critical components have substitutions or procurement risk plan.
133. [BOM] Component tolerances support measurement and calibration assumptions.
134. [BOM] Firmware dependent components include exact variant and address data.
135. [BOM] Production programming fixtures account for connector and access limits.
136. [BOM] Assembly options are reflected in firmware configuration variants.
137. [BOM] DNP parts and jumpers are documented for bringup and production.
138. [BOM] Manufacturing notes include cleaning coating and handling constraints.
139. [BOM] PCB and BOM revisions are traceable to firmware compatibility.
140. [BOM] Manufacturing feedback updates BOM risk and design rules.

## Board Bringup

141. [Bringup] Bringup plan defines order stop conditions and measurement points.
142. [Bringup] Board ID PCB revision and BOM revision are recorded.
143. [Bringup] Visual inspection checks polarity solder bridges and missing parts.
144. [Bringup] Rail to ground resistance is measured before first power.
145. [Bringup] Bench supply current limits are defined before energizing.
146. [Bringup] First power captures current voltage ripple and temperature.
147. [Bringup] Reset release timing is measured and documented.
148. [Bringup] Clock startup and frequency are verified with evidence.
149. [Bringup] Debugger can read chip ID erase program and halt.
150. [Bringup] Minimal firmware toggles GPIO and emits versioned log.
151. [Bringup] Reset reason and boot path are confirmed on prototype.
152. [Bringup] Each peripheral smoke test records expected and observed behavior.
153. [Bringup] Communication buses are tested with missing device fault cases.
154. [Bringup] ADC and sensor paths are checked with known input values.
155. [Bringup] Actuator outputs are tested with safe loads or simulation.
156. [Bringup] Power mode transitions are measured on actual board.
157. [Bringup] Hardware issues are linked to firmware workaround or respin.
158. [Bringup] Bringup findings are reviewed before broader firmware development.
159. [Bringup] Prototype limitations are visible to test and release teams.
160. [Bringup] Bringup evidence is retained by board serial number.

## Firmware Architecture

161. [FirmwareArchitecture] Firmware layers separate platform BSP drivers middleware application.
162. [FirmwareArchitecture] Lower layers never call product specific application policy.
163. [FirmwareArchitecture] Module contracts define lifecycle context timing and errors.
164. [FirmwareArchitecture] Public APIs state buffer ownership and concurrency rules.
165. [FirmwareArchitecture] Startup sequence initializes clocks memory drivers and diagnostics safely.
166. [FirmwareArchitecture] Linker script matches target memory map and release layout.
167. [FirmwareArchitecture] Interrupt vector ownership and weak handlers are reviewed.
168. [FirmwareArchitecture] Configuration data has version defaults validation and migration.
169. [FirmwareArchitecture] Calibration data has units ranges checksum and traceability.
170. [FirmwareArchitecture] Logging architecture is bounded and configurable by build.
171. [FirmwareArchitecture] Error architecture distinguishes timeout busy invalid and hardware faults.
172. [FirmwareArchitecture] Diagnostics expose state counters versions and last faults.
173. [FirmwareArchitecture] Persistent storage handles partial writes and corruption.
174. [FirmwareArchitecture] Low power design coordinates drivers tasks clocks and GPIO.
175. [FirmwareArchitecture] Build variants are explicit and controlled by configuration.
176. [FirmwareArchitecture] Generated code boundaries are protected from manual edits.
177. [FirmwareArchitecture] Feature modules include test seams and mocks where useful.
178. [FirmwareArchitecture] Firmware architecture supports manufacturing and field service hooks.
179. [FirmwareArchitecture] Architecture reviews cover ownership and dependency direction.
180. [FirmwareArchitecture] Firmware architecture updates after platform level defects.

## Firmware Implementation

181. [Firmware] Fixed width integer types are used for hardware facing values.
182. [Firmware] Public functions return explicit status or documented void rationale.
183. [Firmware] Blocking calls include timeout and observable failure handling.
184. [Firmware] ISR paths avoid logging allocation and long computations.
185. [Firmware] Shared variables use volatile atomic critical or ownership rules.
186. [Firmware] Unit conversions include explicit names units and overflow checks.
187. [Firmware] Ring buffers handle full empty wrap and overflow diagnostics.
188. [Firmware] External input parsing validates length checksum range and state.
189. [Firmware] State machines handle invalid events and timeout transitions.
190. [Firmware] Watchdog breadcrumbs are saved before intentional reset paths.
191. [Firmware] Dynamic memory use is forbidden or monitored and justified.
192. [Firmware] Assertions are classified for debug release and safety behavior.
193. [Firmware] Compiler warnings are reviewed and not globally hidden.
194. [Firmware] Code review checks initialization order and error paths.
195. [Firmware] Code review checks array bounds and signed conversions.
196. [Firmware] Code review checks low power entry and resume interactions.
197. [Firmware] Code review checks storage migration and compatibility impacts.
198. [Firmware] Implementation changes update tests diagnostics or risk records.
199. [Firmware] Defect fixes include root cause and regression evidence.
200. [Firmware] Firmware commits avoid unrelated generated or metadata churn.

## RTOS And Driver Framework

201. [RTOS] Task list defines responsibility trigger priority stack and watchdog role.
202. [RTOS] Task priorities are assigned from timing not organizational importance.
203. [RTOS] Stack budgets are validated using high water marks under stress.
204. [RTOS] Queue depths are sized from peak traffic and tested overflow.
205. [RTOS] Mutex use is bounded and priority inversion is considered.
206. [RTOS] Event flags do not replace payload ownership when data matters.
207. [RTOS] Critical sections are measured for worst case latency impact.
208. [RTOS] Interrupt priorities comply with RTOS system call restrictions.
209. [RTOS] Scheduler lock and interrupt disable durations are reviewed.
210. [RTOS] Per task health metrics feed watchdog or supervisor logic.
211. [Drivers] Driver APIs state boot task ISR and callback safety.
212. [Drivers] Driver initialization validates configuration and hardware presence.
213. [Drivers] Driver transfer APIs define busy timeout cancel and completion.
214. [Drivers] DMA buffers define alignment lifetime and cache maintenance.
215. [Drivers] Driver callbacks never call undocumented blocking APIs.
216. [Drivers] Bus manager centralizes chip select speed mode and locks.
217. [Drivers] Bus recovery covers timeout stuck line reset and reinit.
218. [Drivers] Driver diagnostics expose last error state and counters.
219. [Drivers] Driver tests cover timeout cancel fault and stress cases.
220. [Drivers] Driver changes update interface contracts and dependent tests.

## Toolchain And CI

221. [Toolchain] Toolchain manifest pins compiler linker SDK HAL and RTOS versions.
222. [Toolchain] Code generator version and settings are recorded for releases.
223. [Toolchain] Programmer debugger and flash tool versions are controlled.
224. [Toolchain] Build scripts avoid developer specific absolute paths.
225. [Toolchain] Build environment variables are documented and validated.
226. [Toolchain] External downloads have version source and checksum records.
227. [Toolchain] Build output embeds controlled version metadata when allowed.
228. [Toolchain] Release builds are reproducible or variance is explained.
229. [Toolchain] Build artifacts include elf map bin hex logs hashes.
230. [Toolchain] Artifact naming encodes product board config version source.
231. [CI] CI has fast checks for feature branches and full checks for releases.
232. [CI] Build matrix covers boards configs bootloader and application variants.
233. [CI] CI detects generated code drift and configuration drift.
234. [CI] CI fails or flags new compiler warnings according to policy.
235. [CI] CI tracks Flash RAM and section size budget changes.
236. [CI] Host unit tests run without hardware dependencies.
237. [CI] Static analysis output is preserved and triaged by owner.
238. [CI] HIL jobs use hardware locks timeouts and recovery steps.
239. [CI] CI failures show command versions target config and logs.
240. [CI] CI dashboards show trend not only latest pass fail.

## Static Analysis And Code Quality

241. [Quality] Coding standard is documented and mapped to review checks.
242. [Quality] Formatting rules are automated to reduce subjective reviews.
243. [Quality] Static analysis configuration is versioned and reviewed.
244. [Quality] Suppressed findings require reason owner and review date.
245. [Quality] High severity static findings block release unless excepted.
246. [Quality] MISRA or equivalent rules are applied when project risk requires.
247. [Quality] Complexity hot spots are identified for critical modules.
248. [Quality] Dead code and unused interfaces are removed or justified.
249. [Quality] Public headers avoid leaking private hardware dependencies.
250. [Quality] Build warnings are tracked by target and owner.
251. [Quality] Code coverage is used where meaningful for host tests.
252. [Quality] Generated code is excluded or handled consistently in metrics.
253. [Quality] Review checklists vary by module risk and ownership.
254. [Quality] Security sensitive code receives additional review depth.
255. [Quality] Safety related code receives traceability and evidence review.
256. [Quality] Code review comments are closed with evidence not assertion.
257. [Quality] Repeated review findings update standards or templates.
258. [Quality] Quality metrics are visible to firmware and management.
259. [Quality] Quality gates are calibrated to prevent noisy false blockers.
260. [Quality] Quality exceptions expire and require follow up action.

## Verification Strategy

261. [Verification] Test plan maps requirements to verification levels.
262. [Verification] High risk requirements have normal boundary fault recovery tests.
263. [Verification] Unit tests cover algorithms parsers and state machines.
264. [Verification] Integration tests cover drivers storage boot and reset.
265. [Verification] HIL tests cover real timing power and external devices.
266. [Verification] Acceptance tests match customer visible requirements.
267. [Verification] Regression suite includes every fixed critical defect.
268. [Verification] Test cases include preconditions steps thresholds evidence.
269. [Verification] Test environments record firmware hardware fixture versions.
270. [Verification] Manual tests include repeatable procedures and evidence rules.
271. [Verification] Automated tests fail with actionable diagnostic information.
272. [Verification] Fault injection covers sensors buses storage and power loss.
273. [Verification] Long run tests monitor leaks counters resets and drift.
274. [Verification] Boundary tests include maximum rates payloads and temperatures.
275. [Verification] Negative tests include invalid frames corrupt storage and timeouts.
276. [Verification] Requirements without tests are visible as release risk.
277. [Verification] Test reports separate not run skipped failed and blocked.
278. [Verification] Test evidence is linked to source and artifact versions.
279. [Verification] Verification exceptions require risk owner and expiry.
280. [Verification] Verification gaps update future automation roadmap.

## HIL And Regression Operations

281. [HIL] HIL bench inventory tracks board fixture instrument and firmware versions.
282. [HIL] HIL resources have booking locking and health status mechanisms.
283. [HIL] HIL setup performs known state reset before every test.
284. [HIL] HIL logs console debugger power and instrument evidence.
285. [HIL] HIL scripts handle timeout cleanup and board recovery.
286. [HIL] HIL flaky failures are classified before suppression.
287. [HIL] HIL fixtures have calibration and maintenance records.
288. [HIL] HIL tests include power interruption and reset scenarios.
289. [HIL] HIL tests include communication loss and corrupted payloads.
290. [HIL] HIL tests include actuator safe state verification.
291. [Regression] Regression suite prioritizes escaped defects and high risk paths.
292. [Regression] Regression duration is tracked and optimized by risk.
293. [Regression] Regression failures create defects with reproduction evidence.
294. [Regression] Regression pass rate is reviewed before release gates.
295. [Regression] Nightly regression results trend by target and fixture.
296. [Regression] Release regression suite is frozen with documented scope.
297. [Regression] Regression exceptions require owner reason and compensating tests.
298. [Regression] Test data sets are versioned with expected results.
299. [Regression] Test infrastructure changes are tested separately from product.
300. [Regression] Regression learnings update test plan and CI strategy.

## Debug And Optimization

301. [Debug] Fault handlers capture PC LR SP xPSR and fault registers.
302. [Debug] Reset reason and breadcrumbs survive reboot where feasible.
303. [Debug] Crash reports include firmware version board revision and context.
304. [Debug] Symbol and map files are archived for released images.
305. [Debug] Watchdog resets identify stalled task or progress counter.
306. [Debug] Deadlock analysis reviews queues mutexes events and priorities.
307. [Debug] Memory corruption analysis reviews stack DMA buffers and persistence.
308. [Debug] Communication debug captures electrical status and protocol state.
309. [Debug] Debug logs are bounded and safe for timing sensitive paths.
310. [Debug] Field diagnostic commands are authenticated when risk requires.
311. [Optimization] Optimization starts with metric target baseline and tool.
312. [Optimization] Timing optimization uses trace GPIO timestamp or cycle counter.
313. [Optimization] Power optimization measures debugger detached where possible.
314. [Optimization] Memory optimization tracks Flash RAM heap and stack trends.
315. [Optimization] Boot optimization separates hardware bootloader runtime phases.
316. [Optimization] Optimization tradeoffs record complexity reliability and risk.
317. [Optimization] Performance changes include regression and measurement evidence.
318. [Optimization] Power changes include wake source and resume validation.
319. [Optimization] Debug discoveries update diagnostics and test hooks.
320. [Optimization] Repeated failures update architecture or coding standard.

## Safety Engineering

321. [Safety] Hazards are identified with severity likelihood and exposure.
322. [Safety] Safety goals are linked to product operating scenarios.
323. [Safety] Failure modes cover sensors actuators power storage and communications.
324. [Safety] Safe state is defined for each hazardous function.
325. [Safety] Degraded mode behavior is documented and testable.
326. [Safety] Watchdog safety role is tied to real progress monitoring.
327. [Safety] Brownout behavior is tested for unsafe output prevention.
328. [Safety] Sensor plausibility checks include range rate and consistency.
329. [Safety] Actuator outputs default safe during reset and fault.
330. [Safety] Fault counters avoid uncontrolled repeated recovery loops.
331. [Safety] Safety requirements trace to design implementation and tests.
332. [Safety] Safety controls include diagnostic coverage rationale where needed.
333. [Safety] Safety related code has strengthened review and test evidence.
334. [Safety] Fault injection validates critical safety mechanisms.
335. [Safety] Production tests cover safety critical I O paths.
336. [Safety] Safety exceptions require formal residual risk acceptance.
337. [Safety] Safety analysis updates after design or requirement changes.
338. [Safety] Safety evidence is retained for audit and customer review.
339. [Safety] Returned unit analysis checks safety relevant failure patterns.
340. [Safety] Safety lessons update requirements diagnostics and regression tests.

## Security Engineering

341. [Security] Threat model identifies assets interfaces attackers and impacts.
342. [Security] Firmware image authenticity is considered for updateable products.
343. [Security] Secure boot or verified boot decision is documented.
344. [Security] Update packages include integrity and authenticity checks.
345. [Security] Anti rollback policy is defined where older firmware is risky.
346. [Security] Debug port production policy is approved and testable.
347. [Security] Readout protection and option bytes are controlled release inputs.
348. [Security] Key material is never stored in source control or logs.
349. [Security] Key injection process records identity without exposing secrets.
350. [Security] Diagnostic logs redact sensitive customer or security data.
351. [Security] Service tools require authentication when access is sensitive.
352. [Security] Bootloader command surface is minimized and reviewed.
353. [Security] Communication protocols validate length authentication and replay risk.
354. [Security] Third party libraries have version license and vulnerability review.
355. [Security] Security tests cover update tampering and downgrade attempts.
356. [Security] Security settings are verified during production programming.
357. [Security] Field recovery path does not bypass critical protections.
358. [Security] Security exceptions require expiry and compensating controls.
359. [Security] Security incidents update threat model and test coverage.
360. [Security] Security evidence is linked to release and production records.

## Compliance And Documentation

361. [Compliance] Applicable standards regulations and customer clauses are listed.
362. [Compliance] Compliance requirements are translated into verifiable project controls.
363. [Compliance] Evidence map links clauses to artifacts tests and approvals.
364. [Compliance] Document versions owners and review dates are visible.
365. [Compliance] Configuration management covers code tools hardware and production.
366. [Compliance] Traceability matrix includes requirements design code tests release.
367. [Compliance] Supplier documents and certifications are stored when required.
368. [Compliance] Tool qualification or confidence argument exists when required.
369. [Compliance] License obligations are reviewed for firmware dependencies.
370. [Compliance] Export control or crypto restrictions are reviewed when applicable.
371. [Compliance] EMC relevant software behavior is documented and tested.
372. [Compliance] Wireless or regional requirements map to firmware configurations.
373. [Compliance] Manufacturing records meet retention and traceability needs.
374. [Compliance] Audit findings have owners due dates and closure evidence.
375. [Compliance] Compliance exceptions have formal approval and expiry.
376. [Compliance] Customer documents match actual released firmware behavior.
377. [Compliance] Documentation changes follow review and release workflow.
378. [Compliance] Certification test failures update risk and design records.
379. [Compliance] Compliance evidence is accessible without tribal knowledge.
380. [Compliance] Compliance lessons update templates checklists and skills.

## Release Engineering

381. [Release] Release scope includes requirements defects hardware and markets.
382. [Release] Release branch policy defines freeze merge and hotfix rules.
383. [Release] Version scheme identifies product hardware config and source.
384. [Release] Release candidate is built from controlled toolchain manifest.
385. [Release] Release artifacts include binary hex elf map logs hashes.
386. [Release] Release notes include changes known issues and compatibility.
387. [Release] Test summary includes scope environment gaps and residual risks.
388. [Release] Open defects are triaged with release disposition and owner.
389. [Release] Release approvals include engineering test production and support.
390. [Release] Release package can be rebuilt or variance is documented.
391. [Release] Rollback instructions are validated before field deployment.
392. [Release] Upgrade compatibility matrix covers bootloader and application versions.
393. [Release] Release checklist includes security settings and production scripts.
394. [Release] Release artifacts are stored in controlled durable location.
395. [Release] Release hash verification is part of programming or deployment.
396. [Release] Release gate blocks missing critical evidence unless excepted.
397. [Release] Hotfix releases preserve traceability and regression evidence.
398. [Release] Release retrospective captures late blockers and process gaps.
399. [Release] Release records support field issue root cause analysis.
400. [Release] Release process updates after production or field escapes.

## Production And Manufacturing

401. [Production] Manufacturing pack includes firmware artifacts and hashes.
402. [Production] Programming procedure records tool version target and settings.
403. [Production] Programming flow verifies target voltage and board identity.
404. [Production] Bootloader application parameters and locks program in approved order.
405. [Production] Serial number format and assignment process are controlled.
406. [Production] Calibration procedure defines equipment method limits and storage.
407. [Production] Factory test limits are versioned and linked to requirements.
408. [Production] Factory test distinguishes hardware firmware calibration programming failures.
409. [Production] Production scripts avoid exposing secrets in logs or history.
410. [Production] Readout protection is applied only after verification succeeds.
411. [Production] Rework procedure defines unlock erase reprogram and retest rules.
412. [Production] Scrap or quarantine rules exist for repeated programming failures.
413. [Production] Fixture version and maintenance are tracked with test results.
414. [Production] Production yield is monitored by failure category and revision.
415. [Production] Golden sample or known good unit validates station health.
416. [Production] Manufacturing changes require firmware compatibility review.
417. [Production] Production data links serial board firmware calibration and test.
418. [Production] Production operators have clear pass fail and escalation guidance.
419. [Production] Production pilot feedback updates test limits and procedures.
420. [Production] Production readiness gate includes engineering and manufacturing approval.

## OTA Field And Support

421. [Field] Device can report firmware version hardware revision and configuration.
422. [Field] Fault codes are documented with meaning and support action.
423. [Field] Logs capture enough context without violating security constraints.
424. [Field] OTA process verifies image authenticity integrity and compatibility.
425. [Field] OTA handles power loss interruption and resume or rollback.
426. [Field] OTA progress and failure state are observable to support.
427. [Field] Rollback policy avoids unsafe downgrade and version mismatch.
428. [Field] Recovery mode entry is documented and tested.
429. [Field] Field tools are versioned and compatible with release packages.
430. [Field] Remote support workflow preserves diagnostic evidence.
431. [Field] Returned unit analysis records firmware hardware configuration and symptoms.
432. [Field] Field issue triage links to requirements tests and release records.
433. [Field] Repeat field failures trigger corrective action and regression tests.
434. [Field] Customer configuration migration is validated during updates.
435. [Field] Service replacement parts maintain firmware compatibility rules.
436. [Field] Support scripts cannot accidentally weaken production security.
437. [Field] Field known issues are reflected in release notes and support docs.
438. [Field] Field data trends inform reliability and product roadmap decisions.
439. [Field] Emergency rollback process has owners and communication plan.
440. [Field] Field learnings update diagnostics manufacturing and verification.

## Team Collaboration

441. [Team] RACI assigns responsible and accountable owners for major artifacts.
442. [Team] Single source of truth is defined for each artifact type.
443. [Team] Review findings include impact owner due date and evidence.
444. [Team] Hardware to firmware handoff includes pin power clock reset debug.
445. [Team] Firmware to test handoff includes version diagnostics hooks and risks.
446. [Team] Test to release handoff includes gaps failures flakes and recommendation.
447. [Team] Release to production handoff includes artifacts programming calibration recovery.
448. [Team] Meeting rhythm focuses on risks decisions and blocked evidence.
449. [Team] Cross discipline changes notify affected owners before implementation.
450. [Team] New team members can find standards without private explanations.
451. [Team] Knowledge base captures recurring debug and production lessons.
452. [Team] Review load is balanced by risk and expertise.
453. [Team] Escalations distinguish decision needed from information missing.
454. [Team] Team metrics are reviewed with improvement actions.
455. [Team] Ownership transitions preserve artifact history and open risks.
456. [Team] Communication records avoid relying on private chat decisions.
457. [Team] External suppliers receive clear requirements interfaces and evidence needs.
458. [Team] Customer feedback is translated into controlled project artifacts.
459. [Team] Team retrospectives update process not only meeting notes.
460. [Team] Collaboration breakdowns become visible process risks.

## Metrics And Continuous Improvement

461. [Metrics] Metrics define owner data source cadence and action threshold.
462. [Metrics] Requirement coverage trend is visible by release.
463. [Metrics] Resource margin trend is tracked for Flash RAM CPU and pins.
464. [Metrics] CI pass rate and failure categories are tracked over time.
465. [Metrics] Static analysis findings are tracked by severity and age.
466. [Metrics] HIL flakiness is tracked separately from product failures.
467. [Metrics] Defects track phase introduced and phase found.
468. [Metrics] Escaped defects trigger root cause and preventive action.
469. [Metrics] Production yield trends are linked to revision and station.
470. [Metrics] OTA success and rollback rates are monitored when applicable.
471. [Metrics] Field failure rates are segmented by version and hardware.
472. [Metrics] Review findings trend informs training and standards updates.
473. [Metrics] Exceptions are reviewed for expiry and recurrence.
474. [Metrics] Build time and test duration are managed as productivity signals.
475. [Metrics] Quality dashboards include actionable thresholds not vanity counts.
476. [Metrics] Metrics are audited for accuracy and unintended incentives.
477. [Metrics] Improvement actions have owners and verification criteria.
478. [Metrics] Process changes are piloted before broad rollout when risky.
479. [Metrics] Lessons learned update templates scripts and skill references.
480. [Metrics] Continuous improvement removes waste as well as adding controls.

## Skill Library Operations

481. [SkillOps] Skill descriptions clearly state when each skill should trigger.
482. [SkillOps] Main skill routes to all specialized and cross cutting skills.
483. [SkillOps] Skill bodies stay concise and use references for detail.
484. [SkillOps] Reference files are one level from skill root and discoverable.
485. [SkillOps] Scripts are documented in skill bodies with intended usage.
486. [SkillOps] Scripts can run without hidden local assumptions where possible.
487. [SkillOps] Skill validation runs after every significant edit.
488. [SkillOps] Maturity audit checks structural coverage and routing.
489. [SkillOps] Enterprise audit verifies all 500 controls exist.
490. [SkillOps] Project audit distinguishes warnings from strict CI failures.
491. [SkillOps] Skill updates preserve user or team local modifications.
492. [SkillOps] New recurring project lessons update the relevant skill.
493. [SkillOps] Duplicate guidance is minimized between skill body and references.
494. [SkillOps] Cross skill references avoid circular dependency confusion.
495. [SkillOps] Skill names remain lowercase hyphen case and under limits.
496. [SkillOps] Agent metadata matches the skill purpose and default prompt.
497. [SkillOps] No template placeholders remain in production skill files.
498. [SkillOps] Forward testing uses realistic prompts and raw artifacts.
499. [SkillOps] Skill library supports team onboarding and audit readiness.
500. [SkillOps] Skill system evolves from real project outcomes and evidence.
