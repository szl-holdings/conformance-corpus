# tests/

`test_corpus.py` checks the corpus. It uses only the Python standard library
(`unittest`, Python 3.11 or later). It runs science-gate once for each
entry. The corpus is a fixture collection, not a benchmark.

## Run it

From the corpus root (`conformance-corpus/`), in a POSIX shell such as Git Bash:

```sh
PY=python   # or the full path of a Python 3.11+ interpreter
"$PY" -B -m unittest discover -s tests -v
```

The same command works in PowerShell with `$PY` replaced by the interpreter
(`python`, or its full path).
`"$PY" -B tests/test_corpus.py` does the same as the discover command.
`-B` keeps a `__pycache__/` directory out of `tests/`. Without it the
hygiene test `test_no_build_junk` fails, because the directory it creates
is build junk.

On the author's machine the full run has taken between about 30 and 80
seconds: 12 science-gate runs of about 1 to 7 seconds each, plus the static
checks.

Useful filters (`-k` matches part of a test name):

| Command | What runs |
|---|---|
| `-k test_0 -k Validator -k CorpusLayout -k CorpusHygiene` | static checks only, with no science-gate run (a few seconds) |
| `-k vacuous_pass` | every test for one entry |

### Settings

| Variable | Default | Meaning |
|---|---|---|
| `SCIENCE_GATE_SRC` | `../scientific-evidence-gate/src`, relative to the corpus root | the science-gate `src` directory put on `PYTHONPATH` |
| `SCIENCE_GATE_PYTHON` | the interpreter running the tests | the interpreter used to run science-gate |
| `CORPUS_RUN_TIMEOUT` | `600` | seconds allowed for each science-gate run |

If the science-gate source is not found, every run-based test **fails**. A
missing tool is never reported as a skip or a pass.

## Automated checks

GitHub Actions runs the same suite on Python 3.11 and 3.13 for pull requests
and pushes to `main`. It checks out science-gate at the reviewed commit
`6b0afb1a75517e95594295b2c991c71f26c7866f`, with history so the existing
`environment.lock` provenance assertions can resolve recorded commits.
Changing that source pin requires reviewing the resulting fixture behavior;
it does not rewrite the entries' intended outcomes or historical locks.

Empty discovery and a run with no completed passing tests fail. Documented
`expectedFailure` results remain visible and are counted separately from
completed passing tests. A green workflow therefore does not mean every known
tool gap is resolved. An unexpected success still fails so the documented gap
can be reviewed instead of silently disappearing.

## What is checked

**Corpus level:**

- The entry layout, read from the tree in `../README.md`, and the category
  list, read from its table.
- One template exists for each category.
- Every template has the full layout plus its `README.md`. Every layout
  directory holds at least one file, because git does not keep empty
  directories. The template JSON files parse.
- The small JSON Schema validator rejects what the schemas forbid (self-tests).

**Publication hygiene (`CorpusHygieneTests`), over every file outside `.git`:**

- No build junk: no `__pycache__/`, `*.pyc`, temporary or backup files,
  `science-gate-runs/` or `corpus-run-*` directories.
- No local or personal data: no home-directory path (`<drive>:` followed by
  `Users`, `/home/<name>/`, `AppData`), no email address, and neither the
  home directory nor the user name of the machine running the tests. A
  failure names the file and line, not the matched text. Generic account
  names such as `runner` or `ubuntu` are not searched for.
- LF line endings in every file.
- Every DOI uses the `10.5555` test prefix.
- Every line that mentions "benchmark" also says "not" or "never".
  `test_corpus.py` is not scanned, since it names `benchmark_score` (never a
  corpus claim) to test that the schema rejects it.
- No license has been chosen: no `LICENSE`, `COPYING` or `NOTICE` file, and
  every `source_licenses[].license` is `NOASSERTION`.
- No template placeholder is left in an entry. The templates mark their
  placeholders in several ways, and each is searched for:
  - `REPLACE`;
  - an upper-case `<...>` token such as `<ENTRY_ID ...>`;
  - `<e.g. ...>`;
  - a `(placeholder)` or `(template ...)` heading;
  - an `-synthetic-NN` id.
- Every `receipts/receipt.json` is UNSIGNED, with a null signature and
  `scientific_validity` `NOT ESTABLISHED`. Its README says UNSIGNED and says
  that a receipt does not establish scientific truth.
- Every `environment.lock` records the science-gate version and a 40-hex
  commit, and `git cat-file -t` in the science-gate repository (the parent
  of `SCIENCE_GATE_SRC`) reports that commit as a `commit`. This is the one
  test that starts a git process. It fails when git or the repository is
  missing. It does not check that the commit is the latest one; the
  printed summary lists the locks' commits next to the current HEAD.

**Per entry, static checks (`test_01` to `test_09`):**

1. `entry.json` validates against `intake-schema.json` and the
   `permissions-schema.json` it references. The validator implements the
   keywords the two schemas use: `type`, `enum`, `const`, `required`,
   `properties`, `additionalProperties`, `pattern`, `minLength`,
   `minItems`, `items`, `$ref`, `allOf`, `if`/`then`/`else`. It raises an
   error on any other keyword, so a schema change can never be silently
   ignored.
2. `entry_id` equals the directory name, in `entry.json` and in `expected-results.json`.
3. A synthetic entry is labeled synthetic:
   - `synthetic: true` and `access_class: SYNTHETIC` in `entry.json`;
   - "synthetic" in its id or title;
   - a `SYNTHETIC` label in `claim.md` and `limitations.md`.
4. Training permission is never implied. `training_allowed` must be an
   explicit boolean. It must be `false` when `evidence_of_grant` is
   `NOASSERTION`. The test also applies a stricter rule than the schema: it
   treats an `evidence_of_grant` string that itself says NOASSERTION as no
   grant. The schema's `if`/`then` fires only on the exact string
   `NOASSERTION`.
5. The permission rules, checked again by hand.
6. The entry has the layout that the corpus README declares.
7. `entry.json` (`does_not_prove`), `claim.md`, `limitations.md` and
   `expected-results.json` say what passing does not prove.
8. `expected-results.json` agrees with `entry.json` `expected_outcome` on
   status, exit code, reason, failure modes, `must_mention` and subcommand.
9. The entry's category has a template.

**Per entry, from one science-gate run (`test_20` and later):**

The run executes `expected_outcome.command` from `entry.json`:

- It uses list arguments, never a shell. The working directory is the entry
  directory.
- The environment sets `PYTHONPATH` to the science-gate source,
  `PYTHONDONTWRITEBYTECODE=1` and `SCIENCE_GATE_FIXED_TIME=2026-09-26T00:00:00Z`.
- Every other `SCIENCE_GATE_*` variable is removed, so no HMAC key is used
  and receipts are UNSIGNED.
- `--output` points into a fresh OS temporary directory, which is deleted
  afterwards. The run is offline, and a command containing `--live` is
  refused.

Only `verify` and `mutate` are accepted. `impact` and `revalidate` would
write into the entry.

The run is compared with the **intended** outcome:

| Test | Asserts |
|---|---|
| `test_20_status` | the `status` in `run.json` or `mutation-report.json` |
| `test_21_exit_code` | the process exit code, and `exit_code` in the document |
| `test_22_reason` | the primary `reason` |
| `test_23_failure_modes` | `failure_modes` as an exact set. A mutation report has no such field, so it counts as `[]` |
| `test_24_must_mention_NN_*` | one test per `must_mention` string: a case-sensitive substring of the report named by `must_mention_in` / `must_mention_scope` (`report.md` or `mutation-report.md`) |
| `test_25_must_not_mention` | where declared |
| `test_26_reasons_include` | where declared |
| `test_27_never_a_false_pass` | when the intended status is not PASS: no PASS status and no exit 0. A run with no readable document fails here |
| `test_28_headline_prefix` | where declared: the first stdout line |
| `test_29_run_leaves_the_entry_unchanged` | no file in the entry was added, removed or changed by the run |

### Not asserted

The per-check tables, per-citation or per-claim details, counters,
`additional_expectations`, and `supplementary_verify` runs are not
asserted. Neither are receipt contents, byte-for-byte determinism, or the
control runs described in some entries' `evaluation/` files. Those remain
recorded evidence that a reader can check, not automated assertions.

## Reading the results

- `ok`: the run matched that part of the intended outcome.
- `FAIL`: a divergence. The expected results must not be edited to match a
  run.
- `expected failure`: a divergence that the entry's own `known_failures`
  documents. The test still asserts the intended outcome. Only the rows in
  `DOCUMENTED_GAPS` can be marked this way, and only while the row's anchor
  text is still in `entry.json` `known_failures`. Each such row also gets a
  companion test (`..._divergence_is_the_documented_one`). The companion
  fails if the run diverges in a way the known failure does not describe.
- `unexpected success`: science-gate now meets an intended outcome that was
  documented as a gap. The run fails. Update `known_failures` and
  `DOCUMENTED_GAPS` after checking the change.

A summary is printed at the end of the run. It covers:

- the science-gate version, its git HEAD, and a SHA-256 digest of
  `src/science_gate/*.py`. A warning appears if that source changed during
  the session.
- the science-gate commit(s) recorded in the entries' `environment.lock`
  files. When they differ from the HEAD above, or when the science-gate
  checkout has uncommitted changes (the summary does not show those; use
  `git status`), the locks and `evaluation/` records describe another
  source and must be refreshed before publication.
- expected vs actual status, exit code and reason for every entry, with each
  divergence;
- every documented gap, with the `known_failures` text that justifies it.

To document a new gap:

1. Record it in the entry's `entry.json` `known_failures` (and
   `unresolved_cases` if it is open).
2. Add a `DocumentedGap` row whose `anchor` is a verbatim fragment of that
   text.
3. Never change `expected-results.json` or `expected_outcome` to match a run.

## What passing these tests does not prove

Passing shows that science-gate behaves as declared on these synthetic
fixtures only, which is conformance on declared fixtures. It does not show
that science-gate catches failures outside the corpus. It does not show
that any scientific conclusion is true, or that science-gate is fit for any
particular use.
