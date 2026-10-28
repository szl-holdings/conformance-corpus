# receipts/ (time-source-mismatch-synthetic-01, SYNTHETIC)

> **SYNTHETIC.** Every file in this entry was generated for this corpus. All names, places and values
> are invented. No real person, institution, paper, dataset or DOI appears.

`receipt.json` is the receipt of the recorded `science-gate verify` run (science-gate 0.1.0, commit in `../environment.lock`).

| field | value |
|---|---|
| signature_state | `UNSIGNED` |
| content_sha256 | `9051391bbdfd9922d24d33130da54302f144ebd971abbfac4eb1e5ed4966c29a` |
| run_id | `run-7e468bf65c2d53c1` |

## What this file holds

Since the section 17 upgrade, a science-gate run writes its receipt as two files: `receipt.json`, the
bare statement, and `receipt.auth.json`, the sidecar that carries `signature_state` and the content
hash. This corpus keeps them as one file: the receipt *record* that
`science_gate.receipts.build_run_receipt` returns, with the keys `body` (the statement, unchanged),
`content_sha256`, `signature_state`, `signature`, `key_id` and `detail`, written as canonical JSON.

- `science_gate.receipts.receipt_files(record)` turns it back into the run's `receipt.json` and
  `receipt.auth.json`. Both came back byte for byte when this record was written.
- Their SHA-256 digests, and the result of `verify_receipt_documents` on them, are in
  `../evaluation/`.
- `verify_receipt` reads only the two-file form. Given this record file directly, it reports
  `LEGACY_ENVELOPE`; write the two files with `receipt_files` first.

## It is UNSIGNED

- **No key was configured.** `SCIENCE_GATE_HMAC_KEY_FILE` was unset, so `signature_state` is
  `UNSIGNED` and `signature` is null.
- **What its content hash does.** `content_sha256` detects accidental change only.
- **What it cannot do.** Anyone who can edit this directory can rewrite the statement and recompute
  its hash, so it is not an attestation.

## What a receipt does not establish

A receipt supports integrity, provenance and replayability of one run on the declared synthetic
fixtures. It does not establish scientific truth, accuracy, safety or fitness for use. Its
`body.evidence_boundary.scientific_validity` is `NOT ESTABLISHED`. Passing this entry shows
conformance on declared fixtures only.
