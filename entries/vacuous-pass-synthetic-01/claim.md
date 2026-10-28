# Claim: Stored PASS over a header-only input (vacuous pass), synthetic

> **SYNTHETIC ENTRY.** Every file in this entry was generated for this corpus. The names, sites,
> citations and values are invented; DOIs use the 10.5555 test prefix. Nothing here describes real
> people, institutions, papers or datasets. This is a draft: it has not been independently reviewed.

## The check under test

A fictional QC tool, *tallyfern-qc*, stored a summary that says **PASS** for the input `readings`. The
summary pins the input's exact bytes (sha256) and records `rows: 0`. The input file has a header and no
data records. The tool therefore reported success over zero examined rows: a **vacuous pass**.

## The claim about the verifier

Given `manifest.json`, `science-gate verify` must not confirm that PASS. It must return:

- status **ABSTAIN**, exit code **2**
- reason **INSUFFICIENT_EVIDENCE**
- failure modes exactly **VACUOUS_PASS**
- a report that mentions: `VACUOUS_PASS`, `fixtures/data/readings.csv`, `EMPTY`, `with 0 rows`, `rows_examined`

ABSTAIN, not FAIL: nothing was contradicted. There is simply nothing to have passed.

**Falsified by:** science-gate returns PASS or exit code 0 on this manifest; or it reports the stored PASS as confirmed; or its report omits VACUOUS_PASS, the empty input or the zero-row pin; or it states that rows were examined when the only input has none.

## Recorded result

The recorded run (science-gate commit e563fd3, refreshed 2026-10-28) matches every asserted field of the intended outcome. The two divergences recorded against commit 7ec36c6 (an extra PARTIAL_EXECUTION, and no `rows_examined` in report.md) were resolved by the tool's section 17.7 rules (G1, G2). See `evaluation/README.md`.

## What passing does not prove

- **Scope of a pass.** Reproducing this entry's expected outcome shows conformance on this declared
  synthetic fixture only. That is a performance claim about one declared case.
- **Not shown.** It does not show that the verifier catches failures outside the corpus. It does not
  show that any scientific conclusion is true. It does not show that the verifier is fit for any use.
