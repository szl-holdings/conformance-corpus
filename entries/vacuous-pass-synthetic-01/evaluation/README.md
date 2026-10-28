# evaluation/ (vacuous-pass-synthetic-01, SYNTHETIC)

## How to evaluate locally

From the entry directory, with no network and no shell features needed:

```sh
PYTHONPATH=<SEG>/src PYTHONDONTWRITEBYTECODE=1 SCIENCE_GATE_FIXED_TIME=2026-09-26T00:00:00Z \
  <python> -m science_gate.cli verify manifest.json --output <tmp>/run
```

`<SEG>` is a checkout of scientific-evidence-gate, `<python>` is Python 3.11 or later, and `<tmp>` is
any temporary directory outside the entry. Leave `SCIENCE_GATE_HMAC_KEY_FILE` unset to reproduce the
UNSIGNED receipt. Then compare with `../expected-results.json`:

- the process exit code equals `exit_code`
- `run.json` `status` and `reason` equal `status` and `reason`
- the sorted `run.json` `failure_modes` equal `failure_modes`
- every `must_mention` string occurs in `report.md` (case-sensitive substring)

## Recorded evaluation

- `command.txt`: the exact command, environment and exit code
- `stdout.txt`: what science-gate printed (paths replaced by `<tmp>`; Windows CRLF line endings
  normalized to LF)
- `report.md`, `run.json`: copied from the run directory byte for byte (they contained no local path)
- `comparison.json`: the intended outcome against the recorded one, field by field, a second run
  with `PYTHONHASHSEED=4242` compared byte for byte, and the receipt re-check

| field | intended (expected-results.json) | recorded run | match |
|---|---|---|---|
| status | ABSTAIN | ABSTAIN | yes |
| exit_code | 2 | 2 | yes |
| reason | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | yes |
| failure_modes | VACUOUS_PASS | VACUOUS_PASS | yes |
| must_mention | 5 string(s) | 5 found | yes |

The recorded run matches every intended field.

Environment: see `../environment.lock`. Receipt: see `../receipts/`.

## What passing does not prove

- **Scope of a pass.** Reproducing this entry's expected outcome shows conformance on this declared
  synthetic fixture only. That is a performance claim about one declared case.
- **Not shown.** It does not show that the verifier catches failures outside the corpus. It does not
  show that any scientific conclusion is true. It does not show that the verifier is fit for any use.
