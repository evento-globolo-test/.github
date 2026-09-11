## Acceptance surface

- [ ] Source repositories and third-party actions are pinned to immutable commits.
- [ ] Declared Git submodule, Zed, and native-package lanes are preserved.
- [ ] Product assertions execute; this is not a no-op smoke test.
- [ ] Failure and recovery paths execute where applicable.
- [ ] Failure classification is explicit: product regression, blocked dependency, or harness regression.
- [ ] Fixtures are synthetic and logs contain no credentials, private media, biometrics, or unredacted private content.
- [ ] Expensive live-provider, emulator, database, chaos, scale, and soak checks are scheduled or manually gated.
- [ ] Overlapping or superseded work has been semantically traced, including every unique invariant retained or intentionally rejected.

## Salvage check

If this PR supersedes or replaces an older one, say which, and name at least one
concrete thing carried forward from it (a test, a fixture, an error message, a
pin, a doc paragraph). See [`docs/pr-salvage-policy.md`](../docs/pr-salvage-policy.md).

- [ ] Supersedes nothing, **or** the salvaged item is named above.
