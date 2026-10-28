# review/ (template: partial-execution)

Empty until reviewed. An independent reviewer (not the author) adds one record here: who, when, what
they checked, and whether they agree with `expected-results.json` and `known_failures`. Only then is
their name added to `entry.json` `provenance.reviewed_by`. An entry with no reviewers is a draft.

## What passing does not prove

- **Scope of a pass.** Reproducing an entry's expected outcome shows conformance on that declared
  fixture only. That is a performance claim about one declared case.
- **Not shown.** It does not show that the verifier catches failures outside the corpus. It does not
  show that any scientific conclusion is true. It does not show that the verifier is fit for any use.
