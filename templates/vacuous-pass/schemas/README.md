# schemas/ (template: vacuous-pass)

<LIST EVERY FORMAT THE FIXTURES USE.> For a format science-gate publishes a schema for
(`schemas/manifest.schema.json`, `schemas/citations.schema.json`, ...), cite the file and its sha256 at
the recorded commit instead of copying it. For a format it does not publish (for example
`science-gate-summary/v1`, `science-gate-time-sources/v1`, a CSV's columns), add a small
corpus-authored JSON Schema here and say that it is not an official science-gate schema.

## What passing does not prove

- **Scope of a pass.** Reproducing an entry's expected outcome shows conformance on that declared
  fixture only. That is a performance claim about one declared case.
- **Not shown.** It does not show that the verifier catches failures outside the corpus. It does not
  show that any scientific conclusion is true. It does not show that the verifier is fit for any use.
