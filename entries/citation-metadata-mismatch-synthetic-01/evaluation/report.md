## STATUS

**FAIL** (SOURCE_MISMATCH), exit code 1.

- Run: `run-14e19b81fbfed4fc`
- Started 2026-09-26T00:00:00Z; completed 2026-09-26T00:00:00Z
- Reasons: SOURCE_MISMATCH
- Failure modes: SOURCE_MISMATCH
- Verdict rises: NONE -> PASS at step 1 (`check:citation-log`, VERIFIED); PASS -> FAIL at step 3 (`check:citation-metadata`, SOURCE_MISMATCH)
- Evidence manifest sha256: `4744f7dd1fd3a0229d21ce9c9033bf3c1bdd0957ad6781d23b8f5a45a7fe5297`
- Ledger: 19 entries, head `624edec45fbc085e2dd5476bec9f874c9e203693c81f7a3321a789e415a79f05`
- Receipt: content sha256 `383502fc327348a30454a216b43b00c13541b90ff3e1ac0623f9a7674582053d`, UNSIGNED
- Scope: integrity and the declared evaluation only. Scientific validity is not established by this tool.

## WHAT WAS EXPECTED

- Manifest `manifest.json`, sha256 `9e1013e14cdaf982bb90a5ef70620148d07a1b683bfe997e8a3cab9b2bae9d33`, run label `corpus-citation-metadata-mismatch-synthetic-01`

Inputs declared: 1 (expected_inputs 1)

- `observations`: `fixtures/observations.csv`, csv, required, expected_rows 3 (INDEPENDENT), declared sha256 `050eacc36df51309da52b1e5a88faaf3462269f4f9323105541630dd3ae6e233`

Checks declared: 4, of which 4 required (checks_expected 4)

- `observations`: row_count v1, required, inputs observations
- `citation-log`: verification_log v1, required, inputs 
- `doi-resolution`: citation_resolver v1, required, inputs 
- `citation-metadata`: citation_metadata v1, required, inputs 

PASS requires: every required input found, opened, parsed and matching any declared digest; at least one input opened; at least one data row examined; checks_executed == checks_expected; every required check PASS with a falsifier witness showing it could have failed; every applicable invariant holding; a non-empty evidence manifest.

## WHAT WAS EXAMINED

- Input funnel: expected 1 -> discovered 1 -> opened 1 -> parsed 1 -> examined 1; input closure holds (1 of 1, INDEPENDENT)
- rows_examined: 3 (distinct data rows of declared inputs read by an executed check)
- Each check line under WHAT PASSED, WHAT FAILED and WHAT ABSTAINED gives that check's own subject records examined (its run.json checks[].rows_examined); those figures are not summed.

Inputs:

- `observations` PARSED: `fixtures/observations.csv`, sha256 `050eacc36df51309da52b1e5a88faaf3462269f4f9323105541630dd3ae6e233`, 124 bytes, 3 records (admitted 3, excluded 0, deferred 0, unresolved 0, failed 0); row closure holds (3 of 3, INDEPENDENT)

Other documents read:

- `fixtures/citations/entries.json` (citations.entries): PARSED, sha256 `81aede2d70a1c35629a44f6452bf1abde3b29c15023a2d3b7e5086e11b3ddc66`
- `fixtures/citations/frozen.json` (citations.frozen): PARSED, sha256 `e4b03e35dd02b8495e8c6cd69cccb726d856b11ae625285ea92f257d79effc98`
- `fixtures/citations/verification-log.json` (citations.log): PARSED, sha256 `9d6905051fe6969dbdf341e8e433f162cf4178f27cfae6c3ae33d632618fde7e`

## WHAT ACTUALLY RAN

- checks_executed 4 of checks_expected 4 (required checks that reached CHECKED with a terminal invocation)
- Ledger sealed at 19 entries, head `624edec45fbc085e2dd5476bec9f874c9e203693c81f7a3321a789e415a79f05`
- PLAN: ledger entry 1, entry sha256 `c19be5c70501225d7afa4e358372459bb40b46ad83b69e40a8e6b28d7cf7c6b8`, written before any check ran: 1 input(s), 4 check(s) and 7 pin(s) planned, manifest sha256 `9e1013e14cdaf982bb90a5ef70620148d07a1b683bfe997e8a3cab9b2bae9d33`

Invocations:

- `citation-log` (verification_log v1): invocation `inv-282bc7a7f45a`, CHECKED, PASS; falsifier witness WITNESSED (1 of 1 case(s) rejected as expected)
- `citation-metadata` (citation_metadata v1): invocation `inv-3c21e92a517f`, CHECKED, FAIL; no falsifier ran (only a would-be PASS is falsified)
- `doi-resolution` (citation_resolver v1): invocation `inv-07d9384249de`, CHECKED, FAIL; no falsifier ran (only a would-be PASS is falsified)
- `observations` (row_count v1): invocation `inv-0779cb57da0f`, CHECKED, PASS; falsifier witness WITNESSED (1 of 1 case(s) rejected as expected)

Controls (each its own invocation, never counted as a check):

- comparator self-test: invocation `inv-7974776933c4`, 3 of 3 known pair(s) compared as expected; holds
- canary: must_fail invocation `inv-07f62e85d39a` gave FAIL (SOURCE_MISMATCH), expected FAIL; must_pass invocation `inv-66822bc168e5` gave PASS (VERIFIED), expected PASS; holds
- harness pins: 7 file(s) pinned; changed: none; writes to pinned paths: none; holds
- falsifier witnesses: WITNESSED 2 (`citation-log`, `observations`), REFUTED 0, UNWITNESSED 0, NO_CASE 0, NO_GENERATOR 0; 2 falsifier invocation(s)
- claim-to-invocation join: no claim_join check ran

## WHAT PASSED

Checks:

- `citation-log`: verification_log PASS (VERIFIED), subject records examined 3
- `observations`: row_count PASS (VERIFIED), subject records examined 3

Weakest discrimination: no PASS result records a discrimination ratio

Invariants that hold:

- `canary_controls_hold`: the must-fail canary failed and its known-good twin passed
- `checked_claims_le_invocations`: check results marked CHECKED: 4 claimed <= 9 invoked; citation-log: claimed_verified vs complete invocation records: 3 claimed <= 3 invoked; citation-log: entries claimed VERIFIED vs entries with a record: 3 claimed <= 3 invoked
- `comparator_self_test`: 3 known pairs compared as expected
- `every_invocation_has_terminal_result`: 9 invocation(s) each reached exactly one terminal result
- `every_required_check_has_terminal_state`: 4 required check(s) each reached a terminal state
- `every_verdict_has_invocation`: 4 verdict(s) each trace to a terminal invocation
- `harness_pins_intact`: 7 pinned file(s) unchanged and never written during the run
- `input_accounting_closure`: 2 INDEPENDENT closure(s) hold
- `ledger_chain_intact`: 19 entries chain to head 624edec45fbc085e2dd5476bec9f874c9e203693c81f7a3321a789e415a79f05
- `pass_requires_complete_required_inputs`: every input behind a PASS is complete
- `pass_requires_examined_rows`: rows_examined=3 (distinct data rows of declared inputs)
- `pass_requires_falsifier_witness`: 2 PASS result(s) each carry a ledger-backed falsifier witness
- `pass_requires_nonempty_evidence`: every PASS carries non-empty, hashed evidence
- `plan_closure`: 7 planned item(s) each ran exactly once
- `plan_matches_manifest`: the recorded PLAN equals the plan the manifest implies

## WHAT FAILED

Findings:

- none

Checks:

- `citation-metadata`: citation_metadata FAIL (SOURCE_MISMATCH), subject records examined 3; FIELD_MISMATCH: citation C2 (10.5555/cc-synth.cmm.0002): AUTHOR_MISMATCH; FIELD_MISMATCH: citation C3 (10.5555/cc-synth.cmm.0003): DOI_WORK_MISMATCH
- `doi-resolution`: citation_resolver FAIL (SOURCE_MISMATCH), subject records examined 3; DOI_TARGET_MISMATCH: 10.5555/cc-synth.cmm.0003 (cited as C3) reached the work 10.5555/cc-synth.cmm.0030

## WHAT ABSTAINED

Findings:

- none

Checks:

- none

## WHAT REMAINS UNRESOLVED

- invariant `pass_requires_complete_required_checks` not applicable: the run does not claim PASS
- the receipt is UNSIGNED (receipt.auth.json says so): its content hash detects accidental change, but anyone able to edit the run directory can rewrite and rehash it

## WHAT THIS RESULT DOES NOT PROVE

- Scientific validity: NOT ESTABLISHED. Whether any conclusion holds in its intended domain is outside what this tool can show.
- Integrity (what was established): SHA-256 recorded for 1 of 1 declared input(s); execution ledger sealed at 19 entries; ledger head 624edec45fbc085e2dd5476bec9f874c9e203693c81f7a3321a789e415a79f05; evidence manifest 4744f7dd1fd3a0229d21ce9c9033bf3c1bdd0957ad6781d23b8f5a45a7fe5297.
- Performance (how the checkers and the declared checks behaved): CHECKER: falsifier witnesses 2 WITNESSED, 0 REFUTED, 0 UNWITNESSED, 0 NO_CASE, 0 NO_GENERATOR (2 falsifier invocation(s)); must-fail/must-pass canary held; comparator self-test held. RUN: Run status FAIL (SOURCE_MISMATCH) from 4 check result(s): 2 PASS, 2 FAIL, 0 ABSTAIN, 0 ERROR; 15 applicable invariant(s), 0 violated. This describes how the declared checks behaved on the declared inputs only.
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
