# invalid-mutation-baseline-synthetic-01: limitations

> **SYNTHETIC ENTRY.** All data, names and values were invented for this
> corpus. The setting (Cobblewick canal, reach-north, reach-south, gauges
> CW-01 to CW-04) is fictional. No DOI, real person, institution, paper or
> dataset appears. This entry is a draft with no independent review
> (`provenance.reviewed_by` is empty).

## What passing this entry does not prove

- **Only this fixture.** A tool that reproduces `expected-results.json` has
  shown conformance on this one declared, synthetic fixture. It has not
  shown scientific validity, and it has not shown fitness for any use.
- **No generalisation.** It has not shown that the mutation harness handles
  other invalid baselines. A baseline that ABSTAINs or ERRORs, or that FAILs
  for another reason, is not exercised here.
- **Nothing about the gauges.** It has not shown that the declared or stored
  gauge value is correct. The fixture deliberately disagrees with itself.

## Scope limits of the fixture

- **One baseline failure.** The only cause is a `numeric_agreement`
  disagreement on one key, `CW-03`, where 97.51 is declared and 97.15 is
  stored. Every other check passes.
- **Small tree.** One CSV input with a declared digest and an INDEPENDENT
  row count of 4, plus four checks: `rows`, `columns`, `duplicates` and
  `depth`.
- **No receipt from mutate.** `science-gate mutate` writes
  `mutation-report.json` and `mutation-report.md` only. The receipt kept in
  `receipts/` belongs to a supplementary `science-gate verify` of the same
  manifest, which shows the baseline FAIL directly. It is UNSIGNED.
- **Offline.** Every run is offline.
- **Recorded on one platform.** Expected results were confirmed on Windows,
  with CPython 3.11.9 and scientific-evidence-gate 0.1.0 at the commit in
  `environment.lock`. Other platforms have not been run.

## Permissions

- **Access class.** SYNTHETIC.
- **What is allowed.** Evaluation is allowed. Training, redistribution,
  derivatives, public display and commercial use are **not** allowed.
- **No license yet.** No license has been chosen (`NOASSERTION`).
- **Evaluation is not training.** Evaluation permission does not imply
  training permission.
