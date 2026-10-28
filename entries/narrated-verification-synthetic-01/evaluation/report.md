## STATUS

**ABSTAIN** (UNVERIFIED), exit code 2.

- Run: `run-90ccfbdd98889d7d`
- Started 2026-09-26T00:00:00Z; completed 2026-09-26T00:00:00Z
- Reasons: UNVERIFIED
- Failure modes: NARRATED_VERIFICATION
- Verdict rises: NONE -> PASS at step 1 (`check:rows`, VERIFIED); PASS -> ABSTAIN at step 2 (`check:citation-log`, UNVERIFIED)
- Evidence manifest sha256: `ce2659172e7fa581ba572c6634d26472b818ec8a0a03d8c87350795e4188c08a`
- Ledger: 13 entries, head `07f4d20bab9ee4a6c41f5030aff1ee96eaf9c2094fab6580d2e7930b0b3036c1`
- Receipt: content sha256 `82df013f7c60494d4e055aad03faf3d811cd1fa2eb108b55c0214f734a7d50fa`, UNSIGNED
- Scope: integrity and the declared evaluation only. Scientific validity is not established by this tool.

## WHAT WAS EXPECTED

- Manifest `manifest.json`, sha256 `e9c680da1a776b1b6f5d05ff096772b288d485aae7193d66c626b9ea729f4a42`, run label `corpus-narrated-verification-synthetic-01`

Inputs declared: 1 (expected_inputs 1)

- `observations`: `fixtures/data/observations.csv`, csv, required, expected_rows 4 (INDEPENDENT), declared sha256 `fe0bcf4b94b84891ad23a4c8150ad477ad6f1b2114090e1afe401d2565dbd216`

Checks declared: 2, of which 2 required (checks_expected 2)

- `rows`: row_count v1, required, inputs observations
- `citation-log`: verification_log v1, required, inputs 

PASS requires: every required input found, opened, parsed and matching any declared digest; at least one input opened; at least one data row examined; checks_executed == checks_expected; every required check PASS with a falsifier witness showing it could have failed; every applicable invariant holding; a non-empty evidence manifest.

## WHAT WAS EXAMINED

- Input funnel: expected 1 -> discovered 1 -> opened 1 -> parsed 1 -> examined 1; input closure holds (1 of 1, INDEPENDENT)
- rows_examined: 4 (distinct data rows of declared inputs read by an executed check)
- Each check line under WHAT PASSED, WHAT FAILED and WHAT ABSTAINED gives that check's own subject records examined (its run.json checks[].rows_examined); those figures are not summed.

Inputs:

- `observations` PARSED: `fixtures/data/observations.csv`, sha256 `fe0bcf4b94b84891ad23a4c8150ad477ad6f1b2114090e1afe401d2565dbd216`, 210 bytes, 4 records (admitted 4, excluded 0, deferred 0, unresolved 0, failed 0); row closure holds (4 of 4, INDEPENDENT)

Other documents read:

- `fixtures/citations/entries.json` (citations.entries): PARSED, sha256 `af74bbe24e6f23440afa24f34a83ce4d7fd054609d592ec25e163570dca23b41`
- `fixtures/citations/verification-log.json` (citations.log): PARSED, sha256 `4c4ba19e296cd3ac2f055a19a8d295496eb4530a81b10771b9277c244b458b34`

## WHAT ACTUALLY RAN

- checks_executed 2 of checks_expected 2 (required checks that reached CHECKED with a terminal invocation)
- Ledger sealed at 13 entries, head `07f4d20bab9ee4a6c41f5030aff1ee96eaf9c2094fab6580d2e7930b0b3036c1`
- PLAN: ledger entry 1, entry sha256 `c28f898507d11f6cf201709f4e63731d8185374656678b2f58505e63885bb34b`, written before any check ran: 1 input(s), 2 check(s) and 6 pin(s) planned, manifest sha256 `e9c680da1a776b1b6f5d05ff096772b288d485aae7193d66c626b9ea729f4a42`

Invocations:

- `citation-log` (verification_log v1): invocation `inv-b65d33796999`, CHECKED, ABSTAIN; no falsifier ran (only a would-be PASS is falsified)
- `rows` (row_count v1): invocation `inv-93024ffa4c12`, CHECKED, PASS; falsifier witness WITNESSED (1 of 1 case(s) rejected as expected)

Controls (each its own invocation, never counted as a check):

- comparator self-test: invocation `inv-03a23b6ba44d`, 3 of 3 known pair(s) compared as expected; holds
- canary: must_fail invocation `inv-577774a04f97` gave FAIL (SOURCE_MISMATCH), expected FAIL; must_pass invocation `inv-c35570988504` gave PASS (VERIFIED), expected PASS; holds
- harness pins: 6 file(s) pinned; changed: none; writes to pinned paths: none; holds
- falsifier witnesses: WITNESSED 1 (`rows`), REFUTED 0, UNWITNESSED 0, NO_CASE 0, NO_GENERATOR 0; 1 falsifier invocation(s)
- claim-to-invocation join: no claim_join check ran

## WHAT PASSED

Checks:

- `rows`: row_count PASS (VERIFIED), subject records examined 4

Weakest discrimination: no PASS result records a discrimination ratio

Invariants that hold:

- `canary_controls_hold`: the must-fail canary failed and its known-good twin passed
- `comparator_self_test`: 3 known pairs compared as expected
- `every_invocation_has_terminal_result`: 6 invocation(s) each reached exactly one terminal result
- `every_required_check_has_terminal_state`: 2 required check(s) each reached a terminal state
- `every_verdict_has_invocation`: 2 verdict(s) each trace to a terminal invocation
- `harness_pins_intact`: 6 pinned file(s) unchanged and never written during the run
- `input_accounting_closure`: 2 INDEPENDENT closure(s) hold
- `ledger_chain_intact`: 13 entries chain to head 07f4d20bab9ee4a6c41f5030aff1ee96eaf9c2094fab6580d2e7930b0b3036c1
- `pass_requires_complete_required_inputs`: every input behind a PASS is complete
- `pass_requires_examined_rows`: rows_examined=4 (distinct data rows of declared inputs)
- `pass_requires_falsifier_witness`: 1 PASS result(s) each carry a ledger-backed falsifier witness
- `pass_requires_nonempty_evidence`: every PASS carries non-empty, hashed evidence
- `plan_closure`: 5 planned item(s) each ran exactly once
- `plan_matches_manifest`: the recorded PLAN equals the plan the manifest implies

## WHAT FAILED

Findings:

- none

Checks:

- none

## WHAT ABSTAINED

Findings:

- [invariant:checked_claims_le_invocations] ABSTAIN UNVERIFIED (NARRATED_VERIFICATION): citation-log: claimed_verified vs complete invocation records: 5 claimed but only 2 invoked; citation-log: entries claimed VERIFIED vs entries with a record: 5 claimed but only 2 invoked

Checks:

- `citation-log`: verification_log ABSTAIN (UNVERIFIED), subject records examined 5; NARRATED_VERIFICATION: 3 citation(s) claimed VERIFIED with no complete invocation record: ['C3', 'C4', 'C5']

## WHAT REMAINS UNRESOLVED

- invariant `pass_requires_complete_required_checks` not applicable: the run does not claim PASS
- the receipt is UNSIGNED (receipt.auth.json says so): its content hash detects accidental change, but anyone able to edit the run directory can rewrite and rehash it

## WHAT THIS RESULT DOES NOT PROVE

- Scientific validity: NOT ESTABLISHED. Whether any conclusion holds in its intended domain is outside what this tool can show.
- Integrity (what was established): SHA-256 recorded for 1 of 1 declared input(s); execution ledger sealed at 13 entries; ledger head 07f4d20bab9ee4a6c41f5030aff1ee96eaf9c2094fab6580d2e7930b0b3036c1; evidence manifest ce2659172e7fa581ba572c6634d26472b818ec8a0a03d8c87350795e4188c08a.
- Performance (how the checkers and the declared checks behaved): CHECKER: falsifier witnesses 1 WITNESSED, 0 REFUTED, 0 UNWITNESSED, 0 NO_CASE, 0 NO_GENERATOR (1 falsifier invocation(s)); must-fail/must-pass canary held; comparator self-test held. RUN: Run status ABSTAIN (UNVERIFIED) from 2 check result(s): 1 PASS, 0 FAIL, 1 ABSTAIN, 0 ERROR; 15 applicable invariant(s), 1 violated. This describes how the declared checks behaved on the declared inputs only.
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
