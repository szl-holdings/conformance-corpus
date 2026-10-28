# Limitations: partial-execution-synthetic-01

> **SYNTHETIC ENTRY.** Every file in this entry was generated for this corpus. The names, sites,
> citations and values are invented; DOIs use the 10.5555 test prefix. Nothing here describes real
> people, institutions, papers or datasets. This is a draft: it has not been independently reviewed.

## What passing does not prove

- **Scope of a pass.** Reproducing this entry's expected outcome shows conformance on this declared
  synthetic fixture only. That is a performance claim about one declared case.
- **Not shown.** It does not show that the verifier catches failures outside the corpus. It does not
  show that any scientific conclusion is true. It does not show that the verifier is fit for any use.

## Limits of this entry

- **Synthetic.** The samples, stations and pipeline were invented for this corpus.
- **An approximation of the category.** The corpus defines partial execution as a required check that
  never reached a terminal state. science-gate verify cannot ingest an external execution ledger, so
  this entry uses a required check that could not execute because its evidence was never written.
  A crash in the middle of a check, a timeout, or a ledger with an unterminated invocation are not
  covered.
- **Intended outcome unreachable at commit e563fd3.** The intended primary reason and failure mode
  (PARTIAL_EXECUTION) differ from the recorded ones; see `entry.json` `known_failures` and
  `unresolved_cases`. Section 17.7 (G2) of the science-gate architecture now gives a labelled skip
  ABSTAIN with its label's reason, and only an unlabelled skip FAIL / PARTIAL_EXECUTION; no fixture
  can produce an unlabelled skip through `verify`, because the label rules of section 17.7 give
  every verify skip path a label, and INPUT_UNAVAILABLE maps to OMITTED_POPULATION. This is a spec
  contradiction that needs a gate or spec decision. Until then the divergence is a documented gap
  (`known_failures` and `DOCUMENTED_GAPS`, owner-approved on 2026-10-28); the intended outcome is unchanged.
- **One author, not reviewed.** `reviewed_by` is empty.
- **Tool-version bound.** The recorded outcome is for science-gate 0.1.0 at the commit in
  `environment.lock`.
- **No redistribution yet.** No license has been chosen (NOASSERTION). Evaluation permission does not
  imply training permission, and training is not allowed.
