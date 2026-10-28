## STATUS

**FAIL** (SOURCE_MISMATCH), exit code 1.

- Run: `run-904472dc8e8d38f7`
- Started 2026-09-26T00:00:00Z; completed 2026-09-26T00:00:00Z
- Reasons: BLIND_SPOT, SOURCE_MISMATCH
- Failure modes: OMITTED_POPULATION, VACUOUS_PASS
- Verdict rises: NONE -> PASS at step 1 (`check:columns`, VERIFIED); PASS -> ABSTAIN at step 3 (`check:rows`, BLIND_SPOT); ABSTAIN -> FAIL at step 4 (`check:snapshot`, SOURCE_MISMATCH)
- Evidence manifest sha256: `bbbf549a4bf51f5e340a92dfe919d00d1384bf171442c7b05f2ef6ae54ae697d`
- Ledger: 19 entries, head `5edaa084af31cee22777033d5d1686a65029d2fd25e896a014a5d31349d29d1f`
- Receipt: content sha256 `455ee96f5c1d73dc620e1515510d968cd40d10ca108f4d51acc7d82940533446`, UNSIGNED
- Scope: integrity and the declared evaluation only. Scientific validity is not established by this tool.

## WHAT WAS EXPECTED

- Manifest `manifest.json`, sha256 `7083263b900fd06b40dbabcd7dd4b7adf9742c21ab9a02cf2f3346f140f6b2b5`, run label `corpus-omitted-population-synthetic-01`

Inputs declared: 1 (expected_inputs 1)

- `specimens`: `fixtures/specimens.csv`, csv, required, expected_rows 5 (OBSERVED), declared sha256 `332625dbf3d73ae54d7a2411db2c43d61d7a71a7675ecfaa4f01fb0dc5c020f8`

Checks declared: 4, of which 4 required (checks_expected 4)

- `rows`: row_count v1, required, inputs specimens
- `columns`: required_columns v1, required, inputs specimens
- `duplicates`: duplicate_rows v1, required, inputs specimens
- `snapshot`: snapshot_completeness v1, required, inputs specimens

PASS requires: every required input found, opened, parsed and matching any declared digest; at least one input opened; at least one data row examined; checks_executed == checks_expected; every required check PASS with a falsifier witness showing it could have failed; every applicable invariant holding; a non-empty evidence manifest.

## WHAT WAS EXAMINED

- Input funnel: expected 1 -> discovered 1 -> opened 1 -> parsed 1 -> examined 1; input closure holds (1 of 1, INDEPENDENT)
- rows_examined: 5 (distinct data rows of declared inputs read by an executed check)
- Each check line under WHAT PASSED, WHAT FAILED and WHAT ABSTAINED gives that check's own subject records examined (its run.json checks[].rows_examined); those figures are not summed.

Inputs:

- `specimens` PARSED: `fixtures/specimens.csv`, sha256 `332625dbf3d73ae54d7a2411db2c43d61d7a71a7675ecfaa4f01fb0dc5c020f8`, 159 bytes, 5 records (admitted 5, excluded 0, deferred 0, unresolved 0, failed 0); row closure not evaluable (OBSERVED expectation)

Other documents read:

- `fixtures/snapshots/accepted.json` (accepted_snapshot): PARSED, sha256 `e5957696dc49a3cfeedc6387a3a4fa92c5080bcb12d3bbe6390d0df4f100d8b8`

## WHAT ACTUALLY RAN

- checks_executed 4 of checks_expected 4 (required checks that reached CHECKED with a terminal invocation)
- Ledger sealed at 19 entries, head `5edaa084af31cee22777033d5d1686a65029d2fd25e896a014a5d31349d29d1f`
- PLAN: ledger entry 1, entry sha256 `3159e2771b5efb3704d61ed0e249c8ccb5a4a475737e44cb2623c1b66da66c08`, written before any check ran: 1 input(s), 4 check(s) and 4 pin(s) planned, manifest sha256 `7083263b900fd06b40dbabcd7dd4b7adf9742c21ab9a02cf2f3346f140f6b2b5`

Invocations:

- `columns` (required_columns v1): invocation `inv-1786eff6e4cb`, CHECKED, PASS; falsifier witness WITNESSED (1 of 1 case(s) rejected as expected)
- `duplicates` (duplicate_rows v1): invocation `inv-2a97957e2163`, CHECKED, PASS; falsifier witness WITNESSED (1 of 1 case(s) rejected as expected)
- `rows` (row_count v1): invocation `inv-e11393bc4ff8`, CHECKED, ABSTAIN; falsifier witness NO_CASE (0 of 0 case(s) rejected as expected)
- `snapshot` (snapshot_completeness v1): invocation `inv-16c3edb519cc`, CHECKED, FAIL; no falsifier ran (only a would-be PASS is falsified)

Controls (each its own invocation, never counted as a check):

- comparator self-test: invocation `inv-9dc09021b338`, 3 of 3 known pair(s) compared as expected; holds
- canary: must_fail invocation `inv-3d363bd6a777` gave FAIL (SOURCE_MISMATCH), expected FAIL; must_pass invocation `inv-9c33f3e0aabb` gave PASS (VERIFIED), expected PASS; holds
- harness pins: 4 file(s) pinned; changed: none; writes to pinned paths: none; holds
- falsifier witnesses: WITNESSED 2 (`columns`, `duplicates`), REFUTED 0, UNWITNESSED 0, NO_CASE 1 (`rows`), NO_GENERATOR 0; 2 falsifier invocation(s)
- claim-to-invocation join: no claim_join check ran

## WHAT PASSED

Checks:

- `columns`: required_columns PASS (VERIFIED), subject records examined 5
- `duplicates`: duplicate_rows PASS (VERIFIED), subject records examined 5

Weakest discrimination: no PASS result records a discrimination ratio

Invariants that hold:

- `canary_controls_hold`: the must-fail canary failed and its known-good twin passed
- `checked_claims_le_invocations`: check results marked CHECKED: 4 claimed <= 9 invoked
- `comparator_self_test`: 3 known pairs compared as expected
- `every_invocation_has_terminal_result`: 9 invocation(s) each reached exactly one terminal result
- `every_required_check_has_terminal_state`: 4 required check(s) each reached a terminal state
- `every_verdict_has_invocation`: 4 verdict(s) each trace to a terminal invocation
- `harness_pins_intact`: 4 pinned file(s) unchanged and never written during the run
- `input_accounting_closure`: 1 INDEPENDENT closure(s) hold
- `ledger_chain_intact`: 19 entries chain to head 5edaa084af31cee22777033d5d1686a65029d2fd25e896a014a5d31349d29d1f
- `pass_requires_complete_required_inputs`: every input behind a PASS is complete
- `pass_requires_examined_rows`: rows_examined=5 (distinct data rows of declared inputs)
- `pass_requires_falsifier_witness`: 2 PASS result(s) each carry a ledger-backed falsifier witness
- `pass_requires_nonempty_evidence`: every PASS carries non-empty, hashed evidence
- `plan_closure`: 7 planned item(s) each ran exactly once
- `plan_matches_manifest`: the recorded PLAN equals the plan the manifest implies

## WHAT FAILED

Findings:

- none

Checks:

- `snapshot`: snapshot_completeness FAIL (SOURCE_MISMATCH), subject records examined 5; input 'specimens': 1 accepted row(s) were deleted

## WHAT ABSTAINED

Findings:

- none

Checks:

- `rows`: row_count ABSTAIN (BLIND_SPOT), subject records examined 5; FALSIFIER_NO_CASE: the generator found no known-bad case for this row_count instance

## WHAT REMAINS UNRESOLVED

- row closure of input `specimens` not evaluated (OBSERVED)
- invariant `pass_requires_complete_required_checks` not applicable: the run does not claim PASS
- the receipt is UNSIGNED (receipt.auth.json says so): its content hash detects accidental change, but anyone able to edit the run directory can rewrite and rehash it

## WHAT THIS RESULT DOES NOT PROVE

- Scientific validity: NOT ESTABLISHED. Whether any conclusion holds in its intended domain is outside what this tool can show.
- Integrity (what was established): SHA-256 recorded for 1 of 1 declared input(s); execution ledger sealed at 19 entries; ledger head 5edaa084af31cee22777033d5d1686a65029d2fd25e896a014a5d31349d29d1f; evidence manifest bbbf549a4bf51f5e340a92dfe919d00d1384bf171442c7b05f2ef6ae54ae697d.
- Performance (how the checkers and the declared checks behaved): CHECKER: falsifier witnesses 2 WITNESSED, 0 REFUTED, 0 UNWITNESSED, 1 NO_CASE, 0 NO_GENERATOR (2 falsifier invocation(s)); must-fail/must-pass canary held; comparator self-test held. RUN: Run status FAIL (SOURCE_MISMATCH) from 4 check result(s): 2 PASS, 1 FAIL, 1 ABSTAIN, 0 ERROR; 15 applicable invariant(s), 0 violated. This describes how the declared checks behaved on the declared inputs only.
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
