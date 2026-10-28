## STATUS

**ABSTAIN** (INSUFFICIENT_EVIDENCE), exit code 2.

- Run: `run-36a763016ef9da5c`
- Started 2026-09-26T00:00:00Z; completed 2026-09-26T00:00:00Z
- Reasons: INSUFFICIENT_EVIDENCE, PARTIAL_EXECUTION, UNVERIFIED
- Failure modes: PARTIAL_EXECUTION, VACUOUS_PASS
- Evidence manifest sha256: `c260b1b9642bf7fdda006a915b79ad335d855177c7d7b201d7b2c7746f083fb9`
- Ledger: 8 entries, head `fee5f3832ede269966919d53032e5958a8bf1a0fad2544006edbdd35dc47eae1`
- Receipt: content sha256 `1450ea286c3412eb0821a7bd07cc5ec90a532621b736106630b91ed2dd1808a4`, UNSIGNED
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

PASS requires: every required input found, opened, parsed and matching any declared digest; at least one input opened; at least one row examined; checks_executed == checks_expected; every required check PASS; every applicable invariant holding; a non-empty evidence manifest.

## WHAT WAS EXAMINED

- Input funnel: expected 1 -> discovered 1 -> opened 1 -> parsed 1 -> examined 0; input closure holds (1 of 1, INDEPENDENT)
- Rows examined in scope: 1

Inputs:

- `readings` EMPTY: `fixtures/data/readings.csv`, sha256 `16ce60c2b70a83f14ef500ed7f147750eebefa86a75befc06ed62e8cc10e9eaa`, 31 bytes, 0 records (admitted 0, excluded 0, deferred 0, unresolved 0, failed 0); row closure not evaluable (UNAVAILABLE expectation)

Other documents read:

- `fixtures/summary/stored-summary.json` (summary_claim): PARSED, sha256 `f662d10b436d4ac467d7c6ebc54d0858ebcb41b107853823e81dcf0057f1e75d`

## WHAT ACTUALLY RAN

- checks_executed 1 of checks_expected 4 (required checks that reached CHECKED with a terminal invocation)
- Ledger sealed at 8 entries, head `fee5f3832ede269966919d53032e5958a8bf1a0fad2544006edbdd35dc47eae1`

Invocations:

- `columns` (required_columns v1): invocation `inv-0693bc78fd13`, NOT_APPLICABLE, ABSTAIN, rows examined 0
- `duplicates` (duplicate_rows v1): invocation `inv-ae4d789e0baa`, NOT_APPLICABLE, ABSTAIN, rows examined 0
- `rows` (row_count v1): invocation `inv-c42147d73d06`, NOT_APPLICABLE, ABSTAIN, rows examined 0
- `stored-pass` (summary_consistency v1): invocation `inv-b78591ed65b3`, CHECKED, ABSTAIN, rows examined 1

## WHAT PASSED

Checks:

- none

Invariants that hold:

- `checked_claims_le_invocations`: check results marked CHECKED: 1 claimed <= 4 invoked
- `every_invocation_has_terminal_result`: 4 invocation(s) each reached exactly one terminal result
- `every_required_check_has_terminal_state`: 4 required check(s) each reached a terminal state
- `every_verdict_has_invocation`: 4 verdict(s) each trace to a terminal invocation
- `input_accounting_closure`: 1 INDEPENDENT closure(s) hold
- `ledger_chain_intact`: 8 entries chain to head fee5f3832ede269966919d53032e5958a8bf1a0fad2544006edbdd35dc47eae1

## WHAT FAILED

Findings:

- none

Checks:

- none

## WHAT ABSTAINED

Findings:

- [input:readings] ABSTAIN INSUFFICIENT_EVIDENCE (VACUOUS_PASS): required input is EMPTY: EMPTY: the input contains no data records
- [contract:checks_executed] ABSTAIN PARTIAL_EXECUTION (PARTIAL_EXECUTION): checks_executed=1 of checks_expected=4

Checks:

- `columns`: required_columns ABSTAIN (INSUFFICIENT_EVIDENCE), rows examined 0; input 'readings' is EMPTY: not examined; no input has rows to examine
- `duplicates`: duplicate_rows ABSTAIN (INSUFFICIENT_EVIDENCE), rows examined 0; input 'readings' is EMPTY: not examined; no input has rows to examine
- `rows`: row_count ABSTAIN (INSUFFICIENT_EVIDENCE), rows examined 0; input 'readings' is EMPTY: not examined; no input has rows to examine
- `stored-pass`: summary_consistency ABSTAIN (UNVERIFIED), rows examined 1; the summary pins input 'readings' with 0 rows

## WHAT REMAINS UNRESOLVED

- required input `readings` is EMPTY: EMPTY: the input contains no data records
- row closure of input `readings` not evaluated (UNAVAILABLE)
- check `columns` was NOT_APPLICABLE
- check `duplicates` was NOT_APPLICABLE
- check `rows` was NOT_APPLICABLE
- invariant `pass_requires_complete_required_checks` not applicable: the run does not claim PASS
- invariant `pass_requires_complete_required_inputs` not applicable: no check result and no run-level status claims PASS
- invariant `pass_requires_examined_rows` not applicable: no check result and no run-level status claims PASS
- invariant `pass_requires_nonempty_evidence` not applicable: no check result and no run-level status claims PASS
- the receipt is UNSIGNED: its content hash detects accidental change, but anyone able to edit the run directory can rewrite and rehash it

## WHAT THIS RESULT DOES NOT PROVE

- Scientific validity: NOT ESTABLISHED. Whether any conclusion holds in its intended domain is outside what this tool can show.
- Integrity (what was established): SHA-256 recorded for 1 of 1 declared input(s); execution ledger sealed at 8 entries; ledger head fee5f3832ede269966919d53032e5958a8bf1a0fad2544006edbdd35dc47eae1; evidence manifest c260b1b9642bf7fdda006a915b79ad335d855177c7d7b201d7b2c7746f083fb9.
- Performance (how the declared checks behaved): Run status ABSTAIN (INSUFFICIENT_EVIDENCE) from 4 check result(s): 0 PASS, 0 FAIL, 4 ABSTAIN, 0 ERROR; 6 applicable invariant(s), 0 violated. This describes how the declared checks behaved on the declared inputs only.
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
