## STATUS

**ABSTAIN** (INSUFFICIENT_EVIDENCE), exit code 2.

- Run: `run-ebeaf9c4a4607f57`
- Started 2026-09-26T00:00:00Z; completed 2026-09-26T00:00:00Z
- Reasons: INSUFFICIENT_EVIDENCE, PARTIAL_EXECUTION
- Failure modes: PARTIAL_EXECUTION
- Evidence manifest sha256: `ad002ce289dbe5c99946bb400864781493da67f2eb0667659fb0768e4eba24f8`
- Ledger: 8 entries, head `f97b5b79700c1c7d1f81dc17fa48c898b985d2eb66846cbf9464ba004576f0f7`
- Receipt: content sha256 `26ab74de2f2d10ca7ab7d5b2b5695b5ed5ddf81b3cfba9a83b4c32c7e2fe197f`, UNSIGNED
- Scope: integrity and the declared evaluation only. Scientific validity is not established by this tool.

## WHAT WAS EXPECTED

- Manifest `manifest.json`, sha256 `6b74a38cec314b6d1f00651c4cd4cc66d801f959cb7dfd31a96939bed4cac524`, run label `corpus-partial-execution-synthetic-01`

Inputs declared: 1 (expected_inputs 1)

- `samples`: `fixtures/data/samples.csv`, csv, required, expected_rows 5 (INDEPENDENT), declared sha256 `1581a2901c01c139f255390ff7782d7fa2a5290625114f80a23bf35705dfe199`

Checks declared: 4, of which 4 required (checks_expected 4)

- `rows`: row_count v1, required, inputs samples
- `columns`: required_columns v1, required, inputs samples
- `duplicates`: duplicate_rows v1, required, inputs samples
- `time-window`: time_source v1, required, inputs 

PASS requires: every required input found, opened, parsed and matching any declared digest; at least one input opened; at least one row examined; checks_executed == checks_expected; every required check PASS; every applicable invariant holding; a non-empty evidence manifest.

## WHAT WAS EXAMINED

- Input funnel: expected 1 -> discovered 1 -> opened 1 -> parsed 1 -> examined 1; input closure holds (1 of 1, INDEPENDENT)
- Rows examined in scope: 5

Inputs:

- `samples` PARSED: `fixtures/data/samples.csv`, sha256 `1581a2901c01c139f255390ff7782d7fa2a5290625114f80a23bf35705dfe199`, 249 bytes, 5 records (admitted 5, excluded 0, deferred 0, unresolved 0, failed 0); row closure holds (5 of 5, INDEPENDENT)

Other documents read:

- `fixtures/time/events.json` (time_sources): MISSING, sha256 `unknown`

## WHAT ACTUALLY RAN

- checks_executed 3 of checks_expected 4 (required checks that reached CHECKED with a terminal invocation)
- Ledger sealed at 8 entries, head `f97b5b79700c1c7d1f81dc17fa48c898b985d2eb66846cbf9464ba004576f0f7`

Invocations:

- `columns` (required_columns v1): invocation `inv-dda39c018130`, CHECKED, PASS, rows examined 5
- `duplicates` (duplicate_rows v1): invocation `inv-b8e1415a1d09`, CHECKED, PASS, rows examined 5
- `rows` (row_count v1): invocation `inv-ca38fd780015`, CHECKED, PASS, rows examined 5
- `time-window` (time_source v1): invocation `inv-c6a767737dd2`, SKIPPED, ABSTAIN, rows examined 0

## WHAT PASSED

Checks:

- `columns`: required_columns PASS (VERIFIED), rows examined 5
- `duplicates`: duplicate_rows PASS (VERIFIED), rows examined 5
- `rows`: row_count PASS (VERIFIED), rows examined 5

Invariants that hold:

- `checked_claims_le_invocations`: check results marked CHECKED: 3 claimed <= 4 invoked
- `every_invocation_has_terminal_result`: 4 invocation(s) each reached exactly one terminal result
- `every_required_check_has_terminal_state`: 4 required check(s) each reached a terminal state
- `every_verdict_has_invocation`: 4 verdict(s) each trace to a terminal invocation
- `input_accounting_closure`: 2 INDEPENDENT closure(s) hold
- `ledger_chain_intact`: 8 entries chain to head f97b5b79700c1c7d1f81dc17fa48c898b985d2eb66846cbf9464ba004576f0f7
- `pass_requires_complete_required_inputs`: every input behind a PASS is complete
- `pass_requires_examined_rows`: rows_examined=15
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

- `time-window`: time_source ABSTAIN (INSUFFICIENT_EVIDENCE), rows examined 0; time_sources (fixtures/time/events.json) unavailable: MISSING: no file at fixtures/time/events.json

## WHAT REMAINS UNRESOLVED

- document `fixtures/time/events.json` is MISSING: MISSING: no file at fixtures/time/events.json
- check `time-window` was SKIPPED
- invariant `pass_requires_complete_required_checks` not applicable: the run does not claim PASS
- the receipt is UNSIGNED: its content hash detects accidental change, but anyone able to edit the run directory can rewrite and rehash it

## WHAT THIS RESULT DOES NOT PROVE

- Scientific validity: NOT ESTABLISHED. Whether any conclusion holds in its intended domain is outside what this tool can show.
- Integrity (what was established): SHA-256 recorded for 1 of 1 declared input(s); execution ledger sealed at 8 entries; ledger head f97b5b79700c1c7d1f81dc17fa48c898b985d2eb66846cbf9464ba004576f0f7; evidence manifest ad002ce289dbe5c99946bb400864781493da67f2eb0667659fb0768e4eba24f8.
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
