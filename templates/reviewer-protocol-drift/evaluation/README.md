# Evaluation (template)

<REPLACE: this placeholder with the recorded evaluation.>

Record the evaluation in these files:

| file | content |
|---|---|
| `command.txt` | the exact command, cwd and environment, with local paths replaced by `<tmp>` and `<scientific-evidence-gate>` |
| `recorded/stdout.txt` | standard output, with the output directory replaced by `<tmp>` |
| `recorded/exit-code.txt` | the exit code |
| `recorded/report.md` | the run's `report.md`, with any local path replaced by `<tmp>` |
| `recorded/run.json` | the run's `run.json`, with any local path replaced by `<tmp>` |
| `recorded/reproduction.txt` | a second run compared byte for byte (recommended) |

Command, from the entry directory, writing only to an OS temporary
directory:

```
PYTHONPATH=<scientific-evidence-gate>/src PYTHONDONTWRITEBYTECODE=1 SCIENCE_GATE_FIXED_TIME=2026-09-26T00:00:00Z python -m science_gate.cli verify manifest.json --output <tmp>
```

A reproduced result shows conformance on declared fixtures only. It does
not show scientific validity or fitness for use.
