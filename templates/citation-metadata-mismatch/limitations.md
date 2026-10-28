# REPLACE-ENTRY-ID: limitations

<!-- Guidance: keep the SYNTHETIC banner for synthetic entries. -->

> **SYNTHETIC.** Every file in this entry was generated for this corpus. The names, sites, values, works, authors, journals and DOIs (all under the 10.5555 test prefix) are invented. Nothing here describes real people, institutions, papers or datasets.

## What passing does not prove

Reproducing `expected-results.json` shows **conformance on declared fixtures only**:
science-gate produced the declared outcome on these synthetic fixtures, with the
tool version recorded in `environment.lock`.

- It does not show that science-gate catches this failure outside this entry.
- It does not establish scientific validity. The data is invented, so no
  scientific conclusion is supported or refuted.
- It does not show that science-gate, or any pipeline that uses it, is fit for
  any particular use.

## Limits of this entry

- REPLACE: what this entry exercises only narrowly (one defect, one layout,
  one tool version).
- REPLACE: anything that was not examined (for example no live network lookup).
- It was written by one author and has not been independently reviewed. It is
  a draft until `provenance.reviewed_by` names an independent reviewer.
- The corpus is a fixture collection, not a benchmark.

## Status

- Category: `citation-metadata-mismatch`.
- License: none chosen (`NOASSERTION`). Permissions: evaluation only.
