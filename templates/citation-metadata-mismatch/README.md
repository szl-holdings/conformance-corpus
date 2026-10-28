# Template: citation-metadata-mismatch

Exercises a citation whose frozen resolver metadata disagrees with the cited author list or DOI, while the verification log claims every citation VERIFIED and backs each claim with an invocation record.

This is a template for one corpus entry. Copy the whole directory to
`entries/<entry-id>/`, then replace every `REPLACE` value. `entry.json` is
already valid against `intake-schema.json` and `permissions-schema.json`, so a
copy stays valid while you fill it in; a finished entry contains no `REPLACE`.

**Intended outcome for this category:** `verify manifest.json` returns FAIL, exit 1, reason SOURCE_MISMATCH, failure mode SOURCE_MISMATCH; `citation_metadata` (and, when the cited DOI reaches a work with another DOI, `citation_resolver`) FAILs and report.md names the defect (e.g. AUTHOR_MISMATCH, DOI_WORK_MISMATCH, DOI_TARGET_MISMATCH) and the citation.

## Steps

1. Write `fixtures/citations/entries.json` (science-gate-citations/v1), `fixtures/citations/frozen.json` (science-gate-citations-frozen/v1) and `fixtures/citations/verification-log.json` (science-gate-verification-log/v1). See `fixtures/README.md`.
2. Make the log structurally honest (every VERIFIED claim has a complete invocation record), so only the metadata layer can catch the defect.
3. Avoid accidental CONFLATED_ENTRY: a defective citation's DOI, title and author set must not each match different frozen works unless conflation is what you mean to test.
4. Add a small CSV input with an INDEPENDENT `expected_rows` and its `sha256` so the run is otherwise complete.
5. Fill in `manifest.json`, then `expected-results.json` and `entry.json`, then run and record.

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
