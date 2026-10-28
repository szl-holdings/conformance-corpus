# receipts/ (vacuous-pass-synthetic-01, SYNTHETIC)

`receipt.json` is the run receipt from the recorded evaluation, copied byte for byte.

- signature_state: **UNSIGNED** (no key was configured; `signature` is null)
- content_sha256: `1450ea286c3412eb0821a7bd07cc5ec90a532621b736106630b91ed2dd1808a4`
- The content hash was re-checked with `science_gate.receipts.verify_receipt` after copying: it holds.

An UNSIGNED receipt detects accidental change only. Anyone who can edit this directory can rewrite the
receipt and recompute its hash. A receipt supports integrity, provenance and replayability; it does not
establish scientific truth, accuracy, safety or fitness for use.

## What passing does not prove

- **Scope of a pass.** Reproducing this entry's expected outcome shows conformance on this declared
  synthetic fixture only. That is a performance claim about one declared case.
- **Not shown.** It does not show that the verifier catches failures outside the corpus. It does not
  show that any scientific conclusion is true. It does not show that the verifier is fit for any use.
