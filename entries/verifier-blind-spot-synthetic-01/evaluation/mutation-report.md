# Mutation report

## STATUS

**FAIL** (BLIND_SPOT), exit code 1.

8 of 9 executed mutations were detected by their expected detector; 1 escaped as blind spots.

Report `mut-50e087e15796d6b4` for manifest `manifest.json` (sha256 `7112354b66dcb1e3867fc318833888c34af3e5f446148e9cef97f4ef74381bb3`), generated 2026-09-26T00:00:00Z.

## BASELINE

The untouched copy verified as **PASS** (VERIFIED), run `run-fb54a3f2ab4c6bae`: expected_inputs 1, inputs_opened 1, rows_examined 4, checks_expected 3, checks_executed 3.

## SENSITIVITY

8/9 = 0.8889 (ROUND_HALF_EVEN to 4 places).

- applicable_mutations: 9
- executed_mutations: 9
- detected_mutations: 8
- escaped_mutations: 1
- skipped_mutations: 0
- not_applicable_mutations: 11

## DETECTED

- `M01_empty_input`: truncate required input 'readings' (fixtures/data/readings.csv) to zero bytes; its declared digest is re-declared so a digest mismatch cannot mask the detector under test
  - expected: the status is not PASS and input:EMPTY reports ABSTAIN
  - actual: ABSTAIN (INSUFFICIENT_EVIDENCE), fresh copy
  - fired: check:numeric_agreement (check:lumen) ABSTAIN INSUFFICIENT_EVIDENCE
  - fired: check:required_columns (check:columns) ABSTAIN INSUFFICIENT_EVIDENCE
  - fired: check:row_count (check:rows) ABSTAIN INSUFFICIENT_EVIDENCE
  - fired: contract:checks_executed (contract:checks_executed) ABSTAIN PARTIAL_EXECUTION [PARTIAL_EXECUTION]
  - fired: contract:rows_examined (contract:rows_examined) ABSTAIN INSUFFICIENT_EVIDENCE [VACUOUS_PASS]
  - fired: input:EMPTY (input:readings) ABSTAIN INSUFFICIENT_EVIDENCE [VACUOUS_PASS]
- `M02_missing_expected_file`: delete required input 'readings' (fixtures/data/readings.csv)
  - expected: the status is not PASS and input:MISSING reports ABSTAIN
  - actual: ABSTAIN (INSUFFICIENT_EVIDENCE), fresh copy
  - fired: check:numeric_agreement (check:lumen) ABSTAIN INSUFFICIENT_EVIDENCE [OMITTED_POPULATION]
  - fired: check:required_columns (check:columns) ABSTAIN INSUFFICIENT_EVIDENCE [OMITTED_POPULATION]
  - fired: check:row_count (check:rows) ABSTAIN INSUFFICIENT_EVIDENCE [OMITTED_POPULATION]
  - fired: contract:checks_executed (contract:checks_executed) ABSTAIN PARTIAL_EXECUTION [PARTIAL_EXECUTION]
  - fired: contract:inputs_opened (contract:inputs_opened) ABSTAIN INSUFFICIENT_EVIDENCE [VACUOUS_PASS]
  - fired: contract:rows_examined (contract:rows_examined) ABSTAIN INSUFFICIENT_EVIDENCE [VACUOUS_PASS]
  - fired: input:MISSING (input:readings) ABSTAIN INSUFFICIENT_EVIDENCE [OMITTED_POPULATION]
- `M07_changed_source_hash`: re-encode the final line ending of input 'readings' (fixtures/data/readings.csv) without re-declaring its digest; the parsed records are unchanged, so only the digest can catch it
  - expected: the status is not PASS and input:HASH_MISMATCH reports FAIL with SOURCE_MISMATCH
  - actual: FAIL (SOURCE_MISMATCH), fresh copy
  - fired: check:numeric_agreement (check:lumen) ABSTAIN SOURCE_MISMATCH [SOURCE_MISMATCH]
  - fired: check:required_columns (check:columns) ABSTAIN SOURCE_MISMATCH [SOURCE_MISMATCH]
  - fired: check:row_count (check:rows) ABSTAIN SOURCE_MISMATCH [SOURCE_MISMATCH]
  - fired: contract:checks_executed (contract:checks_executed) ABSTAIN PARTIAL_EXECUTION [PARTIAL_EXECUTION]
  - fired: contract:rows_examined (contract:rows_examined) ABSTAIN INSUFFICIENT_EVIDENCE [VACUOUS_PASS]
  - fired: input:HASH_MISMATCH (input:readings) FAIL SOURCE_MISMATCH [SOURCE_MISMATCH]
- `M10_changed_numeric_value`: change the stored 'lumen_level' at line 2 (key ['BM-01']) of input 'readings' from 12.50 to 22.50, a value that numeric_agreement check 'lumen' cites; its declared digest is re-declared so a digest mismatch cannot mask the detector under test
  - expected: the status is not PASS and check:numeric_agreement reports FAIL with SOURCE_MISMATCH
  - actual: FAIL (SOURCE_MISMATCH), fresh copy
  - fired: check:numeric_agreement (check:lumen) FAIL SOURCE_MISMATCH [SOURCE_MISMATCH]
- `M11_changed_numeric_formatting`: reprint the stored 'lumen_level' at line 2 (key ['BM-01']) of input 'readings' from '12.50' to '12,50' (decimal and grouping marks exchanged), a value that numeric_agreement check 'lumen' cites; its declared digest is re-declared so a digest mismatch cannot mask the detector under test
  - expected: the status is not PASS and check:numeric_agreement reports ABSTAIN or FAIL with REQUIRES_HUMAN_REVIEW or SOURCE_MISMATCH
  - actual: ABSTAIN (REQUIRES_HUMAN_REVIEW), fresh copy
  - fired: check:numeric_agreement (check:lumen) ABSTAIN REQUIRES_HUMAN_REVIEW
- `M15_skipped_required_checker`: replace the row_count checker behind required check 'rows' with one that returns SKIPPED without examining anything
  - expected: the status is not PASS and contract:checks_executed reports ABSTAIN with PARTIAL_EXECUTION
  - actual: ABSTAIN (INSUFFICIENT_EVIDENCE), fresh copy
  - fired: check:row_count (check:rows) ABSTAIN INSUFFICIENT_EVIDENCE
  - fired: contract:checks_executed (contract:checks_executed) ABSTAIN PARTIAL_EXECUTION [PARTIAL_EXECUTION]
- `M16_truncated_ledger`: drop the last sealed ledger entry (seq 6, the COMPLETED entry of check 'lumen') and keep the original seal (ledger_length 6)
  - expected: the status is not PASS and invariant:ledger_chain_intact reports FAIL
  - actual: FAIL (PROTOCOL_BROKEN), sealed-run replay
  - fired: contract:checks_executed (contract:checks_executed) ABSTAIN PARTIAL_EXECUTION [PARTIAL_EXECUTION]
  - fired: invariant:checked_claims_le_invocations (invariant:checked_claims_le_invocations) ABSTAIN UNVERIFIED [NARRATED_VERIFICATION]
  - fired: invariant:every_invocation_has_terminal_result (invariant:every_invocation_has_terminal_result) ABSTAIN PARTIAL_EXECUTION [PARTIAL_EXECUTION]
  - fired: invariant:every_required_check_has_terminal_state (invariant:every_required_check_has_terminal_state) ABSTAIN PARTIAL_EXECUTION [PARTIAL_EXECUTION]
  - fired: invariant:every_verdict_has_invocation (invariant:every_verdict_has_invocation) ABSTAIN UNVERIFIED [NARRATED_VERIFICATION]
  - fired: invariant:ledger_chain_intact (invariant:ledger_chain_intact) FAIL PROTOCOL_BROKEN [DEFECTIVE_VERIFICATION]
- `M17_reordered_hash_chain`: swap sealed ledger entries 2 and 3 (seq 2, the COMPLETED entry of check 'rows' and seq 3, the STARTED entry of check 'columns'), leaving each entry's own hash intact; the invocations still read as plausibly interleaved
  - expected: the status is not PASS and invariant:ledger_chain_intact reports FAIL
  - actual: FAIL (PROTOCOL_BROKEN), sealed-run replay
  - fired: invariant:ledger_chain_intact (invariant:ledger_chain_intact) FAIL PROTOCOL_BROKEN [DEFECTIVE_VERIFICATION]

## BLIND SPOTS

- `M04_duplicate_row`: duplicate the record at line 5 (key ['BM-04']) of input 'readings' (fixtures/data/readings.csv); its declared digest is re-declared so a digest mismatch cannot mask the detector under test
  - expected: the status is not PASS and check:duplicate_rows reports FAIL
  - actual: PASS (VERIFIED), fresh copy
  - BLIND_SPOT: the mutant verified as PASS; expected check:duplicate_rows reports FAIL

## SKIPPED

No applicable mutation was skipped.

## NOT APPLICABLE

- `M03_deleted_accepted_row`: A record accepted in the snapshot is deleted from its input.
  - expected: the status is not PASS and check:snapshot_completeness reports FAIL with OMITTED_POPULATION
  - NOT_APPLICABLE: the manifest declares no readable accepted_snapshot
- `M05_duplicate_reviewer_verdict`: A required reviewer's verdict is recorded twice.
  - expected: the status is not PASS and check:reviewer_protocol reports ABSTAIN with PROTOCOL_BROKEN
  - NOT_APPLICABLE: the manifest declares no readable reviewer verdicts
- `M06_missing_required_reviewer`: Every verdict of a required reviewer is removed.
  - expected: the status is not PASS and check:reviewer_protocol reports ABSTAIN with PROTOCOL_BROKEN
  - NOT_APPLICABLE: the manifest declares no readable reviewer verdicts
- `M08_changed_author`: The first author of a citation entry is replaced.
  - expected: the status is not PASS and check:citation_metadata reports FAIL with SOURCE_MISMATCH
  - NOT_APPLICABLE: the manifest declares no readable citation entries
- `M09_changed_doi`: A citation entry's DOI is changed to one that no frozen record holds.
  - expected: the status is not PASS and check:citation_resolver reports ABSTAIN with SOURCE_UNAVAILABLE
  - NOT_APPLICABLE: the manifest declares no readable citation entries
- `M12_timezone_shift`: An observation's declared timezone shifts by one hour.
  - expected: the status is not PASS and check:time_source reports FAIL with SOURCE_MISMATCH
  - NOT_APPLICABLE: the manifest declares no readable time sources
- `M13_removed_invocation`: An invocation record behind a claimed citation verification is removed.
  - expected: the status is not PASS and check:verification_log reports ABSTAIN or FAIL with NARRATED_VERIFICATION or UNVERIFIED
  - NOT_APPLICABLE: the manifest declares no citation verification log with invocation records
- `M14_pass_summary_without_evidence`: A stored PASS summary loses every pinned digest.
  - expected: the status is not PASS and check:summary_consistency reports ABSTAIN with NARRATED_VERIFICATION or VACUOUS_PASS
  - NOT_APPLICABLE: the manifest declares no stored PASS summary that pins evidence
- `M18_changed_upstream_design`: An upstream DESIGN artifact changes beneath its recorded digest.
  - expected: the status is not PASS and check:dependency_currency reports FAIL with STALE_DEPENDENCY
  - NOT_APPLICABLE: the manifest declares no readable dependency graph
- `M19_replaced_stored_claim_output`: A registered claim's stored output is replaced.
  - expected: the status is not PASS and check:claim_registry reports ABSTAIN or FAIL with SOURCE_MISMATCH
  - NOT_APPLICABLE: the manifest declares no readable claim registry
- `M20_metadata_change_under_unchanged_pass_summary`: Evidence metadata changes while the stored PASS summary stays the same.
  - expected: the status is not PASS and check:summary_consistency reports FAIL with SOURCE_MISMATCH
  - NOT_APPLICABLE: the manifest declares no stored PASS summary to hold unchanged

## WHAT THIS RESULT DOES NOT PROVE

- Mutation testing measures how this verifier reacted to the injected defects on this one evidence tree. Defects of other kinds, or the same defects in other trees, may still go undetected.
- A detected mutation shows that a detector fired, not that the evidence it guards is scientifically valid. Scientific validity is not established by this tool.
- Every verify ran offline with a network opener that refuses all requests; live citation lookups were not exercised.
