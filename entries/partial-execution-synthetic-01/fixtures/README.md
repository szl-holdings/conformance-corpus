# fixtures/ (partial-execution-synthetic-01, SYNTHETIC)

> **SYNTHETIC ENTRY.** Every file in this entry was generated for this corpus. The names, sites,
> citations and values are invented; DOIs use the 10.5555 test prefix. Nothing here describes real
> people, institutions, papers or datasets. This is a draft: it has not been independently reviewed.

- `data/samples.csv`: five invented water samples at two fictional stations. Three of the four required
  checks (`rows`, `columns`, `duplicates`) examine it and pass.
- `time/events.json`: **deliberately absent** (see `time/README.md`). In the scenario, a fictional
  clock-normalization stage was started and never completed, so the file the required `time-window`
  check examines was never written.

## What passing does not prove

- **Scope of a pass.** Reproducing this entry's expected outcome shows conformance on this declared
  synthetic fixture only. That is a performance claim about one declared case.
- **Not shown.** It does not show that the verifier catches failures outside the corpus. It does not
  show that any scientific conclusion is true. It does not show that the verifier is fit for any use.
