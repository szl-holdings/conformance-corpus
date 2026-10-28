## STATUS

**ABSTAIN** (OUT_OF_SCOPE), exit code 2.

- Run: `run-739f4765bf370c62`
- Started 2026-09-26T00:00:00Z; completed 2026-09-26T00:00:00Z
- Reasons: OUT_OF_SCOPE
- Failure modes: none
- Verdict rises: NONE -> PASS at step 1 (`check:columns`, VERIFIED); PASS -> ABSTAIN at step 4 (`check:time_window`, OUT_OF_SCOPE)
- Evidence manifest sha256: `5a40778b2f979588271ca74afaad017615a23e04baedd1031f2ca70691151742`
- Ledger: 21 entries, head `f44a63f353e99e3569e2f3b8e0247b77403d65ca9716cf156d3c04b7a1a1efc1`
- Receipt: content sha256 `1ae7724d7b65776db7fcc106531647e3d7dc69c780a77506481359f0ddf732c2`, UNSIGNED
- Scope: integrity and the declared evaluation only. Scientific validity is not established by this tool.

## WHAT WAS EXPECTED

- Manifest `manifest.json`, sha256 `0fbe1336c0ce43a210b7cc9eac5c1b60068a8cfaac5473b70b300a0658a2aa75`, run label `corpus-coverage-debt-synthetic-01`

Inputs declared: 1 (expected_inputs 1)

- `readings`: `fixtures/readings.csv`, csv, required, expected_rows 4 (INDEPENDENT), declared sha256 `6717b12e09e1b262927e09e3619b12e1ed9a11d9aa114e7b858a5f663d2c91b9`

Checks declared: 4, of which 4 required (checks_expected 4)

- `rows`: row_count v1, required, inputs readings
- `columns`: required_columns v1, required, inputs readings
- `duplicates`: duplicate_rows v1, required, inputs readings
- `time_window`: time_source v1, required, inputs 

PASS requires: every required input found, opened, parsed and matching any declared digest; at least one input opened; at least one data row examined; checks_executed == checks_expected; every required check PASS with a falsifier witness showing it could have failed; every applicable invariant holding; a non-empty evidence manifest.

## WHAT WAS EXAMINED

- Input funnel: expected 1 -> discovered 1 -> opened 1 -> parsed 1 -> examined 1; input closure holds (1 of 1, INDEPENDENT)
- rows_examined: 4 (distinct data rows of declared inputs read by an executed check)
- Each check line under WHAT PASSED, WHAT FAILED and WHAT ABSTAINED gives that check's own subject records examined (its run.json checks[].rows_examined); those figures are not summed.

Inputs:

- `readings` PARSED: `fixtures/readings.csv`, sha256 `6717b12e09e1b262927e09e3619b12e1ed9a11d9aa114e7b858a5f663d2c91b9`, 140 bytes, 4 records (admitted 4, excluded 0, deferred 0, unresolved 0, failed 0); row closure holds (4 of 4, INDEPENDENT)

Other documents read:

- none

## WHAT ACTUALLY RAN

- checks_executed 3 of checks_expected 4 (required checks that reached CHECKED with a terminal invocation)
- Ledger sealed at 21 entries, head `f44a63f353e99e3569e2f3b8e0247b77403d65ca9716cf156d3c04b7a1a1efc1`
- PLAN: ledger entry 1, entry sha256 `0f55a15982231911265e51771c31fc3a7f1aac764d0b541192497d446098d299`, written before any check ran: 1 input(s), 4 check(s) and 3 pin(s) planned, manifest sha256 `0fbe1336c0ce43a210b7cc9eac5c1b60068a8cfaac5473b70b300a0658a2aa75`

Invocations:

- `columns` (required_columns v1): invocation `inv-9caad6d837f5`, CHECKED, PASS; falsifier witness WITNESSED (1 of 1 case(s) rejected as expected)
- `duplicates` (duplicate_rows v1): invocation `inv-1ed386bd6822`, CHECKED, PASS; falsifier witness WITNESSED (1 of 1 case(s) rejected as expected)
- `rows` (row_count v1): invocation `inv-90625c1b68e0`, CHECKED, PASS; falsifier witness WITNESSED (1 of 1 case(s) rejected as expected)
- `time_window` (time_source v1): invocation `inv-74ba568d795e`, NOT_APPLICABLE, ABSTAIN; no falsifier ran (only a would-be PASS is falsified)

Controls (each its own invocation, never counted as a check):

- comparator self-test: invocation `inv-3d0832f5c49e`, 3 of 3 known pair(s) compared as expected; holds
- canary: must_fail invocation `inv-cbe68cc29395` gave FAIL (SOURCE_MISMATCH), expected FAIL; must_pass invocation `inv-7747753a5bb2` gave PASS (VERIFIED), expected PASS; holds
- harness pins: 3 file(s) pinned; changed: none; writes to pinned paths: none; holds
- falsifier witnesses: WITNESSED 3 (`columns`, `duplicates`, `rows`), REFUTED 0, UNWITNESSED 0, NO_CASE 0, NO_GENERATOR 0; 3 falsifier invocation(s)
- claim-to-invocation join: no claim_join check ran

## WHAT PASSED

Checks:

- `columns`: required_columns PASS (VERIFIED), subject records examined 4
- `duplicates`: duplicate_rows PASS (VERIFIED), subject records examined 4
- `rows`: row_count PASS (VERIFIED), subject records examined 4

Weakest discrimination: no PASS result records a discrimination ratio

Invariants that hold:

- `canary_controls_hold`: the must-fail canary failed and its known-good twin passed
- `checked_claims_le_invocations`: check results marked CHECKED: 3 claimed <= 10 invoked
- `comparator_self_test`: 3 known pairs compared as expected
- `every_invocation_has_terminal_result`: 10 invocation(s) each reached exactly one terminal result
- `every_required_check_has_terminal_state`: 4 required check(s) each reached a terminal state
- `every_verdict_has_invocation`: 4 verdict(s) each trace to a terminal invocation
- `harness_pins_intact`: 3 pinned file(s) unchanged and never written during the run
- `input_accounting_closure`: 2 INDEPENDENT closure(s) hold
- `ledger_chain_intact`: 21 entries chain to head f44a63f353e99e3569e2f3b8e0247b77403d65ca9716cf156d3c04b7a1a1efc1
- `pass_requires_complete_required_inputs`: every input behind a PASS is complete
- `pass_requires_examined_rows`: rows_examined=4 (distinct data rows of declared inputs)
- `pass_requires_falsifier_witness`: 3 PASS result(s) each carry a ledger-backed falsifier witness
- `pass_requires_nonempty_evidence`: every PASS carries non-empty, hashed evidence
- `plan_closure`: 7 planned item(s) each ran exactly once
- `plan_matches_manifest`: the recorded PLAN equals the plan the manifest implies

## WHAT FAILED

Findings:

- none

Checks:

- none

## WHAT ABSTAINED

Findings:

- [contract:checks_executed] ABSTAIN OUT_OF_SCOPE: required check 'time_window' did not execute: it was NOT_APPLICABLE, justified as NOT_DECLARED (checks_executed=3 of checks_expected=4)

Checks:

- `time_window`: time_source ABSTAIN (OUT_OF_SCOPE), subject records examined 0; the manifest declares no time_sources

## WHAT REMAINS UNRESOLVED

- check `time_window` was NOT_APPLICABLE
- invariant `pass_requires_complete_required_checks` not applicable: the run does not claim PASS
- the receipt is UNSIGNED (receipt.auth.json says so): its content hash detects accidental change, but anyone able to edit the run directory can rewrite and rehash it

## WHAT THIS RESULT DOES NOT PROVE

- Scientific validity: NOT ESTABLISHED. Whether any conclusion holds in its intended domain is outside what this tool can show.
- Integrity (what was established): SHA-256 recorded for 1 of 1 declared input(s); execution ledger sealed at 21 entries; ledger head f44a63f353e99e3569e2f3b8e0247b77403d65ca9716cf156d3c04b7a1a1efc1; evidence manifest 5a40778b2f979588271ca74afaad017615a23e04baedd1031f2ca70691151742.
- Performance (how the checkers and the declared checks behaved): CHECKER: falsifier witnesses 3 WITNESSED, 0 REFUTED, 0 UNWITNESSED, 0 NO_CASE, 0 NO_GENERATOR (3 falsifier invocation(s)); must-fail/must-pass canary held; comparator self-test held. RUN: Run status ABSTAIN (OUT_OF_SCOPE) from 4 check result(s): 3 PASS, 0 FAIL, 1 ABSTAIN, 0 ERROR; 15 applicable invariant(s), 0 violated. This describes how the declared checks behaved on the declared inputs only.
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
