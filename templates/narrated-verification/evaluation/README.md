# evaluation/ (template: narrated-verification)

## How to evaluate locally

From the entry directory, with no network:

```sh
PYTHONPATH=<SEG>/src PYTHONDONTWRITEBYTECODE=1 SCIENCE_GATE_FIXED_TIME=2026-09-26T00:00:00Z \
  <python> -m science_gate.cli verify manifest.json --output <tmp>/run
```

Then compare with `../expected-results.json`: exit code; `run.json` `status` and `reason`; sorted
`run.json` `failure_modes`; every `must_mention` string in `report.md`.

## Recorded evaluation (fill after the run)

- `command.txt`: the exact argument list, environment and exit code
- `stdout.txt`: what science-gate printed, local paths replaced by `<tmp>`
- `report.md`, `run.json`: copied from the run directory, local paths replaced
- `comparison.json`: intended against recorded, field by field

## What passing does not prove

- **Scope of a pass.** Reproducing an entry's expected outcome shows conformance on that declared
  fixture only. That is a performance claim about one declared case.
- **Not shown.** It does not show that the verifier catches failures outside the corpus. It does not
  show that any scientific conclusion is true. It does not show that the verifier is fit for any use.
