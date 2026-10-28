## STATUS

**FAIL** (SOURCE_MISMATCH), exit code 1.

- Run: `run-7e468bf65c2d53c1`
- Started 2026-09-26T00:00:00Z; completed 2026-09-26T00:00:00Z
- Reasons: SOURCE_MISMATCH
- Failure modes: SOURCE_MISMATCH
- Evidence manifest sha256: `f2d414db6600cdaf377caf6b8d88fc3c3f02e24ab4cf2799914463266d272736`
- Ledger: 6 entries, head `daf00271550005fa25d00dbb87a89d1b4b68f0011c8f805349e41ae09b6ac673`
- Receipt: content sha256 `12d1dee641f300f6c83103fa3f1c94117a0342c871232a149526b42373b657da`, UNSIGNED
- Scope: integrity and the declared evaluation only. Scientific validity is not established by this tool.

## WHAT WAS EXPECTED

- Manifest `manifest.json`, sha256 `519aaae97a00eaef8603495af67b470b86f894dfe3f3fce6870096e77405c7be`, run label `corpus-time-source-mismatch-synthetic-01`

Inputs declared: 1 (expected_inputs 1)

- `readings`: `fixtures/data/readings.csv`, csv, required, expected_rows 3 (INDEPENDENT), declared sha256 `6ca454843013ae196556324e1b2c03d0385f15045009db0a4c4dba2c0ab5c9a8`

Checks declared: 3, of which 3 required (checks_expected 3)

- `rows`: row_count v1, required, inputs readings
- `columns`: required_columns v1, required, inputs readings
- `timing`: time_source v1, required, inputs 

PASS requires: every required input found, opened, parsed and matching any declared digest; at least one input opened; at least one row examined; checks_executed == checks_expected; every required check PASS; every applicable invariant holding; a non-empty evidence manifest.

## WHAT WAS EXAMINED

- Input funnel: expected 1 -> discovered 1 -> opened 1 -> parsed 1 -> examined 1; input closure holds (1 of 1, INDEPENDENT)
- Rows examined in scope: 6

Inputs:

- `readings` PARSED: `fixtures/data/readings.csv`, sha256 `6ca454843013ae196556324e1b2c03d0385f15045009db0a4c4dba2c0ab5c9a8`, 128 bytes, 3 records (admitted 3, excluded 0, deferred 0, unresolved 0, failed 0); row closure holds (3 of 3, INDEPENDENT)

Other documents read:

- `fixtures/time/events.json` (time_sources): PARSED, sha256 `8fc7eb0f8412cba9425987cc3ae154906bbca67a9103b20bd424a1623d2016c6`

## WHAT ACTUALLY RAN

- checks_executed 3 of checks_expected 3 (required checks that reached CHECKED with a terminal invocation)
- Ledger sealed at 6 entries, head `daf00271550005fa25d00dbb87a89d1b4b68f0011c8f805349e41ae09b6ac673`

Invocations:

- `columns` (required_columns v1): invocation `inv-3ebb21033743`, CHECKED, PASS, rows examined 3
- `rows` (row_count v1): invocation `inv-87151f286fea`, CHECKED, PASS, rows examined 3
- `timing` (time_source v1): invocation `inv-1dca57956418`, CHECKED, FAIL, rows examined 3

## WHAT PASSED

Checks:

- `columns`: required_columns PASS (VERIFIED), rows examined 3
- `rows`: row_count PASS (VERIFIED), rows examined 3

Invariants that hold:

- `checked_claims_le_invocations`: check results marked CHECKED: 3 claimed <= 3 invoked
- `every_invocation_has_terminal_result`: 3 invocation(s) each reached exactly one terminal result
- `every_required_check_has_terminal_state`: 3 required check(s) each reached a terminal state
- `every_verdict_has_invocation`: 3 verdict(s) each trace to a terminal invocation
- `input_accounting_closure`: 2 INDEPENDENT closure(s) hold
- `ledger_chain_intact`: 6 entries chain to head daf00271550005fa25d00dbb87a89d1b4b68f0011c8f805349e41ae09b6ac673
- `pass_requires_complete_required_inputs`: every input behind a PASS is complete
- `pass_requires_examined_rows`: rows_examined=9
- `pass_requires_nonempty_evidence`: every PASS carries non-empty, hashed evidence

## WHAT FAILED

Findings:

- none

Checks:

- `timing`: time_source FAIL (SOURCE_MISMATCH), rows examined 3; event 'syn-obs-03': OUTSIDE_WINDOW

## WHAT ABSTAINED

Findings:

- none

Checks:

- none

## WHAT REMAINS UNRESOLVED

- invariant `pass_requires_complete_required_checks` not applicable: the run does not claim PASS
- the receipt is UNSIGNED: its content hash detects accidental change, but anyone able to edit the run directory can rewrite and rehash it

## WHAT THIS RESULT DOES NOT PROVE

- Scientific validity: NOT ESTABLISHED. Whether any conclusion holds in its intended domain is outside what this tool can show.
- Integrity (what was established): SHA-256 recorded for 1 of 1 declared input(s); execution ledger sealed at 6 entries; ledger head daf00271550005fa25d00dbb87a89d1b4b68f0011c8f805349e41ae09b6ac673; evidence manifest f2d414db6600cdaf377caf6b8d88fc3c3f02e24ab4cf2799914463266d272736.
- Performance (how the declared checks behaved): Run status FAIL (SOURCE_MISMATCH) from 3 check result(s): 2 PASS, 1 FAIL, 0 ABSTAIN, 0 ERROR; 9 applicable invariant(s), 0 violated. This describes how the declared checks behaved on the declared inputs only.
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
