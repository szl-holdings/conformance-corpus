# Limitations: vacuous-pass-synthetic-01

> **SYNTHETIC ENTRY.** Every file in this entry was generated for this corpus. The names, sites,
> citations and values are invented; DOIs use the 10.5555 test prefix. Nothing here describes real
> people, institutions, papers or datasets. This is a draft: it has not been independently reviewed.

## What passing does not prove

- **Scope of a pass.** Reproducing this entry's expected outcome shows conformance on this declared
  synthetic fixture only. That is a performance claim about one declared case.
- **Not shown.** It does not show that the verifier catches failures outside the corpus. It does not
  show that any scientific conclusion is true. It does not show that the verifier is fit for any use.

## Limits of this entry

- **Synthetic.** The data, the fictional QC tool and its summary were invented for this corpus. They show
  the shape of a vacuous pass, not its frequency or form in real pipelines.
- **One shape of emptiness.** Only a header-only CSV is covered. Empty JSON inputs, filters that exclude
  every row, and checks whose scope is empty for other reasons are not.
- **One author, not reviewed.** `reviewed_by` is empty. The intended failure-mode set and the
  `rows_examined` expectation are the author's position and are disputed by the recorded run (see
  `entry.json` `known_failures` and `unresolved_cases`). coverage-debt-synthetic-01 expects the
  opposite treatment of NOT_APPLICABLE required checks; the corpus has no single rule yet.
- **Tool-version bound.** The recorded outcome is for science-gate 0.1.0 at the commit in
  `environment.lock`; other versions may differ.
- **No redistribution yet.** No license has been chosen (NOASSERTION); redistribution is not allowed.
  Evaluation permission does not imply training permission, and training is not allowed.
