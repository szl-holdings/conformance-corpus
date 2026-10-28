# Fixtures (template: time-source-mismatch)

<REPLACE: this placeholder with the entry's generated fixture files, and
keep a short README that lists them.>

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

All fixture data must be SYNTHETIC unless permissions are confirmed.
Passing an entry built from these fixtures shows conformance on declared
fixtures only. It does not show scientific validity or fitness for use.
