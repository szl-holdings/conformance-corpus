# Template: ephemeral-claim

Exercises: **a manuscript number has no registered derivation**. Failure mode `EPHEMERAL_CLAIM`. Command: `science-gate verify`.

## How to use this template

1. **Copy the directory.** Copy it to `entries/ephemeral-claim-synthetic-NN/`, and
   replace `NN` with the next free number, lowercase digits only. The
   `entry_id` must match `^[a-z0-9][a-z0-9-]{2,63}$`. The template's own
   id, which contains `NN`, deliberately does not.
2. **Generate the fixtures.** Write them under `fixtures/` with invented,
   obviously fictional names. Use no real person, institution, paper or
   dataset. A DOI, if one is needed at all, goes under `10.5555` only.
   Compute every SHA-256 from the exact bytes written.
3. **Fill in the skeletons.** Replace every `<...>` placeholder in
   `manifest.json`, `entry.json`, `claim.md`, `limitations.md` and
   `expected-results.json`. Remove the `GUIDANCE` text as you go.
4. **Write the expected outcome first.** Fill in `expected-results.json`
   from the *intended* behaviour, as the tool's contract states it,
   before running anything.
5. **Run the tool.** Run `science-gate verify` as `evaluation/README.md`
   describes, and record the command, the output, the report and the
   JSON result in `evaluation/`. Local paths become `<tmp>`. Put the
   receipt in `receipts/`.
6. **Handle a mismatch honestly.** If the run disagrees with the intended
   outcome, **do not** edit the expectation to match, and do not modify
   the tool. Record the gap in `entry.json` `known_failures`, keep the
   intended outcome, and add a note.
7. **Validate `entry.json`.** It must validate against `intake-schema.json`
   and `permissions-schema.json`. Leave `provenance.reviewed_by` empty
   until an independent reviewer signs off in `review/`.

Every file that describes the entry must say what passing does not prove.
Missing evidence must never be turned into PASS.

## What passing this entry does not prove

- **Scope of a pass.** Reproducing `expected-results.json` shows conformance
  on this declared fixture only. That is a performance claim about declared
  fixtures.
- **What it does not show.** It does not show scientific validity. It does
  not show that the verifier catches failures outside the corpus, or that
  the tool is fit for any particular use.
