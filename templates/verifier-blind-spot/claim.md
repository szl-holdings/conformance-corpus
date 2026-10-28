# verifier-blind-spot-synthetic-NN: the claim about the check

> **SYNTHETIC ENTRY.** <GUIDANCE: keep this banner for a synthetic entry. Say
> that every file was generated for this corpus, name the fictional setting,
> and say that no real person, institution, paper or dataset is described.
> Say that the entry is a draft until it has been independently reviewed.>

## Claim under test

The claim is about the **check**, not about the world.

<GUIDANCE: The tree verifies as PASS (a valid baseline), but its declared checks cannot see one defect class that a mutation operator injects (state which operator and why). science-gate mutate must execute that operator, report it as escaped (blind_spot true), and report FAIL / BLIND_SPOT / exit 1; every other executed operator must be detected by its expected detector.>

When `science-gate mutate manifest.json` runs on this tree, the outcome must be:

- **Status.** FAIL.
- **Reason.** BLIND_SPOT.
- **Exit code.** 1.
- **Failure modes.** `[]`.
- **Report.** `mutation-report.md` must mention: <list the must_mention strings>.

## Why this can look like success when it is not

<GUIDANCE: The baseline passes and most mutations are caught, so a high sensitivity reads as 'the verifier works'. One escape is a whole defect class the declared evaluation cannot see and must surface as FAIL.>

## What passing this entry does not prove

- **Scope of a pass.** Reproducing `expected-results.json` shows conformance
  on this declared fixture only. That is a performance claim about declared
  fixtures.
- **What it does not show.** It does not show scientific validity. It does
  not show that the verifier catches failures outside the corpus, or that
  the tool is fit for any particular use.
