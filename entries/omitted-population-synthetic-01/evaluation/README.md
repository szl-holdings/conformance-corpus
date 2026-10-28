# evaluation/

How to evaluate `omitted-population-synthetic-01` (SYNTHETIC) locally, and the recorded result.

## Run it

From Git Bash, with the entry directory as the working directory and an output
directory **outside** the corpus (an OS temp directory):

```sh
cd <corpus>/entries/omitted-population-synthetic-01
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
  they match, whether a second run (`PYTHONHASHSEED=4242`) was byte-identical,
  and the result of `science-gate report` re-verifying the run directory.
- `../receipts/receipt.json`: the run's UNSIGNED receipt record (statement and
  sidecar; see `../receipts/README.md`).
- `control.json`: a repaired-fixture control. A temp copy with only the defect
  undone was run the same way. `repaired_fixture` holds every changed file
  exactly as it was run, and `match` says whether the control returned PASS.

The recorded run does **not** match every expected field: `checks.rows.verdict`. expected-results.json was **not** changed to match it; the differences are listed in entry.json `known_failures`.

A match shows conformance on declared fixtures only. It does not establish
scientific validity or fitness for use.
