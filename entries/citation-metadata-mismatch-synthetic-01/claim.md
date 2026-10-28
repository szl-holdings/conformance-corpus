# citation-metadata-mismatch-synthetic-01: claim

> **SYNTHETIC.** Every file in this entry was generated for this corpus. The names, sites, values, works, authors, journals and DOIs (all under the 10.5555 test prefix) are invented. Nothing here describes real people, institutions, papers or datasets.

Category: `citation-metadata-mismatch`: frozen metadata disagrees with the cited author or DOI.

## Claim about the check

A verification log can be structurally honest and still vouch for wrong
citations. Here the log claims all three citations VERIFIED, and every claim
has a complete invocation record, so layer 1 (`verification_log`) passes. The
claim is that `science-gate verify manifest.json` does not stop there: it
compares every citation with the frozen resolver capture and returns **FAIL,
exit 1, reason SOURCE_MISMATCH**, with:

- `citation-metadata` (`citation_metadata`) FAIL: C2 is FIELD_MISMATCH with
  AUTHOR_MISMATCH, and C3 is FIELD_MISMATCH with DOI_WORK_MISMATCH;
- `doi-resolution` (`citation_resolver`) FAIL: the DOI cited by C3 is
  DOI_TARGET_MISMATCH, because it reached a work carrying another DOI;
- C1 left as VERIFIED_WITHIN_DECLARED_SCOPE;
- report.md naming each defect, each affected citation and the DOI reached.

## Setup (all invented)

| citation | cited DOI | what disagrees with the frozen record |
|---|---|---|
| C1 | `10.5555/cc-synth.cmm.0001` | nothing: the control |
| C2 | `10.5555/cc-synth.cmm.0002` | second author cited as Madeupson; the record lists Fictivus |
| C3 | `10.5555/cc-synth.cmm.0003` | title, authors, year, journal, volume and issue match, but the DOI reached a record whose work DOI is `10.5555/cc-synth.cmm.0030` |

The frozen capture's request URLs point at `resolver.invalid`, so nothing is
fetched. A small three-row CSV input with an INDEPENDENT row count lets the
rest of the run succeed, so the citation defects are the only findings.

## What would falsify the claim

PASS, ABSTAIN or ERROR; an exit code other than 1; a reason other than
SOURCE_MISMATCH; C2 or C3 reported VERIFIED_WITHIN_DECLARED_SCOPE; C1 flagged;
or a report.md that omits a `must_mention` string in `expected-results.json`.

## What passing does not prove

Reproducing `expected-results.json` shows **conformance on declared fixtures only**:
science-gate produced the declared outcome on these synthetic fixtures, with the
tool version recorded in `environment.lock`.

- It does not show that science-gate catches this failure outside this entry.
- It does not establish scientific validity. The data is invented, so no
  scientific conclusion is supported or refuted.
- It does not show that science-gate, or any pipeline that uses it, is fit for
  any particular use.
- It does not show that any citation outside this entry is correct, or that a
  live resolver would return what the frozen capture records. No network
  lookup is performed.
