## STATUS

**FAIL** (SOURCE_MISMATCH), exit code 1.

- Run: `run-38ae6718d765c8f5`
- Started 2026-09-26T00:00:00Z; completed 2026-09-26T00:00:00Z
- Reasons: SOURCE_MISMATCH
- Failure modes: STALE_DEPENDENCY
- Verdict rises: NONE -> PASS at step 1 (`check:columns`, VERIFIED); PASS -> FAIL at step 3 (`check:currency`, SOURCE_MISMATCH)
- Evidence manifest sha256: `8decda1b0147eb4b1198c398b14ab60119c8787909b44bec4e6ea043fe5783fa`
- Ledger: 17 entries, head `435df4817512e70db37c2c53d9ef18c8a21003770ca3fde42a274b891f95f78d`
- Receipt: content sha256 `f9cec90a7af017d9135514082f3aba768d6557a27df1abca47e0b496f8b04cc0`, UNSIGNED
- Scope: integrity and the declared evaluation only. Scientific validity is not established by this tool.

## WHAT WAS EXPECTED

- Manifest `manifest.json`, sha256 `e9cf152319b5686870affd470f18f48cdef1ff92c5d3ef02e9fbcb64546ea533`, run label `corpus-stale-dependency-synthetic-01`

Inputs declared: 1 (expected_inputs 1)

- `plots`: `fixtures/data/plots.csv`, csv, required, expected_rows 6 (INDEPENDENT), declared sha256 `bc2f606fb2c361aef613a1311069ed5483a8aff17d0b789c99b96dc1069e19f3`

Checks declared: 3, of which 3 required (checks_expected 3)

- `rows`: row_count v1, required, inputs plots
- `columns`: required_columns v1, required, inputs plots
- `currency`: dependency_currency v1, required, inputs 

PASS requires: every required input found, opened, parsed and matching any declared digest; at least one input opened; at least one data row examined; checks_executed == checks_expected; every required check PASS with a falsifier witness showing it could have failed; every applicable invariant holding; a non-empty evidence manifest.

## WHAT WAS EXAMINED

- Input funnel: expected 1 -> discovered 1 -> opened 1 -> parsed 1 -> examined 1; input closure holds (1 of 1, INDEPENDENT)
- rows_examined: 6 (distinct data rows of declared inputs read by an executed check)
- Each check line under WHAT PASSED, WHAT FAILED and WHAT ABSTAINED gives that check's own subject records examined (its run.json checks[].rows_examined); those figures are not summed.

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
- Ledger sealed at 17 entries, head `435df4817512e70db37c2c53d9ef18c8a21003770ca3fde42a274b891f95f78d`
- PLAN: ledger entry 1, entry sha256 `032346c39170f5eab2fe542e63e7f3bb0b69d5eb26683b2618e0fdd54828769a`, written before any check ran: 1 input(s), 3 check(s) and 10 pin(s) planned, manifest sha256 `e9cf152319b5686870affd470f18f48cdef1ff92c5d3ef02e9fbcb64546ea533`

Invocations:

- `columns` (required_columns v1): invocation `inv-e8eeec79c84b`, CHECKED, PASS; falsifier witness WITNESSED (1 of 1 case(s) rejected as expected)
- `currency` (dependency_currency v1): invocation `inv-052756f92570`, CHECKED, FAIL; no falsifier ran (only a would-be PASS is falsified)
- `rows` (row_count v1): invocation `inv-1378e5b6915f`, CHECKED, PASS; falsifier witness WITNESSED (1 of 1 case(s) rejected as expected)

Controls (each its own invocation, never counted as a check):

- comparator self-test: invocation `inv-f37725e0978f`, 3 of 3 known pair(s) compared as expected; holds
- canary: must_fail invocation `inv-d9f11ddb43e6` gave FAIL (SOURCE_MISMATCH), expected FAIL; must_pass invocation `inv-25002bd6a29b` gave PASS (VERIFIED), expected PASS; holds
- harness pins: 10 file(s) pinned; changed: none; writes to pinned paths: none; holds
- falsifier witnesses: WITNESSED 2 (`columns`, `rows`), REFUTED 0, UNWITNESSED 0, NO_CASE 0, NO_GENERATOR 0; 2 falsifier invocation(s)
- claim-to-invocation join: no claim_join check ran

## WHAT PASSED

Checks:

- `columns`: required_columns PASS (VERIFIED), subject records examined 6
- `rows`: row_count PASS (VERIFIED), subject records examined 6

Weakest discrimination: no PASS result records a discrimination ratio

Invariants that hold:

- `canary_controls_hold`: the must-fail canary failed and its known-good twin passed
- `checked_claims_le_invocations`: check results marked CHECKED: 3 claimed <= 8 invoked
- `comparator_self_test`: 3 known pairs compared as expected
- `every_invocation_has_terminal_result`: 8 invocation(s) each reached exactly one terminal result
- `every_required_check_has_terminal_state`: 3 required check(s) each reached a terminal state
- `every_verdict_has_invocation`: 3 verdict(s) each trace to a terminal invocation
- `harness_pins_intact`: 10 pinned file(s) unchanged and never written during the run
- `input_accounting_closure`: 2 INDEPENDENT closure(s) hold
- `ledger_chain_intact`: 17 entries chain to head 435df4817512e70db37c2c53d9ef18c8a21003770ca3fde42a274b891f95f78d
- `pass_requires_complete_required_inputs`: every input behind a PASS is complete
- `pass_requires_examined_rows`: rows_examined=6 (distinct data rows of declared inputs)
- `pass_requires_falsifier_witness`: 2 PASS result(s) each carry a ledger-backed falsifier witness
- `pass_requires_nonempty_evidence`: every PASS carries non-empty, hashed evidence
- `plan_closure`: 6 planned item(s) each ran exactly once
- `plan_matches_manifest`: the recorded PLAN equals the plan the manifest implies

## WHAT FAILED

Findings:

- none

Checks:

- `currency`: dependency_currency FAIL (SOURCE_MISMATCH), subject records examined 4; publication blocked: CONCLUSION/FIGURE_OR_TABLE node(s) 'conclusion-south-highest' are STALE_PENDING_REVALIDATION; node(s) 'site-means', 'study-design' are STALE_PENDING_REVALIDATION: they block no publication node, but the graph is not current

## WHAT ABSTAINED

Findings:

- none

Checks:

- none

## WHAT REMAINS UNRESOLVED

- no saved graph state at `fixtures/graph/graph-state.json`: the graph's declared node states were used
- invariant `pass_requires_complete_required_checks` not applicable: the run does not claim PASS
- the receipt is UNSIGNED (receipt.auth.json says so): its content hash detects accidental change, but anyone able to edit the run directory can rewrite and rehash it

## WHAT THIS RESULT DOES NOT PROVE

- Scientific validity: NOT ESTABLISHED. Whether any conclusion holds in its intended domain is outside what this tool can show.
- Integrity (what was established): SHA-256 recorded for 1 of 1 declared input(s); execution ledger sealed at 17 entries; ledger head 435df4817512e70db37c2c53d9ef18c8a21003770ca3fde42a274b891f95f78d; evidence manifest 8decda1b0147eb4b1198c398b14ab60119c8787909b44bec4e6ea043fe5783fa.
- Performance (how the checkers and the declared checks behaved): CHECKER: falsifier witnesses 2 WITNESSED, 0 REFUTED, 0 UNWITNESSED, 0 NO_CASE, 0 NO_GENERATOR (2 falsifier invocation(s)); must-fail/must-pass canary held; comparator self-test held. RUN: Run status FAIL (SOURCE_MISMATCH) from 3 check result(s): 2 PASS, 1 FAIL, 0 ABSTAIN, 0 ERROR; 15 applicable invariant(s), 0 violated. This describes how the declared checks behaved on the declared inputs only.
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
