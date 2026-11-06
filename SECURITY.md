# Security

This repository is a private fixture collection for scientific-evidence-gate:
entries, templates, the intake and permissions schemas, and a test suite that
uses only the Python standard library. It ships no installable package,
service or container image. This file says how to report a problem, what the
tests guard against, and what they do not.

## Reporting a problem

The corpus is unreleased and has not been published. Report a suspected
vulnerability privately to the repository owner, not in an issue or pull
request. Include the entry or file involved, the command, the exit code and
the output. Use synthetic data only: never put real credentials, personal
data or controlled data in a report.

- The organization-wide policy, with its reporting address and response
  times, is the
  [szl-holdings/.github security policy](https://github.com/szl-holdings/.github/blob/main/SECURITY.md).
- A problem in science-gate itself belongs to
  [scientific-evidence-gate](https://github.com/szl-holdings/scientific-evidence-gate/blob/main/SECURITY.md),
  whose security policy says what the tool protects against.

Examples of a problem in this repository: a file that holds personal, local
or third-party data; an entry whose command makes a run change the entry,
write outside its temporary directory or reach the network; a workflow with
more permissions than it uses.

## Supported versions

Only `main`. The corpus has no releases or tags.

## What the tests guard against

Each item is enforced by `tests/test_corpus.py`. `tests/README.md` describes
the checks in full.

- **Personal or local data.** `test_no_local_path_user_name_or_email` rejects
  home-directory paths, e-mail addresses, and the home directory and user
  name of the machine running the tests, in every file outside `.git`.
  Generic account names such as `runner` are not searched for. A failure
  names the file and line, not the matched text.
- **Build junk.** `test_no_build_junk` rejects `__pycache__/`, `*.pyc`,
  temporary and backup files, and leftover run directories.
- **Run commands.** An entry's `expected_outcome.command` runs from the entry
  directory as a list of arguments, never through a shell, with a timeout
  (`CORPUS_RUN_TIMEOUT`, 600 seconds by default). Only `verify` and `mutate`
  are accepted, and a command with `--live` is refused. `--output` must
  start with the `<tmp>` placeholder, which becomes a fresh OS temporary
  directory that is deleted after the run; any other `<...>` placeholder is
  refused.
- **A run that changes its entry.** `test_29_run_leaves_the_entry_unchanged`
  fails if a run adds, removes or changes any file in the entry directory.
- **Receipt keys.** The run environment drops every `SCIENCE_GATE_*`
  variable the caller set and adds only `SCIENCE_GATE_FIXED_TIME`, so no HMAC
  key is used, and `test_receipts_are_unsigned_and_not_called_proof` requires
  every committed `receipts/receipt.json` to be UNSIGNED with a null
  signature.

## What they do not guard against

- **Credentials.** No test scans for tokens, keys or passwords. A secret in a
  fixture would not be caught by the tests.
- **The rest of the environment.** Apart from the `SCIENCE_GATE_*` variables
  and `PYTHONPATH`, `PYTHONHOME` and `PYTHONSTARTUP`, a run inherits the
  environment of the process that runs the tests.
- **`..` after `<tmp>`.** The `<tmp>` prefix is checked as text, so
  `--output <tmp>/../name` is accepted: the run then writes beside its
  temporary directory, and that output is not deleted afterwards. Every
  current entry writes inside the temporary directory.
- **Writes elsewhere.** The unchanged-entry check covers only the entry
  directory, not the rest of the file system.
- **Rewritten entries.** Receipts are UNSIGNED, and the tests check only
  their signature state and evidence boundary, never their digests. Anyone
  who can edit the repository can change an entry and its receipt together.
- **Scientific validity.** Nothing in this corpus establishes that a
  scientific conclusion is true.
