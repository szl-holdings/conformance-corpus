## STATUS

**ABSTAIN** (PROTOCOL_BROKEN), exit code 2.

- Run: `run-4b040081a8b6d019`
- Started 2026-09-26T00:00:00Z; completed 2026-09-26T00:00:00Z
- Reasons: PROTOCOL_BROKEN
- Failure modes: PROTOCOL_DRIFT
- Evidence manifest sha256: `cf03da130604214b0ac1a706f226333fc09a66306aa2c7ec7c8d5d8d7e414b5c`
- Ledger: 6 entries, head `a5ed0328d1af412128632734c6f4d0b3bd793892bee8e644365daee1610bdd39`
- Receipt: content sha256 `b4c729358e88d3bace4a1180d68bc1f13e05f63c134b10fd7f95a355fc8f1faf`, UNSIGNED
- Scope: integrity and the declared evaluation only. Scientific validity is not established by this tool.

## WHAT WAS EXPECTED

- Manifest `manifest.json`, sha256 `6ff18e2b947833e22d923337b4559867dcdb4da6dfa8c7245e6850d4e78acf89`, run label `corpus-reviewer-protocol-drift-synthetic-01`

Inputs declared: 1 (expected_inputs 1)

- `samples`: `fixtures/data/samples.csv`, csv, required, expected_rows 4 (INDEPENDENT), declared sha256 `56d2a65b338bf5977d78b03f8143cc48b07e2913f7b576d1a722aefeb53c440a`

Checks declared: 3, of which 3 required (checks_expected 3)

- `rows`: row_count v1, required, inputs samples
- `columns`: required_columns v1, required, inputs samples
- `reviewers`: reviewer_protocol v1, required, inputs 

PASS requires: every required input found, opened, parsed and matching any declared digest; at least one input opened; at least one row examined; checks_executed == checks_expected; every required check PASS; every applicable invariant holding; a non-empty evidence manifest.

## WHAT WAS EXAMINED

- Input funnel: expected 1 -> discovered 1 -> opened 1 -> parsed 1 -> examined 1; input closure holds (1 of 1, INDEPENDENT)
- Rows examined in scope: 7

Inputs:

- `samples` PARSED: `fixtures/data/samples.csv`, sha256 `56d2a65b338bf5977d78b03f8143cc48b07e2913f7b576d1a722aefeb53c440a`, 146 bytes, 4 records (admitted 4, excluded 0, deferred 0, unresolved 0, failed 0); row closure holds (4 of 4, INDEPENDENT)

Other documents read:

- `fixtures/reviews/verdicts.json` (reviews.verdicts): PARSED, sha256 `82c2836b62964ad6c40f9d478bc32e3cc33350f9c70505086c83ab6642712c42`

## WHAT ACTUALLY RAN

- checks_executed 3 of checks_expected 3 (required checks that reached CHECKED with a terminal invocation)
- Ledger sealed at 6 entries, head `a5ed0328d1af412128632734c6f4d0b3bd793892bee8e644365daee1610bdd39`

Invocations:

- `columns` (required_columns v1): invocation `inv-d9e0dd88507a`, CHECKED, PASS, rows examined 4
- `reviewers` (reviewer_protocol v1): invocation `inv-7b936224ac5a`, CHECKED, ABSTAIN, rows examined 3
- `rows` (row_count v1): invocation `inv-fa12bff1feb5`, CHECKED, PASS, rows examined 4

## WHAT PASSED

Checks:

- `columns`: required_columns PASS (VERIFIED), rows examined 4
- `rows`: row_count PASS (VERIFIED), rows examined 4

Invariants that hold:

- `checked_claims_le_invocations`: check results marked CHECKED: 3 claimed <= 3 invoked
- `every_invocation_has_terminal_result`: 3 invocation(s) each reached exactly one terminal result
- `every_required_check_has_terminal_state`: 3 required check(s) each reached a terminal state
- `every_verdict_has_invocation`: 3 verdict(s) each trace to a terminal invocation
- `input_accounting_closure`: 2 INDEPENDENT closure(s) hold
- `ledger_chain_intact`: 6 entries chain to head a5ed0328d1af412128632734c6f4d0b3bd793892bee8e644365daee1610bdd39
- `pass_requires_complete_required_inputs`: every input behind a PASS is complete
- `pass_requires_examined_rows`: rows_examined=11
- `pass_requires_nonempty_evidence`: every PASS carries non-empty, hashed evidence

## WHAT FAILED

Findings:

- none

Checks:

- none

## WHAT ABSTAINED

Findings:

- none

Checks:

- `reviewers`: reviewer_protocol ABSTAIN (PROTOCOL_BROKEN), rows examined 3; required reviewer(s) ['syn-reviewer-c'] recorded no verdict; reviewer(s) ['syn-reviewer-b'] recorded more than one verdict

## WHAT REMAINS UNRESOLVED

- invariant `pass_requires_complete_required_checks` not applicable: the run does not claim PASS
- the receipt is UNSIGNED: its content hash detects accidental change, but anyone able to edit the run directory can rewrite and rehash it

## WHAT THIS RESULT DOES NOT PROVE

- Scientific validity: NOT ESTABLISHED. Whether any conclusion holds in its intended domain is outside what this tool can show.
- Integrity (what was established): SHA-256 recorded for 1 of 1 declared input(s); execution ledger sealed at 6 entries; ledger head a5ed0328d1af412128632734c6f4d0b3bd793892bee8e644365daee1610bdd39; evidence manifest cf03da130604214b0ac1a706f226333fc09a66306aa2c7ec7c8d5d8d7e414b5c.
- Performance (how the declared checks behaved): Run status ABSTAIN (PROTOCOL_BROKEN) from 3 check result(s): 2 PASS, 0 FAIL, 1 ABSTAIN, 0 ERROR; 9 applicable invariant(s), 0 violated. This describes how the declared checks behaved on the declared inputs only.
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
