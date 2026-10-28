# Claim: Required time-window check cannot execute because its stage never completed, synthetic

> **SYNTHETIC ENTRY.** Every file in this entry was generated for this corpus. The names, sites,
> citations and values are invented; DOIs use the 10.5555 test prefix. Nothing here describes real
> people, institutions, papers or datasets. This is a draft: it has not been independently reviewed.

## The check under test

A fictional pipeline declares four required checks over five invented samples. Its clock-normalization
stage was started and never completed, so it never wrote `fixtures/time/events.json`. The required
`time-window` check therefore cannot execute. The other three checks run and pass. A pipeline that
reports "3 passed, 0 failed" here has **partially executed** its required checks and must not look
complete.

## The claim about the verifier

Given `manifest.json`, `science-gate verify` must return:

- status **ABSTAIN**, exit code **2**
- primary reason **PARTIAL_EXECUTION**
- failure modes exactly **PARTIAL_EXECUTION**
- a report that mentions: `PARTIAL_EXECUTION`, `checks_executed=3 of checks_expected=4`, `fixtures/time/events.json`, `time-window`

ABSTAIN, not FAIL: nothing was contradicted. One required check simply never ran.

**Falsified by:** science-gate returns PASS or exit code 0; or it presents the three passing checks as a complete run; or it does not name the time-window check or the missing file; or its primary reason is not PARTIAL_EXECUTION.

## Recorded result

The run against science-gate commit 7ec36c6 returned ABSTAIN, exit 2, failure modes PARTIAL_EXECUTION, and mentioned every required string, but its primary reason was **INSUFFICIENT_EVIDENCE**, not PARTIAL_EXECUTION. `expected-results.json` was not changed to match. See `entry.json` `known_failures` and `unresolved_cases`. The run against commit e563fd3 (refreshed 2026-10-28) returns ABSTAIN, exit 2, primary reason INSUFFICIENT_EVIDENCE and failure modes **OMITTED_POPULATION** only, and its report no longer mentions PARTIAL_EXECUTION: the skipped check now carries the closed-vocabulary label INPUT_UNAVAILABLE (section 17.7 of the science-gate architecture). Section 17.7 (G2) re-baselines this category to an unlabelled skip, FAIL / PARTIAL_EXECUTION, which no fixture can produce through `verify`, so the intended outcome was left unchanged for a reviewer. See `entry.json` `known_failures` and `unresolved_cases`.

## What passing does not prove

- **Scope of a pass.** Reproducing this entry's expected outcome shows conformance on this declared
  synthetic fixture only. That is a performance claim about one declared case.
- **Not shown.** It does not show that the verifier catches failures outside the corpus. It does not
  show that any scientific conclusion is true. It does not show that the verifier is fit for any use.
