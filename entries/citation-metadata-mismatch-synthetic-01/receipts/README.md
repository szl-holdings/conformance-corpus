# receipts/

`receipt.json` is the receipt of the recorded run of `citation-metadata-mismatch-synthetic-01` (SYNTHETIC).
It contained no local path, so it is kept unchanged.

- **Signature: UNSIGNED.** No HMAC key was configured
  (`SCIENCE_GATE_HMAC_KEY_FILE` was unset). Its `content_sha256` detects
  accidental change only. Anyone who can edit these files can rewrite and
  rehash it.
- **What a receipt supports.** Integrity, provenance and replayability of one
  run on the declared synthetic fixtures. It does not establish scientific
  truth, accuracy, safety or fitness for use. Passing shows conformance on
  declared fixtures only.
- **Re-checking it.** `science_gate.receipts.verify_receipt` recomputes its
  `content_sha256` from the body. The digests of the original run files are in
  `../evaluation/command.json`.
