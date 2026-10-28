# fixtures: ephemeral-claim-synthetic-01

> **SYNTHETIC.** Every file here was generated for this corpus. All names,
> places and values are invented. No real person, institution, paper,
> dataset or DOI appears.

The data the entry's `manifest.json` points at. Paths in the manifest are
relative to the entry directory. `.gitattributes` at the entry root stops
Git from converting line endings, so each file keeps the exact bytes its
digest covers.

| file | what it is | sha256 |
|---|---|---|
| `fixtures/data/tallies.csv` | five invented sprite tallies at three fictional plots (the `tallies` input) | `6a717a23dd44026f8220481a66c60fc665609792a532a273f153672b270dc573` |
| `fixtures/claims/registry.json` | claim registry (science-gate-claims/v1): CLM-01 fully traced, CLM-02 with no derivation and no stored output | `6ae9dd3332836b210975ec88c833e433294562a8bc833d9107a29b5789ad454a` |
| `fixtures/claims/manuscript.md` | the manuscript whose two numbers are CLM-01 and CLM-02 | `b1296ea071057b243b174d9bb5bedfb7a4b326af5f2f0448ad5e1769688f7c96` |
| `fixtures/claims/analysis-inputs.json` | input manifest of the invented analysis behind CLM-01 (its digest is CLM-01's input_manifest_sha256) | `13f913d8120c034a4391ce7c6fd4a651132d07a79ee4174debcf25ae4f0d09aa` |
| `fixtures/outputs/plot-summary.json` | stored output of CLM-01 (its digest is pinned in the registry) | `38453298d808ea671fe0e1a9cf7a237494ee9d0b5101efc21e29214972889855` |

This README is not read by any check. Only the files listed above are.

## What passing this entry does not prove

- **Scope of a pass.** Reproducing `expected-results.json` shows conformance
  on this declared, synthetic fixture only.
- **What it does not show.** It does not show scientific validity. It does
  not show that the verifier catches failures outside the corpus, or that
  the tool is fit for any particular use.
