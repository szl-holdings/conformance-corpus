# Template: partial-execution

**Category.** a required check never reached a terminal state (intake `failure_mode`: `PARTIAL_EXECUTION`).

This directory holds every file of the entry layout, with placeholders. To make an entry:

1. Copy this directory to `entries/<ENTRY_ID>/` (for example `entries/partial-execution-synthetic-02/`) and
   delete this README.md from the copy.
2. Generate the fixtures under `fixtures/` and describe any format they use under `schemas/`.
3. Fill `manifest.json` (science-gate-manifest/v1; paths relative to the entry directory) and put each
   fixture's sha256 in it.
4. Fill `expected-results.json` and `entry.json` `expected_outcome` with the **intended** outcome.
5. Run science-gate as `evaluation/README.md` describes, with `--output` in a temporary directory
   outside the entry. Copy `report.md` and `run.json` into `evaluation/`, the receipt into `receipts/`,
   and replace local paths with `<tmp>`, `<entry>`, `<SEG>` and `<python>`. Fill `environment.lock`.
6. Compare. Record every difference in `entry.json` `known_failures`; never edit the expected outcome
   to match a run.
7. Leave `provenance.reviewed_by` empty. Only an independent reviewer adds a name, with a record in
   `review/`.

## Guidance for partial-execution

- **Defect.** A run declares required checks, and at least one of them never ran to completion, yet
  the run's own tally ("3 passed, 0 failed") looks complete.
- **What science-gate verify can be given.** It cannot ingest an external execution ledger, so a
  literally unterminated invocation cannot be presented to `verify`. Approximate the category with a
  required check that cannot execute because the stage producing its evidence never completed: declare
  the evidence path (e.g. `time_sources`) and leave the file absent, with a `README.md` beside it
  saying so. Make every other required check pass, so the unexecuted check is the only defect.
- **Conforming outcome.** ABSTAIN (exit 2), failure mode PARTIAL_EXECUTION, and a report stating
  `checks_executed=<N> of checks_expected=<M>`. Never FAIL: nothing was contradicted.
- **Observed on `partial-execution-synthetic-01` (science-gate 0.1.0, commit 7ec36c6).** Status, exit
  code, failure modes and strings matched, but the primary reason was INSUFFICIENT_EVIDENCE (the
  skipped check's own finding precedes the contract's PARTIAL_EXECUTION finding), and the invariant
  `every_required_check_has_terminal_state` held because SKIPPED counts as terminal there. Record such
  differences in `known_failures`; do not change the intended outcome.

## Rules for every entry made from this template

- **Synthetic by default.** Generate the data yourself. Use obviously fictional names, DOIs under
  `10.5555` only, and never real people, institutions, papers or datasets. Real artifacts need a
  confirmed permission grant first (see `permissions-schema.json`).
- **Small.** Keep each entry to a few kilobytes of fixtures.
- **Write the intended outcome first.** Fill `expected-results.json` from the category's intent
  *before* running science-gate. Never edit it to match a run. If the run differs, record the
  difference in `entry.json` `known_failures` (and `unresolved_cases` if the right answer is disputed).
- **Never convert missing evidence into PASS.** A conforming outcome for these categories is never PASS.
- **Permissions are explicit.** Evaluation permission does not imply training permission. With
  `evidence_of_grant: NOASSERTION`, every flag other than `evaluation_allowed` must be false.
- **No license is chosen** for the corpus (`NOASSERTION`). Do not invent one.
- **Say what passing does not prove** in every file that describes the entry. `manifest.json` cannot
  carry prose (science-gate refuses unknown keys), so it is the one exception.
- **Replace every `<...>` placeholder.** `grep -rn '<[A-Z]' <entry>` must print nothing but the
  recorded `<tmp>`, `<entry>`, `<SEG>` and `<python>` path tokens.

## What passing does not prove

- **Scope of a pass.** Reproducing an entry's expected outcome shows conformance on that declared
  fixture only. That is a performance claim about one declared case.
- **Not shown.** It does not show that the verifier catches failures outside the corpus. It does not
  show that any scientific conclusion is true. It does not show that the verifier is fit for any use.
