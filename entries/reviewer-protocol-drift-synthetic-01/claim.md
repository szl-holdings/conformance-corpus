# Reviewer protocol drift: a missing reviewer hidden by a case-variant duplicate verdict (SYNTHETIC)

> **SYNTHETIC.** Every file in this entry was generated for the conformance corpus. The names, sites, reviewers, values and dates are invented, and no real person, institution, paper or data set is involved. **Passing shows conformance on declared fixtures only. It does not show scientific validity or fitness for use.**

**Entry:** `reviewer-protocol-drift-synthetic-01`. **Category:** `reviewer-protocol-drift`. **Failure mode:**
`PROTOCOL_DRIFT`. **Status:** draft, not independently reviewed.

## The claim about the check

Given three required reviewers (syn-reviewer-a, syn-reviewer-b, syn-reviewer-c) and three recorded verdicts, where syn-reviewer-c recorded none and syn-reviewer-b recorded two under spellings that differ only in case and trailing whitespace ('syn-reviewer-b' and 'SYN-Reviewer-B '), science-gate verify with a required reviewer_protocol check reports ABSTAIN with exit code 2, reason PROTOCOL_BROKEN and failure modes exactly [PROTOCOL_DRIFT], and its report names syn-reviewer-c as recording no verdict and syn-reviewer-b as recording more than one. It must not PASS because the number of verdicts equals the number of required reviewers.

## The case

**What the fixture contains.** The manifest requires three reviewers:
`syn-reviewer-a`, `syn-reviewer-b` and `syn-reviewer-c`.
`fixtures/reviews/verdicts.json` (`science-gate-reviews/v1`) records three
verdicts:

| # | reviewer as written | verdict |
|---|---|---|
| 1 | `syn-reviewer-a` | ACCEPT |
| 2 | `syn-reviewer-b` | ACCEPT |
| 3 | `SYN-Reviewer-B ` (upper case, trailing space) | ACCEPT |

**Why a check could appear to succeed.** Three verdicts for three required
reviewers, all ACCEPT, looks complete. A check that counted verdicts, or
that compared reviewer names byte-for-byte, would treat entry 3 as a third
reviewer. The required `rows` and `columns` checks pass on
`fixtures/data/samples.csv`.

**What a conforming verifier must do.** It must compare reviewer identities
after trimming and case folding. It must then report that `syn-reviewer-c`
recorded no verdict and that `syn-reviewer-b` recorded two. For
science-gate that is `verify manifest.json` with the outcome below.

## Expected outcome

Run from this directory:

```
PYTHONPATH=<scientific-evidence-gate>/src PYTHONDONTWRITEBYTECODE=1 \
SCIENCE_GATE_FIXED_TIME=2026-09-26T00:00:00Z \
python -m science_gate.cli verify manifest.json --output <tmp>
```

- **Status:** `ABSTAIN`
- **Exit code:** `2`
- **Reason:** `PROTOCOL_BROKEN`
- **Failure modes:** exactly `["PROTOCOL_DRIFT"]`
- **`report.md` must mention:** `PROTOCOL_DRIFT`, `PROTOCOL_BROKEN`, `syn-reviewer-c`, `recorded no verdict`, `syn-reviewer-b`, `more than one verdict`

`expected-results.json` holds the machine-readable form. `evaluation/`
holds the recorded run.

## What passing does not prove

- Passing this entry shows only that a verifier produced the declared outcome (status, exit code, reason, failure modes and required report strings) on these declared SYNTHETIC fixtures. It is a conformance result on declared fixtures only.
- It does not show that the verifier catches this failure outside this corpus, in other data, or when the failure takes another form.
- It does not show that any scientific conclusion is true or false. The data, the study and the conclusion here are invented and mean nothing.
- It does not show that the verifier, or anything checked with it, is fit for any particular use.
- It does not show that the reviewers exist, that they are independent, or that their verdicts are sound. The reviewers are invented names.
- An ABSTAIN here is not a finding that the reviewed work is wrong; it means the review protocol was not completed.
