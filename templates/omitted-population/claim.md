# REPLACE-ENTRY-ID: claim

<!-- Guidance: if the entry is synthetic, keep the SYNTHETIC banner below as the
first thing a reader sees. If it is not synthetic, delete the banner and state
the data's owner, license and permission evidence instead. -->

> **SYNTHETIC.** Every file in this entry was generated for this corpus. The names, sites, values, works, authors, journals and DOIs (all under the 10.5555 test prefix) are invented. Nothing here describes real people, institutions, papers or datasets.

Category: `omitted-population`: a row accepted earlier is silently missing.

## Claim about the check

REPLACE: one paragraph stating the claim about the CHECK, not about the world.
Name the subcommand, the check ids and kinds, and the exact status, exit code
and reason a conforming verifier must produce.

## Setup

REPLACE: what the fixtures contain and which detail makes the check able to
appear to succeed without doing its work. Typically: the declared digest and row count were refreshed after the deletion, so only the snapshot comparison can see it.

## What would falsify the claim

REPLACE: the observation that would show the claim is false (another status or
exit code, a PASS, or a report that does not name the defect).

## What passing does not prove

Reproducing `expected-results.json` shows **conformance on declared fixtures only**:
science-gate produced the declared outcome on these synthetic fixtures, with the
tool version recorded in `environment.lock`.

- It does not show that science-gate catches this failure outside this entry.
- It does not establish scientific validity. The data is invented, so no
  scientific conclusion is supported or refuted.
- It does not show that science-gate, or any pipeline that uses it, is fit for
  any particular use.
