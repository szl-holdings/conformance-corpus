# schemas: invalid-mutation-baseline-synthetic-NN

List every format the fixtures use. Reference each schema of
scientific-evidence-gate by path and SHA-256 at the commit in
`environment.lock`, for example `schemas/manifest.schema.json`. Copy a
schema here only if the entry defines its own.

| entry file | format | schema | sha256 |
|---|---|---|---|
| `manifest.json` | `science-gate-manifest/v1` | `schemas/manifest.schema.json` (in scientific-evidence-gate) | `<sha256>` |

## What passing this entry does not prove

- **Scope of a pass.** Reproducing `expected-results.json` shows conformance
  on this declared fixture only. That is a performance claim about declared
  fixtures.
- **What it does not show.** It does not show scientific validity. It does
  not show that the verifier catches failures outside the corpus, or that
  the tool is fit for any particular use.
