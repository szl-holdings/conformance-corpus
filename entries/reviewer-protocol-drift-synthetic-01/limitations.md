# Limitations: `reviewer-protocol-drift-synthetic-01`

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
- It does not show that the reviewers exist, that they are independent, or that their verdicts are sound. The reviewers are invented names.
- An ABSTAIN here is not a finding that the reviewed work is wrong; it means the review protocol was not completed.

## What this entry does not exercise

- **Protocol completeness only.** Only protocol completeness is exercised.
  Whether ACCEPT was the right verdict is outside the check and outside this
  entry.
- **Identity is a trimmed, case-folded name.** A duplicate that differs by
  more than case and surrounding whitespace, such as a different name for
  the same person, would not be detected.
- **Nothing is authenticated.** The verdicts document is not
  authenticated. Anyone who can edit it can add or remove verdicts.
- **Both defects at once.** The entry combines a missing reviewer and a
  duplicate verdict. Each defect alone is not a separate entry yet.

## Unresolved

- The content of the verdicts (all ACCEPT here) is not judged; the check establishes protocol completeness only.
- Reviewer identity is a name string compared after trimming and case folding. One person recording under two unrelated names, or two people sharing a name, cannot be detected, and the verdicts document is not authenticated.
- A verdict from a reviewer who is not required is listed as evidence but is not exercised here.
- A missing reviewer alone, and a duplicate alone, are not separate entries; this entry combines both.
- report.md prints two different row figures: 'Rows examined in scope: 7' (4 sample rows + 3 verdicts) and the pass_requires_examined_rows line, which sums per-check counts. Neither is asserted here.

## Permissions

- **Access class.** `SYNTHETIC`.
- **Permissions.** Evaluation is allowed. Training, redistribution,
  derivatives, public display and commercial use are **not** allowed,
  because no license has been chosen (`NOASSERTION`).
- **Evaluation is not training.** Permission to evaluate does not imply
  permission to train.
