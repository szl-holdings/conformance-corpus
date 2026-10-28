# Time-source mismatch: local date inside the window, normalized UTC outside it (SYNTHETIC)

> **SYNTHETIC.** Every file in this entry was generated for the conformance corpus. The names, sites, reviewers, values and dates are invented, and no real person, institution, paper or data set is involved. **Passing shows conformance on declared fixtures only. It does not show scientific validity or fitness for use.**

**Entry:** `time-source-mismatch-synthetic-01`. **Category:** `time-source-mismatch`. **Failure mode:**
`SOURCE_MISMATCH`. **Status:** draft, not independently reviewed.

## The claim about the check

Given a time-sources document whose requested window is 2026-05-01T00:00:00Z to 2026-05-31T23:59:59Z, and whose event syn-obs-03 is recorded at local time 2026-05-31T22:30:00 with offset -04:00 and an internally consistent normalized UTC of 2026-06-01T02:30:00Z, science-gate verify with a required time_source check reports FAIL with exit code 1, reason SOURCE_MISMATCH and failure modes exactly [SOURCE_MISMATCH], and its report names syn-obs-03 as OUTSIDE_WINDOW. It must not PASS on the local date, which falls inside the window.

## The case

**What the fixture contains.** `fixtures/time/events.json`
(`science-gate-time-sources/v1`) requests the evidence window
`2026-05-01T00:00:00Z` to `2026-05-31T23:59:59Z`. It lists three
observations, one per row of `fixtures/data/readings.csv`:

| event | local time | offset | recorded UTC | inside window? |
|---|---|---|---|---|
| syn-obs-01 | 2026-05-10T09:00:00 | +03:00 | 2026-05-10T06:00:00Z | yes |
| syn-obs-02 | 2026-05-20T12:00:00 | UTC | 2026-05-20T12:00:00Z | yes |
| syn-obs-03 | 2026-05-31T22:30:00 | -04:00 | 2026-06-01T02:30:00Z | **no** |

**Why a check could appear to succeed.** For syn-obs-03 the local date, 31
May, lies inside the window. Local time minus the offset equals the recorded
UTC, so the record is internally consistent. A check that compared local
dates with the window, or that only confirmed a UTC value was present, would
report success. The required `rows` and `columns` checks pass.

**What a conforming verifier must do.** It must normalize the observation to
UTC and compare that value with the window. The result is 1 June, which is
outside the window. For science-gate that is `verify manifest.json` with the
outcome below.

## Expected outcome

Run from this directory:

```
PYTHONPATH=<scientific-evidence-gate>/src PYTHONDONTWRITEBYTECODE=1 \
SCIENCE_GATE_FIXED_TIME=2026-09-26T00:00:00Z \
python -m science_gate.cli verify manifest.json --output <tmp>
```

- **Status:** `FAIL`
- **Exit code:** `1`
- **Reason:** `SOURCE_MISMATCH`
- **Failure modes:** exactly `["SOURCE_MISMATCH"]`
- **`report.md` must mention:** `OUTSIDE_WINDOW`, `syn-obs-03`, `SOURCE_MISMATCH`

`expected-results.json` holds the machine-readable form. `evaluation/`
holds the recorded run.

## What passing does not prove

- Passing this entry shows only that a verifier produced the declared outcome (status, exit code, reason, failure modes and required report strings) on these declared SYNTHETIC fixtures. It is a conformance result on declared fixtures only.
- It does not show that the verifier catches this failure outside this corpus, in other data, or when the failure takes another form.
- It does not show that any scientific conclusion is true or false. The data, the study and the conclusion here are invented and mean nothing.
- It does not show that the verifier, or anything checked with it, is fit for any particular use.
- It does not show that the declared offsets are the true local offsets, or that any clock was accurate. The offsets are taken as declared.
- It does not show that the readings themselves are correct or meaningful.
