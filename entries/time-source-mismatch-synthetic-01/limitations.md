# Limitations: `time-source-mismatch-synthetic-01`

> **SYNTHETIC.** Every file in this entry was generated for the conformance corpus. The names, sites, reviewers, values and dates are invented, and no real person, institution, paper or data set is involved. **Passing shows conformance on declared fixtures only. It does not show scientific validity or fitness for use.**

## Synthetic status

- **Origin.** Every data file here was generated for this corpus, and
  every name is invented.
- **Numbers and dates.** The numbers and dates mean nothing. No real
  measurement, study, reviewer or institution is involved.
- **Review status.** The entry is a draft. `provenance.reviewed_by` is
  empty, and nobody other than its author has reviewed it.

## What passing does not prove

- Passing this entry shows only that a verifier produced the declared outcome (status, exit code, reason, failure modes and required report strings) on these declared SYNTHETIC fixtures. It is a conformance result on declared fixtures only.
- It does not show that the verifier catches this failure outside this corpus, in other data, or when the failure takes another form.
- It does not show that any scientific conclusion is true or false. The data, the study and the conclusion here are invented and mean nothing.
- It does not show that the verifier, or anything checked with it, is fit for any particular use.
- It does not show that the declared offsets are the true local offsets, or that any clock was accurate. The offsets are taken as declared.
- It does not show that the readings themselves are correct or meaningful.

## What this entry does not exercise

- **What is exercised.** Only the window comparison after normalization is
  exercised.
- **Consistent records only.** The local time, the offset and the UTC are
  consistent with one another. A record in which they disagree is a
  separate case and is not included.
- **Offsets are taken as declared.** Nothing here checks that -04:00 was
  the true offset at the (invented) observing place, or that any logger
  clock was right.
- **Fixed offsets only.** science-gate accepts only fixed offsets and
  `UTC`/`Z`. Named zones are not resolved, and this entry does not test
  them.

## Unresolved

- A disagreement between local time, offset and recorded UTC (UTC_MISMATCH) is not exercised; here the three agree and only the window is violated.
- Named zones such as Region/City (ABSTAIN, REQUIRES_HUMAN_REVIEW), missing timezones and missing UTC values (ABSTAIN, INSUFFICIENT_EVIDENCE) are not exercised.
- An observation exactly on a window boundary is not exercised.
- Whether the recorded offset was the true offset at the observing location is not checked by anything; the offset is taken as declared.
- report.md prints two different row figures: 'Rows examined in scope: 6' (3 reading rows + 3 events) and the pass_requires_examined_rows line, which sums per-check counts. Neither is asserted here.

## Permissions

- **Access class.** `SYNTHETIC`.
- **Permissions.** Evaluation is allowed. Training, redistribution,
  derivatives, public display and commercial use are **not** allowed,
  because no license has been chosen (`NOASSERTION`).
- **Evaluation is not training.** Permission to evaluate does not imply
  permission to train.
