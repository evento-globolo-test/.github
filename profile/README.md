# evento-globolo-test

Independent acceptance organization for **evento-globolo**.

Readiness-gated event API, OAuth, provider cross-posting, reconciliation, dedupe, and Flutter/web UI certification.

## Portfolio

| Repository | Class | Readiness | Primary dependency path |
|---|---|---|---|
| `api-contract` | API contract | `planned_dependency` | `matrix` |
| `meta-crosspost` | provider adapter | `planned_dependency` | `matrix` |
| `eventbrite-crosspost` | provider adapter | `planned_dependency` | `matrix` |
| `meetup-crosspost` | provider adapter | `planned_dependency` | `matrix` |
| `craigslist-adapter` | provider adapter | `planned_dependency` | `matrix` |
| `oauth-refresh` | authentication | `planned_dependency` | `matrix` |
| `webhook-reconciliation` | synchronization | `planned_dependency` | `matrix` |
| `dedupe-idempotency` | synchronization | `planned_dependency` | `matrix` |
| `flutter-web-ui-e2e` | UI/accessibility | `planned_dependency` | `matrix` |

Pull requests run deterministic harness checks. Emulators, desktop matrices, live APIs/providers, databases, chaos, scale, and soaks are scheduled/manual. Missing upstreams or credentials are blocked readiness—not false passes or product regressions.
