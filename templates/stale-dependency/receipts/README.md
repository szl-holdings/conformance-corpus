# Receipts (template)

<REPLACE: this placeholder with the recorded run's `receipt.json`, copied
byte for byte, and a short README.>

A receipt is UNSIGNED unless `SCIENCE_GATE_HMAC_KEY_FILE` was configured,
and its README must say so. Never commit the key. Editing a receipt breaks
its content hash, so a receipt that contains a local path must be
regenerated rather than edited.

A receipt supports integrity, provenance and replayability. It does not
establish scientific truth, accuracy, safety or fitness for use.
