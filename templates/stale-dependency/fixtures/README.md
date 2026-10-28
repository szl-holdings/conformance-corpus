# Fixtures (template: stale-dependency)

<REPLACE: this placeholder with the entry's generated fixture files, and
keep a short README that lists them.>

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

All fixture data must be SYNTHETIC unless permissions are confirmed.
Passing an entry built from these fixtures shows conformance on declared
fixtures only. It does not show scientific validity or fitness for use.
