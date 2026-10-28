# receipts/ (template: partial-execution)

<COPY receipt.json FROM THE RECORDED RUN, byte for byte, and state its signature_state and
content_sha256.> It will be UNSIGNED unless `SCIENCE_GATE_HMAC_KEY_FILE` pointed at a key. An UNSIGNED
receipt detects accidental change only. A receipt supports integrity, provenance and replayability; it
does not establish scientific truth, accuracy, safety or fitness for use.

## What passing does not prove

- **Scope of a pass.** Reproducing an entry's expected outcome shows conformance on that declared
  fixture only. That is a performance claim about one declared case.
- **Not shown.** It does not show that the verifier catches failures outside the corpus. It does not
  show that any scientific conclusion is true. It does not show that the verifier is fit for any use.
