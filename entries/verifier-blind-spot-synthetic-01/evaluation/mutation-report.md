# Mutation report

## STATUS

**FAIL** (BLIND_SPOT), exit code 1.

9 of 10 executed mutations were detected by their expected detector; 1 escaped (1 blind spot(s), 0 verifier error(s)).

Report `mut-639e31adfdcd67f5` for manifest `manifest.json` (sha256 `1b0ef6b2b7ee8cb9bd0fd32a00eaf15e01d9e62c5fc92c79a7a64fe9ba925941`), generated 2026-09-26T00:00:00Z. Sampled: no. Reused: no.

## BASELINE

The untouched copy verified as **PASS** (VERIFIED), run `run-ab1808a64dc72890`: expected_inputs 1, inputs_opened 1, rows_examined 4, checks_expected 2, checks_executed 2.
- digest ledger_sha256: `b21170baac31f6b4cbb274606f7492eed11ed570093cd8f68d126a0b9271d03b`
- digest tree_canonical_sha256: `684f761e6f5b56e3062150de6497d93a3835717cb6a61bed3646f0f462475e02`
- digest tree_sha256: `b578e2eeb1f3080669228dd04ba9ee4c5ed01de63ece3342e6a13b2dccfc4086`

## FORCED DETECTION

`M00_forced_detection` detected by `invariant:ledger_chain_intact`: flip the first hex digit of the sealed ledger head (ebd9bb01d871... to 0bd9bb01d871...) and replay the sealed run against it.
- fired: invariant:ledger_chain_intact (invariant:ledger_chain_intact) FAIL PROTOCOL_BROKEN [DEFECTIVE_VERIFICATION]

## SENSITIVITY

9/10 = 0.9000 (ROUND_HALF_EVEN to 4 places).

- applicable_mutations: 10
- executed_mutations: 10
- detected_mutations: 9
- escaped_mutations: 1
- skipped_mutations: 0
- not_applicable_mutations: 11
- generated_mutations: 21
- blind_spot_mutations: 1
- verifier_error_mutations: 0
- timed_out_mutations: 0
- flaky_mutations: 0
- not_activated_mutations: 0
- noop_mutations: 0
- canonically_equivalent_mutations: 0
- duplicate_mutations: 0
- suppressed_mutations: 0

## CONSERVATION

- generated = executed + unexecuted buckets: holds
- executed = DETECTED + BLIND_SPOT + VERIFIER_ERROR + TIMED_OUT + FLAKY: holds
- buckets disjoint: yes
- detection table: only DETECTED counts as detected

## DETECTED

- `M01_empty_input` (DETECTED): truncate required input 'readings' (fixtures/data/readings.csv) to zero bytes; its declared digest is re-declared so a digest mismatch cannot mask the detector under test
  - expected: the status is not PASS and input:EMPTY reports ABSTAIN
  - actual: ABSTAIN (INSUFFICIENT_EVIDENCE), fresh copy
  - fired: check:numeric_agreement (check:lumen) ABSTAIN INSUFFICIENT_EVIDENCE
  - fired: check:required_columns (check:columns) ABSTAIN INSUFFICIENT_EVIDENCE
  - fired: contract:checks_executed (contract:checks_executed) ABSTAIN INSUFFICIENT_EVIDENCE [VACUOUS_PASS]
  - fired: contract:checks_executed (contract:checks_executed) ABSTAIN INSUFFICIENT_EVIDENCE [VACUOUS_PASS]
  - fired: contract:rows_examined (contract:rows_examined) ABSTAIN INSUFFICIENT_EVIDENCE [VACUOUS_PASS]
  - fired: input:EMPTY (input:readings) ABSTAIN INSUFFICIENT_EVIDENCE [VACUOUS_PASS]
  - activation: file mutant, activated; 2 file(s) read from the copy; mutated paths read 2/2; 0 value read(s)
- `M02_missing_expected_file` (DETECTED): delete required input 'readings' (fixtures/data/readings.csv)
  - expected: the status is not PASS and input:MISSING reports ABSTAIN
  - actual: ABSTAIN (INSUFFICIENT_EVIDENCE), fresh copy
  - fired: check:numeric_agreement (check:lumen) ABSTAIN INSUFFICIENT_EVIDENCE [OMITTED_POPULATION]
  - fired: check:required_columns (check:columns) ABSTAIN INSUFFICIENT_EVIDENCE [OMITTED_POPULATION]
  - fired: contract:checks_executed (contract:checks_executed) ABSTAIN INSUFFICIENT_EVIDENCE [OMITTED_POPULATION]
  - fired: contract:checks_executed (contract:checks_executed) ABSTAIN INSUFFICIENT_EVIDENCE [OMITTED_POPULATION]
  - fired: contract:inputs_opened (contract:inputs_opened) ABSTAIN INSUFFICIENT_EVIDENCE [VACUOUS_PASS]
  - fired: contract:rows_examined (contract:rows_examined) ABSTAIN INSUFFICIENT_EVIDENCE [VACUOUS_PASS]
  - fired: input:MISSING (input:readings) ABSTAIN INSUFFICIENT_EVIDENCE [OMITTED_POPULATION]
  - activation: file mutant, activated; 2 file(s) read from the copy; mutated paths read 1/1; 0 value read(s)
- `M07_changed_source_hash` (DETECTED): re-encode the final line ending of input 'readings' (fixtures/data/readings.csv) without re-declaring its digest; the parsed records are unchanged, so only the digest can catch it
  - expected: the status is not PASS and input:HASH_MISMATCH reports FAIL with SOURCE_MISMATCH
  - actual: FAIL (SOURCE_MISMATCH), fresh copy
  - fired: check:numeric_agreement (check:lumen) ABSTAIN SOURCE_MISMATCH [SOURCE_MISMATCH]
  - fired: check:required_columns (check:columns) ABSTAIN SOURCE_MISMATCH [SOURCE_MISMATCH]
  - fired: contract:checks_executed (contract:checks_executed) ABSTAIN SOURCE_MISMATCH [SOURCE_MISMATCH]
  - fired: contract:checks_executed (contract:checks_executed) ABSTAIN SOURCE_MISMATCH [SOURCE_MISMATCH]
  - fired: contract:rows_examined (contract:rows_examined) ABSTAIN INSUFFICIENT_EVIDENCE [VACUOUS_PASS]
  - fired: input:HASH_MISMATCH (input:readings) FAIL SOURCE_MISMATCH [SOURCE_MISMATCH]
  - activation: file mutant, activated; 2 file(s) read from the copy; mutated paths read 1/1; 0 value read(s)
- `M10_changed_numeric_value` (DETECTED): change the stored 'lumen_level' at line 2 (key ['BM-01']) of input 'readings' from 12.50 to 22.50, a value that numeric_agreement check 'lumen' cites; its declared digest is re-declared so a digest mismatch cannot mask the detector under test
  - expected: the status is not PASS and check:numeric_agreement reports FAIL with SOURCE_MISMATCH
  - actual: FAIL (SOURCE_MISMATCH), fresh copy
  - fired: check:numeric_agreement (check:lumen) FAIL SOURCE_MISMATCH [SOURCE_MISMATCH]
  - activation: file mutant, activated; 2 file(s) read from the copy; mutated paths read 2/2; 6 value read(s)
- `M11_changed_numeric_formatting` (DETECTED): reprint the stored 'lumen_level' at line 2 (key ['BM-01']) of input 'readings' from '12.50' to '12,50' (decimal and grouping marks exchanged), a value that numeric_agreement check 'lumen' cites; its declared digest is re-declared so a digest mismatch cannot mask the detector under test
  - expected: the status is not PASS and check:numeric_agreement reports ABSTAIN or FAIL with REQUIRES_HUMAN_REVIEW or SOURCE_MISMATCH
  - actual: ABSTAIN (REQUIRES_HUMAN_REVIEW), fresh copy
  - fired: check:numeric_agreement (check:lumen) ABSTAIN REQUIRES_HUMAN_REVIEW
  - activation: file mutant, activated; 2 file(s) read from the copy; mutated paths read 2/2; 6 value read(s)
- `M15_skipped_required_checker` (DETECTED): replace the required_columns checker behind required check 'columns' with one that returns SKIPPED without examining anything
  - expected: the status is not PASS and contract:checks_executed reports FAIL with PARTIAL_EXECUTION
  - actual: FAIL (PARTIAL_EXECUTION), fresh copy
  - fired: check:required_columns (check:columns) ABSTAIN INSUFFICIENT_EVIDENCE
  - fired: contract:checks_executed (contract:checks_executed) FAIL PARTIAL_EXECUTION [PARTIAL_EXECUTION]
  - activation: registry mutant, activated; 2 file(s) read from the copy; mutated paths read 0/0; 6 value read(s)
- `M16_truncated_ledger` (DETECTED): drop the last sealed ledger entry (seq 15, the COMPLETED entry of check 'control:canary:must_pass') and keep the original seal (ledger_length 15)
  - expected: the status is not PASS and invariant:ledger_chain_intact reports FAIL
  - actual: FAIL (PROTOCOL_BROKEN), sealed-run replay
  - fired: invariant:canary_controls_hold (invariant:canary_controls_hold) FAIL BLIND_SPOT [DEFECTIVE_VERIFICATION]
  - fired: invariant:every_invocation_has_terminal_result (invariant:every_invocation_has_terminal_result) ABSTAIN PARTIAL_EXECUTION [PARTIAL_EXECUTION]
  - fired: invariant:ledger_chain_intact (invariant:ledger_chain_intact) FAIL PROTOCOL_BROKEN [DEFECTIVE_VERIFICATION]
  - fired: invariant:plan_closure (invariant:plan_closure) FAIL PARTIAL_EXECUTION [PARTIAL_EXECUTION]
  - activation: replay of the sealed run (activated)
- `M17_reordered_hash_chain` (DETECTED): swap sealed ledger entries 2 and 3 (seq 2, the STARTED entry of check 'columns' and seq 3, the STARTED entry of check 'control:falsifier:columns:drop-column'), leaving each entry's own hash intact; the invocations still read as plausibly interleaved
  - expected: the status is not PASS and invariant:ledger_chain_intact reports FAIL
  - actual: FAIL (PROTOCOL_BROKEN), sealed-run replay
  - fired: invariant:ledger_chain_intact (invariant:ledger_chain_intact) FAIL PROTOCOL_BROKEN [DEFECTIVE_VERIFICATION]
  - activation: replay of the sealed run (activated)
- `M21_removed_plan` (DETECTED): remove the PLAN entry and reseal the remaining 14 entries as one consistent chain (new seq, invocation ids, links and head), as a thorough forger would; the results follow their renamed invocations
  - expected: the status is not PASS and invariant:plan_closure reports FAIL
  - actual: FAIL (PARTIAL_EXECUTION), sealed-run replay
  - fired: invariant:plan_closure (invariant:plan_closure) FAIL PARTIAL_EXECUTION [PARTIAL_EXECUTION]
  - activation: replay of the sealed run (activated)

## BLIND SPOTS

- `M04_duplicate_row` (BLIND_SPOT): duplicate the record at line 5 (key ['BM-04']) of input 'readings' (fixtures/data/readings.csv); its declared digest is re-declared so a digest mismatch cannot mask the detector under test
  - expected: the status is not PASS and check:duplicate_rows reports FAIL
  - actual: PASS (VERIFIED), fresh copy
  - activation: file mutant, activated; 2 file(s) read from the copy; mutated paths read 2/2; 7 value read(s)
  - stage: PROPAGATED_NOT_CHECKED
  - BLIND_SPOT: the mutant verified as PASS; expected check:duplicate_rows reports FAIL [PROPAGATED_NOT_CHECKED]

## VERIFIER ERRORS

No verify raised, timed out or flaked.

## NOT ACTIVATED

Every verified mutant read its own copy.

## NOT EXECUTED

No mutant was a no-op, an equivalent, a duplicate or suppressed.

## SKIPPED

No applicable mutation was skipped.

## NOT APPLICABLE

- `M03_deleted_accepted_row` (NOT_APPLICABLE): A record accepted in the snapshot is deleted from its input.
  - expected: the status is not PASS and check:snapshot_completeness reports FAIL with OMITTED_POPULATION
  - NOT_APPLICABLE: the manifest declares no readable accepted_snapshot
- `M05_duplicate_reviewer_verdict` (NOT_APPLICABLE): A required reviewer's verdict is recorded twice.
  - expected: the status is not PASS and check:reviewer_protocol reports ABSTAIN with PROTOCOL_BROKEN
  - NOT_APPLICABLE: the manifest declares no readable reviewer verdicts
- `M06_missing_required_reviewer` (NOT_APPLICABLE): Every verdict of a required reviewer is removed.
  - expected: the status is not PASS and check:reviewer_protocol reports ABSTAIN with PROTOCOL_BROKEN
  - NOT_APPLICABLE: the manifest declares no readable reviewer verdicts
- `M08_changed_author` (NOT_APPLICABLE): The first author of a citation entry is replaced.
  - expected: the status is not PASS and check:citation_metadata reports FAIL with SOURCE_MISMATCH
  - NOT_APPLICABLE: the manifest declares no readable citation entries
- `M09_changed_doi` (NOT_APPLICABLE): A citation entry's DOI is changed to one that no frozen record holds.
  - expected: the status is not PASS and check:citation_resolver reports ABSTAIN with SOURCE_UNAVAILABLE
  - NOT_APPLICABLE: the manifest declares no readable citation entries
- `M12_timezone_shift` (NOT_APPLICABLE): An observation's declared timezone shifts by one hour.
  - expected: the status is not PASS and check:time_source reports FAIL with SOURCE_MISMATCH
  - NOT_APPLICABLE: the manifest declares no readable time sources
- `M13_removed_invocation` (NOT_APPLICABLE): An invocation record behind a claimed citation verification is removed.
  - expected: the status is not PASS and check:verification_log reports ABSTAIN or FAIL with NARRATED_VERIFICATION or UNVERIFIED
  - NOT_APPLICABLE: the manifest declares no citation verification log with invocation records
- `M14_pass_summary_without_evidence` (NOT_APPLICABLE): A stored PASS summary loses every pinned digest.
  - expected: the status is not PASS and check:summary_consistency reports ABSTAIN with NARRATED_VERIFICATION or VACUOUS_PASS
  - NOT_APPLICABLE: the manifest declares no stored PASS summary that pins evidence
- `M18_changed_upstream_design` (NOT_APPLICABLE): An upstream DESIGN artifact changes beneath its recorded digest.
  - expected: the status is not PASS and check:dependency_currency reports FAIL with STALE_DEPENDENCY
  - NOT_APPLICABLE: the manifest declares no readable dependency graph
- `M19_replaced_stored_claim_output` (NOT_APPLICABLE): A registered claim's stored output is replaced.
  - expected: the status is not PASS and check:claim_registry reports ABSTAIN or FAIL with SOURCE_MISMATCH
  - NOT_APPLICABLE: the manifest declares no readable claim registry
- `M20_metadata_change_under_unchanged_pass_summary` (NOT_APPLICABLE): Evidence metadata changes while the stored PASS summary stays the same.
  - expected: the status is not PASS and check:summary_consistency reports FAIL with SOURCE_MISMATCH
  - NOT_APPLICABLE: the manifest declares no stored PASS summary to hold unchanged

## WHAT THIS RESULT DOES NOT PROVE

- Mutation testing measures how this verifier reacted to the injected defects on this one evidence tree. Defects of other kinds, or the same defects in other trees, may still go undetected.
- A detected mutation shows that a detector fired, not that the evidence it guards is scientifically valid. Scientific validity is not established by this tool.
- Every verify ran offline with a network opener that refuses all requests; live citation lookups were not exercised.
- Activation is judged from file opens seen by one in-process audit hook. Reads made by a subprocess or by a C extension that bypasses Python's audited file APIs are invisible to it.
- Nothing was sampled and nothing was reused: every applicable operator was generated, applied and judged afresh in this call.
