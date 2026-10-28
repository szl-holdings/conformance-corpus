# Conformance corpus for scientific-evidence-gate

This is a **fixture collection**, not a benchmark. Each entry is a small,
self-contained case in which a check can appear to succeed without doing the
work it claims. Each entry states the exact outcome that a conforming verifier
must produce.

It will not be called a benchmark until it holds multiple independently
contributed and independently reviewed cases. Today every entry is synthetic
and was written by one author.

## What an entry is

```
entries/<entry-id>/
├── entry.json            intake record (intake-schema.json): question, claim, falsifier,
│                         owners, permissions, exact expected outcome, limits
├── claim.md              the claim about the check, in prose
├── limitations.md        what passing does not prove; synthetic status
├── manifest.json         science-gate-manifest/v1: the run to perform
├── expected-results.json the exact status, exit code, reason and strings the report must contain
├── environment.lock      interpreter and tool versions the expected results were produced with
├── schemas/              any schema the fixtures use
├── fixtures/             the data (synthetic here)
├── evaluation/           how to evaluate locally, and the recorded evaluation output
├── receipts/             receipts from the recorded evaluation (UNSIGNED unless a key was configured)
└── review/               independent review records (empty until reviewed)
```

`templates/` holds one template per failure category. `tests/` checks that:

- every entry matches `intake-schema.json` and `permissions-schema.json`
- every synthetic entry is labeled synthetic
- training permission is never implied by evaluation permission
- every template has the full layout
- running `science-gate` on the entry reproduces the intended status, exit
  code, reason, failure modes and report strings in `expected-results.json`.
  A divergence fails, unless the entry's own `known_failures` documents it
  (then it is reported as an expected failure).
- the publication-hygiene rules hold:
  - no local path, user name, email address, build junk or leftover
    template placeholder;
  - LF line endings and DOIs under `10.5555` only;
  - the corpus is never called a benchmark;
  - no license chosen, and UNSIGNED receipts;
  - every `environment.lock` names a science-gate commit that exists.

`tests/README.md` lists what is and is not asserted.

## Categories

| Template | What it exercises |
|---|---|
| vacuous-pass | a check reports success over zero examined rows |
| narrated-verification | a log claims verifications that have no invocation records |
| partial-execution | a required check never reached a terminal state |
| citation-metadata-mismatch | frozen metadata disagrees with the cited author or DOI |
| omitted-population | a row accepted earlier is silently missing |
| coverage-debt | a declared check had nothing to look at |
| stale-dependency | an upstream artifact changed beneath a conclusion |
| time-source-mismatch | an observation falls outside the requested evidence window |
| reviewer-protocol-drift | a required reviewer is missing, or a verdict is duplicated |
| ephemeral-claim | a manuscript number has no registered derivation |
| invalid-mutation-baseline | mutation sensitivity is requested while the baseline fails |
| verifier-blind-spot | a declared mutation escapes detection |

## Permissions

- Every entry declares an access class (`PUBLIC`, `REFERENCE_ONLY`, `SYNTHETIC`,
  `CONTROLLED_LOCAL`) and six explicit permission flags.
- **Evaluation permission does not imply training permission.**
- Controlled data stays local. A public package carries only schemas, hashes,
  expected results, approved redactions and local execution instructions.
- No third-party data is included. Real artifacts will be added only with
  confirmed permission.

## What passing an entry does not prove

- **Scope of a pass.** A verifier that reproduces every expected result has
  shown that it behaves as declared on these cases. That is a performance
  claim about declared fixtures.
- **What it does not show.** It does not show that the verifier catches
  failures outside the corpus. It does not show that any scientific
  conclusion is true. It does not show that the verifier is fit for any
  particular use.

## Status

- **Stage.** Local draft. The corpus has not been published.
- **License.** None has been chosen (`NOASSERTION`).
- **Reviews.** The entries have not been independently reviewed. Every
  `provenance.reviewed_by` is empty.
- **Size.** 12 entries in 12 categories, one entry per category, and 12
  templates.
  - All 12 entries are synthetic, with access class `SYNTHETIC`.
  - Evaluation is allowed. Every other permission, including training, is
    false.
- **Last test run.** On 2026-10-06, `tests/test_corpus.py` printed `Ran
  280 tests` and `OK (expected failures=3)`.
  - It ran science-gate 0.1.0 at commit `7ec36c6`, plus uncommitted changes
    to `src/science_gate/_html.py` and `tests/test_html.py` made by a
    concurrent process. The test run prints a digest of the source it used
    (`932b23f64a2b0037...`).
  - Each entry was run once.
  - Passing shows conformance on declared fixtures only.
- **Audit re-run (2026-09-29).** An audit pass that did not write the
  entries re-ran every entry's `expected_outcome.command` into an OS temporary
  directory. It also re-ran the two supplementary `verify` runs of the mutate
  entries, the three repaired-fixture controls, and `science-gate report` on
  three run directories.
  - Every status, exit code, reason and failure-mode set matched the entry's
    `evaluation/` record.
  - Every kept `report.md`, `mutation-report.md`, `run.json` and receipt
    was byte-identical to the re-run. Where only a SHA-256 of a run file is
    kept, the re-run file had that digest.
  - All 12 receipts pass `verify_receipt` as UNSIGNED.
  - This re-run is not an independent review of the expectations. No
    `reviewed_by` was changed.
- **Audit re-run (2026-10-06).** A second audit pass re-ran the following,
  each into an OS temporary directory:
  - every entry's `expected_outcome.command`;
  - the two supplementary `verify` runs;
  - the three repaired-fixture controls, on temporary copies;
  - `science-gate report` on three run directories;
  - every entry a second time with `PYTHONHASHSEED=4242`.

  The results were:
  - Every status, exit code, reason, failure-mode set and stdout headline
    matched the entry's `evaluation/` record.
  - Every kept `report.md`, `mutation-report.md`, `run.json` and receipt was
    byte-identical to the re-run, and so were the `PYTHONHASHSEED=4242` runs.
  - Every run-file digest kept in `evaluation/command.json` or
    `evaluation/result.json` reproduced, except `report.html` in
    citation-metadata-mismatch, coverage-debt and omitted-population. The
    science-gate source used differs from commit `7ec36c6` only in the
    uncommitted `src/science_gate/_html.py`, the module that renders
    `report.html`. No entry keeps or asserts that file.
  - Each control reproduced PASS, exit 0, VERIFIED. The citation and
    omitted-population controls also reproduced their recorded headline,
    including the run id. The coverage-debt control did not reproduce its
    run id, because `control.json` does not record the exact event that was
    added.
  - Nine locks claim a clean worktree. Their source digests recompute from
    commit `7ec36c6`, which supports that claim.
  - No run changed a file in its entry. This re-run is not an independent
    review either.
- **Reproduction.** 10 of 12 entries reproduce every asserted field of their
  intended outcome: citation-metadata-mismatch, coverage-debt,
  ephemeral-claim, invalid-mutation-baseline, narrated-verification,
  omitted-population, reviewer-protocol-drift, stale-dependency,
  time-source-mismatch and verifier-blind-spot. Two entries diverge in
  part. Each divergence is documented in the entry's `known_failures`:
  - `vacuous-pass-synthetic-01`. Status ABSTAIN, exit code 2 and reason
    INSUFFICIENT_EVIDENCE match. Its failure modes are `[PARTIAL_EXECUTION,
    VACUOUS_PASS]`, not `[VACUOUS_PASS]`. `report.md` lacks
    `rows_examined`: it reports 1 row examined for an input with 0 data
    records.
  - `partial-execution-synthetic-01`. Status ABSTAIN, exit code 2, the
    failure modes and every `must_mention` string match. Its primary reason
    is INSUFFICIENT_EVIDENCE, not PARTIAL_EXECUTION.

  No entry produced a PASS or exit code 0 where the intended outcome was not
  PASS. No run changed a file in its entry.
- **Known tool gaps.** There are four, all recorded in the entries'
  `known_failures`:
  1. In vacuous-pass, required checks that are NOT_APPLICABLE count as not
     executed, which adds PARTIAL_EXECUTION. This may be a taxonomy
     disagreement rather than a defect. coverage-debt expects the same
     behaviour (see the first open item below).
  2. In vacuous-pass, the run-level `rows_examined` counts a pin comparison
     as a row, so the PASS contract's zero-rows rule never fires. The run
     still abstains.
  3. In partial-execution, the primary-reason precedence names the missing
     document instead of the required check that did not execute.
     coverage-debt expects that precedence (see the second open item below).
  4. In partial-execution, `verify` cannot be given a check that started and
     never finished, so the category is reached only through the
     `checks_executed` counter. This gap is documented but no test asserts
     it.

  The tests assert gaps 1 to 3 against the intended outcome and mark them
  `expectedFailure`.
- **Open corpus items.** None of these makes a test fail. Each needs a
  decision by an independent reviewer. No expected outcome has been edited
  to resolve any of them.
  - **NOT_APPLICABLE and PARTIAL_EXECUTION.** coverage-debt intends
    `[PARTIAL_EXECUTION]` because one NOT_APPLICABLE required check is not
    counted as executed. vacuous-pass intends that NOT_APPLICABLE required
    checks do not add PARTIAL_EXECUTION, and it records the tool's
    PARTIAL_EXECUTION as a known failure. One rule cannot satisfy both.
  - **Primary-reason precedence.** coverage-debt intends
    INSUFFICIENT_EVIDENCE and partial-execution intends PARTIAL_EXECUTION.
    Both runs report the reasons `[INSUFFICIENT_EVIDENCE, PARTIAL_EXECUTION]`
    and the finding `checks_executed=3 of checks_expected=4`. The only
    difference is that the fourth check is NOT_APPLICABLE in one and SKIPPED
    in the other. No stated rule separates the two.
  - **Refresh before publication.** Every `environment.lock` and every
    `evaluation/` record is tied to science-gate commit `7ec36c6`. For
    ephemeral-claim, invalid-mutation-baseline and verifier-blind-spot, the
    lock also records an uncommitted worktree whose source digest no longer
    exists.
    - science-gate is still changing. Its `_html.py` changed again during
      the 2026-09-29 re-run. On 2026-10-06 its HEAD was still `7ec36c6`,
      with uncommitted changes to `src/science_gate/_html.py` and
      `tests/test_html.py`.
    - The `report.html` digests in three `evaluation/command.json` files no
      longer reproduce (see the 2026-10-06 audit above).
    - The locks, `evaluation/` records and receipts must be regenerated
      against the final science-gate commit, from a clean worktree.
    - At the refresh, record the exact repaired fixture of each control in
      its `control.json`. coverage-debt's control lacks it today.
  - **Lock formats.** The 12 `environment.lock` files use four different
    formats and several different source-digest methods. Standardize them
    at the refresh.
  - **Two row counts, one name.** Reports print "Rows examined in scope: N"
    beside a contract line `rows_examined=M`, which counts rows once per
    check. These are two quantities with one name. No expected result pins
    either of them.
