# Template: coverage-debt

Exercises a required check that ran but had nothing to look at (for example a time_source check whose events list is empty). A gate that counts 'no failures' as success would PASS; the check must instead be NOT_APPLICABLE, which is never PASS.

This is a template for one corpus entry. Copy the whole directory to
`entries/<entry-id>/`, then replace every `REPLACE` value. `entry.json` is
already valid against `intake-schema.json` and `permissions-schema.json`, so a
copy stays valid while you fill it in; a finished entry contains no `REPLACE`.

**Intended outcome for this category:** `verify manifest.json` returns ABSTAIN, exit 2, reason INSUFFICIENT_EVIDENCE; the empty check is NOT_APPLICABLE with verdict ABSTAIN and 0 rows examined, and it is not counted as executed, so checks_executed < checks_expected (failure mode PARTIAL_EXECUTION).

**Disputed, not settled.** This intended outcome conflicts with two other entries. vacuous-pass-synthetic-01 expects NOT_APPLICABLE required checks not to add PARTIAL_EXECUTION. partial-execution-synthetic-01 expects PARTIAL_EXECUTION, not INSUFFICIENT_EVIDENCE, as the primary reason for a run with the same reasons. See `unresolved_cases` in `entries/coverage-debt-synthetic-01/entry.json`. Until a reviewer settles one rule, record the dispute in each new entry's `unresolved_cases`.

## Steps

1. Give the run real data that the other checks can PASS on (a CSV with an INDEPENDENT row count and its sha256), so the empty check is the only finding.
2. Declare the empty check as required, with a document that exists and parses but holds nothing to examine (e.g. `{"events": []}` for time_source).
3. Fill in `manifest.json`, then `expected-results.json` and `entry.json`, then run and record.

## Rules

- Synthetic data only unless permission is confirmed. Use obviously fictional
  names and DOIs under `10.5555` only. Never real people, institutions, papers
  or datasets.
- Write `expected-results.json` from the entry's intent **before** running
  science-gate. If the tool does not produce it, keep the intended values, add
  the difference to `known_failures` in `entry.json`, and say so in
  `expected-results.json` `notes`. Never edit the tool to make an entry pass.
- Missing evidence is never PASS.
- Keep the entry small (a few KB).
- Do not choose a license (`NOASSERTION`).

## What passing does not prove

It shows conformance on declared fixtures only. It does not show scientific
validity or fitness for use.
