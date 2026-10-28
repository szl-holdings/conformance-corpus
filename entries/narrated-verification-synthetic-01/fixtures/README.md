# fixtures/ (narrated-verification-synthetic-01, SYNTHETIC)

> **SYNTHETIC ENTRY.** Every file in this entry was generated for this corpus. The names, sites,
> citations and values are invented; DOIs use the 10.5555 test prefix. Nothing here describes real
> people, institutions, papers or datasets. This is a draft: it has not been independently reviewed.

- `data/observations.csv`: four invented readings at two fictional sites. It exists so that the run has a
  real, non-empty input; it is not the subject of the entry.
- `citations/entries.json`: a bibliography of five invented works (C1 to C5), DOIs `10.5555/corpus.nv.*`.
- `citations/verification-log.json`: a log from a fictional checker ("inkwell-refcheck") that claims all
  five as VERIFIED (`claimed_verified: 5`) but records invocations for **C1 and C2 only**. The two
  `response_sha256` values hash an invented string; no response body exists.

## What passing does not prove

- **Scope of a pass.** Reproducing this entry's expected outcome shows conformance on this declared
  synthetic fixture only. That is a performance claim about one declared case.
- **Not shown.** It does not show that the verifier catches failures outside the corpus. It does not
  show that any scientific conclusion is true. It does not show that the verifier is fit for any use.
