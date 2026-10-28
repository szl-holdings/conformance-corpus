## STATUS

**ABSTAIN** (UNVERIFIED), exit code 2.

- Run: `run-e32f6fa09ea74fc0`
- Started 2026-09-26T00:00:00Z; completed 2026-09-26T00:00:00Z
- Reasons: UNVERIFIED
- Failure modes: EPHEMERAL_CLAIM
- Evidence manifest sha256: `2b07d38601b9d08c0abb204b07b4c54be84af7b665062dda96c77304350ce38a`
- Ledger: 4 entries, head `cf50c27bbdc5586abbe3b4fe737a3a17407be53dd437cbb20eda6d686f4b95d7`
- Receipt: content sha256 `318fdffc271514f01cd8ae83f26537457d32a7f489dfde17cb7b46cb915acc96`, UNSIGNED
- Scope: integrity and the declared evaluation only. Scientific validity is not established by this tool.

## WHAT WAS EXPECTED

- Manifest `manifest.json`, sha256 `6ced9c8b6dba7509566ee1eaacde95dda55279946208cf26e9c302a03a69cc03`, run label `corpus-ephemeral-claim-synthetic-01`

Inputs declared: 1 (expected_inputs 1)

- `tallies`: `fixtures/data/tallies.csv`, csv, required, expected_rows 5 (INDEPENDENT), declared sha256 `6a717a23dd44026f8220481a66c60fc665609792a532a273f153672b270dc573`

Checks declared: 2, of which 2 required (checks_expected 2)

- `rows`: row_count v1, required, inputs tallies
- `claims`: claim_registry v1, required, inputs 

PASS requires: every required input found, opened, parsed and matching any declared digest; at least one input opened; at least one row examined; checks_executed == checks_expected; every required check PASS; every applicable invariant holding; a non-empty evidence manifest.

## WHAT WAS EXAMINED

- Input funnel: expected 1 -> discovered 1 -> opened 1 -> parsed 1 -> examined 1; input closure holds (1 of 1, INDEPENDENT)
- Rows examined in scope: 9

Inputs:

- `tallies` PARSED: `fixtures/data/tallies.csv`, sha256 `6a717a23dd44026f8220481a66c60fc665609792a532a273f153672b270dc573`, 174 bytes, 5 records (admitted 5, excluded 0, deferred 0, unresolved 0, failed 0); row closure holds (5 of 5, INDEPENDENT)

Other documents read:

- `fixtures/claims/manuscript.md` (manuscript): PARSED, sha256 `b1296ea071057b243b174d9bb5bedfb7a4b326af5f2f0448ad5e1769688f7c96`
- `fixtures/claims/registry.json` (claims): PARSED, sha256 `6ae9dd3332836b210975ec88c833e433294562a8bc833d9107a29b5789ad454a`
- `fixtures/outputs/plot-summary.json` (claims.stored_output): PARSED, sha256 `38453298d808ea671fe0e1a9cf7a237494ee9d0b5101efc21e29214972889855`

## WHAT ACTUALLY RAN

- checks_executed 2 of checks_expected 2 (required checks that reached CHECKED with a terminal invocation)
- Ledger sealed at 4 entries, head `cf50c27bbdc5586abbe3b4fe737a3a17407be53dd437cbb20eda6d686f4b95d7`

Invocations:

- `claims` (claim_registry v1): invocation `inv-794cb9548c34`, CHECKED, ABSTAIN, rows examined 4
- `rows` (row_count v1): invocation `inv-749b693318fa`, CHECKED, PASS, rows examined 5

## WHAT PASSED

Checks:

- `rows`: row_count PASS (VERIFIED), rows examined 5

Invariants that hold:

- `checked_claims_le_invocations`: check results marked CHECKED: 2 claimed <= 2 invoked
- `every_invocation_has_terminal_result`: 2 invocation(s) each reached exactly one terminal result
- `every_required_check_has_terminal_state`: 2 required check(s) each reached a terminal state
- `every_verdict_has_invocation`: 2 verdict(s) each trace to a terminal invocation
- `input_accounting_closure`: 2 INDEPENDENT closure(s) hold
- `ledger_chain_intact`: 4 entries chain to head cf50c27bbdc5586abbe3b4fe737a3a17407be53dd437cbb20eda6d686f4b95d7
- `pass_requires_complete_required_inputs`: every input behind a PASS is complete
- `pass_requires_examined_rows`: rows_examined=9
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

- `claims`: claim_registry ABSTAIN (UNVERIFIED), rows examined 4; claim 'CLM-02' EPHEMERAL_CLAIM: no reproducible derivation: missing link(s) ANALYSIS_RECIPE, CODE_VERSION, ENVIRONMENT, INPUT_MANIFEST, STORED_OUTPUT

## WHAT REMAINS UNRESOLVED

- invariant `pass_requires_complete_required_checks` not applicable: the run does not claim PASS
- the receipt is UNSIGNED: its content hash detects accidental change, but anyone able to edit the run directory can rewrite and rehash it

## WHAT THIS RESULT DOES NOT PROVE

- Scientific validity: NOT ESTABLISHED. Whether any conclusion holds in its intended domain is outside what this tool can show.
- Integrity (what was established): SHA-256 recorded for 1 of 1 declared input(s); execution ledger sealed at 4 entries; ledger head cf50c27bbdc5586abbe3b4fe737a3a17407be53dd437cbb20eda6d686f4b95d7; evidence manifest 2b07d38601b9d08c0abb204b07b4c54be84af7b665062dda96c77304350ce38a.
- Performance (how the declared checks behaved): Run status ABSTAIN (UNVERIFIED) from 2 check result(s): 1 PASS, 0 FAIL, 1 ABSTAIN, 0 ERROR; 9 applicable invariant(s), 0 violated. This describes how the declared checks behaved on the declared inputs only.
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
