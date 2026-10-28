# Mutation report

## STATUS

**FAIL** (INVALID_BASELINE), exit code 1.

No sensitivity figure was produced because the verifier failed its accepting baseline.

Report `mut-3f40cabadd6f265e` for manifest `manifest.json` (sha256 `920bd0fac69904844b728031fc5c4404f2507a27c974c2636555a912ca439d01`), generated 2026-09-26T00:00:00Z.

## BASELINE

The untouched copy verified as **FAIL** (SOURCE_MISMATCH), run `run-debea99fd49b07b0`: expected_inputs 1, inputs_opened 1, rows_examined 4, checks_expected 4, checks_executed 4.
- finding check:depth: FAIL SOURCE_MISMATCH: numeric_agreement CHECKED FAIL: key ['CW-03']: stored value rounds half-even to 97.15 at 2 decimal(s), not 97.51

## WHAT THIS RESULT DOES NOT PROVE

- Mutation testing measures how this verifier reacted to the injected defects on this one evidence tree. Defects of other kinds, or the same defects in other trees, may still go undetected.
- A detected mutation shows that a detector fired, not that the evidence it guards is scientifically valid. Scientific validity is not established by this tool.
- Every verify ran offline with a network opener that refuses all requests; live citation lookups were not exercised.
