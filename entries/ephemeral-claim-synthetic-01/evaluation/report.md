## STATUS

**ABSTAIN** (UNVERIFIED), exit code 2.

- Run: `run-d9b47d958c208f5f`
- Started 2026-09-26T00:00:00Z; completed 2026-09-26T00:00:00Z
- Reasons: UNVERIFIED
- Failure modes: EPHEMERAL_CLAIM
- Verdict rises: NONE -> PASS at step 1 (`check:rows`, VERIFIED); PASS -> ABSTAIN at step 2 (`check:claims`, UNVERIFIED)
- Evidence manifest sha256: `538f7aa3e338f34dc65944395898d6166ab5cf22ab2ba3438b7fc359a285d85d`
- Ledger: 13 entries, head `fa6543329b9fa2bdcd01af3405a76aa8b291a545d026b7b4cb1d3f755a5609d3`
- Receipt: content sha256 `c4b86b9b0f1f6f3ecedf6636768d9676c254605a6f92716dd30776f81c5a2bb7`, UNSIGNED
- Scope: integrity and the declared evaluation only. Scientific validity is not established by this tool.

## WHAT WAS EXPECTED

- Manifest `manifest.json`, sha256 `c8dd3460d35bf4a0dfe7560ca6f72c5281cc367f03c8c9f4bca3d9a8445ee730`, run label `corpus-ephemeral-claim-synthetic-01`

Inputs declared: 1 (expected_inputs 1)

- `tallies`: `fixtures/data/tallies.csv`, csv, required, expected_rows 5 (INDEPENDENT), declared sha256 `6a717a23dd44026f8220481a66c60fc665609792a532a273f153672b270dc573`

Checks declared: 2, of which 2 required (checks_expected 2)

- `rows`: row_count v1, required, inputs tallies
- `claims`: claim_registry v1, required, inputs 

PASS requires: every required input found, opened, parsed and matching any declared digest; at least one input opened; at least one data row examined; checks_executed == checks_expected; every required check PASS with a falsifier witness showing it could have failed; every applicable invariant holding; a non-empty evidence manifest.

## WHAT WAS EXAMINED

- Input funnel: expected 1 -> discovered 1 -> opened 1 -> parsed 1 -> examined 1; input closure holds (1 of 1, INDEPENDENT)
- rows_examined: 5 (distinct data rows of declared inputs read by an executed check)
- Each check line under WHAT PASSED, WHAT FAILED and WHAT ABSTAINED gives that check's own subject records examined (its run.json checks[].rows_examined); those figures are not summed.

Inputs:

- `tallies` PARSED: `fixtures/data/tallies.csv`, sha256 `6a717a23dd44026f8220481a66c60fc665609792a532a273f153672b270dc573`, 174 bytes, 5 records (admitted 5, excluded 0, deferred 0, unresolved 0, failed 0); row closure holds (5 of 5, INDEPENDENT)

Other documents read:

- `fixtures/claims/manuscript.md` (manuscript): PARSED, sha256 `b1296ea071057b243b174d9bb5bedfb7a4b326af5f2f0448ad5e1769688f7c96`
- `fixtures/claims/registry.json` (claims): PARSED, sha256 `6ae9dd3332836b210975ec88c833e433294562a8bc833d9107a29b5789ad454a`
- `fixtures/outputs/plot-summary.json` (claims.stored_output): PARSED, sha256 `38453298d808ea671fe0e1a9cf7a237494ee9d0b5101efc21e29214972889855`

## WHAT ACTUALLY RAN

- checks_executed 2 of checks_expected 2 (required checks that reached CHECKED with a terminal invocation)
- Ledger sealed at 13 entries, head `fa6543329b9fa2bdcd01af3405a76aa8b291a545d026b7b4cb1d3f755a5609d3`
- PLAN: ledger entry 1, entry sha256 `e54a5b3a72f492bd1db9ab227dc99b3a032b1fb16e105d2b0e6134a73e41b6b1`, written before any check ran: 1 input(s), 2 check(s) and 7 pin(s) planned, manifest sha256 `c8dd3460d35bf4a0dfe7560ca6f72c5281cc367f03c8c9f4bca3d9a8445ee730`

Invocations:

- `claims` (claim_registry v1): invocation `inv-96f090ae21d4`, CHECKED, ABSTAIN; no falsifier ran (only a would-be PASS is falsified)
- `rows` (row_count v1): invocation `inv-549832a73665`, CHECKED, PASS; falsifier witness WITNESSED (1 of 1 case(s) rejected as expected)

Controls (each its own invocation, never counted as a check):

- comparator self-test: invocation `inv-e022021a3c1b`, 3 of 3 known pair(s) compared as expected; holds
- canary: must_fail invocation `inv-21e5e65347cb` gave FAIL (SOURCE_MISMATCH), expected FAIL; must_pass invocation `inv-e6c13867e65f` gave PASS (VERIFIED), expected PASS; holds
- harness pins: 7 file(s) pinned; changed: none; writes to pinned paths: none; holds
- falsifier witnesses: WITNESSED 1 (`rows`), REFUTED 0, UNWITNESSED 0, NO_CASE 0, NO_GENERATOR 0; 1 falsifier invocation(s)
- claim-to-invocation join: no claim_join check ran

## WHAT PASSED

Checks:

- `rows`: row_count PASS (VERIFIED), subject records examined 5

Weakest discrimination: no PASS result records a discrimination ratio

Invariants that hold:

- `canary_controls_hold`: the must-fail canary failed and its known-good twin passed
- `checked_claims_le_invocations`: check results marked CHECKED: 2 claimed <= 6 invoked
- `comparator_self_test`: 3 known pairs compared as expected
- `every_invocation_has_terminal_result`: 6 invocation(s) each reached exactly one terminal result
- `every_required_check_has_terminal_state`: 2 required check(s) each reached a terminal state
- `every_verdict_has_invocation`: 2 verdict(s) each trace to a terminal invocation
- `harness_pins_intact`: 7 pinned file(s) unchanged and never written during the run
- `input_accounting_closure`: 2 INDEPENDENT closure(s) hold
- `ledger_chain_intact`: 13 entries chain to head fa6543329b9fa2bdcd01af3405a76aa8b291a545d026b7b4cb1d3f755a5609d3
- `pass_requires_complete_required_inputs`: every input behind a PASS is complete
- `pass_requires_examined_rows`: rows_examined=5 (distinct data rows of declared inputs)
- `pass_requires_falsifier_witness`: 1 PASS result(s) each carry a ledger-backed falsifier witness
- `pass_requires_nonempty_evidence`: every PASS carries non-empty, hashed evidence
- `plan_closure`: 5 planned item(s) each ran exactly once
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

- `claims`: claim_registry ABSTAIN (UNVERIFIED), subject records examined 4; claim 'CLM-02' EPHEMERAL_CLAIM: no reproducible derivation: missing link(s) ANALYSIS_RECIPE, CODE_VERSION, ENVIRONMENT, INPUT_MANIFEST, STORED_OUTPUT

## WHAT REMAINS UNRESOLVED

- invariant `pass_requires_complete_required_checks` not applicable: the run does not claim PASS
- the receipt is UNSIGNED (receipt.auth.json says so): its content hash detects accidental change, but anyone able to edit the run directory can rewrite and rehash it

## WHAT THIS RESULT DOES NOT PROVE

- Scientific validity: NOT ESTABLISHED. Whether any conclusion holds in its intended domain is outside what this tool can show.
- Integrity (what was established): SHA-256 recorded for 1 of 1 declared input(s); execution ledger sealed at 13 entries; ledger head fa6543329b9fa2bdcd01af3405a76aa8b291a545d026b7b4cb1d3f755a5609d3; evidence manifest 538f7aa3e338f34dc65944395898d6166ab5cf22ab2ba3438b7fc359a285d85d.
- Performance (how the checkers and the declared checks behaved): CHECKER: falsifier witnesses 1 WITNESSED, 0 REFUTED, 0 UNWITNESSED, 0 NO_CASE, 0 NO_GENERATOR (1 falsifier invocation(s)); must-fail/must-pass canary held; comparator self-test held. RUN: Run status ABSTAIN (UNVERIFIED) from 2 check result(s): 1 PASS, 0 FAIL, 1 ABSTAIN, 0 ERROR; 15 applicable invariant(s), 0 violated. This describes how the declared checks behaved on the declared inputs only.
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
