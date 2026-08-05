# Evento Globolo test-fleet reconciliation

Audit date: 2026-08-05

The canonical portfolio declares one policy repository plus twelve specialized acceptance repositories for `evento-globolo-test`. The remote organization currently contains the policy repository and the three Rust web-surface browser repositories.

## Present

- `.github`
- `mash-web-e2e`
- `leptos-web-e2e`
- `dioxus-web-e2e`

## Missing canonical certification repositories

- `api-contract`
- `meta-crosspost`
- `eventbrite-crosspost`
- `meetup-crosspost`
- `craigslist-adapter`
- `oauth-refresh`
- `webhook-reconciliation`
- `dedupe-idempotency`
- `flutter-web-ui-e2e`

## Hardening already in progress

`evento-globolo-test/mash-web-e2e#2` corrects the stale MASH source coordinate and adds executable OAuth replay, cross-post idempotency, partial-provider-failure, WebSocket resume, CSRF, owner-isolation, and redaction contracts.

## Completion rule

The fleet is not considered complete until every repository above exists, contains an immutable production source pin or an explicit source gate, and has a credential-free pull-request validation path. Extra repositories are preserved; reconciliation never deletes or overwrites independently added tests.
