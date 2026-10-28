# fixtures: ephemeral-claim-synthetic-NN

> **SYNTHETIC.** <GUIDANCE: say that every file here was generated for this
> corpus and that all names and values are invented.>

Place the entry's data here. Paths in `manifest.json` are relative to the
entry directory, so they read `fixtures/...`. Keep every file small.

| file | what it is | sha256 |
|---|---|---|
| `fixtures/data/<input>.csv` | the declared input (synthetic rows, invented identifiers) | `<sha256>` |
| `fixtures/claims/registry.json` | science-gate-claims/v1 registry: at least one ephemeral claim; optionally a fully traced sibling claim | `<sha256>` |
| `fixtures/claims/manuscript.md` | the manuscript; every number in it must be a registered claim value (or a digest-pinned not_claims exemption), so that the ephemeral claim is the only finding | `<sha256>` |
| `fixtures/outputs/<stored-output>.json` | stored output of any fully traced claim, with its sha256 pinned in the registry | `<sha256>` |

## What passing this entry does not prove

- **Scope of a pass.** Reproducing `expected-results.json` shows conformance
  on this declared fixture only. That is a performance claim about declared
  fixtures.
- **What it does not show.** It does not show scientific validity. It does
  not show that the verifier catches failures outside the corpus, or that
  the tool is fit for any particular use.
