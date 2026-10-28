# fixtures: invalid-mutation-baseline-synthetic-01

> **SYNTHETIC.** Every file here was generated for this corpus. All names,
> places and values are invented. No real person, institution, paper,
> dataset or DOI appears.

The data the entry's `manifest.json` points at. Paths in the manifest are
relative to the entry directory. `.gitattributes` at the entry root stops
Git from converting line endings, so each file keeps the exact bytes its
digest covers.

| file | what it is | sha256 |
|---|---|---|
| `fixtures/data/gauges.csv` | four invented depth-gauge readings at a fictional canal (the `gauges` input); CW-03 is stored as 97.15 while the manifest declares 97.51 | `dcc4f349c83a08ea45743be6fd3fae78587fe001a47ec7fc824cd76849bb02bf` |

This README is not read by any check. Only the files listed above are.

## What passing this entry does not prove

- **Scope of a pass.** Reproducing `expected-results.json` shows conformance
  on this declared, synthetic fixture only.
- **What it does not show.** It does not show scientific validity. It does
  not show that the verifier catches failures outside the corpus, or that
  the tool is fit for any particular use.
