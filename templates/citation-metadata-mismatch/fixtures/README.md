# fixtures/ (placeholder)

Replace this README with the entry's data files:

- `observations.csv`: a small CSV input (header row; values are strings).
- `citations/entries.json`:
  `{"schema": "science-gate-citations/v1", "citations": [{"citation_id", "doi", "title", "authors": [{"family", "given"}], "year", "journal", "volume", "issue"}]}`
- `citations/frozen.json`:
  `{"schema": "science-gate-citations-frozen/v1", "records": [{"doi", "outcome": "FOUND|NOT_FOUND|ERROR", "http_status", "work": {...}, "retrieved_at", "request_url_or_query", "response_sha256", "resolver_identity", "resolver_schema_version", "live_refresh_performed"}]}`
  Use `https://resolver.invalid/...` request URLs; nothing is fetched.
- `citations/verification-log.json`:
  `{"schema": "science-gate-verification-log/v1", "claimed_verified", "verifier": {"name", "version"}, "entries": [{"citation_id", "claimed_status"}], "invocations": [{"invocation_id", "citation_id", "request", "response_sha256", "retrieved_at"}]}`

DOIs only under `10.5555`. Obviously fictional names only.
