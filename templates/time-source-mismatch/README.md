# Template: time-source-mismatch

This template is for entries in which an observation falls outside the requested evidence window.

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

## Fixture recipe: time-source-mismatch

1. **Data file.** Write a small data file, for example
   `fixtures/data/readings.csv`, with one invented row per observation.
   Declare it as a required input with its `sha256`, an INDEPENDENT
   `expected_rows` and a `row_key`.
2. **Time sources.** Write `fixtures/time/events.json`
   (`science-gate-time-sources/v1`). Use only fixed offsets (`+HH:MM`,
   `-HH:MM`) or `UTC`/`Z`. Named zones such as `Region/City` are not
   resolved; they give ABSTAIN, which is a different case.
3. **Consistency.** In every event, `local_time` minus the offset must
   equal `utc` exactly. Otherwise the outcome is UTC_MISMATCH, which is a
   different case.
4. **The trap.** Exactly one event should look inside the window when read
   by its local date, but fall outside it once normalized to UTC.

```json
{
  "schema": "science-gate-time-sources/v1",
  "window": {"start": "2026-05-01T00:00:00Z", "end": "2026-05-31T23:59:59Z"},
  "events": [
    {"id": "obs-in", "local_time": "2026-05-10T09:00:00", "timezone": "+03:00",
     "utc": "2026-05-10T06:00:00Z", "source": "synthetic-logger-1"},
    {"id": "obs-out", "local_time": "2026-05-31T22:30:00", "timezone": "-04:00",
     "utc": "2026-06-01T02:30:00Z", "source": "synthetic-logger-2"}
  ]
}
```
