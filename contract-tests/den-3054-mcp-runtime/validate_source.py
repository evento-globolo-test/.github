#!/usr/bin/env python3
"""Validate an exact Evento Globolo MCP runtime checkout before compilation."""

from __future__ import annotations

import json
import re
import subprocess
import sys
import tomllib
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
PINS_PATH = HERE / "source-pins.json"


def fail(message: str) -> None:
    raise SystemExit(message)


def load_toml(path: Path) -> dict[str, Any]:
    try:
        return tomllib.loads(path.read_text(encoding="utf-8"))
    except (OSError, tomllib.TOMLDecodeError) as error:
        fail(f"cannot parse {path}: {error}")


def require_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError as error:
        fail(f"cannot read {path}: {error}")


def git_output(root: Path, *arguments: str) -> str:
    try:
        return subprocess.check_output(
            ["git", "-C", str(root), *arguments], text=True
        ).strip()
    except subprocess.CalledProcessError as error:
        fail(f"git {' '.join(arguments)} failed: {error}")


def validate_credentials(root: Path) -> None:
    patterns = [
        re.compile("gh" + r"[pousr]_[A-Za-z0-9_]{20,}"),
        re.compile("github" + r"_pat_[A-Za-z0-9_]{20,}"),
        re.compile("cf" + r"at_[A-Za-z0-9_-]{20,}"),
        re.compile("lin" + r"_api_[A-Za-z0-9_-]{20,}"),
        re.compile(r"AKIA[0-9A-Z]{16}"),
        re.compile("sk" + r"-[A-Za-z0-9_-]{20,}"),
        re.compile(r"-----BEGIN [A-Z0-9 ]*PRIVATE KEY-----"),
    ]
    allowed = {Path(".github/workflows/ci.yml")}
    tracked = git_output(root, "ls-files", "-z").encode().split(b"\0")
    for raw_path in tracked:
        if not raw_path:
            continue
        relative = Path(raw_path.decode())
        path = root / relative
        if relative in allowed or not path.is_file():
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if any(pattern.search(text) for pattern in patterns):
            fail(f"credential-shaped content found in {relative}")


def main() -> None:
    if len(sys.argv) != 2:
        fail("usage: validate_source.py <source-checkout>")
    root = Path(sys.argv[1]).resolve()
    pins = json.loads(PINS_PATH.read_text(encoding="utf-8"))

    expected_commit = pins["productionCommit"]
    actual_commit = git_output(root, "rev-parse", "HEAD")
    if actual_commit != expected_commit:
        fail(f"source commit mismatch: expected {expected_commit}, got {actual_commit}")
    if git_output(root, "status", "--porcelain"):
        fail("source checkout is not clean")

    manifest = load_toml(root / "Cargo.toml")
    dependencies = manifest.get("dependencies", {})
    dev_dependencies = manifest.get("dev-dependencies", {})
    shared_revision = pins["sharedRevision"]
    for name, table in {
        "ore-mcp-runtime": dependencies.get("ore-mcp-runtime"),
        "ore-mcp-zed-graph": dependencies.get("ore-mcp-zed-graph"),
        "ore-mcp-testkit": dev_dependencies.get("ore-mcp-testkit"),
    }.items():
        if not isinstance(table, dict) or table.get("rev") != shared_revision:
            fail(f"{name} does not pin shared revision {shared_revision}")

    rmcp = dependencies.get("rmcp")
    expected_rmcp = f"={pins['rmcpVersion']}"
    if not isinstance(rmcp, dict) or rmcp.get("version") != expected_rmcp:
        fail(f"rmcp must be pinned exactly to {expected_rmcp}")

    lock = load_toml(root / "Cargo.lock")
    lock_packages = lock.get("package", [])
    rmcp_versions = {
        package.get("version")
        for package in lock_packages
        if package.get("name") in {"rmcp", "rmcp-macros"}
    }
    if rmcp_versions != {pins["rmcpVersion"]}:
        fail(f"unexpected rmcp lock versions: {sorted(rmcp_versions)}")
    for name in ("ore-mcp-runtime", "ore-mcp-zed-graph", "ore-mcp-testkit"):
        matches = [package for package in lock_packages if package.get("name") == name]
        if len(matches) != 1:
            fail(f"expected one locked {name} package, found {len(matches)}")
        source = matches[0].get("source", "")
        if not source.endswith(f"#{shared_revision}"):
            fail(f"{name} lock source does not end in #{shared_revision}")

    main_rs = require_text(root / "src/main.rs")
    lib_rs = require_text(root / "src/lib.rs")
    tests_rs = require_text(root / "tests/stdio_conformance.rs")
    for token in (
        "ExactProtocol::new",
        "ProtocolVersion::V_2025_11_25",
        "run_stdio",
    ):
        if token not in main_rs:
            fail(f"src/main.rs is missing {token}")
    for forbidden in ("read_line", "println!", "2025-06-18"):
        if forbidden in main_rs or forbidden in lib_rs:
            fail(f"production source contains forbidden token {forbidden}")
    for token in (
        "impl ServerHandler for EvglMcp",
        '"unknown tool"',
        '"method not found"',
        "ProtocolVersion::V_2025_11_25",
    ):
        if token not in lib_rs:
            fail(f"src/lib.rs is missing {token}")
    for token in (
        "official_rmcp_process_preserves_protocol_and_tool_contract",
        "exact_protocol_wrapper_rejects_preview_and_legacy_versions",
        '"2026-07-28"',
        '"2025-06-18"',
    ):
        if token not in tests_rs:
            fail(f"real-process tests are missing {token}")

    zpkg = load_toml(root / ".zpkg.toml")
    actual_zed_dependencies = set(zpkg.get("dependencies", {}))
    expected_zed_dependencies = set(pins["expectedDependencies"])
    if actual_zed_dependencies != expected_zed_dependencies:
        fail(
            "Zed dependency mismatch: "
            f"expected {sorted(expected_zed_dependencies)}, "
            f"got {sorted(actual_zed_dependencies)}"
        )
    if zpkg.get("install", {}).get("dir") != ".vendor/.zed":
        fail("Zed install directory is not .vendor/.zed")

    temporary_workflows = list((root / ".github/workflows").glob("reconcile-*.yml"))
    if temporary_workflows:
        fail(f"temporary workflows remain: {temporary_workflows}")

    validate_credentials(root)
    print(
        json.dumps(
            {
                "productionCommit": actual_commit,
                "sharedRevision": shared_revision,
                "rmcpVersion": pins["rmcpVersion"],
                "protocolVersion": pins["protocolVersion"],
                "dependencyCount": len(actual_zed_dependencies),
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
