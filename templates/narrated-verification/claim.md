# Claim: <TITLE>

> **SYNTHETIC ENTRY.** <KEEP THIS BANNER FOR SYNTHETIC ENTRIES. Every file was generated for this corpus;
> names, sites, citations and values are invented; DOIs use the 10.5555 test prefix only; nothing
> describes real people, institutions, papers or datasets. Say 'draft' until reviewed_by is non-empty.>

## The check under test

<DESCRIBE, in prose, the fictional tool or pipeline and how it shows the defect: a log claims verifications that have no invocation records.>

## The claim about the verifier

Given `manifest.json`, `science-gate verify` must return:

- status **ABSTAIN**, exit code **2**
- reason **UNVERIFIED**
- failure modes exactly **NARRATED_VERIFICATION**
- a report that mentions: <EACH must_mention STRING>

<WHY THIS STATUS AND NOT ANOTHER, e.g. why ABSTAIN and not FAIL.>

**Falsified by:** <COPY entry.json falsified_by>

## Recorded result

<WHETHER THE RECORDED RUN MATCHES; if not, what differs, and that expected-results.json was not changed.>

## What passing does not prove

- **Scope of a pass.** Reproducing an entry's expected outcome shows conformance on that declared
  fixture only. That is a performance claim about one declared case.
- **Not shown.** It does not show that the verifier catches failures outside the corpus. It does not
  show that any scientific conclusion is true. It does not show that the verifier is fit for any use.
