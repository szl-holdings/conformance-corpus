# Schemas: `time-source-mismatch-synthetic-01`

> **SYNTHETIC.** Every file in this entry was generated for the conformance corpus. The names, sites, reviewers, values and dates are invented, and no real person, institution, paper or data set is involved. **Passing shows conformance on declared fixtures only. It does not show scientific validity or fitness for use.**

| file | document it describes | schema id | normative definition |
|---|---|---|---|
| `time-sources.fixture.schema.json` | `fixtures/time/events.json` | `science-gate-time-sources/v1` | scientific-evidence-gate src/science_gate/verifier.py (_parse_time_sources, _judge_event); SEG ships no schema file for this document |

`manifest.json` uses `science-gate-manifest/v1`. Its normative definition
is scientific-evidence-gate `schemas/manifest.schema.json` (sha256
`83270fea58e9df8fc67e2accc0a4d62cbfbe922bc37dc4ff1691cd8b2de84e86`) and
`src/science_gate/manifests.py`, at the commit in `environment.lock`.

The schema file here is documentation written for this corpus. The tool's
code is what actually validates the fixture. `entry.json` is validated
against the corpus-level `intake-schema.json` and `permissions-schema.json`.
