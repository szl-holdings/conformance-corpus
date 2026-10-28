# schemas/ (partial-execution-synthetic-01, SYNTHETIC)

- `samples.row.schema.json`: the columns of `fixtures/data/samples.csv` (corpus-authored).
- The absent file `fixtures/time/events.json` would have followed `science-gate-time-sources/v1`
  (`{schema, window: {start, end}, events: [{id, local_time, timezone, utc, source}]}`), as read from
  science-gate's `time_source` check. science-gate publishes no JSON Schema for it, and none is needed
  here because the file is deliberately missing.
- `manifest.json` follows `science-gate-manifest/v1`: scientific-evidence-gate
  `schemas/manifest.schema.json`, sha256 `83270fea58e9df8fc67e2accc0a4d62cbfbe922bc37dc4ff1691cd8b2de84e86` at commit
  `7ec36c6bb134`. It validates.

## What passing does not prove

- **Scope of a pass.** Reproducing this entry's expected outcome shows conformance on this declared
  synthetic fixture only. That is a performance claim about one declared case.
- **Not shown.** It does not show that the verifier catches failures outside the corpus. It does not
  show that any scientific conclusion is true. It does not show that the verifier is fit for any use.
