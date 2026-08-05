# evento-globolo-test governance

Organization-wide community health, privacy, and reusable workflow policy for Evento Globolo acceptance testing.

The live organization contains **26 test repositories** plus this governance repository:

- **17 generated specialized harnesses** covering API, browser, WebSocket, SDK, ticketing, recurrence, search, payments, permissions, offline sync, performance, infrastructure, and CLI contracts.
- **9 legacy readiness-gated harnesses** covering provider cross-posting, OAuth refresh, reconciliation, deduplication, and Flutter/web UI certification.

Both sets remain visible until their behavior and history have been semantically reconciled. Similar names are not evidence that one repository may be deleted.

## Policy

- Pin source repositories and third-party actions to immutable commits.
- Preserve declared Git submodule, Zed, and native-package dependency lanes.
- Run credential-free deterministic checks on pull requests.
- Classify failures as product regressions, blocked dependencies, or harness regressions.
- Treat missing upstreams and credentials as explicit gates, never successful tests.
- Use only approved short-lived GitHub App installation tokens for gated private cross-organization access; do not add PAT fallbacks or persistent fleet tokens.
- Keep production user data, private messages, media, biometrics, and credentials out of fixtures and logs.

Reusable workflows provide generated-plan validation and bounded offline hardening contracts. Live provider, emulator, database, chaos, scale, and soak checks remain scheduled or manually gated.
