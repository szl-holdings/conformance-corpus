# omitted-population-synthetic-01: claim

> **SYNTHETIC.** Every file in this entry was generated for this corpus. The names, sites, values, works, authors, journals and DOIs (all under the 10.5555 test prefix) are invented. Nothing here describes real people, institutions, papers or datasets.

Category: `omitted-population`: a row accepted earlier is silently missing.

## Claim about the check

The snapshot `fixtures/snapshots/accepted.json` accepted six specimen rows. The
current export `fixtures/specimens.csv` has five. Row `OP-0004` is gone, and
nothing else points to the loss:

- the manifest's `sha256` is the digest of the shortened file, so the digest
  check agrees;
- `expected_rows` is 5 with `denominator_source` OBSERVED (it was counted from
  the file itself), so row closure cannot be enforced;
- the remaining rows have the right columns and no duplicates.

The claim is that `science-gate verify manifest.json` still returns **FAIL,
exit 1, reason SOURCE_MISMATCH, failure mode OMITTED_POPULATION**. The
`snapshot` check (`snapshot_completeness`) should FAIL and report
"1 accepted row(s) were deleted", and run.json should name the key `OP-0004`.
`rows`, `columns` and `duplicates` should PASS, and report.md should say that
row closure was not evaluated (OBSERVED).

## The deleted row (so a reviewer can recompute its digest)

`specimen_id=OP-0004, plot=plot-fictus-2, mass_mg=0.3` (all values are
strings). Its digest in the snapshot is the sha256 of the canonical JSON
`{"mass_mg":"0.3","plot":"plot-fictus-2","specimen_id":"OP-0004"}`.

It was also the smallest value in the invented data. Silently losing it would
move any summary of the plot, which is why a silent omission matters even
when every other check agrees.

## What would falsify the claim

- PASS, ABSTAIN or ERROR
- an exit code other than 1
- OMITTED_POPULATION missing from the failure modes
- the missing row reported as changed rather than deleted
- no `OP-0004` in run.json
- a report.md that omits a `must_mention` string in `expected-results.json`

## What passing does not prove

Reproducing `expected-results.json` shows **conformance on declared fixtures only**:
science-gate produced the declared outcome on these synthetic fixtures, with the
tool version recorded in `environment.lock`.

- It does not show that science-gate catches this failure outside this entry.
- It does not establish scientific validity. The data is invented, so no
  scientific conclusion is supported or refuted.
- It does not show that science-gate, or any pipeline that uses it, is fit for
  any particular use.
- It does not show that rows never accepted into the snapshot are complete.
  The snapshot vouches only for the rows it accepted.
