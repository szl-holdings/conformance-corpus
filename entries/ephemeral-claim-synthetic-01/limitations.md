# ephemeral-claim-synthetic-01: limitations

> **SYNTHETIC ENTRY.** All data, names and values were invented for this
> corpus. The setting (Glassreed Fen, plot-umber, plot-verdigris,
> plot-cinnabar, "mooncress sprites") is fictional. No DOI, real person,
> institution, paper or dataset appears. This entry is a draft with no
> independent review (`provenance.reviewed_by` is empty).

## What passing this entry does not prove

- **Only this fixture.** A verifier that reproduces `expected-results.json`
  has shown conformance on this one declared, synthetic fixture. It has not
  shown scientific validity, and it has not shown fitness for any use.
- **No generalisation.** It has not shown that the verifier detects
  ephemeral claims outside this fixture.
- **Nothing about the numbers.** It has not shown that CLM-01 or CLM-02, or
  any real-world number, is correct or incorrect.
- **Presence, not re-execution.** The tool checks the derivation links of
  CLM-01 only for presence (DECLARED). It re-hashes the stored output but
  never re-runs the analysis. So a pass does not show that the recipe, code
  or environment named for CLM-01 would reproduce 40.00.

## Scope limits of the fixture

- **One ephemeral claim.** It has no derivation fields and no stored output
  at all. Partial derivations (one link missing) are not covered.
- **Two numbers only.** The manuscript is five lines of Markdown with two
  numbers, and it has no `not_claims` exemptions. Tables, footnotes,
  separators, ranges and exponents are not exercised.
- **One number format.** The claim registry check runs with the default
  number format: decimal point `.` and no thousands separator.
- **Offline.** Every run is offline. No live lookup is involved.
- **Recorded on one platform.** Expected results were confirmed on Windows,
  with CPython 3.11.9 and scientific-evidence-gate 0.1.0 at the commit in
  `environment.lock`. Other platforms have not been run.

## Permissions

- **Access class.** SYNTHETIC.
- **What is allowed.** Evaluation is allowed. Training, redistribution,
  derivatives, public display and commercial use are **not** allowed.
- **No license yet.** No license has been chosen (`NOASSERTION`), so no
  grant exists beyond local evaluation.
- **Evaluation is not training.** Evaluation permission does not imply
  training permission.
