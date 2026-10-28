# schemas: invalid-mutation-baseline-synthetic-01

> **SYNTHETIC.** Every file here was generated for this corpus. All names,
> places and values are invented. No real person, institution, paper,
> dataset or DOI appears.

The entry defines no schema of its own. Its files follow the formats of
scientific-evidence-gate, and the authoritative schema files live in that
repository. They are referenced here by path and digest, not copied. That
keeps the entry small, and it avoids a second copy drifting from the tool's
contract. The digests are those of the files at the commit recorded in
`environment.lock`.

| entry file | format | schema in scientific-evidence-gate | sha256 |
|---|---|---|---|
| `manifest.json` | `science-gate-manifest/v1` | `schemas/manifest.schema.json` | `83270fea58e9df8fc67e2accc0a4d62cbfbe922bc37dc4ff1691cd8b2de84e86` |

`entry.json` follows the corpus's own `intake-schema.json` and
`permissions-schema.json`, which are at the corpus root.

## What passing this entry does not prove

- **Scope of a pass.** Reproducing `expected-results.json` shows conformance
  on this declared, synthetic fixture only.
- **What it does not show.** It does not show scientific validity. It does
  not show that the verifier catches failures outside the corpus, or that
  the tool is fit for any particular use.
