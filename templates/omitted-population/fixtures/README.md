# fixtures/ (placeholder)

Replace this README with the entry's data files:

- `<data>.csv`: the current export, missing at least one accepted row.
- `snapshots/accepted.json`:
  `{"schema": "science-gate-snapshot/v1", "inputs": {"<input id>": {"row_key": ["<key column>"], "rows": [{"key": ["<key value>"], "sha256": "<row digest>"}]}}}`
  A row digest is the sha256 of the canonical JSON (sorted keys, separators
  `,` and `:`, UTF-8) of the row as `{column: value}` with every value a string.

Obviously fictional names only.
