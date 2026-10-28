## STATUS

**ABSTAIN** (INSUFFICIENT_EVIDENCE), exit code 2.

- Run: `run-36a763016ef9da5c`
- Started 2026-09-26T00:00:00Z; completed 2026-09-26T00:00:00Z
- Reasons: INSUFFICIENT_EVIDENCE, UNVERIFIED
- Failure modes: VACUOUS_PASS
- Verdict rises: NONE -> ABSTAIN at step 1 (`input:readings`, INSUFFICIENT_EVIDENCE)
- Evidence manifest sha256: `4bb86362d505fc4b25cf0cac7909b9c87d2311cbacd74a8e5ad6cfd8352a17d9`
- Ledger: 15 entries, head `413063f432c56a8c7e3afef6e29e23aaf54a399a2f9b98cf7d9f3f6ee94653fa`
- Receipt: content sha256 `d33f9b009598d7034d05e0a115aafb2d88dc85f3700bd90015643ebffea81492`, UNSIGNED
- Scope: integrity and the declared evaluation only. Scientific validity is not established by this tool.

## WHAT WAS EXPECTED

- Manifest `manifest.json`, sha256 `5a1965efb458051fd3cff2feaa36bbea50d53efbaa65ab1fb68e5c527711257f`, run label `corpus-vacuous-pass-synthetic-01`

Inputs declared: 1 (expected_inputs 1)

- `readings`: `fixtures/data/readings.csv`, csv, required, expected_rows unknown (UNAVAILABLE), declared sha256 `16ce60c2b70a83f14ef500ed7f147750eebefa86a75befc06ed62e8cc10e9eaa`

Checks declared: 4, of which 4 required (checks_expected 4)

- `rows`: row_count v1, required, inputs readings
- `columns`: required_columns v1, required, inputs readings
- `duplicates`: duplicate_rows v1, required, inputs readings
- `stored-pass`: summary_consistency v1, required, inputs 

PASS requires: every required input found, opened, parsed and matching any declared digest; at least one input opened; at least one data row examined; checks_executed == checks_expected; every required check PASS with a falsifier witness showing it could have failed; every applicable invariant holding; a non-empty evidence manifest.

## WHAT WAS EXAMINED

- Input funnel: expected 1 -> discovered 1 -> opened 1 -> parsed 1 -> examined 0; input closure holds (1 of 1, INDEPENDENT)
- rows_examined: 0 (distinct data rows of declared inputs read by an executed check)
- Each check line under WHAT PASSED, WHAT FAILED and WHAT ABSTAINED gives that check's own subject records examined (its run.json checks[].rows_examined); those figures are not summed.

Inputs:

- `readings` EMPTY: `fixtures/data/readings.csv`, sha256 `16ce60c2b70a83f14ef500ed7f147750eebefa86a75befc06ed62e8cc10e9eaa`, 31 bytes, 0 records (admitted 0, excluded 0, deferred 0, unresolved 0, failed 0); row closure not evaluable (UNAVAILABLE expectation)

Other documents read:

- `fixtures/summary/stored-summary.json` (summary_claim): PARSED, sha256 `f662d10b436d4ac467d7c6ebc54d0858ebcb41b107853823e81dcf0057f1e75d`

## WHAT ACTUALLY RAN

- checks_executed 1 of checks_expected 4 (required checks that reached CHECKED with a terminal invocation)
- Ledger sealed at 15 entries, head `413063f432c56a8c7e3afef6e29e23aaf54a399a2f9b98cf7d9f3f6ee94653fa`
- PLAN: ledger entry 1, entry sha256 `2c9da193019b2124aa39e319949eff2835b28761d0700e27f403d08d08dc9f7f`, written before any check ran: 1 input(s), 4 check(s) and 4 pin(s) planned, manifest sha256 `5a1965efb458051fd3cff2feaa36bbea50d53efbaa65ab1fb68e5c527711257f`

Invocations:

- `columns` (required_columns v1): invocation `inv-5700bc53a57d`, NOT_APPLICABLE, ABSTAIN; no falsifier ran (only a would-be PASS is falsified)
- `duplicates` (duplicate_rows v1): invocation `inv-c35101494307`, NOT_APPLICABLE, ABSTAIN; no falsifier ran (only a would-be PASS is falsified)
- `rows` (row_count v1): invocation `inv-edb083639ed8`, NOT_APPLICABLE, ABSTAIN; no falsifier ran (only a would-be PASS is falsified)
- `stored-pass` (summary_consistency v1): invocation `inv-ef2ba6d0ffda`, CHECKED, ABSTAIN; no falsifier ran (only a would-be PASS is falsified)

Controls (each its own invocation, never counted as a check):

- comparator self-test: invocation `inv-f4d9ce5ef664`, 3 of 3 known pair(s) compared as expected; holds
- canary: must_fail invocation `inv-218036d750f0` gave FAIL (SOURCE_MISMATCH), expected FAIL; must_pass invocation `inv-7432b9811761` gave PASS (VERIFIED), expected PASS; holds
- harness pins: 4 file(s) pinned; changed: none; writes to pinned paths: none; holds
- falsifier witnesses: WITNESSED 0, REFUTED 0, UNWITNESSED 0, NO_CASE 0, NO_GENERATOR 0; 0 falsifier invocation(s)
- claim-to-invocation join: no claim_join check ran

## WHAT PASSED

Checks:

- none

Weakest discrimination: no PASS result records a discrimination ratio

Invariants that hold:

- `canary_controls_hold`: the must-fail canary failed and its known-good twin passed
- `checked_claims_le_invocations`: check results marked CHECKED: 1 claimed <= 7 invoked
- `comparator_self_test`: 3 known pairs compared as expected
- `every_invocation_has_terminal_result`: 7 invocation(s) each reached exactly one terminal result
- `every_required_check_has_terminal_state`: 4 required check(s) each reached a terminal state
- `every_verdict_has_invocation`: 4 verdict(s) each trace to a terminal invocation
- `harness_pins_intact`: 4 pinned file(s) unchanged and never written during the run
- `input_accounting_closure`: 1 INDEPENDENT closure(s) hold
- `ledger_chain_intact`: 15 entries chain to head 413063f432c56a8c7e3afef6e29e23aaf54a399a2f9b98cf7d9f3f6ee94653fa
- `plan_closure`: 7 planned item(s) each ran exactly once
- `plan_matches_manifest`: the recorded PLAN equals the plan the manifest implies

## WHAT FAILED

Findings:

- none

Checks:

- none

## WHAT ABSTAINED

Findings:

- [input:readings] ABSTAIN INSUFFICIENT_EVIDENCE (VACUOUS_PASS): required input is EMPTY: EMPTY: the input contains no data records
- [contract:rows_examined] ABSTAIN INSUFFICIENT_EVIDENCE (VACUOUS_PASS): rows_examined=0 (distinct data rows of declared inputs); a PASS needs at least 1
- [contract:checks_executed] ABSTAIN INSUFFICIENT_EVIDENCE (VACUOUS_PASS): required check 'columns' did not execute: it was NOT_APPLICABLE, justified as EMPTY_POPULATION (checks_executed=1 of checks_expected=4)
- [contract:checks_executed] ABSTAIN INSUFFICIENT_EVIDENCE (VACUOUS_PASS): required check 'duplicates' did not execute: it was NOT_APPLICABLE, justified as EMPTY_POPULATION (checks_executed=1 of checks_expected=4)
- [contract:checks_executed] ABSTAIN INSUFFICIENT_EVIDENCE (VACUOUS_PASS): required check 'rows' did not execute: it was NOT_APPLICABLE, justified as EMPTY_POPULATION (checks_executed=1 of checks_expected=4)

Checks:

- `columns`: required_columns ABSTAIN (INSUFFICIENT_EVIDENCE), subject records examined 0; input 'readings' is EMPTY: not examined; no input has rows to examine
- `duplicates`: duplicate_rows ABSTAIN (INSUFFICIENT_EVIDENCE), subject records examined 0; input 'readings' is EMPTY: not examined; no input has rows to examine
- `rows`: row_count ABSTAIN (INSUFFICIENT_EVIDENCE), subject records examined 0; input 'readings' is EMPTY: not examined; no input has rows to examine
- `stored-pass`: summary_consistency ABSTAIN (UNVERIFIED), subject records examined 1; the summary pins input 'readings' with 0 rows

## WHAT REMAINS UNRESOLVED

- required input `readings` is EMPTY: EMPTY: the input contains no data records
- row closure of input `readings` not evaluated (UNAVAILABLE)
- check `columns` was NOT_APPLICABLE
- check `duplicates` was NOT_APPLICABLE
- check `rows` was NOT_APPLICABLE
- invariant `pass_requires_complete_required_checks` not applicable: the run does not claim PASS
- invariant `pass_requires_complete_required_inputs` not applicable: no check result and no run-level status claims PASS
- invariant `pass_requires_examined_rows` not applicable: no check result and no run-level status claims PASS
- invariant `pass_requires_falsifier_witness` not applicable: no check result is PASS
- invariant `pass_requires_nonempty_evidence` not applicable: no check result and no run-level status claims PASS
- the receipt is UNSIGNED (receipt.auth.json says so): its content hash detects accidental change, but anyone able to edit the run directory can rewrite and rehash it

## WHAT THIS RESULT DOES NOT PROVE

- Scientific validity: NOT ESTABLISHED. Whether any conclusion holds in its intended domain is outside what this tool can show.
- Integrity (what was established): SHA-256 recorded for 1 of 1 declared input(s); execution ledger sealed at 15 entries; ledger head 413063f432c56a8c7e3afef6e29e23aaf54a399a2f9b98cf7d9f3f6ee94653fa; evidence manifest 4bb86362d505fc4b25cf0cac7909b9c87d2311cbacd74a8e5ad6cfd8352a17d9.
- Performance (how the checkers and the declared checks behaved): CHECKER: falsifier witnesses 0 WITNESSED, 0 REFUTED, 0 UNWITNESSED, 0 NO_CASE, 0 NO_GENERATOR (0 falsifier invocation(s)); must-fail/must-pass canary held; comparator self-test held. RUN: Run status ABSTAIN (INSUFFICIENT_EVIDENCE) from 4 check result(s): 0 PASS, 0 FAIL, 4 ABSTAIN, 0 ERROR; 11 applicable invariant(s), 0 violated. This describes how the declared checks behaved on the declared inputs only.
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
