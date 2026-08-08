# DEN-3054 Evento Globolo MCP runtime provenance

This contract independently fetches the exact public production merge commit for `evento-globolo/evgl-mcp-server.rs`, validates its immutable dependency and protocol boundaries, and compiles and executes it on Linux, macOS, and Windows with both the Rust 1.88.0 MSRV and Rust 1.97.1.

The source checkout is fetched anonymously by commit SHA. The workflow does not use a production PAT, private-repository token, Linear token, Cloudflare token, R2 credential, or product secret.

The executable checks cover the production repository's own unit tests and real-process MCP sessions, including final `2025-11-25` initialization and rejection of preview and legacy protocol versions.

This is an independent test-organization runtime and provenance proof. It is **not**:

- a Zed registry publication;
- a resolver-generated `.zpkg.lock`;
- an isolated `zed install --frozen` replay;
- a deployment test; or
- provider-backed AI review consensus.

Those gates remain separate under DEN-2290, DEN-957, and the shared AI Agent Bridge queue.
