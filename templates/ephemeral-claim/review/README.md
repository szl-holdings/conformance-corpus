# review: ephemeral-claim-synthetic-NN

This directory stays empty, apart from this file, until someone other than
the entry's author reviews the entry. The reviewer then adds
`<reviewer>-<date>.md`, recording:

- who they are and the date;
- the commit reviewed;
- whether the fixture isolates the stated defect;
- whether the expected outcome follows from the tool's contract;
- whether they reproduced the run;
- any disagreement.

Only then is the reviewer added to `provenance.reviewed_by`.

## What passing this entry does not prove

- **Scope of a pass.** Reproducing `expected-results.json` shows conformance
  on this declared fixture only. That is a performance claim about declared
  fixtures.
- **What it does not show.** It does not show scientific validity. It does
  not show that the verifier catches failures outside the corpus, or that
  the tool is fit for any particular use.
