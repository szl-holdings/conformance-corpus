## STATUS

**FAIL** (SOURCE_MISMATCH), exit code 1.

- Run: `run-350cb2fc2f3085dd`
- Started 2026-09-26T00:00:00Z; completed 2026-09-26T00:00:00Z
- Reasons: SOURCE_MISMATCH
- Failure modes: SOURCE_MISMATCH
- Evidence manifest sha256: `d2090cfeb13bad06905413703091ade6b1969178ef81b445aed160a8f25ec922`
- Ledger: 8 entries, head `26ad8a89e39dfff986ae98780f7d5903b7a7339eea71023d95ea926b748c8864`
- Receipt: content sha256 `a45146a3b5ee72f5ff2c39f998d30189dd30863acfb2475332d79082648c208d`, UNSIGNED
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

PASS requires: every required input found, opened, parsed and matching any declared digest; at least one input opened; at least one row examined; checks_executed == checks_expected; every required check PASS; every applicable invariant holding; a non-empty evidence manifest.

## WHAT WAS EXAMINED

- Input funnel: expected 1 -> discovered 1 -> opened 1 -> parsed 1 -> examined 1; input closure holds (1 of 1, INDEPENDENT)
- Rows examined in scope: 12

Inputs:

- `observations` PARSED: `fixtures/observations.csv`, sha256 `050eacc36df51309da52b1e5a88faaf3462269f4f9323105541630dd3ae6e233`, 124 bytes, 3 records (admitted 3, excluded 0, deferred 0, unresolved 0, failed 0); row closure holds (3 of 3, INDEPENDENT)

Other documents read:

- `fixtures/citations/entries.json` (citations.entries): PARSED, sha256 `81aede2d70a1c35629a44f6452bf1abde3b29c15023a2d3b7e5086e11b3ddc66`
- `fixtures/citations/frozen.json` (citations.frozen): PARSED, sha256 `0d6b0b030c13ed56a599a6702baead038ca120d3468b627884ccbe9c980af7d5`
- `fixtures/citations/verification-log.json` (citations.log): PARSED, sha256 `9d6905051fe6969dbdf341e8e433f162cf4178f27cfae6c3ae33d632618fde7e`

## WHAT ACTUALLY RAN

- checks_executed 4 of checks_expected 4 (required checks that reached CHECKED with a terminal invocation)
- Ledger sealed at 8 entries, head `26ad8a89e39dfff986ae98780f7d5903b7a7339eea71023d95ea926b748c8864`

Invocations:

- `citation-log` (verification_log v1): invocation `inv-27b6ce963f81`, CHECKED, PASS, rows examined 3
- `citation-metadata` (citation_metadata v1): invocation `inv-751784105fd2`, CHECKED, FAIL, rows examined 3
- `doi-resolution` (citation_resolver v1): invocation `inv-634be97e511f`, CHECKED, FAIL, rows examined 3
- `observations` (row_count v1): invocation `inv-0ab4de6becc9`, CHECKED, PASS, rows examined 3

## WHAT PASSED

Checks:

- `citation-log`: verification_log PASS (VERIFIED), rows examined 3
- `observations`: row_count PASS (VERIFIED), rows examined 3

Invariants that hold:

- `checked_claims_le_invocations`: check results marked CHECKED: 4 claimed <= 4 invoked; citation-log: claimed_verified vs complete invocation records: 3 claimed <= 3 invoked; citation-log: entries claimed VERIFIED vs entries with a record: 3 claimed <= 3 invoked
- `every_invocation_has_terminal_result`: 4 invocation(s) each reached exactly one terminal result
- `every_required_check_has_terminal_state`: 4 required check(s) each reached a terminal state
- `every_verdict_has_invocation`: 4 verdict(s) each trace to a terminal invocation
- `input_accounting_closure`: 2 INDEPENDENT closure(s) hold
- `ledger_chain_intact`: 8 entries chain to head 26ad8a89e39dfff986ae98780f7d5903b7a7339eea71023d95ea926b748c8864
- `pass_requires_complete_required_inputs`: every input behind a PASS is complete
- `pass_requires_examined_rows`: rows_examined=12
- `pass_requires_nonempty_evidence`: every PASS carries non-empty, hashed evidence

## WHAT FAILED

Findings:

- none

Checks:

- `citation-metadata`: citation_metadata FAIL (SOURCE_MISMATCH), rows examined 3; FIELD_MISMATCH: citation C2 (10.5555/cc-synth.cmm.0002): AUTHOR_MISMATCH; FIELD_MISMATCH: citation C3 (10.5555/cc-synth.cmm.0003): DOI_WORK_MISMATCH
- `doi-resolution`: citation_resolver FAIL (SOURCE_MISMATCH), rows examined 3; DOI_TARGET_MISMATCH: 10.5555/cc-synth.cmm.0003 (cited as C3) reached the work 10.5555/cc-synth.cmm.0030

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
- Integrity (what was established): SHA-256 recorded for 1 of 1 declared input(s); execution ledger sealed at 8 entries; ledger head 26ad8a89e39dfff986ae98780f7d5903b7a7339eea71023d95ea926b748c8864; evidence manifest d2090cfeb13bad06905413703091ade6b1969178ef81b445aed160a8f25ec922.
- Performance (how the declared checks behaved): Run status FAIL (SOURCE_MISMATCH) from 4 check result(s): 2 PASS, 2 FAIL, 0 ABSTAIN, 0 ERROR; 9 applicable invariant(s), 0 violated. This describes how the declared checks behaved on the declared inputs only.
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
