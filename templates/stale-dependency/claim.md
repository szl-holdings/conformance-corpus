# <REPLACE: entry title> (stale-dependency)

> **SYNTHETIC.** Every file in this entry was generated for the conformance corpus. The names, sites, reviewers, values and dates are invented, and no real person, institution, paper or data set is involved. **Passing shows conformance on declared fixtures only. It does not show scientific validity or fitness for use.**

<!-- Keep the SYNTHETIC banner above for any synthetic entry. Remove it only for a non-synthetic entry, and
     then state the data's origin and permissions instead. -->

**Entry:** `<REPLACE: entry id>`. **Category:** `stale-dependency` (an upstream artifact changed beneath a conclusion).
**Failure mode:** `STALE_DEPENDENCY`. **Status:** draft, not independently
reviewed.

## The claim about the check

<REPLACE: the same text as entry.json claim_tested. Pattern: Given a dependency graph in which <upstream node> no longer matches its recorded SHA-256 while <conclusion node> is byte-identical to its own recorded digest, science-gate verify with a required dependency_currency check reports FAIL (exit 1, reason SOURCE_MISMATCH, failure modes exactly [STALE_DEPENDENCY]) and names the stale conclusion, instead of passing because the conclusion file is unchanged.>

## The case

<REPLACE: what the fixture contains. Why a check could appear to succeed.
What a conforming verifier must do.>

## Expected outcome

Run from the entry directory:

```
PYTHONPATH=<scientific-evidence-gate>/src PYTHONDONTWRITEBYTECODE=1 \
SCIENCE_GATE_FIXED_TIME=2026-09-26T00:00:00Z \
python -m science_gate.cli verify manifest.json --output <tmp>
```

- **Status:** `FAIL`
- **Exit code:** `1`
- **Reason:** `SOURCE_MISMATCH`
- **Failure modes:** exactly `["STALE_DEPENDENCY"]`
- **`report.md` must mention:** <REPLACE: the must_mention strings>

## What passing does not prove

- Passing this entry shows only that a verifier produced the declared outcome (status, exit code, reason, failure modes and required report strings) on these declared SYNTHETIC fixtures. It is a conformance result on declared fixtures only.
- It does not show that the verifier catches this failure outside this corpus, in other data, or when the failure takes another form.
- It does not show that any scientific conclusion is true or false. The data, the study and the conclusion here are invented and mean nothing.
- It does not show that the verifier, or anything checked with it, is fit for any particular use.
- <REPLACE: category-specific limits>
