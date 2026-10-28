# coverage-debt-synthetic-01: claim

> **SYNTHETIC.** Every file in this entry was generated for this corpus. The names, sites, values, works, authors, journals and DOIs (all under the 10.5555 test prefix) are invented. Nothing here describes real people, institutions, papers or datasets.

Category: `coverage-debt`: a declared check had nothing to look at.

## Claim about the check

The manifest declares four required checks over four invented water-level
readings: `rows`, `columns`, `duplicates` and `time_window`. The first three
have real rows to examine and should PASS. `time_window` (`time_source`) reads
`fixtures/time/events.json`. That file exists and parses and declares an April
2030 window, but its `events` list is empty, so the check has nothing to look
at. A gate that reads "no failures" as success would report 4 of 4 checks with
no failures and PASS.

The claim is that `science-gate verify manifest.json` returns **ABSTAIN, exit
2, reason INSUFFICIENT_EVIDENCE**, with:

- `time_window` NOT_APPLICABLE, verdict ABSTAIN, 0 rows examined, diagnostic
  "the time sources list no events";
- `time_window` not counted as executed, so checks_executed is 3 of
  checks_expected 4 (failure mode PARTIAL_EXECUTION);
- report.md listing `time_window` under what abstained and what remains
  unresolved.

## What would falsify the claim

- PASS, FAIL or ERROR
- an exit code other than 2
- a reason other than INSUFFICIENT_EVIDENCE
- `time_window` shown as CHECKED or PASS, or counted as executed
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
