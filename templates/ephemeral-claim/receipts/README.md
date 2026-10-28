# receipts: ephemeral-claim-synthetic-NN

Put here the `receipt.json` of the recorded run, copied unchanged.

- **Signing.** It is UNSIGNED unless `SCIENCE_GATE_HMAC_KEY_FILE` was set.
  Never record the key itself.
- **Checking it.** Confirm that its content hash recomputes, using
  `science_gate.receipts.verify_receipt`.
- **What it does not prove.** A receipt supports integrity, provenance and
  replayability. It does not establish scientific truth, accuracy, safety
  or fitness for use.

This file is a placeholder until the entry is instantiated.

## What passing this entry does not prove

- **Scope of a pass.** Reproducing `expected-results.json` shows conformance
  on this declared fixture only. That is a performance claim about declared
  fixtures.
- **What it does not show.** It does not show scientific validity. It does
  not show that the verifier catches failures outside the corpus, or that
  the tool is fit for any particular use.
