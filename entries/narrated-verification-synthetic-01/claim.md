# Claim: Citation log claims five verifications with two invocation records, synthetic

> **SYNTHETIC ENTRY.** Every file in this entry was generated for this corpus. The names, sites,
> citations and values are invented; DOIs use the 10.5555 test prefix. Nothing here describes real
> people, institutions, papers or datasets. This is a draft: it has not been independently reviewed.

## The check under test

A fictional citation checker, *inkwell-refcheck*, wrote a verification log. Its headline says five
citations were verified, and it lists all five (C1 to C5) as `VERIFIED`. It holds invocation records,
each with a request, a response digest and a retrieval time, for **C1 and C2 only**. For C3, C4 and C5
the verification is **narrated**: claimed, with no record of it having happened.

## The claim about the verifier

Given `manifest.json`, `science-gate verify` must return:

- status **ABSTAIN**, exit code **2**
- reason **UNVERIFIED**
- failure modes exactly **NARRATED_VERIFICATION**
- a report that mentions: `NARRATED_VERIFICATION`, `checked_claims_le_invocations`, `3 citation(s) claimed VERIFIED with no complete invocation record`, `5 claimed but only 2 invoked`, `C3`, `C4`, `C5`

ABSTAIN and UNVERIFIED, not FAIL: the three citations may well be right. They have not been *shown* to
be checked, and a verifier must not count them as checked.

**Falsified by:** science-gate returns PASS or exit code 0; or it counts C3, C4 or C5 as verified; or it reports checked_claims_le_invocations as holding; or it returns FAIL, which would treat unshown claims as shown false.

## Recorded result

The recorded run matches every intended field. See `evaluation/README.md`.

## What passing does not prove

- **Scope of a pass.** Reproducing this entry's expected outcome shows conformance on this declared
  synthetic fixture only. That is a performance claim about one declared case.
- **Not shown.** It does not show that the verifier catches failures outside the corpus. It does not
  show that any scientific conclusion is true. It does not show that the verifier is fit for any use.
