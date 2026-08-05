# evento-globolo-test

Independent acceptance organization for **evento-globolo**.

The organization intentionally retains two complementary test portfolios while their unique behavior and history are reconciled.

## Generated specialized fleet

Seventeen repositories provide generated contracts with immutable source pins and profile-specific checks:

| Repository | Surface |
|---|---|
| `mash-web-e2e` | Maud/Axum/SeaORM/HTMX and WebSocket browser behavior |
| `leptos-web-e2e` | Leptos SSR, hydration, routing, accessibility |
| `dioxus-web-e2e` | Dioxus SSR, hydration, routing, accessibility |
| `api-contract-e2e` | Event CRUD, search, attendance, organizers, auth |
| `websocket-event-updates-e2e` | Ordering, resume, RSVP fanout, backpressure |
| `clients-rust-consumer` | Rust SDK consumption |
| `clients-typescript-consumer` | TypeScript browser/Node/WebSocket consumption |
| `clients-dart-consumer` | Dart/Flutter and offline RSVP consumption |
| `ticketing-checkin-e2e` | Ticket issuance, QR check-in, offline scanner sync |
| `recurrence-timezone-locale-e2e` | Recurrence, DST, IANA zones, locale and calendar export |
| `search-discovery-e2e` | Geo/full-text search, facets, ranking, large catalogs |
| `payments-webhooks-e2e` | Checkout, refunds, signatures, webhook idempotency |
| `organizer-permissions-e2e` | Roles, tenant isolation, visibility, moderation audit |
| `sync-offline-e2e` | Offline drafts, RSVP queue, conflicts, restart durability |
| `load-performance-e2e` | Search throughput, WebSocket fanout, RSVP bursts, pools |
| `infra-cloudflare-worker-e2e` | Worker routing, caching, limits, failover, rollback |
| `cli-contract-e2e` | Event/organizer commands, JSON, flags-to-env, packaging |

Each repository’s `test-plan.json` and source-gate file are authoritative for current readiness. A missing upstream is a blocked dependency, not a passing product assertion.

## Legacy readiness-gated portfolio

Nine repositories preserve independent fixtures and scenarios not yet proven redundant:

| Repository | Surface |
|---|---|
| `api-contract` | Broad API and canonical fixture certification |
| `meta-crosspost` | Meta provider adapter behavior |
| `eventbrite-crosspost` | Eventbrite provider adapter behavior |
| `meetup-crosspost` | Meetup provider adapter behavior |
| `craigslist-adapter` | Craigslist adapter behavior |
| `oauth-refresh` | OAuth refresh and replay handling |
| `webhook-reconciliation` | Webhook reconciliation and recovery |
| `dedupe-idempotency` | Deduplication and idempotency invariants |
| `flutter-web-ui-e2e` | Flutter/web UI and accessibility certification |

These repositories are not deletion candidates merely because a newer generated repository has a similar name. Retirement requires a semantic behavior/history comparison and explicit evidence that every unique invariant is preserved.

Pull requests run deterministic, credential-free checks. Provider, emulator, database, chaos, scale, and soak execution remains scheduled or manually gated.
