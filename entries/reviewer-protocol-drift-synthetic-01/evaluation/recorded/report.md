## STATUS

**ABSTAIN** (PROTOCOL_BROKEN), exit code 2.

- Run: `run-4b040081a8b6d019`
- Started 2026-09-26T00:00:00Z; completed 2026-09-26T00:00:00Z
- Reasons: PROTOCOL_BROKEN
- Failure modes: PROTOCOL_DRIFT
- Verdict rises: NONE -> PASS at step 1 (`check:columns`, VERIFIED); PASS -> ABSTAIN at step 3 (`check:reviewers`, PROTOCOL_BROKEN)
- Evidence manifest sha256: `99e85c41c843067731c701d27ea478577b2ef9ffc8cc2c06c33e97ade672c337`
- Ledger: 17 entries, head `b2674a4221fd4a825c7e7ad3205a4958ef9d9d92ea13d5dc3f2b7063697acaa8`
- Receipt: content sha256 `cc38c4d0aea07bc8e450cf36b1ae65007d304e345feecd7c89161a06cc2d0993`, UNSIGNED
- Scope: integrity and the declared evaluation only. Scientific validity is not established by this tool.

## WHAT WAS EXPECTED

- Manifest `manifest.json`, sha256 `6ff18e2b947833e22d923337b4559867dcdb4da6dfa8c7245e6850d4e78acf89`, run label `corpus-reviewer-protocol-drift-synthetic-01`

Inputs declared: 1 (expected_inputs 1)

- `samples`: `fixtures/data/samples.csv`, csv, required, expected_rows 4 (INDEPENDENT), declared sha256 `56d2a65b338bf5977d78b03f8143cc48b07e2913f7b576d1a722aefeb53c440a`

Checks declared: 3, of which 3 required (checks_expected 3)

- `rows`: row_count v1, required, inputs samples
- `columns`: required_columns v1, required, inputs samples
- `reviewers`: reviewer_protocol v1, required, inputs 

PASS requires: every required input found, opened, parsed and matching any declared digest; at least one input opened; at least one data row examined; checks_executed == checks_expected; every required check PASS with a falsifier witness showing it could have failed; every applicable invariant holding; a non-empty evidence manifest.

## WHAT WAS EXAMINED

- Input funnel: expected 1 -> discovered 1 -> opened 1 -> parsed 1 -> examined 1; input closure holds (1 of 1, INDEPENDENT)
- rows_examined: 4 (distinct data rows of declared inputs read by an executed check)
- Each check line under WHAT PASSED, WHAT FAILED and WHAT ABSTAINED gives that check's own subject records examined (its run.json checks[].rows_examined); those figures are not summed.

Inputs:

- `samples` PARSED: `fixtures/data/samples.csv`, sha256 `56d2a65b338bf5977d78b03f8143cc48b07e2913f7b576d1a722aefeb53c440a`, 146 bytes, 4 records (admitted 4, excluded 0, deferred 0, unresolved 0, failed 0); row closure holds (4 of 4, INDEPENDENT)

Other documents read:

- `fixtures/reviews/verdicts.json` (reviews.verdicts): PARSED, sha256 `82c2836b62964ad6c40f9d478bc32e3cc33350f9c70505086c83ab6642712c42`

## WHAT ACTUALLY RAN

- checks_executed 3 of checks_expected 3 (required checks that reached CHECKED with a terminal invocation)
- Ledger sealed at 17 entries, head `b2674a4221fd4a825c7e7ad3205a4958ef9d9d92ea13d5dc3f2b7063697acaa8`
- PLAN: ledger entry 1, entry sha256 `45739450b990a44987aefe996364ce61fd395fee4cf31d51b25a0a68def5a5af`, written before any check ran: 1 input(s), 3 check(s) and 4 pin(s) planned, manifest sha256 `6ff18e2b947833e22d923337b4559867dcdb4da6dfa8c7245e6850d4e78acf89`

Invocations:

- `columns` (required_columns v1): invocation `inv-fadfa99d5a1b`, CHECKED, PASS; falsifier witness WITNESSED (1 of 1 case(s) rejected as expected)
- `reviewers` (reviewer_protocol v1): invocation `inv-97cc26763dee`, CHECKED, ABSTAIN; no falsifier ran (only a would-be PASS is falsified)
- `rows` (row_count v1): invocation `inv-98e38e0a1f93`, CHECKED, PASS; falsifier witness WITNESSED (1 of 1 case(s) rejected as expected)

Controls (each its own invocation, never counted as a check):

- comparator self-test: invocation `inv-17245bfcbd9c`, 3 of 3 known pair(s) compared as expected; holds
- canary: must_fail invocation `inv-bad05959fddc` gave FAIL (SOURCE_MISMATCH), expected FAIL; must_pass invocation `inv-a4af5821b741` gave PASS (VERIFIED), expected PASS; holds
- harness pins: 4 file(s) pinned; changed: none; writes to pinned paths: none; holds
- falsifier witnesses: WITNESSED 2 (`columns`, `rows`), REFUTED 0, UNWITNESSED 0, NO_CASE 0, NO_GENERATOR 0; 2 falsifier invocation(s)
- claim-to-invocation join: no claim_join check ran

## WHAT PASSED

Checks:

- `columns`: required_columns PASS (VERIFIED), subject records examined 4
- `rows`: row_count PASS (VERIFIED), subject records examined 4

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
- `ledger_chain_intact`: 17 entries chain to head b2674a4221fd4a825c7e7ad3205a4958ef9d9d92ea13d5dc3f2b7063697acaa8
- `pass_requires_complete_required_inputs`: every input behind a PASS is complete
- `pass_requires_examined_rows`: rows_examined=4 (distinct data rows of declared inputs)
- `pass_requires_falsifier_witness`: 2 PASS result(s) each carry a ledger-backed falsifier witness
- `pass_requires_nonempty_evidence`: every PASS carries non-empty, hashed evidence
- `plan_closure`: 6 planned item(s) each ran exactly once
- `plan_matches_manifest`: the recorded PLAN equals the plan the manifest implies

## WHAT FAILED

Findings:

- none

Checks:

- none

## WHAT ABSTAINED

Findings:

- none

Checks:

- `reviewers`: reviewer_protocol ABSTAIN (PROTOCOL_BROKEN), subject records examined 3; required reviewer(s) ['syn-reviewer-c'] recorded no verdict; reviewer(s) ['syn-reviewer-b'] recorded more than one verdict

## WHAT REMAINS UNRESOLVED

- invariant `pass_requires_complete_required_checks` not applicable: the run does not claim PASS
- the receipt is UNSIGNED (receipt.auth.json says so): its content hash detects accidental change, but anyone able to edit the run directory can rewrite and rehash it

## WHAT THIS RESULT DOES NOT PROVE

- Scientific validity: NOT ESTABLISHED. Whether any conclusion holds in its intended domain is outside what this tool can show.
- Integrity (what was established): SHA-256 recorded for 1 of 1 declared input(s); execution ledger sealed at 17 entries; ledger head b2674a4221fd4a825c7e7ad3205a4958ef9d9d92ea13d5dc3f2b7063697acaa8; evidence manifest 99e85c41c843067731c701d27ea478577b2ef9ffc8cc2c06c33e97ade672c337.
- Performance (how the checkers and the declared checks behaved): CHECKER: falsifier witnesses 2 WITNESSED, 0 REFUTED, 0 UNWITNESSED, 0 NO_CASE, 0 NO_GENERATOR (2 falsifier invocation(s)); must-fail/must-pass canary held; comparator self-test held. RUN: Run status ABSTAIN (PROTOCOL_BROKEN) from 3 check result(s): 2 PASS, 0 FAIL, 1 ABSTAIN, 0 ERROR; 15 applicable invariant(s), 0 violated. This describes how the declared checks behaved on the declared inputs only.
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
