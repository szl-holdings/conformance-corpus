# omitted-population-synthetic-01: limitations

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
- It does not show that rows never accepted into the snapshot are complete. An
  OBSERVED row count cannot reveal a loss, and the snapshot vouches only for
  the rows it accepted.

## Limits of this entry

- **One deletion only.** It exercises one deleted row in a fully parsed CSV.
  It does not exercise a deletion inside a PARTIAL input, where the correct
  outcome is ABSTAIN because the row may be among the unexamined records. It
  also does not exercise a snapshot without a row key, or several deletions.
- **The snapshot is trusted as given.** Nothing here checks how it was
  produced or whether it was right to accept those rows.
- **The row count cannot be witnessed (2026-10-28).** `specimens` declares an
  OBSERVED-only `expected_rows`. Under decisions D2 and 17.5 of the
  science-gate architecture a row_count PASS needs a falsifier witness, and
  row_count's only case (drop-last-row) needs an INDEPENDENT expectation, so
  the check `rows` is ABSTAIN / BLIND_SPOT with VACUOUS_PASS. The intended
  failure modes became [OMITTED_POPULATION, VACUOUS_PASS] and the pinned
  snapshot line took the G1 wording "subject records examined 5"; both
  updates were owner-approved on 2026-10-28. The repaired-fixture control now
  ABSTAINs for the same reason (see `evaluation/control.json`).
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
