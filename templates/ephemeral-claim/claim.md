# ephemeral-claim-synthetic-NN: the claim about the check

> **SYNTHETIC ENTRY.** <GUIDANCE: keep this banner for a synthetic entry. Say
> that every file was generated for this corpus, name the fictional setting,
> and say that no real person, institution, paper or dataset is described.
> Say that the entry is a draft until it has been independently reviewed.>

## Claim under test

The claim is about the **check**, not about the world.

<GUIDANCE: A registered claim printed in the manuscript has no derivation (recipe, code version, environment, input manifest) and/or no stored output. The claim_registry check must ABSTAIN with UNVERIFIED and EPHEMERAL_CLAIM, name the claim and every missing link, and neither pass it nor call it false.>

When `science-gate verify manifest.json` runs on this tree, the outcome must be:

- **Status.** ABSTAIN.
- **Reason.** UNVERIFIED.
- **Exit code.** 2.
- **Failure modes.** `["EPHEMERAL_CLAIM"]`.
- **Report.** `report.md` must mention: <list the must_mention strings>.

## Why this can look like success when it is not

<GUIDANCE: The number matches a registry entry, or a sibling claim traces cleanly, so 'registered' is read as 'verified'. Missing evidence must never become PASS, and never become 'false' either.>

## What passing this entry does not prove

- **Scope of a pass.** Reproducing `expected-results.json` shows conformance
  on this declared fixture only. That is a performance claim about declared
  fixtures.
- **What it does not show.** It does not show scientific validity. It does
  not show that the verifier catches failures outside the corpus, or that
  the tool is fit for any particular use.
