# fixtures/ (vacuous-pass-synthetic-01, SYNTHETIC)

> **SYNTHETIC ENTRY.** Every file in this entry was generated for this corpus. The names, sites,
> citations and values are invented; DOIs use the 10.5555 test prefix. Nothing here describes real
> people, institutions, papers or datasets. This is a draft: it has not been independently reviewed.

- `data/readings.csv`: a header (`reading_id,site,depth_cm,count`) and **zero data records**.
- `summary/stored-summary.json`: a stored summary from a fictional QC tool ("tallyfern-qc") that claims
  `PASS` and pins `readings` by its sha256 with `rows: 0`. This is the vacuous success under test.

## What passing does not prove

- **Scope of a pass.** Reproducing this entry's expected outcome shows conformance on this declared
  synthetic fixture only. That is a performance claim about one declared case.
- **Not shown.** It does not show that the verifier catches failures outside the corpus. It does not
  show that any scientific conclusion is true. It does not show that the verifier is fit for any use.
