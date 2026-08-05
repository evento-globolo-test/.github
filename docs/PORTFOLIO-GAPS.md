# Evento Globolo test-fleet reconciliation

Audit date: 2026-08-05
Canonical source: `zed-pkg-test/zed-pkg-e2e` live 341-repository manifest

## Current result

The live portfolio declares **17 specialized repositories plus one public `.github` governance repository** for `evento-globolo-test`: **18 canonical repositories** in total.

The remote organization currently contains **21 repositories**, so the canonical count is met and exceeded. Independently added repositories are preserved; reconciliation never treats extras as deletion targets.

## Remaining verification

Count completeness is established. Name-level drift should be checked against the deterministic canonical index proposed in `zed-pkg-test/zed-pkg-e2e#94` before declaring the organization fully reconciled. Every canonical repository must retain:

- an immutable production source pin or explicit source gate;
- credential-free pull-request validation;
- separate classification for product, upstream dependency, credential, and harness failures; and
- no committed provider credentials or personal event data.

## Hardening in progress

`evento-globolo-test/mash-web-e2e#2` corrects the stale MASH source coordinate and adds executable OAuth replay, cross-post idempotency, partial-provider-failure, WebSocket resume, CSRF, owner-isolation, and redaction contracts.

## Completion rule

The fleet is complete when the exact canonical name set is present, generated bootstrap pull requests are merged in dependency order, and product-specific hardening checks remain green. Extra repositories remain intact.
