# schemas/ (vacuous-pass-synthetic-01, SYNTHETIC)

- `readings.row.schema.json`: the columns of `fixtures/data/readings.csv` (corpus-authored).
- `stored-summary.schema.json`: the `science-gate-summary/v1` document in
  `fixtures/summary/stored-summary.json` (corpus-authored; science-gate publishes no schema for it).
- `manifest.json` follows `science-gate-manifest/v1`: scientific-evidence-gate
  `schemas/manifest.schema.json`, sha256 `83270fea58e9df8fc67e2accc0a4d62cbfbe922bc37dc4ff1691cd8b2de84e86` at commit
  `7ec36c6bb134`. The manifest validates against it.

## What passing does not prove

- **Scope of a pass.** Reproducing this entry's expected outcome shows conformance on this declared
  synthetic fixture only. That is a performance claim about one declared case.
- **Not shown.** It does not show that the verifier catches failures outside the corpus. It does not
  show that any scientific conclusion is true. It does not show that the verifier is fit for any use.
