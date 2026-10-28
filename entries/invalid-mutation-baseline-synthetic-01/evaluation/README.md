# evaluation: invalid-mutation-baseline-synthetic-01

> **SYNTHETIC.** Every file here was generated for this corpus. All names,
> places and values are invented. No real person, institution, paper,
> dataset or DOI appears.

## How to evaluate locally

Run the command from this entry's directory. `<SEG>` is a checkout of
scientific-evidence-gate at the commit in `../environment.lock`, and
`<tmp>` is any empty temporary directory outside the entry. No network
is needed.

```
PYTHONPATH=<SEG>/src PYTHONDONTWRITEBYTECODE=1 SCIENCE_GATE_FIXED_TIME=2026-09-26T00:00:00Z \
  python -m science_gate.cli mutate manifest.json --output <tmp>/mutate
```

Then compare the run with `../expected-results.json`:

- **The exit code** comes from the process.
- **status, reason and failure_modes** come from the JSON result.
- **must_mention.** Every `must_mention` string must appear in `mutation-report.md`.
- **The remaining expected fields.**

## Recorded evaluation

- **`command.txt`.** The exact command lines that were run.
- **`stdout.txt`.** The command's output and its exit code. Local paths are
  replaced by `<tmp>`.
- **`mutation-report.md`.** The human report, copied from the run directory.
- **`result.json`.** The JSON result: the whole file when it is small, or an
  extract with the full file's SHA-256 when it is not.
- **`comparison.json`.** A field-by-field comparison of the run with
  `expected-results.json`, and a check that the receipt's content hash
  recomputes. It also records a second run with `PYTHONHASHSEED=4242`,
  which must be byte-identical.
- **A supplementary run.** `science-gate mutate` writes
  `mutation-report.json` and `mutation-report.md` only. It writes no run
  receipt, so a supplementary `science-gate verify manifest.json` of the
  same tree was run. Its command and output are in `command.txt` and
  `stdout.txt`, and its receipt is in `../receipts/`.

The expected results were written from the intended behaviour before the
recorded run, and were not edited to fit it.

## What passing this entry does not prove

- **Scope of a pass.** Reproducing `expected-results.json` shows conformance
  on this declared, synthetic fixture only.
- **What it does not show.** It does not show scientific validity. It does
  not show that the verifier catches failures outside the corpus, or that
  the tool is fit for any particular use.
