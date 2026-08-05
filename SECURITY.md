# Security policy

Never commit tokens, keys, production user data, biometric evidence, private messages, recordings, or unpublished provider credentials. Reproduce failures with synthetic fixtures and report vulnerabilities privately to the production owner.

Pull-request workflows must remain credential-free. Gated private cross-organization integration may use an approved short-lived GitHub App installation token with least privilege. Do not add PAT fallbacks, persistent fleet tokens, or credentials written to repository files, artifacts, summaries, or logs.
