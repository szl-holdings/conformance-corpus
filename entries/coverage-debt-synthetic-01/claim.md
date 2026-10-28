# coverage-debt-synthetic-01: claim

> **SYNTHETIC.** Every file in this entry was generated for this corpus. The names, sites, values, works, authors, journals and DOIs (all under the 10.5555 test prefix) are invented. Nothing here describes real people, institutions, papers or datasets.

Category: `coverage-debt`: a declared check had nothing to look at.

## Claim about the check

The manifest declares four required checks over four invented water-level
readings: `rows`, `columns`, `duplicates` and `time_window`. The first three
have real rows to examine and should PASS, each with a falsifier witness.
`time_window` (`time_source`) reads the manifest's time-sources document, but
the manifest declares none, so the check has nothing to look at. A gate that
reads "no failures" as success would report 4 of 4 checks with no failures and
PASS.

The claim is that `science-gate verify manifest.json` returns **ABSTAIN, exit
2, reason OUT_OF_SCOPE, with no failure mode**, with:

- `time_window` NOT_APPLICABLE, verdict ABSTAIN, reason OUT_OF_SCOPE, 0
  subject records examined, diagnostic "the manifest declares no
  time_sources", and the closed-vocabulary justification NOT_DECLARED;
- `time_window` not counted as executed, so checks_executed is 3 of
  checks_expected 4, and the contract finding names the NOT_DECLARED
  justification instead of PARTIAL_EXECUTION;
- report.md listing `time_window` under what abstained and what remains
  unresolved.

This intended outcome was re-baselined on 2026-10-28 under
scientific-evidence-gate `docs/ARCHITECTURE.md` section 17.7 (G2): a required
check NOT_APPLICABLE as NOT_DECLARED gives ABSTAIN / OUT_OF_SCOPE. Before that,
the entry used a declared time-sources document with no events and intended
ABSTAIN / INSUFFICIENT_EVIDENCE with PARTIAL_EXECUTION (see
`expected-results.json` `rebaseline`).

## What would falsify the claim

- PASS, FAIL or ERROR
- an exit code other than 2
- a reason other than OUT_OF_SCOPE
- any failure mode, PARTIAL_EXECUTION in particular
- `time_window` shown as CHECKED or PASS, counted as executed, or labelled
  with anything but NOT_DECLARED
- a report.md that omits a `must_mention` string in `expected-results.json`

## What passing does not prove

Reproducing `expected-results.json` shows **conformance on declared fixtures only**:
science-gate produced the declared outcome on these synthetic fixtures, with the
tool version recorded in `environment.lock`.

- It does not show that science-gate catches this failure outside this entry.
- It does not establish scientific validity. The data is invented, so no
  scientific conclusion is supported or refuted.
- It does not show that science-gate, or any pipeline that uses it, is fit for
  any particular use.
- It does not show that the readings fall inside or outside the window. No
  observation time was examined, so nothing is known about it.
