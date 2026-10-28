# schemas/ (narrated-verification-synthetic-01, SYNTHETIC)

- `observations.row.schema.json`: the columns of `fixtures/data/observations.csv` (corpus-authored).
- `fixtures/citations/entries.json` (`science-gate-citations/v1`) and
  `fixtures/citations/verification-log.json` (`science-gate-verification-log/v1`) follow
  scientific-evidence-gate `schemas/citations.schema.json`, sha256
  `126e26118ef5cfa15733cd113cd3242e5dfe3c0c1c1c1a2c9072e9e17cb5f760` at commit `7ec36c6bb134`. Both validate against it.
- `manifest.json` follows `science-gate-manifest/v1`: scientific-evidence-gate
  `schemas/manifest.schema.json`, sha256 `83270fea58e9df8fc67e2accc0a4d62cbfbe922bc37dc4ff1691cd8b2de84e86`. It validates.

## What passing does not prove

- **Scope of a pass.** Reproducing this entry's expected outcome shows conformance on this declared
  synthetic fixture only. That is a performance claim about one declared case.
- **Not shown.** It does not show that the verifier catches failures outside the corpus. It does not
  show that any scientific conclusion is true. It does not show that the verifier is fit for any use.
