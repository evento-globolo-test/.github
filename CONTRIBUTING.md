# Contributing

Keep tests black-box where possible and use synthetic data. Classify every failure as a product regression, blocked dependency, or harness regression.

Preserve immutable source pins and every declared Git submodule, Zed, or native-package dependency lane. Add product assertions rather than replacing contract checks with no-op smoke tests. Record the upstream revision and retain evidence needed to reproduce failures.

Pull-request checks must be deterministic and credential-free. Put live providers, emulators, databases, chaos, scale, and soak checks in scheduled or manually gated workflows.

When branches overlap, reconcile their behavior and recent history. Do not resolve conflicts by mechanically selecting one side, and do not retire a repository until all unique invariants and history have an explicit destination.
