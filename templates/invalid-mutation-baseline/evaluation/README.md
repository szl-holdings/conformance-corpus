# evaluation: invalid-mutation-baseline-synthetic-NN

## How to evaluate locally

Run the command from the entry directory. `<SEG>` is a checkout of
scientific-evidence-gate at the commit in `../environment.lock`, and
`<tmp>` is an empty temporary directory outside the entry.

```
PYTHONPATH=<SEG>/src PYTHONDONTWRITEBYTECODE=1 SCIENCE_GATE_FIXED_TIME=2026-09-26T00:00:00Z \
  python -m science_gate.cli mutate manifest.json --output <tmp>/mutate
```

## What to record here

In every recorded file, local paths are replaced by `<tmp>`.

- **`command.txt`.** The exact command lines.
- **`stdout.txt`.** The command's output and its exit code.
- **`mutation-report.md`.** The human report, copied from the run directory.
- **`result.json`.** The JSON result: the whole file, or an extract with the
  full file's SHA-256.
- **`comparison.json`.** A field-by-field comparison of the run with
  `../expected-results.json`.
- **A supplementary run.** `science-gate mutate` writes no receipt, so
  also run `science-gate verify manifest.json --output <tmp>/verify`,
  and keep its receipt in `../receipts/`.

This file is a placeholder until the entry is instantiated.

## What passing this entry does not prove

- **Scope of a pass.** Reproducing `expected-results.json` shows conformance
  on this declared fixture only. That is a performance claim about declared
  fixtures.
- **What it does not show.** It does not show scientific validity. It does
  not show that the verifier catches failures outside the corpus, or that
  the tool is fit for any particular use.
