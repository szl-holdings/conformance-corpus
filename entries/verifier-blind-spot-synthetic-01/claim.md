# verifier-blind-spot-synthetic-01: the claim about the check

> **SYNTHETIC ENTRY.** Every file in this entry was generated for this corpus.
> The Brassmoor stations (station-thistle, station-quartz) and their lantern
> readings are fictional. No real station, instrument, person, institution,
> paper or dataset is described. The entry is a draft and has not been
> independently reviewed.

## Claim under test

The claim is about the **mutation harness**, not about the world.

The evidence tree verifies as **PASS**, so the baseline is valid. It
declares three checks:

- `row_count`
- `required_columns`
- `numeric_agreement`, citing records BM-01 and BM-02

It declares **no `duplicate_rows` check**. Its input declares **no
independent row count**. So nothing in the declared evaluation is in a
position to notice that a record appears twice.

When `science-gate mutate manifest.json` runs on this tree, the report must
do all of the following:

1. Execute operator **`M04_duplicate_row`**. It duplicates record BM-04 and
   re-declares the file digest, so that the digest cannot mask the check
   under test.
2. Report that the mutant **verified as PASS**. The expected detector,
   `check:duplicate_rows`, never fired, so M04 is **escaped**
   (`blind_spot: true`).
3. Report overall **FAIL** with reason **BLIND_SPOT**, exit code **1**.
4. Report every other executed operator as detected by its *expected*
   detector. The sensitivity is **8/9**, not rounded up and not hidden.

The blind-spot set must be exactly `[M04_duplicate_row]`.

## Why this can look like success when it is not

The baseline passes. Eight of nine mutations are caught, and a headline
figure of 89% can read as "the verifier works". The one that escaped is a
whole class of defect, duplicated records, that this declared evaluation
cannot see at all. A conforming harness must surface that escape as a FAIL,
not bury it in an average.

## What passing this entry does not prove

- **What a pass shows.** Reproducing the expected result shows only that the
  harness reported this one escape, on **this synthetic fixture**, as
  declared. That is a performance claim about declared fixtures.
- **Other blind spots.** It does not show that the harness finds every blind
  spot, or that a tree with no reported blind spot has no undetected defect
  kinds.
- **Truth.** It does not show that any reading is right or wrong. The data
  are invented, and no scientific validity is established.
- **Fitness.** It does not show that scientific-evidence-gate is fit for any
  particular use.
