## STATUS

**ABSTAIN** (INSUFFICIENT_EVIDENCE), exit code 2.

- Run: `run-c94566eed728c723`
- Started 2026-09-26T00:00:00Z; completed 2026-09-26T00:00:00Z
- Reasons: INSUFFICIENT_EVIDENCE, PARTIAL_EXECUTION
- Failure modes: PARTIAL_EXECUTION
- Evidence manifest sha256: `2143cd8d0c05e86d2d635aedb79a226bf8ed756b696cfe6383a48993cc4436c3`
- Ledger: 8 entries, head `011c9976aa33ad146a0973a7f5ba710707b7725d0a801b11d390519f2a7bf377`
- Receipt: content sha256 `d965cfd4520220f68c94526db58ba3f0fc0127f438e3aeb81d5e43f017af0a00`, UNSIGNED
- Scope: integrity and the declared evaluation only. Scientific validity is not established by this tool.

## WHAT WAS EXPECTED

- Manifest `manifest.json`, sha256 `663d7597f7eef6d2e266300bd51bfa69e4777a98e1e15b88c60599c4a128d9b9`, run label `corpus-coverage-debt-synthetic-01`

Inputs declared: 1 (expected_inputs 1)

- `readings`: `fixtures/readings.csv`, csv, required, expected_rows 4 (INDEPENDENT), declared sha256 `6717b12e09e1b262927e09e3619b12e1ed9a11d9aa114e7b858a5f663d2c91b9`

Checks declared: 4, of which 4 required (checks_expected 4)

- `rows`: row_count v1, required, inputs readings
- `columns`: required_columns v1, required, inputs readings
- `duplicates`: duplicate_rows v1, required, inputs readings
- `time_window`: time_source v1, required, inputs 

PASS requires: every required input found, opened, parsed and matching any declared digest; at least one input opened; at least one row examined; checks_executed == checks_expected; every required check PASS; every applicable invariant holding; a non-empty evidence manifest.

## WHAT WAS EXAMINED

- Input funnel: expected 1 -> discovered 1 -> opened 1 -> parsed 1 -> examined 1; input closure holds (1 of 1, INDEPENDENT)
- Rows examined in scope: 4

Inputs:

- `readings` PARSED: `fixtures/readings.csv`, sha256 `6717b12e09e1b262927e09e3619b12e1ed9a11d9aa114e7b858a5f663d2c91b9`, 140 bytes, 4 records (admitted 4, excluded 0, deferred 0, unresolved 0, failed 0); row closure holds (4 of 4, INDEPENDENT)

Other documents read:

- `fixtures/time/events.json` (time_sources): PARSED, sha256 `6082057c520337da9b7ede9db1cacc3a4dcde6b2e2b9873f594ae4bf269186ea`

## WHAT ACTUALLY RAN

- checks_executed 3 of checks_expected 4 (required checks that reached CHECKED with a terminal invocation)
- Ledger sealed at 8 entries, head `011c9976aa33ad146a0973a7f5ba710707b7725d0a801b11d390519f2a7bf377`

Invocations:

- `columns` (required_columns v1): invocation `inv-3bccffb21ed6`, CHECKED, PASS, rows examined 4
- `duplicates` (duplicate_rows v1): invocation `inv-9418e70a4891`, CHECKED, PASS, rows examined 4
- `rows` (row_count v1): invocation `inv-f66509e1f730`, CHECKED, PASS, rows examined 4
- `time_window` (time_source v1): invocation `inv-f8399be1c761`, NOT_APPLICABLE, ABSTAIN, rows examined 0

## WHAT PASSED

Checks:

- `columns`: required_columns PASS (VERIFIED), rows examined 4
- `duplicates`: duplicate_rows PASS (VERIFIED), rows examined 4
- `rows`: row_count PASS (VERIFIED), rows examined 4

Invariants that hold:

- `checked_claims_le_invocations`: check results marked CHECKED: 3 claimed <= 4 invoked
- `every_invocation_has_terminal_result`: 4 invocation(s) each reached exactly one terminal result
- `every_required_check_has_terminal_state`: 4 required check(s) each reached a terminal state
- `every_verdict_has_invocation`: 4 verdict(s) each trace to a terminal invocation
- `input_accounting_closure`: 2 INDEPENDENT closure(s) hold
- `ledger_chain_intact`: 8 entries chain to head 011c9976aa33ad146a0973a7f5ba710707b7725d0a801b11d390519f2a7bf377
- `pass_requires_complete_required_inputs`: every input behind a PASS is complete
- `pass_requires_examined_rows`: rows_examined=12
- `pass_requires_nonempty_evidence`: every PASS carries non-empty, hashed evidence

## WHAT FAILED

Findings:

- none

Checks:

- none

## WHAT ABSTAINED

Findings:

- [contract:checks_executed] ABSTAIN PARTIAL_EXECUTION (PARTIAL_EXECUTION): checks_executed=3 of checks_expected=4

Checks:

- `time_window`: time_source ABSTAIN (INSUFFICIENT_EVIDENCE), rows examined 0; the time sources list no events

## WHAT REMAINS UNRESOLVED

- check `time_window` was NOT_APPLICABLE
- invariant `pass_requires_complete_required_checks` not applicable: the run does not claim PASS
- the receipt is UNSIGNED: its content hash detects accidental change, but anyone able to edit the run directory can rewrite and rehash it

## WHAT THIS RESULT DOES NOT PROVE

- Scientific validity: NOT ESTABLISHED. Whether any conclusion holds in its intended domain is outside what this tool can show.
- Integrity (what was established): SHA-256 recorded for 1 of 1 declared input(s); execution ledger sealed at 8 entries; ledger head 011c9976aa33ad146a0973a7f5ba710707b7725d0a801b11d390519f2a7bf377; evidence manifest 2143cd8d0c05e86d2d635aedb79a226bf8ed756b696cfe6383a48993cc4436c3.
- Performance (how the declared checks behaved): Run status ABSTAIN (INSUFFICIENT_EVIDENCE) from 4 check result(s): 3 PASS, 0 FAIL, 1 ABSTAIN, 0 ERROR; 9 applicable invariant(s), 0 violated. This describes how the declared checks behaved on the declared inputs only.
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
