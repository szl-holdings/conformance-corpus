## STATUS

**ABSTAIN** (UNVERIFIED), exit code 2.

- Run: `run-90ccfbdd98889d7d`
- Started 2026-09-26T00:00:00Z; completed 2026-09-26T00:00:00Z
- Reasons: UNVERIFIED
- Failure modes: NARRATED_VERIFICATION
- Evidence manifest sha256: `8ad6705ac7e39c1822ee2a3fea5567517706856eaca33260cdcd409a46937743`
- Ledger: 4 entries, head `cbe28383d5d7b351b57f50b1c1d6ce165e11f85648c69d6e117d3573a58e05de`
- Receipt: content sha256 `9764403743b5d82c55324e51adf464318480be29e07cefafc864af7ad446999b`, UNSIGNED
- Scope: integrity and the declared evaluation only. Scientific validity is not established by this tool.

## WHAT WAS EXPECTED

- Manifest `manifest.json`, sha256 `e9c680da1a776b1b6f5d05ff096772b288d485aae7193d66c626b9ea729f4a42`, run label `corpus-narrated-verification-synthetic-01`

Inputs declared: 1 (expected_inputs 1)

- `observations`: `fixtures/data/observations.csv`, csv, required, expected_rows 4 (INDEPENDENT), declared sha256 `fe0bcf4b94b84891ad23a4c8150ad477ad6f1b2114090e1afe401d2565dbd216`

Checks declared: 2, of which 2 required (checks_expected 2)

- `rows`: row_count v1, required, inputs observations
- `citation-log`: verification_log v1, required, inputs 

PASS requires: every required input found, opened, parsed and matching any declared digest; at least one input opened; at least one row examined; checks_executed == checks_expected; every required check PASS; every applicable invariant holding; a non-empty evidence manifest.

## WHAT WAS EXAMINED

- Input funnel: expected 1 -> discovered 1 -> opened 1 -> parsed 1 -> examined 1; input closure holds (1 of 1, INDEPENDENT)
- Rows examined in scope: 9

Inputs:

- `observations` PARSED: `fixtures/data/observations.csv`, sha256 `fe0bcf4b94b84891ad23a4c8150ad477ad6f1b2114090e1afe401d2565dbd216`, 210 bytes, 4 records (admitted 4, excluded 0, deferred 0, unresolved 0, failed 0); row closure holds (4 of 4, INDEPENDENT)

Other documents read:

- `fixtures/citations/entries.json` (citations.entries): PARSED, sha256 `af74bbe24e6f23440afa24f34a83ce4d7fd054609d592ec25e163570dca23b41`
- `fixtures/citations/verification-log.json` (citations.log): PARSED, sha256 `4c4ba19e296cd3ac2f055a19a8d295496eb4530a81b10771b9277c244b458b34`

## WHAT ACTUALLY RAN

- checks_executed 2 of checks_expected 2 (required checks that reached CHECKED with a terminal invocation)
- Ledger sealed at 4 entries, head `cbe28383d5d7b351b57f50b1c1d6ce165e11f85648c69d6e117d3573a58e05de`

Invocations:

- `citation-log` (verification_log v1): invocation `inv-a04d3285b985`, CHECKED, ABSTAIN, rows examined 5
- `rows` (row_count v1): invocation `inv-28593f19b03a`, CHECKED, PASS, rows examined 4

## WHAT PASSED

Checks:

- `rows`: row_count PASS (VERIFIED), rows examined 4

Invariants that hold:

- `every_invocation_has_terminal_result`: 2 invocation(s) each reached exactly one terminal result
- `every_required_check_has_terminal_state`: 2 required check(s) each reached a terminal state
- `every_verdict_has_invocation`: 2 verdict(s) each trace to a terminal invocation
- `input_accounting_closure`: 2 INDEPENDENT closure(s) hold
- `ledger_chain_intact`: 4 entries chain to head cbe28383d5d7b351b57f50b1c1d6ce165e11f85648c69d6e117d3573a58e05de
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

- [invariant:checked_claims_le_invocations] ABSTAIN UNVERIFIED (NARRATED_VERIFICATION): citation-log: claimed_verified vs complete invocation records: 5 claimed but only 2 invoked; citation-log: entries claimed VERIFIED vs entries with a record: 5 claimed but only 2 invoked

Checks:

- `citation-log`: verification_log ABSTAIN (UNVERIFIED), rows examined 5; NARRATED_VERIFICATION: 3 citation(s) claimed VERIFIED with no complete invocation record: ['C3', 'C4', 'C5']

## WHAT REMAINS UNRESOLVED

- invariant `pass_requires_complete_required_checks` not applicable: the run does not claim PASS
- the receipt is UNSIGNED: its content hash detects accidental change, but anyone able to edit the run directory can rewrite and rehash it

## WHAT THIS RESULT DOES NOT PROVE

- Scientific validity: NOT ESTABLISHED. Whether any conclusion holds in its intended domain is outside what this tool can show.
- Integrity (what was established): SHA-256 recorded for 1 of 1 declared input(s); execution ledger sealed at 4 entries; ledger head cbe28383d5d7b351b57f50b1c1d6ce165e11f85648c69d6e117d3573a58e05de; evidence manifest 8ad6705ac7e39c1822ee2a3fea5567517706856eaca33260cdcd409a46937743.
- Performance (how the declared checks behaved): Run status ABSTAIN (UNVERIFIED) from 2 check result(s): 1 PASS, 0 FAIL, 1 ABSTAIN, 0 ERROR; 9 applicable invariant(s), 1 violated. This describes how the declared checks behaved on the declared inputs only.
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
