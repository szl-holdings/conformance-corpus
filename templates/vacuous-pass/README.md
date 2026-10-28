# Template: vacuous-pass

**Category.** a check reports success over zero examined rows (intake `failure_mode`: `VACUOUS_PASS`).

This directory holds every file of the entry layout, with placeholders. To make an entry:

1. Copy this directory to `entries/<ENTRY_ID>/` (for example `entries/vacuous-pass-synthetic-02/`) and
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

## Guidance for vacuous-pass

- **Defect.** Something reported success although nothing was examined: an input with a header and no
  records, an empty JSON list, a filter that excluded every row, a check whose scope was empty.
- **Make the success explicit.** The strongest fixture pairs the empty population with a stored claim
  of success, e.g. a `summary_claim` (`science-gate-summary/v1`) that says `PASS` and pins the empty
  input with `rows: 0`.
- **Do not declare `expected_rows > 0` with an INDEPENDENT source.** That turns the case into
  omitted-population (a closure failure, FAIL). A vacuous pass has no contradiction, so the conforming
  status is ABSTAIN (exit 2), reason INSUFFICIENT_EVIDENCE, failure mode VACUOUS_PASS.
- **Observed on `vacuous-pass-synthetic-01` (science-gate 0.1.0, commit 7ec36c6).** Status, exit code
  and reason matched. science-gate also added PARTIAL_EXECUTION (it counts NOT_APPLICABLE required
  checks as not executed), and it counted the summary check's one pin comparison as a row examined,
  so its report said "Rows examined in scope: 1" for an input with zero records. Decide your intended
  outcome from the category, not from that behavior, and record any difference in `known_failures`.

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
