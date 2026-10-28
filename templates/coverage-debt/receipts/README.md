# receipts/ (placeholder)

Replace with the `receipt.json` of the recorded run (local paths replaced).
It is UNSIGNED unless `SCIENCE_GATE_HMAC_KEY_FILE` pointed to a key when the
run was made. An unsigned receipt's content hash detects accidental change
only; anyone who can edit the files can rewrite and rehash it.

A receipt supports integrity, provenance and replayability. It does not
establish scientific truth, accuracy, safety or fitness for use.
