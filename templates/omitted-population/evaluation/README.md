# evaluation/ (placeholder)

Replace with:

- `README.md`: how to evaluate this entry locally (the exact command, the
  environment variables, and what to compare).
- `command.json`: the exact argv, working directory and environment of the
  recorded run, its exit code and its stdout, with local paths replaced by
  `<tmp>` (the OS temp output directory), `<entry>` and `<seg>`.
- `report.md` and the run's JSON result, copied from the recorded run with
  local paths replaced.
- `comparison.json`: each field of `expected-results.json` next to what the
  recorded run produced, and whether they match.

Always pass `SCIENCE_GATE_FIXED_TIME=2026-09-26T00:00:00Z` and an `--output`
inside an OS temp directory. Never write the run into the corpus directly.
