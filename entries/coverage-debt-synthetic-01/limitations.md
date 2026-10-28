# coverage-debt-synthetic-01: limitations

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
- It does not show that the readings fall inside or outside the window. No
  observation time was examined.

## Limits of this entry

- **One check kind.** It exercises one empty required check (`time_source`).
  It does not cover other checks that can have nothing to examine: a snapshot
  that accepts no rows, a citations list with no entries, a review file with no
  verdicts.
- **Required checks only.** It does not cover an optional empty check, which is
  shown in the report but does not decide the run.
- **Undeclared document only.** This entry covers a required check whose
  document the manifest does not declare (NOT_DECLARED). A declared document
  with no events (EMPTY_POPULATION) and a missing or malformed one (SKIPPED)
  are different cases, with different outcomes under section 17.7 of the
  science-gate architecture, and are not exercised here.
- **Re-baselined.** On 2026-10-28 the intended outcome changed from ABSTAIN /
  INSUFFICIENT_EVIDENCE with PARTIAL_EXECUTION to ABSTAIN / OUT_OF_SCOPE with
  no failure mode, under section 17.7 (G2). The cross-entry conflicts recorded
  before (with vacuous-pass-synthetic-01 and partial-execution-synthetic-01)
  are settled by that rule. An independent reviewer should still confirm it.
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
