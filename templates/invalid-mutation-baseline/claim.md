# invalid-mutation-baseline-synthetic-NN: the claim about the check

> **SYNTHETIC ENTRY.** <GUIDANCE: keep this banner for a synthetic entry. Say
> that every file was generated for this corpus, name the fictional setting,
> and say that no real person, institution, paper or dataset is described.
> Say that the entry is a draft until it has been independently reviewed.>

## Claim under test

The claim is about the **check**, not about the world.

<GUIDANCE: The untouched evidence tree does not verify as PASS (state exactly why, e.g. one declared expectation disagrees with the stored value). science-gate mutate must report FAIL / INVALID_BASELINE / exit 1, print the verbatim no-sensitivity sentence, omit every count key and the mutations list, and execute no mutation.>

When `science-gate mutate manifest.json` runs on this tree, the outcome must be:

- **Status.** FAIL.
- **Reason.** INVALID_BASELINE.
- **Exit code.** 1.
- **Failure modes.** `[]`.
- **Report.** `mutation-report.md` must mention: <list the must_mention strings>.

## Why this can look like success when it is not

<GUIDANCE: Every mutant of an already-failing tree is 'not PASS', so a naive harness reports 100% sensitivity for a verifier that rejects good evidence too.>

## What passing this entry does not prove

- **Scope of a pass.** Reproducing `expected-results.json` shows conformance
  on this declared fixture only. That is a performance claim about declared
  fixtures.
- **What it does not show.** It does not show scientific validity. It does
  not show that the verifier catches failures outside the corpus, or that
  the tool is fit for any particular use.
