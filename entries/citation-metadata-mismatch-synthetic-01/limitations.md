# citation-metadata-mismatch-synthetic-01: limitations

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
- It does not show that any citation outside this entry is correct, or that a
  live resolver would return what the frozen capture records.

## Limits of this entry

- **One defect of each kind.** It exercises one author-set mismatch and one DOI
  target mismatch. It does not exercise conflated entries, author-order
  differences, given-name initials or year, journal, volume and issue
  mismatches.
- **Frozen capture only.** The frozen capture is taken as given. Nothing is
  resolved live, and the capture was invented, so it says nothing about any
  real resolver.
- **Only the stated fields are compared.** The check compares the fields it
  declares. A citation can match every one of them and still be the wrong
  source for the claim it supports. Nothing here checks that.
- **One tool version.** The recorded run used the science-gate version and
  commit in `environment.lock`.
- **Unreviewed draft.** It was written by one author and has not been
  independently reviewed (`provenance.reviewed_by` is empty).
- **Not a benchmark.** The corpus is a fixture collection.

## Status

- **Synthetic.** Every file is generated.
- **License.** None chosen (`NOASSERTION`).
- **Permissions.** Evaluation only. Training, redistribution, derivatives,
  public display and commercial use are not permitted.
