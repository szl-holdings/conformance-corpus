# Template: omitted-population

Exercises a row that an accepted snapshot vouched for and that is now silently missing: the file's declared digest and row count were refreshed after the deletion, so only the snapshot can notice.

This is a template for one corpus entry. Copy the whole directory to
`entries/<entry-id>/`, then replace every `REPLACE` value. `entry.json` is
already valid against `intake-schema.json` and `permissions-schema.json`, so a
copy stays valid while you fill it in; a finished entry contains no `REPLACE`.

**Intended outcome for this category:** `verify manifest.json` returns FAIL, exit 1, reason SOURCE_MISMATCH, failure mode OMITTED_POPULATION; `snapshot_completeness` FAILs and run.json names the deleted row key.

## Steps

1. Write the accepted rows first, compute each row digest (sha256 of the canonical JSON of `{column: value}`, all values as strings), and write `fixtures/snapshots/accepted.json` (science-gate-snapshot/v1).
2. Delete one accepted row from the CSV. Record the deleted row's values in claim.md so a reviewer can recompute its digest.
3. Declare the CSV's current sha256, and a denominator that cannot see the loss (OBSERVED, counted from the file itself), so only the snapshot check can fail.
4. Fill in `manifest.json`, then `expected-results.json` and `entry.json`, then run and record.

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
