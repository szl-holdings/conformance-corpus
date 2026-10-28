## STATUS

**FAIL** (SOURCE_MISMATCH), exit code 1.

- Run: `run-ad078c6dec5e4572`
- Started 2026-09-26T00:00:00Z; completed 2026-09-26T00:00:00Z
- Reasons: SOURCE_MISMATCH
- Failure modes: STALE_DEPENDENCY
- Evidence manifest sha256: `e420876f673e900943cbff6afc3523b63ffd738b20bffbe8b9d816b3d681ab82`
- Ledger: 6 entries, head `fffa8f7806e1775291ed0bfc79aa80dc819ecd8b0c973be81f7aadb01408d895`
- Receipt: content sha256 `22fa6f0d8b528080e8a25d80a28e7dc268ad7ac6bb71c303850dae12929b7ca1`, UNSIGNED
- Scope: integrity and the declared evaluation only. Scientific validity is not established by this tool.

## WHAT WAS EXPECTED

- Manifest `manifest.json`, sha256 `e9cf152319b5686870affd470f18f48cdef1ff92c5d3ef02e9fbcb64546ea533`, run label `corpus-stale-dependency-synthetic-01`

Inputs declared: 1 (expected_inputs 1)

- `plots`: `fixtures/data/plots.csv`, csv, required, expected_rows 6 (INDEPENDENT), declared sha256 `bc2f606fb2c361aef613a1311069ed5483a8aff17d0b789c99b96dc1069e19f3`

Checks declared: 3, of which 3 required (checks_expected 3)

- `rows`: row_count v1, required, inputs plots
- `columns`: required_columns v1, required, inputs plots
- `currency`: dependency_currency v1, required, inputs 

PASS requires: every required input found, opened, parsed and matching any declared digest; at least one input opened; at least one row examined; checks_executed == checks_expected; every required check PASS; every applicable invariant holding; a non-empty evidence manifest.

## WHAT WAS EXAMINED

- Input funnel: expected 1 -> discovered 1 -> opened 1 -> parsed 1 -> examined 1; input closure holds (1 of 1, INDEPENDENT)
- Rows examined in scope: 10

Inputs:

- `plots` PARSED: `fixtures/data/plots.csv`, sha256 `bc2f606fb2c361aef613a1311069ed5483a8aff17d0b789c99b96dc1069e19f3`, 250 bytes, 6 records (admitted 6, excluded 0, deferred 0, unresolved 0, failed 0); row closure holds (6 of 6, INDEPENDENT)

Other documents read:

- `fixtures/analysis/site-means.csv` (dependencies.node): PARSED, sha256 `30b91b0e98e0f4f7b3cf9b2b2272ee5383161bdb25fc18fcfc8a4d2d9f220d34`
- `fixtures/conclusions/conclusion-south-highest.md` (dependencies.node): PARSED, sha256 `bed11c00b085a8517ea6f7c7f41ae0272a97924229396ebce2fce4dc7b838286`
- `fixtures/data/plots.csv` (dependencies.node): PARSED, sha256 `bc2f606fb2c361aef613a1311069ed5483a8aff17d0b789c99b96dc1069e19f3`
- `fixtures/design/protocol.md` (dependencies.node): PARSED, sha256 `7987eed13d74508e23f9434dc0a976dbe8095e72a9681075d1836fdd0b947777`
- `fixtures/graph/graph-state.json` (dependencies.state): MISSING, sha256 `unknown`
- `fixtures/graph/graph.json` (dependencies): PARSED, sha256 `9fab7ff816a5335fd4a38bae0c22f7d8f7597cb2ba0e5b73f3709331198f20bb`

## WHAT ACTUALLY RAN

- checks_executed 3 of checks_expected 3 (required checks that reached CHECKED with a terminal invocation)
- Ledger sealed at 6 entries, head `fffa8f7806e1775291ed0bfc79aa80dc819ecd8b0c973be81f7aadb01408d895`

Invocations:

- `columns` (required_columns v1): invocation `inv-a4851455f491`, CHECKED, PASS, rows examined 6
- `currency` (dependency_currency v1): invocation `inv-e2056b8a4957`, CHECKED, FAIL, rows examined 4
- `rows` (row_count v1): invocation `inv-cb0382a984ff`, CHECKED, PASS, rows examined 6

## WHAT PASSED

Checks:

- `columns`: required_columns PASS (VERIFIED), rows examined 6
- `rows`: row_count PASS (VERIFIED), rows examined 6

Invariants that hold:

- `checked_claims_le_invocations`: check results marked CHECKED: 3 claimed <= 3 invoked
- `every_invocation_has_terminal_result`: 3 invocation(s) each reached exactly one terminal result
- `every_required_check_has_terminal_state`: 3 required check(s) each reached a terminal state
- `every_verdict_has_invocation`: 3 verdict(s) each trace to a terminal invocation
- `input_accounting_closure`: 2 INDEPENDENT closure(s) hold
- `ledger_chain_intact`: 6 entries chain to head fffa8f7806e1775291ed0bfc79aa80dc819ecd8b0c973be81f7aadb01408d895
- `pass_requires_complete_required_inputs`: every input behind a PASS is complete
- `pass_requires_examined_rows`: rows_examined=16
- `pass_requires_nonempty_evidence`: every PASS carries non-empty, hashed evidence

## WHAT FAILED

Findings:

- none

Checks:

- `currency`: dependency_currency FAIL (SOURCE_MISMATCH), rows examined 4; publication blocked: CONCLUSION/FIGURE_OR_TABLE node(s) 'conclusion-south-highest' are STALE_PENDING_REVALIDATION; node(s) 'site-means', 'study-design' are STALE_PENDING_REVALIDATION: they block no publication node, but the graph is not current

## WHAT ABSTAINED

Findings:

- none

Checks:

- none

## WHAT REMAINS UNRESOLVED

- document `fixtures/graph/graph-state.json` is MISSING: MISSING: no file at fixtures/graph/graph-state.json
- invariant `pass_requires_complete_required_checks` not applicable: the run does not claim PASS
- the receipt is UNSIGNED: its content hash detects accidental change, but anyone able to edit the run directory can rewrite and rehash it

## WHAT THIS RESULT DOES NOT PROVE

- Scientific validity: NOT ESTABLISHED. Whether any conclusion holds in its intended domain is outside what this tool can show.
- Integrity (what was established): SHA-256 recorded for 1 of 1 declared input(s); execution ledger sealed at 6 entries; ledger head fffa8f7806e1775291ed0bfc79aa80dc819ecd8b0c973be81f7aadb01408d895; evidence manifest e420876f673e900943cbff6afc3523b63ffd738b20bffbe8b9d816b3d681ab82.
- Performance (how the declared checks behaved): Run status FAIL (SOURCE_MISMATCH) from 3 check result(s): 2 PASS, 1 FAIL, 0 ABSTAIN, 0 ERROR; 9 applicable invariant(s), 0 violated. This describes how the declared checks behaved on the declared inputs only.
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
