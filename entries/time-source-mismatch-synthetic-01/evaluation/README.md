# Evaluation: `time-source-mismatch-synthetic-01`

> **SYNTHETIC.** Every file in this entry was generated for the conformance corpus. The names, sites, reviewers, values and dates are invented, and no real person, institution, paper or data set is involved. **Passing shows conformance on declared fixtures only. It does not show scientific validity or fitness for use.**

## How to evaluate locally

1. Check out scientific-evidence-gate at the commit in `../environment.lock`.
2. Run the command in `command.txt` from this entry's directory. The
   output must go to a temporary directory outside the entry.
   `verify` reads the entry and never writes into it.
3. Compare the result with `../expected-results.json`:
   - **Exit code.** The process exit code must equal `exit_code`.
   - **`run.json` fields.** In the output's `run.json`, `status`,
     `reason` and `failure_modes` must equal the expected values exactly.
   - **`report.md` strings.** The output's `report.md` must contain every
     `must_mention` string.

No network access is needed, and none is used.

## Recorded evaluation

| file | content |
|---|---|
| `command.txt` | the exact command, with local paths replaced by `<tmp>` and `<scientific-evidence-gate>` |
| `recorded/stdout.txt` | the command's standard output, with the output directory replaced by `<tmp>` |
| `recorded/exit-code.txt` | the process exit code |
| `recorded/report.md` | the report the run wrote, copied unchanged (it contained no local paths) |
| `recorded/run.json` | the machine-readable result the run wrote, copied unchanged (it contained no local paths) |
| `recorded/reproduction.txt` | a second run compared with the first, byte for byte |

The recorded run's receipt is in `../receipts/`. The run's `ledger.jsonl`,
`evidence-manifest.json`, `receipt.auth.json`, `results.sarif` and `report.html` are not kept
here, to keep the entry small. The same command regenerates them.

**Recorded result:** `FAIL (SOURCE_MISMATCH)`, exit
`1`, failure modes `["SOURCE_MISMATCH"]`. It
matches the intended outcome.

## What passing does not prove

A reproduced result shows only that the verifier behaved as declared on
these SYNTHETIC fixtures. It does not show scientific validity. It does not
show detection of failures outside this corpus. It does not show fitness
for use.
