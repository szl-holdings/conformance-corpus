# fixtures/ (template: narrated-verification)

> **SYNTHETIC ENTRY.** <KEEP THIS BANNER FOR SYNTHETIC ENTRIES. Every file was generated for this corpus;
> names, sites, citations and values are invented; DOIs use the 10.5555 test prefix only; nothing
> describes real people, institutions, papers or datasets. Say 'draft' until reviewed_by is non-empty.>

<DESCRIBE EACH FIXTURE FILE AND ITS ROLE.> Suggested layout for this category:

- `data/<FILE>.csv`: a small, real, non-empty input (so the run is not vacuous).
- `citations/entries.json`: `science-gate-citations/v1`, invented works, DOIs `10.5555/...` only.
- `citations/verification-log.json`: `science-gate-verification-log/v1` with `claimed_verified`
  and `VERIFIED` entries that outnumber the complete `invocations`.

## What passing does not prove

- **Scope of a pass.** Reproducing an entry's expected outcome shows conformance on that declared
  fixture only. That is a performance claim about one declared case.
- **Not shown.** It does not show that the verifier catches failures outside the corpus. It does not
  show that any scientific conclusion is true. It does not show that the verifier is fit for any use.
