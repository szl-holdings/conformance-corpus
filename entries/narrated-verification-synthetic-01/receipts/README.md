# receipts/ (narrated-verification-synthetic-01, SYNTHETIC)

`receipt.json` is the run receipt from the recorded evaluation, copied byte for byte.

- signature_state: **UNSIGNED** (no key was configured; `signature` is null)
- content_sha256: `9764403743b5d82c55324e51adf464318480be29e07cefafc864af7ad446999b`
- The content hash was re-checked with `science_gate.receipts.verify_receipt` after copying: it holds.

An UNSIGNED receipt detects accidental change only. Anyone who can edit this directory can rewrite the
receipt and recompute its hash. A receipt supports integrity, provenance and replayability; it does not
establish scientific truth, accuracy, safety or fitness for use.

## What passing does not prove

- **Scope of a pass.** Reproducing this entry's expected outcome shows conformance on this declared
  synthetic fixture only. That is a performance claim about one declared case.
- **Not shown.** It does not show that the verifier catches failures outside the corpus. It does not
  show that any scientific conclusion is true. It does not show that the verifier is fit for any use.
