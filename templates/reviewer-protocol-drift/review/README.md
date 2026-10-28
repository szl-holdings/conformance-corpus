# Review records (template)

<REPLACE: this placeholder. It stays empty until an independent review
is recorded.>

Add one file per review, `review/<yyyy-mm-dd>-<reviewer-handle>.md`, and
list the reviewer in `entry.json` `provenance.reviewed_by`. An entry with
no reviewers is a draft.

Each review should state:

- **Identity and independence.** Who reviewed the entry, and how they are
  independent of the author.
- **Category.** Whether the fixture exercises the category.
- **Contract basis.** Whether the expected outcome follows from the
  published contract.
- **Reproduction.** Whether the recorded run reproduces.
- **Remaining problems.** What remains unresolved.

## What passing does not prove

Keep the entry's SYNTHETIC banner at the top of this file. A review does not
change what passing the entry proves: conformance on declared fixtures only.
It does not show scientific validity, detection of failures outside the
corpus, or fitness for use.
