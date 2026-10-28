# ephemeral-claim-synthetic-01: the claim about the check

> **SYNTHETIC ENTRY.** Every file in this entry was generated for this corpus.
> The Glassreed Fen, its plots and its "mooncress sprites" are fictional. No
> real survey, place, organism, person, institution, paper or dataset is
> described. The entry is a draft and has not been independently reviewed.

## Claim under test

The claim is about the **check**, not about the world.

A manuscript prints two numbers, and the claim registry lists both.

- **CLM-01 (40.00)** is fully traced. It has an analysis recipe, a code
  version, an environment, an input-manifest digest, and a stored output
  whose SHA-256 is pinned and whose value agrees.
- **CLM-02 (91)** has **no derivation and no stored output**. The number
  exists in the text and in the registry, and nowhere durable.

When `science-gate verify manifest.json` runs on this tree, the
`claim_registry` check must do all of the following:

1. Report **ABSTAIN** with reason **UNVERIFIED** and failure mode
   **EPHEMERAL_CLAIM**.
2. Name `CLM-02`, and list every missing link: ANALYSIS_RECIPE,
   CODE_VERSION, ENVIRONMENT, INPUT_MANIFEST and STORED_OUTPUT.
3. Neither pass CLM-02 nor call it false. Missing evidence is not evidence
   of falsehood, and it is never a PASS.

The run as a whole must then be **ABSTAIN / UNVERIFIED**, exit code **2**,
with failure modes exactly `[EPHEMERAL_CLAIM]`. This holds even though every
other check passes and CLM-01 resolves.

## Why this can look like success when it is not

An implementation can go wrong in two tempting ways.

- **Treating the number as verified.** It matches a registry entry, so
  "registered" gets read as "verified".
- **Letting the sibling claim carry the file.** CLM-01 traces cleanly, and
  every input check is green.

The value 91 even equals the sum of the synthetic `sightings` column. A
checker that re-derived the number by guesswork might be tempted to credit
it. Nothing durable says how 91 was produced, so the only honest outcome is
UNVERIFIED.

## What passing this entry does not prove

- **What a pass shows.** Reproducing the expected result shows only that the
  verifier behaved as declared on **this synthetic fixture**. That is a
  performance claim about declared fixtures.
- **Other inputs.** It does not show that ephemeral claims are caught in
  other manuscripts, registry shapes or number formats.
- **Truth.** It does not show that any number here, or any scientific
  conclusion anywhere, is true or false. The data are invented.
- **Fitness.** It does not show that scientific-evidence-gate is fit for any
  particular use.
