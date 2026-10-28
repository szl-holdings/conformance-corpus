# verifier-blind-spot-synthetic-01: limitations

> **SYNTHETIC ENTRY.** All data, names and values were invented for this
> corpus. The setting (Brassmoor, station-thistle, station-quartz, readings
> BM-01 to BM-04) is fictional. No DOI, real person, institution, paper or
> dataset appears. This entry is a draft with no independent review
> (`provenance.reviewed_by` is empty).

## What passing this entry does not prove

- **Only this fixture.** A tool that reproduces `expected-results.json` has
  shown conformance on this one declared, synthetic fixture. It has not
  shown scientific validity, and it has not shown fitness for any use.
- **No completeness.** It has not shown that mutation testing finds every
  blind spot. It covers only the defect kinds its operators inject, and
  only on this tree.
- **Sensitivity is not accuracy.** The sensitivity of 8/9 describes this
  tree under the 20 operators of science-gate 0.1.0. It is not a measure of
  the verifier's accuracy on real evidence.

## Scope limits of the fixture

- **One tree.** One CSV input with a declared digest and a row key, but no
  independent row count. Three checks.
- **One blind spot, by design.** The only intended blind spot is
  duplicated records. The escaped mutant verifies as PASS.
- **Operator-dependent counts.** The expected counts (9 executed, 8
  detected, 1 escaped, 11 not applicable) depend on the operator set of
  science-gate 0.1.0. The blind-spot set `[M04_duplicate_row]` does not.
- **Uncovered variant.** A duplicate that *another* detector notices for the
  wrong reason is not covered (see `entry.json`, `unresolved_cases`).
- **No receipt from mutate.** `science-gate mutate` writes
  `mutation-report.json` and `mutation-report.md` only. The receipt kept in
  `receipts/` belongs to a supplementary `science-gate verify` of the same
  manifest (the accepting baseline, PASS). It is UNSIGNED.
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
