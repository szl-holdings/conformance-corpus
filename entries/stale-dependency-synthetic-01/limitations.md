# Limitations: `stale-dependency-synthetic-01`

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
- It does not show that the changed design makes the conclusion wrong. STALE_PENDING_REVALIDATION means only that an upstream artifact changed after the conclusion was last established.
- A matching digest for the conclusion shows only byte identity, not that it was regenerated or that the analysis behind it is correct.

## What this entry does not exercise

- **Kind of change.** Only one kind of change is exercised: a DESIGN file
  whose bytes differ from its recorded digest. A changed SOURCE_SNAPSHOT,
  a missing node file (UNRESOLVED) and a node with no recorded digest are
  not exercised.
- **Declared edges only.** Staleness can only follow edges the graph
  declares. A conclusion that silently depends on an undeclared artifact
  would not be caught, and this entry does not test that.
- **Commands.** Only `verify` is exercised. `impact` and `revalidate` write
  `graph-state.json` next to the graph and are not run against the entry.
- **Invented numbers.** The numbers (19.25 and the rest) are invented.
  Nothing here says whether a count threshold of 5 or 8 is appropriate for
  anything.

## Unresolved

- Only verify is exercised. impact and revalidate write graph-state.json beside the graph, so running them here would modify the entry; they must be run on a copy and are not part of this entry.
- Early cutoff (revalidating a node to an unchanged digest and clearing its descendants) is not exercised.
- A dependency that graph.json does not declare cannot make anything stale. This entry does not test that blind spot.
- report.md prints two different row figures: 'Rows examined in scope: 10' (6 plot rows + 4 graph nodes) and the pass_requires_examined_rows line 'rows_examined=16' (the per-check counts summed). Neither is asserted by this entry.

## Permissions

- **Access class.** `SYNTHETIC`.
- **Permissions.** Evaluation is allowed. Training, redistribution,
  derivatives, public display and commercial use are **not** allowed,
  because no license has been chosen (`NOASSERTION`).
- **Evaluation is not training.** Permission to evaluate does not imply
  permission to train.
