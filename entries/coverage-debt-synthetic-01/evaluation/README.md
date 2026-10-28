# evaluation/

How to evaluate `coverage-debt-synthetic-01` (SYNTHETIC) locally, and the recorded result.

## Run it

From Git Bash, with the entry directory as the working directory and an output
directory **outside** the corpus (an OS temp directory):

```sh
cd <corpus>/entries/coverage-debt-synthetic-01
out="$(mktemp -d)/run"
env -u SCIENCE_GATE_HMAC_KEY_FILE \
  PYTHONPATH=<seg>/src PYTHONDONTWRITEBYTECODE=1 \
  SCIENCE_GATE_FIXED_TIME=2026-09-26T00:00:00Z \
  <python>/python.exe -m science_gate.cli verify manifest.json --output "$out"
echo "exit=$?"
```

## Compare

Compare with `../expected-results.json`:

- `status`, `reason`, `failure_modes` and the per-check fields against
  `$out/run.json`;
- `exit_code` against the process exit code;
- each `must_mention` string (and no `must_not_mention` string) against
  `$out/report.md`.

## Recorded files

- `command.json`: the exact argv, working directory, environment, exit code
  and stdout of the recorded run, with the digests of the original run files.
- `report.md`, `run.json`: copied byte for byte from the recorded run. They
  contained no local path, so nothing needed replacing.
- `comparison.json`: every expected field next to the recorded value, whether
  they match, whether a second run was byte-identical, and the result of
  `science-gate report` re-verifying the run directory.
- `../receipts/receipt.json`: the run's UNSIGNED receipt.
- `control.json`: a repaired-fixture control. A temp copy with only the defect undone was run the same way and returned PASS, showing that the recorded outcome comes from the defect.

A match shows conformance on declared fixtures only. It does not establish
scientific validity or fitness for use.
