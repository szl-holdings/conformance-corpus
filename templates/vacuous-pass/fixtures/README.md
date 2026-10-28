# fixtures/ (template: vacuous-pass)

> **SYNTHETIC ENTRY.** <KEEP THIS BANNER FOR SYNTHETIC ENTRIES. Every file was generated for this corpus;
> names, sites, citations and values are invented; DOIs use the 10.5555 test prefix only; nothing
> describes real people, institutions, papers or datasets. Say 'draft' until reviewed_by is non-empty.>

<DESCRIBE EACH FIXTURE FILE AND ITS ROLE.> Suggested layout for this category:

- `data/<EMPTY_FILE>.csv`: a header row and **zero** data records.
- `summary/<STORED_SUMMARY>.json`: `{"schema": "science-gate-summary/v1", "status": "PASS",
  "pinned": {"inputs": {"<INPUT_ID>": {"sha256": "<sha256 of the empty file>", "rows": 0}}}}`
  written by a fictional tool.

## What passing does not prove

- **Scope of a pass.** Reproducing an entry's expected outcome shows conformance on that declared
  fixture only. That is a performance claim about one declared case.
- **Not shown.** It does not show that the verifier catches failures outside the corpus. It does not
  show that any scientific conclusion is true. It does not show that the verifier is fit for any use.
