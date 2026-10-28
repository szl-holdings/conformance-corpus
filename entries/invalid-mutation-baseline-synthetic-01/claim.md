# invalid-mutation-baseline-synthetic-01: the claim about the check

> **SYNTHETIC ENTRY.** Every file in this entry was generated for this corpus.
> The Cobblewick canal, its reaches and its depth gauges are fictional. No
> real canal, gauge, person, institution, paper or dataset is described. The
> entry is a draft and has not been independently reviewed.

## Claim under test

The claim is about the **mutation harness**, not about the world.

Mutation testing injects known defects into copies of an *accepting*
evidence tree. It then counts how many of those defects the verifier
catches. That count means something only if the verifier accepts the
untouched tree first.

In this tree the untouched copy does **not** verify. The manifest declares
that gauge `CW-03` reads `97.51` cm. The stored data say `97.15`, a
transposed digit, so the `numeric_agreement` check `depth` FAILs with
SOURCE_MISMATCH.

When `science-gate mutate manifest.json` runs on this tree, the mutation
report must do all of the following:

1. Report **FAIL** with reason **INVALID_BASELINE**, exit code **1**.
2. Print, verbatim: "No sensitivity figure was produced because the
   verifier failed its accepting baseline."
3. Show the baseline's failing finding: `check:depth`, SOURCE_MISMATCH,
   `CW-03`.
4. Carry **no** sensitivity figure. It must **omit every count key**
   (`applicable_mutations`, `executed_mutations`, `detected_mutations`,
   `escaped_mutations`, `skipped_mutations`, `not_applicable_mutations`)
   and the `mutations` list, and execute no mutation.

## Why this can look like success when it is not

A naive harness would run every operator anyway. Every mutant of an
already-failing tree is "not PASS", so every mutation would look detected,
and the harness would report 100% sensitivity. That figure would describe a
verifier that rejects everything, including good evidence. It says nothing
about whether it rejects bad evidence for the right reason.

## What passing this entry does not prove

- **What a pass shows.** Reproducing the expected result shows only that the
  harness behaved as declared on **this synthetic fixture**. That is a
  performance claim about declared fixtures.
- **Other baselines.** It does not show correct handling of every kind of
  invalid baseline, such as ABSTAIN, ERROR or other FAIL causes.
- **Real sensitivity.** It does not show that sensitivity figures are
  meaningful when a baseline does pass.
- **Truth.** It does not show that any gauge value is right or wrong. The
  data are invented, and no scientific validity is established.
- **Fitness.** It does not show that scientific-evidence-gate is fit for any
  particular use.
