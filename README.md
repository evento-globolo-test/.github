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


<!-- ore-org-baseline:begin -->
## Organization-wide defaults

This public repository is the canonical source for GitHub-supported community-health fallbacks, organization profile content, contribution guidance, public security/support policy, issue and pull-request templates, and agent-governance declarations for [`evento-globolo-test`](https://github.com/evento-globolo-test).

## Canonical organization links

- GitHub organization: https://github.com/evento-globolo-test
- Public organization defaults: https://github.com/evento-globolo-test/.github
- Canonical Linear project: https://linear.app/denman/project/githubcomevento-globolo-test-c65dde2765de
- Fleet tracking issue: https://github.com/ORESoftware/k8s-cluster/issues/1222

## Safety baseline

All Git conflicts must be resolved semantically with full historical, repository-wide, organization-wide, and relevant external-organization context. Automated agents are hard-denied from destructive or history-rewriting operations, including all forms of `git stash`, `git reset`, `git clean`, `git filter-repo`, force pushing, destructive deletion, data or infrastructure teardown, credential revocation, and policy bypass.

## GitHub inheritance boundary

GitHub can use supported community-health files from a public organization `.github` repository as fallbacks and can render `profile/README.md` on the organization page. `agents.md`, `AGENTS.md`, Copilot instructions, workflows, settings, rulesets, branch protections, permissions, and secrets are not automatically inherited merely because they exist here. Each repository must carry or synchronize compatible local policy and explicitly call reusable workflows where enforcement is required.

Generated managed-policy version: `2026-08-08`.
<!-- ore-org-baseline:end -->
