# Fixtures (template: reviewer-protocol-drift)

<REPLACE: this placeholder with the entry's generated fixture files, and
keep a short README that lists them.>

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

All fixture data must be SYNTHETIC unless permissions are confirmed.
Passing an entry built from these fixtures shows conformance on declared
fixtures only. It does not show scientific validity or fitness for use.
