# Receipts: `time-source-mismatch-synthetic-01`

> **SYNTHETIC.** Every file in this entry was generated for the conformance corpus. The names, sites, reviewers, values and dates are invented, and no real person, institution, paper or data set is involved. **Passing shows conformance on declared fixtures only. It does not show scientific validity or fitness for use.**

`receipt.json` is the receipt that the recorded evaluation wrote
(`science-gate-receipt/v1`), copied byte for byte.

| field | value |
|---|---|
| signature_state | `UNSIGNED` |
| content_sha256 | `12d1dee641f300f6c83103fa3f1c94117a0342c871232a149526b42373b657da` |
| run_id | `run-7e468bf65c2d53c1` |

**The receipt is UNSIGNED.** No `SCIENCE_GATE_HMAC_KEY_FILE` was
configured. Its content hash detects accidental change. Anyone who can edit
this file can rewrite it and recompute the hash.

To re-check the content hash, run this with `PYTHONPATH` set as in
`../evaluation/command.txt`:

```
python -c "from science_gate.receipts import verify_receipt; print(verify_receipt('receipts/receipt.json'))"
```

A receipt supports integrity, provenance and replayability. It does not
establish scientific truth, accuracy, safety or fitness for use. Passing
this entry shows conformance on declared fixtures only.
