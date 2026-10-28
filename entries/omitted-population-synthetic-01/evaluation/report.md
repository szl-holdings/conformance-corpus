## STATUS

**FAIL** (SOURCE_MISMATCH), exit code 1.

- Run: `run-904472dc8e8d38f7`
- Started 2026-09-26T00:00:00Z; completed 2026-09-26T00:00:00Z
- Reasons: SOURCE_MISMATCH
- Failure modes: OMITTED_POPULATION
- Evidence manifest sha256: `78d89961ae5860606738ea7c6d7876bf66d4aecf517b288f1a4ff898b140f325`
- Ledger: 8 entries, head `1f86c5f0786d2fba1d80b844345c2eec28f97b996f3a6393c799c578124ebbdb`
- Receipt: content sha256 `53a81904e1af539eceb42da23dfd23a310f1b9a485099f7eb6ad95c2f19402e8`, UNSIGNED
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

PASS requires: every required input found, opened, parsed and matching any declared digest; at least one input opened; at least one row examined; checks_executed == checks_expected; every required check PASS; every applicable invariant holding; a non-empty evidence manifest.

## WHAT WAS EXAMINED

- Input funnel: expected 1 -> discovered 1 -> opened 1 -> parsed 1 -> examined 1; input closure holds (1 of 1, INDEPENDENT)
- Rows examined in scope: 5

Inputs:

- `specimens` PARSED: `fixtures/specimens.csv`, sha256 `332625dbf3d73ae54d7a2411db2c43d61d7a71a7675ecfaa4f01fb0dc5c020f8`, 159 bytes, 5 records (admitted 5, excluded 0, deferred 0, unresolved 0, failed 0); row closure not evaluable (OBSERVED expectation)

Other documents read:

- `fixtures/snapshots/accepted.json` (accepted_snapshot): PARSED, sha256 `e5957696dc49a3cfeedc6387a3a4fa92c5080bcb12d3bbe6390d0df4f100d8b8`

## WHAT ACTUALLY RAN

- checks_executed 4 of checks_expected 4 (required checks that reached CHECKED with a terminal invocation)
- Ledger sealed at 8 entries, head `1f86c5f0786d2fba1d80b844345c2eec28f97b996f3a6393c799c578124ebbdb`

Invocations:

- `columns` (required_columns v1): invocation `inv-a66285ac6c50`, CHECKED, PASS, rows examined 5
- `duplicates` (duplicate_rows v1): invocation `inv-0e7a1d8086d2`, CHECKED, PASS, rows examined 5
- `rows` (row_count v1): invocation `inv-ad24763f08e7`, CHECKED, PASS, rows examined 5
- `snapshot` (snapshot_completeness v1): invocation `inv-654eb4fc2f93`, CHECKED, FAIL, rows examined 5

## WHAT PASSED

Checks:

- `columns`: required_columns PASS (VERIFIED), rows examined 5
- `duplicates`: duplicate_rows PASS (VERIFIED), rows examined 5
- `rows`: row_count PASS (VERIFIED), rows examined 5

Invariants that hold:

- `checked_claims_le_invocations`: check results marked CHECKED: 4 claimed <= 4 invoked
- `every_invocation_has_terminal_result`: 4 invocation(s) each reached exactly one terminal result
- `every_required_check_has_terminal_state`: 4 required check(s) each reached a terminal state
- `every_verdict_has_invocation`: 4 verdict(s) each trace to a terminal invocation
- `input_accounting_closure`: 1 INDEPENDENT closure(s) hold
- `ledger_chain_intact`: 8 entries chain to head 1f86c5f0786d2fba1d80b844345c2eec28f97b996f3a6393c799c578124ebbdb
- `pass_requires_complete_required_inputs`: every input behind a PASS is complete
- `pass_requires_examined_rows`: rows_examined=20
- `pass_requires_nonempty_evidence`: every PASS carries non-empty, hashed evidence

## WHAT FAILED

Findings:

- none

Checks:

- `snapshot`: snapshot_completeness FAIL (SOURCE_MISMATCH), rows examined 5; input 'specimens': 1 accepted row(s) were deleted

## WHAT ABSTAINED

Findings:

- none

Checks:

- none

## WHAT REMAINS UNRESOLVED

- row closure of input `specimens` not evaluated (OBSERVED)
- invariant `pass_requires_complete_required_checks` not applicable: the run does not claim PASS
- the receipt is UNSIGNED: its content hash detects accidental change, but anyone able to edit the run directory can rewrite and rehash it

## WHAT THIS RESULT DOES NOT PROVE

- Scientific validity: NOT ESTABLISHED. Whether any conclusion holds in its intended domain is outside what this tool can show.
- Integrity (what was established): SHA-256 recorded for 1 of 1 declared input(s); execution ledger sealed at 8 entries; ledger head 1f86c5f0786d2fba1d80b844345c2eec28f97b996f3a6393c799c578124ebbdb; evidence manifest 78d89961ae5860606738ea7c6d7876bf66d4aecf517b288f1a4ff898b140f325.
- Performance (how the declared checks behaved): Run status FAIL (SOURCE_MISMATCH) from 4 check result(s): 3 PASS, 1 FAIL, 0 ABSTAIN, 0 ERROR; 9 applicable invariant(s), 0 violated. This describes how the declared checks behaved on the declared inputs only.
- A PASS shows only that the declared checks had the opportunity to fail on the declared inputs and did not. It says nothing about inputs, checks or questions that were not declared, and nothing about whether the declared expectations were the right ones.
- Network: no live lookup was performed; nothing was confirmed against an external source.
- A receipt supports integrity, provenance, and replayability. It does not establish scientific truth, accuracy, safety, or fitness for use.

## FILES

- `run.json`
- `report.md`
- `ledger.jsonl`
- `evidence-manifest.json`
- `receipt.json`
- `results.sarif`
- `report.html`
