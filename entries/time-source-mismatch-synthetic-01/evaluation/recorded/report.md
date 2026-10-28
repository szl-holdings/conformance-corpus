## STATUS

**FAIL** (SOURCE_MISMATCH), exit code 1.

- Run: `run-7e468bf65c2d53c1`
- Started 2026-09-26T00:00:00Z; completed 2026-09-26T00:00:00Z
- Reasons: SOURCE_MISMATCH
- Failure modes: SOURCE_MISMATCH
- Verdict rises: NONE -> PASS at step 1 (`check:columns`, VERIFIED); PASS -> FAIL at step 3 (`check:timing`, SOURCE_MISMATCH)
- Evidence manifest sha256: `c139fb3c9607c89b19b0b43873b913199bc942f984d3b816cdf67a8bc3de8cd6`
- Ledger: 17 entries, head `6eee15235d36fe935d90f1344a4b3c1475732ad519e64b4a9d06caa2572994d5`
- Receipt: content sha256 `9051391bbdfd9922d24d33130da54302f144ebd971abbfac4eb1e5ed4966c29a`, UNSIGNED
- Scope: integrity and the declared evaluation only. Scientific validity is not established by this tool.

## WHAT WAS EXPECTED

- Manifest `manifest.json`, sha256 `519aaae97a00eaef8603495af67b470b86f894dfe3f3fce6870096e77405c7be`, run label `corpus-time-source-mismatch-synthetic-01`

Inputs declared: 1 (expected_inputs 1)

- `readings`: `fixtures/data/readings.csv`, csv, required, expected_rows 3 (INDEPENDENT), declared sha256 `6ca454843013ae196556324e1b2c03d0385f15045009db0a4c4dba2c0ab5c9a8`

Checks declared: 3, of which 3 required (checks_expected 3)

- `rows`: row_count v1, required, inputs readings
- `columns`: required_columns v1, required, inputs readings
- `timing`: time_source v1, required, inputs 

PASS requires: every required input found, opened, parsed and matching any declared digest; at least one input opened; at least one data row examined; checks_executed == checks_expected; every required check PASS with a falsifier witness showing it could have failed; every applicable invariant holding; a non-empty evidence manifest.

## WHAT WAS EXAMINED

- Input funnel: expected 1 -> discovered 1 -> opened 1 -> parsed 1 -> examined 1; input closure holds (1 of 1, INDEPENDENT)
- rows_examined: 3 (distinct data rows of declared inputs read by an executed check)
- Each check line under WHAT PASSED, WHAT FAILED and WHAT ABSTAINED gives that check's own subject records examined (its run.json checks[].rows_examined); those figures are not summed.

Inputs:

- `readings` PARSED: `fixtures/data/readings.csv`, sha256 `6ca454843013ae196556324e1b2c03d0385f15045009db0a4c4dba2c0ab5c9a8`, 128 bytes, 3 records (admitted 3, excluded 0, deferred 0, unresolved 0, failed 0); row closure holds (3 of 3, INDEPENDENT)

Other documents read:

- `fixtures/time/events.json` (time_sources): PARSED, sha256 `8fc7eb0f8412cba9425987cc3ae154906bbca67a9103b20bd424a1623d2016c6`

## WHAT ACTUALLY RAN

- checks_executed 3 of checks_expected 3 (required checks that reached CHECKED with a terminal invocation)
- Ledger sealed at 17 entries, head `6eee15235d36fe935d90f1344a4b3c1475732ad519e64b4a9d06caa2572994d5`
- PLAN: ledger entry 1, entry sha256 `8fc0339df2a672b2d0e8da9c79a0f63035b9049c9b85b15a8912f3def2c392ea`, written before any check ran: 1 input(s), 3 check(s) and 4 pin(s) planned, manifest sha256 `519aaae97a00eaef8603495af67b470b86f894dfe3f3fce6870096e77405c7be`

Invocations:

- `columns` (required_columns v1): invocation `inv-4bb7ce4d8f57`, CHECKED, PASS; falsifier witness WITNESSED (1 of 1 case(s) rejected as expected)
- `rows` (row_count v1): invocation `inv-1da562920b31`, CHECKED, PASS; falsifier witness WITNESSED (1 of 1 case(s) rejected as expected)
- `timing` (time_source v1): invocation `inv-f51cea47dd76`, CHECKED, FAIL; no falsifier ran (only a would-be PASS is falsified)

Controls (each its own invocation, never counted as a check):

- comparator self-test: invocation `inv-6993c2a856b6`, 3 of 3 known pair(s) compared as expected; holds
- canary: must_fail invocation `inv-443189b0d72d` gave FAIL (SOURCE_MISMATCH), expected FAIL; must_pass invocation `inv-3ba1ff2c923f` gave PASS (VERIFIED), expected PASS; holds
- harness pins: 4 file(s) pinned; changed: none; writes to pinned paths: none; holds
- falsifier witnesses: WITNESSED 2 (`columns`, `rows`), REFUTED 0, UNWITNESSED 0, NO_CASE 0, NO_GENERATOR 0; 2 falsifier invocation(s)
- claim-to-invocation join: no claim_join check ran

## WHAT PASSED

Checks:

- `columns`: required_columns PASS (VERIFIED), subject records examined 3
- `rows`: row_count PASS (VERIFIED), subject records examined 3

Weakest discrimination: no PASS result records a discrimination ratio

Invariants that hold:

- `canary_controls_hold`: the must-fail canary failed and its known-good twin passed
- `checked_claims_le_invocations`: check results marked CHECKED: 3 claimed <= 8 invoked
- `comparator_self_test`: 3 known pairs compared as expected
- `every_invocation_has_terminal_result`: 8 invocation(s) each reached exactly one terminal result
- `every_required_check_has_terminal_state`: 3 required check(s) each reached a terminal state
- `every_verdict_has_invocation`: 3 verdict(s) each trace to a terminal invocation
- `harness_pins_intact`: 4 pinned file(s) unchanged and never written during the run
- `input_accounting_closure`: 2 INDEPENDENT closure(s) hold
- `ledger_chain_intact`: 17 entries chain to head 6eee15235d36fe935d90f1344a4b3c1475732ad519e64b4a9d06caa2572994d5
- `pass_requires_complete_required_inputs`: every input behind a PASS is complete
- `pass_requires_examined_rows`: rows_examined=3 (distinct data rows of declared inputs)
- `pass_requires_falsifier_witness`: 2 PASS result(s) each carry a ledger-backed falsifier witness
- `pass_requires_nonempty_evidence`: every PASS carries non-empty, hashed evidence
- `plan_closure`: 6 planned item(s) each ran exactly once
- `plan_matches_manifest`: the recorded PLAN equals the plan the manifest implies

## WHAT FAILED

Findings:

- none

Checks:

- `timing`: time_source FAIL (SOURCE_MISMATCH), subject records examined 3; event 'syn-obs-03': OUTSIDE_WINDOW

## WHAT ABSTAINED

Findings:

- none

Checks:

- none

## WHAT REMAINS UNRESOLVED

- invariant `pass_requires_complete_required_checks` not applicable: the run does not claim PASS
- the receipt is UNSIGNED (receipt.auth.json says so): its content hash detects accidental change, but anyone able to edit the run directory can rewrite and rehash it

## WHAT THIS RESULT DOES NOT PROVE

- Scientific validity: NOT ESTABLISHED. Whether any conclusion holds in its intended domain is outside what this tool can show.
- Integrity (what was established): SHA-256 recorded for 1 of 1 declared input(s); execution ledger sealed at 17 entries; ledger head 6eee15235d36fe935d90f1344a4b3c1475732ad519e64b4a9d06caa2572994d5; evidence manifest c139fb3c9607c89b19b0b43873b913199bc942f984d3b816cdf67a8bc3de8cd6.
- Performance (how the checkers and the declared checks behaved): CHECKER: falsifier witnesses 2 WITNESSED, 0 REFUTED, 0 UNWITNESSED, 0 NO_CASE, 0 NO_GENERATOR (2 falsifier invocation(s)); must-fail/must-pass canary held; comparator self-test held. RUN: Run status FAIL (SOURCE_MISMATCH) from 3 check result(s): 2 PASS, 1 FAIL, 0 ABSTAIN, 0 ERROR; 15 applicable invariant(s), 0 violated. This describes how the declared checks behaved on the declared inputs only.
- A PASS shows only that the declared checks had the opportunity to fail on the declared inputs and did not. It says nothing about inputs, checks or questions that were not declared, and nothing about whether the declared expectations were the right ones.
- A falsifier witness shows that a checker rejected the known-bad cases constructed for it; it does not show that the checker rejects every defect.
- Write detection: the harness pins are watched by an in-process audit hook. File reads and writes made by a subprocess or by C-extension code are invisible to it, so pins that hold do not exclude changes made that way.
- Network: no live lookup was performed; nothing was confirmed against an external source.
- A receipt supports integrity, provenance, and replayability. It does not establish scientific truth, accuracy, safety, or fitness for use.

## FILES

- `run.json`
- `report.md`
- `ledger.jsonl`
- `evidence-manifest.json`
- `receipt.json`
- `receipt.auth.json`
- `results.sarif`
- `report.html`
