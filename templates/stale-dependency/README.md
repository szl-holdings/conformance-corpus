# Template: stale-dependency

This template is for entries in which an upstream artifact changed beneath a conclusion.

**Using the template.**

1. Copy this directory to `entries/<entry-id>/`.
2. Replace every `<REPLACE: ...>` value.
3. Generate the fixtures (see `fixtures/README.md`).
4. Write the **intended** outcome before running anything.
5. Run the command in `evaluation/README.md`.
6. Record the run in `evaluation/` and the receipt in `receipts/`.

A copied template fails `intake-schema.json` validation until its
`entry_id` placeholder is replaced. That is deliberate. The other
placeholders are plain strings, and schema validation cannot catch them.
Search the copy for `<REPLACE` before treating it as an entry.

**Rules for every entry.**

- **Invented data only.** Data is SYNTHETIC unless its permissions are
  confirmed. Names are obviously invented. DOIs, if any, use only the
  `10.5555` test prefix. No real person, institution, paper or data set
  appears.
- **Small entries.** Keep an entry to a few KB.
- **Honest labels.** Label synthetic entries SYNTHETIC in `entry.json`,
  `claim.md` and `limitations.md`.
- **Missing evidence is never a PASS.**
- **Record disagreements.** If science-gate disagrees with the intended
  outcome, keep the intended outcome in `expected-results.json` and list
  the mismatch. Record it in `entry.json` `known_failures`.
- **Say what a pass does not show.** Every file that describes an entry
  says what passing does not prove: it shows conformance on declared
  fixtures only, not scientific validity or fitness for use.

## Fixture recipe: stale-dependency

1. **Data file.** Write a small data file, for example
   `fixtures/data/<name>.csv`, with 4 to 10 invented rows. Declare it
   in `manifest.json` as a required input. Give it its `sha256`, an
   INDEPENDENT `expected_rows` and a `row_key`.
2. **Node files.** Write one file per graph node: SOURCE_SNAPSHOT,
   DESIGN, an intermediate node (ANALYSIS_RUN or
   RANKING_OR_MEASUREMENT), and a CONCLUSION or FIGURE_OR_TABLE.
3. **Recorded design.** Record the SHA-256 of the *original* upstream
   file (for example the design) as its `recorded_sha256`. Keep that
   original text as `fixtures/design/protocol-as-recorded.md` so a
   reviewer can reproduce the digest.
4. **Changed design.** Put a *changed* version at the node's `path`.
   Make it a small, meaningful change, such as an admission threshold.
5. **Unchanged conclusion.** Every other node, and the conclusion in
   particular, must match its recorded digest. The entry then tests
   propagation, not a changed conclusion file.
6. **Graph file.** Write `fixtures/graph/graph.json` with node paths
   relative to the **manifest directory**, not to the graph file:

```json
{
  "schema": "science-gate-graph/v1",
  "nodes": [
    {"id": "source-x", "kind": "SOURCE_SNAPSHOT", "path": "fixtures/data/x.csv",
     "recorded_sha256": "<64 hex>", "validity": "CURRENT", "history": []},
    {"id": "design-x", "kind": "DESIGN", "path": "fixtures/design/protocol.md",
     "recorded_sha256": "<sha256 of protocol-as-recorded.md>", "validity": "CURRENT", "history": []},
    {"id": "means-x", "kind": "RANKING_OR_MEASUREMENT", "path": "fixtures/analysis/means.csv",
     "recorded_sha256": "<64 hex>", "validity": "CURRENT", "history": []},
    {"id": "conclusion-x", "kind": "CONCLUSION", "path": "fixtures/conclusions/conclusion.md",
     "recorded_sha256": "<64 hex>", "validity": "CURRENT", "history": []}
  ],
  "edges": [["source-x", "means-x"], ["design-x", "means-x"], ["means-x", "conclusion-x"]]
}
```

**Do not run `impact` or `revalidate` inside the entry.** They write
`graph-state.json` beside the graph. A saved state is then read by every
later `verify`, and the entry would no longer be what it claims.
