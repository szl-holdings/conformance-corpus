# Stale dependency: the study design changed beneath an unchanged conclusion (SYNTHETIC)

> **SYNTHETIC.** Every file in this entry was generated for the conformance corpus. The names, sites, reviewers, values and dates are invented, and no real person, institution, paper or data set is involved. **Passing shows conformance on declared fixtures only. It does not show scientific validity or fitness for use.**

**Entry:** `stale-dependency-synthetic-01`. **Category:** `stale-dependency`. **Failure mode:**
`STALE_DEPENDENCY`. **Status:** draft, not independently reviewed.

## The claim about the check

Given a dependency graph in which the DESIGN node study-design no longer matches its recorded SHA-256 (the admission rule changed from count >= 5 to count >= 8) while the CONCLUSION node conclusion-south-highest is byte-identical to its own recorded digest, science-gate verify with a required dependency_currency check reports FAIL with exit code 1, reason SOURCE_MISMATCH and failure modes exactly [STALE_DEPENDENCY], and its report names conclusion-south-highest and study-design as STALE_PENDING_REVALIDATION. It must not PASS because the conclusion file itself is unchanged.

## The case

**What the fixture contains.** `fixtures/graph/graph.json` declares four
nodes and three edges:

    source-plots (SOURCE_SNAPSHOT) ----\
                                        >--> site-means (RANKING_OR_MEASUREMENT) --> conclusion-south-highest (CONCLUSION)
    study-design (DESIGN) -------------/

**The change beneath the conclusion.** The recorded digest for
`study-design` is the SHA-256 of the design as it was when the conclusion
was established. That text is kept verbatim in
`fixtures/design/protocol-as-recorded.md`, where it uses the admission rule
*count >= 5*.

The file on disk, `fixtures/design/protocol.md`, is version 2. It uses the
admission rule *count >= 8*. Under that rule plot SYN-P04 would no longer be
admitted, so the synthetic-site-south mean of 19.25 in
`fixtures/analysis/site-means.csv` was computed under a design that no
longer applies.

**Why a check could appear to succeed.** Every other file matches its
recorded digest, including the conclusion itself. The required `rows` and
`columns` checks pass on `fixtures/data/plots.csv`. A check that re-hashed
only the conclusion, or only the declared inputs, would report success.

**What a conforming verifier must do.** It must propagate the change from
`study-design` through `site-means` to `conclusion-south-highest`, and block
publication. For science-gate that is `verify manifest.json` with the
outcome below.

## Expected outcome

Run from this directory:

```
PYTHONPATH=<scientific-evidence-gate>/src PYTHONDONTWRITEBYTECODE=1 \
SCIENCE_GATE_FIXED_TIME=2026-09-26T00:00:00Z \
python -m science_gate.cli verify manifest.json --output <tmp>
```

- **Status:** `FAIL`
- **Exit code:** `1`
- **Reason:** `SOURCE_MISMATCH`
- **Failure modes:** exactly `["STALE_DEPENDENCY"]`
- **`report.md` must mention:** `STALE_DEPENDENCY`, `STALE_PENDING_REVALIDATION`, `publication blocked`, `conclusion-south-highest`, `study-design`

`expected-results.json` holds the machine-readable form. `evaluation/`
holds the recorded run.

## What passing does not prove

- Passing this entry shows only that a verifier produced the declared outcome (status, exit code, reason, failure modes and required report strings) on these declared SYNTHETIC fixtures. It is a conformance result on declared fixtures only.
- It does not show that the verifier catches this failure outside this corpus, in other data, or when the failure takes another form.
- It does not show that any scientific conclusion is true or false. The data, the study and the conclusion here are invented and mean nothing.
- It does not show that the verifier, or anything checked with it, is fit for any particular use.
- It does not show that the changed design makes the conclusion wrong. STALE_PENDING_REVALIDATION means only that an upstream artifact changed after the conclusion was last established.
- A matching digest for the conclusion shows only byte identity, not that it was regenerated or that the analysis behind it is correct.
