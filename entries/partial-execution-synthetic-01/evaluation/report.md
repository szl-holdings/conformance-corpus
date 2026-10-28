## STATUS

**ABSTAIN** (INSUFFICIENT_EVIDENCE), exit code 2.

- Run: `run-ebeaf9c4a4607f57`
- Started 2026-09-26T00:00:00Z; completed 2026-09-26T00:00:00Z
- Reasons: INSUFFICIENT_EVIDENCE
- Failure modes: OMITTED_POPULATION
- Verdict rises: NONE -> PASS at step 1 (`check:columns`, VERIFIED); PASS -> ABSTAIN at step 4 (`check:time-window`, INSUFFICIENT_EVIDENCE)
- Evidence manifest sha256: `7aca8841d228c2e0ef2da63b42cf063768d2ecaec4d2554cc6b9706e677315a5`
- Ledger: 21 entries, head `20b8a63250662eb5d6913a3aba1496d6a5a2130a4a411e398aa0c2b3b2e22a07`
- Receipt: content sha256 `b304311437d4d260b1d828ef7e2daba07ca338496dab211d4d6d001ba716b6b1`, UNSIGNED
- Scope: integrity and the declared evaluation only. Scientific validity is not established by this tool.

## WHAT WAS EXPECTED

- Manifest `manifest.json`, sha256 `6b74a38cec314b6d1f00651c4cd4cc66d801f959cb7dfd31a96939bed4cac524`, run label `corpus-partial-execution-synthetic-01`

Inputs declared: 1 (expected_inputs 1)

- `samples`: `fixtures/data/samples.csv`, csv, required, expected_rows 5 (INDEPENDENT), declared sha256 `1581a2901c01c139f255390ff7782d7fa2a5290625114f80a23bf35705dfe199`

Checks declared: 4, of which 4 required (checks_expected 4)

- `rows`: row_count v1, required, inputs samples
- `columns`: required_columns v1, required, inputs samples
- `duplicates`: duplicate_rows v1, required, inputs samples
- `time-window`: time_source v1, required, inputs 

PASS requires: every required input found, opened, parsed and matching any declared digest; at least one input opened; at least one data row examined; checks_executed == checks_expected; every required check PASS with a falsifier witness showing it could have failed; every applicable invariant holding; a non-empty evidence manifest.

## WHAT WAS EXAMINED

- Input funnel: expected 1 -> discovered 1 -> opened 1 -> parsed 1 -> examined 1; input closure holds (1 of 1, INDEPENDENT)
- rows_examined: 5 (distinct data rows of declared inputs read by an executed check)
- Each check line under WHAT PASSED, WHAT FAILED and WHAT ABSTAINED gives that check's own subject records examined (its run.json checks[].rows_examined); those figures are not summed.

Inputs:

- `samples` PARSED: `fixtures/data/samples.csv`, sha256 `1581a2901c01c139f255390ff7782d7fa2a5290625114f80a23bf35705dfe199`, 249 bytes, 5 records (admitted 5, excluded 0, deferred 0, unresolved 0, failed 0); row closure holds (5 of 5, INDEPENDENT)

Other documents read:

- `fixtures/time/events.json` (time_sources): MISSING, sha256 `unknown`

## WHAT ACTUALLY RAN

- checks_executed 3 of checks_expected 4 (required checks that reached CHECKED with a terminal invocation)
- Ledger sealed at 21 entries, head `20b8a63250662eb5d6913a3aba1496d6a5a2130a4a411e398aa0c2b3b2e22a07`
- PLAN: ledger entry 1, entry sha256 `bd7bc9cfae061e23312937b64c9a79b504d51305eb65ee007f4215621f928591`, written before any check ran: 1 input(s), 4 check(s) and 4 pin(s) planned, manifest sha256 `6b74a38cec314b6d1f00651c4cd4cc66d801f959cb7dfd31a96939bed4cac524`

Invocations:

- `columns` (required_columns v1): invocation `inv-ffbd7745ce96`, CHECKED, PASS; falsifier witness WITNESSED (1 of 1 case(s) rejected as expected)
- `duplicates` (duplicate_rows v1): invocation `inv-398e43f7165d`, CHECKED, PASS; falsifier witness WITNESSED (1 of 1 case(s) rejected as expected)
- `rows` (row_count v1): invocation `inv-4eb1cfe2689f`, CHECKED, PASS; falsifier witness WITNESSED (1 of 1 case(s) rejected as expected)
- `time-window` (time_source v1): invocation `inv-0cd7c008880e`, SKIPPED, ABSTAIN; no falsifier ran (only a would-be PASS is falsified)

Controls (each its own invocation, never counted as a check):

- comparator self-test: invocation `inv-171f59a95f0d`, 3 of 3 known pair(s) compared as expected; holds
- canary: must_fail invocation `inv-94346971c8eb` gave FAIL (SOURCE_MISMATCH), expected FAIL; must_pass invocation `inv-076912a0759f` gave PASS (VERIFIED), expected PASS; holds
- harness pins: 4 file(s) pinned; changed: none; writes to pinned paths: none; holds
- falsifier witnesses: WITNESSED 3 (`columns`, `duplicates`, `rows`), REFUTED 0, UNWITNESSED 0, NO_CASE 0, NO_GENERATOR 0; 3 falsifier invocation(s)
- claim-to-invocation join: no claim_join check ran

## WHAT PASSED

Checks:

- `columns`: required_columns PASS (VERIFIED), subject records examined 5
- `duplicates`: duplicate_rows PASS (VERIFIED), subject records examined 5
- `rows`: row_count PASS (VERIFIED), subject records examined 5

Weakest discrimination: no PASS result records a discrimination ratio

Invariants that hold:

- `canary_controls_hold`: the must-fail canary failed and its known-good twin passed
- `checked_claims_le_invocations`: check results marked CHECKED: 3 claimed <= 10 invoked
- `comparator_self_test`: 3 known pairs compared as expected
- `every_invocation_has_terminal_result`: 10 invocation(s) each reached exactly one terminal result
- `every_required_check_has_terminal_state`: 4 required check(s) each reached a terminal state
- `every_verdict_has_invocation`: 4 verdict(s) each trace to a terminal invocation
- `harness_pins_intact`: 4 pinned file(s) unchanged and never written during the run
- `input_accounting_closure`: 2 INDEPENDENT closure(s) hold
- `ledger_chain_intact`: 21 entries chain to head 20b8a63250662eb5d6913a3aba1496d6a5a2130a4a411e398aa0c2b3b2e22a07
- `pass_requires_complete_required_inputs`: every input behind a PASS is complete
- `pass_requires_examined_rows`: rows_examined=5 (distinct data rows of declared inputs)
- `pass_requires_falsifier_witness`: 3 PASS result(s) each carry a ledger-backed falsifier witness
- `pass_requires_nonempty_evidence`: every PASS carries non-empty, hashed evidence
- `plan_closure`: 7 planned item(s) each ran exactly once
- `plan_matches_manifest`: the recorded PLAN equals the plan the manifest implies

## WHAT FAILED

Findings:

- none

Checks:

- none

## WHAT ABSTAINED

Findings:

- [contract:checks_executed] ABSTAIN INSUFFICIENT_EVIDENCE (OMITTED_POPULATION): required check 'time-window' did not execute: it was SKIPPED, justified as INPUT_UNAVAILABLE (checks_executed=3 of checks_expected=4)

Checks:

- `time-window`: time_source ABSTAIN (INSUFFICIENT_EVIDENCE), subject records examined 0; time_sources (fixtures/time/events.json) unavailable: MISSING: no file at fixtures/time/events.json

## WHAT REMAINS UNRESOLVED

- document `fixtures/time/events.json` is MISSING: MISSING: no file at fixtures/time/events.json
- check `time-window` was SKIPPED
- invariant `pass_requires_complete_required_checks` not applicable: the run does not claim PASS
- the receipt is UNSIGNED (receipt.auth.json says so): its content hash detects accidental change, but anyone able to edit the run directory can rewrite and rehash it

## WHAT THIS RESULT DOES NOT PROVE

- Scientific validity: NOT ESTABLISHED. Whether any conclusion holds in its intended domain is outside what this tool can show.
- Integrity (what was established): SHA-256 recorded for 1 of 1 declared input(s); execution ledger sealed at 21 entries; ledger head 20b8a63250662eb5d6913a3aba1496d6a5a2130a4a411e398aa0c2b3b2e22a07; evidence manifest 7aca8841d228c2e0ef2da63b42cf063768d2ecaec4d2554cc6b9706e677315a5.
- Performance (how the checkers and the declared checks behaved): CHECKER: falsifier witnesses 3 WITNESSED, 0 REFUTED, 0 UNWITNESSED, 0 NO_CASE, 0 NO_GENERATOR (3 falsifier invocation(s)); must-fail/must-pass canary held; comparator self-test held. RUN: Run status ABSTAIN (INSUFFICIENT_EVIDENCE) from 4 check result(s): 3 PASS, 0 FAIL, 1 ABSTAIN, 0 ERROR; 15 applicable invariant(s), 0 violated. This describes how the declared checks behaved on the declared inputs only.
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
