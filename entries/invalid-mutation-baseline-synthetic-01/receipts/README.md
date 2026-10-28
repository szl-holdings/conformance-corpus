# receipts: invalid-mutation-baseline-synthetic-01

> **SYNTHETIC.** Every file here was generated for this corpus. All names,
> places and values are invented. No real person, institution, paper,
> dataset or DOI appears.

`receipt.json` is the run receipt from the supplementary `science-gate verify` run (mutate writes no receipt). It is copied unchanged
from the run directory.

## It is UNSIGNED

- **No key was configured.** `SCIENCE_GATE_HMAC_KEY_FILE` was unset, so
  `signature_state` is `UNSIGNED` and `signature` is null.
- **What its content hash does.** `content_sha256` detects accidental
  change.
- **What it cannot do.** Anyone able to edit this directory could rewrite
  and rehash the receipt, so it is not an attestation.
- **Re-checking it.** Use `science_gate.receipts.verify_receipt`. The
  result of that check at recording time is in
  `../evaluation/comparison.json`.

## What a receipt does not prove

A receipt supports integrity, provenance and replayability. It does not
establish scientific truth, accuracy, safety or fitness for use. Its
`evidence_boundary.scientific_validity` is `NOT ESTABLISHED`.

## What passing this entry does not prove

- **Scope of a pass.** Reproducing `expected-results.json` shows conformance
  on this declared, synthetic fixture only.
- **What it does not show.** It does not show scientific validity. It does
  not show that the verifier catches failures outside the corpus, or that
  the tool is fit for any particular use.
