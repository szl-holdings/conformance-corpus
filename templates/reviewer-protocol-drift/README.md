# Template: reviewer-protocol-drift

This template is for entries in which a required reviewer is missing, or a verdict is duplicated.

**Using the template.**

1. Copy this directory to `entries/<entry-id>/`.
2. Replace every `<REPLACE: ...>` value.
3. Generate the fixtures (see `fixtures/README.md`).
4. Write the **intended** outcome before running anything.
5. Run the command in `evaluation/README.md`.
6. Record the run in `evaluation/` and the receipt in `receipts/`.

A copied template fails `intake-schema.json` validation until its
`entry_id` placeholder is replaced. That is deliberate. The other
placeholders are plain strings, and schema validation cannot catch them.
Search the copy for `<REPLACE` before treating it as an entry.

**Rules for every entry.**

- **Invented data only.** Data is SYNTHETIC unless its permissions are
  confirmed. Names are obviously invented. DOIs, if any, use only the
  `10.5555` test prefix. No real person, institution, paper or data set
  appears.
- **Small entries.** Keep an entry to a few KB.
- **Honest labels.** Label synthetic entries SYNTHETIC in `entry.json`,
  `claim.md` and `limitations.md`.
- **Missing evidence is never a PASS.**
- **Record disagreements.** If science-gate disagrees with the intended
  outcome, keep the intended outcome in `expected-results.json` and list
  the mismatch. Record it in `entry.json` `known_failures`.
- **Say what a pass does not show.** Every file that describes an entry
  says what passing does not prove: it shows conformance on declared
  fixtures only, not scientific validity or fitness for use.

## Fixture recipe: reviewer-protocol-drift

1. **Data file.** Write a small data file, for example
   `fixtures/data/samples.csv`, with 4 to 10 invented rows. Declare it
   as a required input with its `sha256`, an INDEPENDENT
   `expected_rows` and a `row_key`.
2. **Required reviewers.** Declare them in `manifest.json` under
   `reviews.required_reviewers`. Use obviously invented handles such as
   `syn-reviewer-a`. Never use a real person's name.
3. **Verdicts.** Write `fixtures/reviews/verdicts.json`
   (`science-gate-reviews/v1`). To make the drift easy to miss, keep the
   verdict count equal to the number of required reviewers while one
   reviewer is missing and another is duplicated. science-gate compares
   names after trimming and case folding, so a case variant is a
   duplicate.

```json
{
  "schema": "science-gate-reviews/v1",
  "verdicts": [
    {"reviewer": "syn-reviewer-a", "verdict": "ACCEPT", "subject": "<run label>", "recorded_at": "2026-04-02T09:00:00Z"},
    {"reviewer": "syn-reviewer-b", "verdict": "ACCEPT", "subject": "<run label>", "recorded_at": "2026-04-02T11:30:00Z"},
    {"reviewer": "SYN-Reviewer-B ", "verdict": "ACCEPT", "subject": "<run label>", "recorded_at": "2026-04-03T08:15:00Z"}
  ]
}
```

The expected outcome is ABSTAIN, not FAIL. The protocol was not completed,
so no verdict can be relied on, but nothing was shown to be wrong.
