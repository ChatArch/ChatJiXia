<div align="center">
    <a href="https://pypi.python.org/pypi/ChatJiXia">
        <img src="https://img.shields.io/pypi/v/ChatJiXia.svg" alt="PyPI version" />
    </a>
    <a href="https://github.com/ChatArch/ChatJiXia/actions/workflows/ci.yml">
        <img src="https://github.com/ChatArch/ChatJiXia/actions/workflows/ci.yml/badge.svg" alt="Tests" />
    </a>
    <a href="https://arch.gh.wzhecnu.cn/ChatJiXia/">
        <img src="https://img.shields.io/badge/docs-mkdocs-blue.svg" alt="Documentation" />
    </a>
</div>

<div align="center">

[English](README.en.md) | [简体中文](README.md)
</div>

# ChatJiXia

ChatJiXia is the ChatArch JiXia Lean analysis integration package entrypoint. The package currently keeps a minimal root-only CLI so the integration shell remains installable, discoverable, and releasable; real JiXia/Lean analysis commands are not exposed yet.

## Quick Start

```bash
pip install ChatJiXia
chatjixia --help
chatjixia --version
chatjixia --tree
chatjixia --tree-brief
```

## Current CLI Tree

```text
chatjixia
├── --help  # Show this message and exit.
├── --version  # Show the version and exit.
├── --tree  # Print the registered CLI tree and exit.
└── --tree-brief  # Print the registered CLI tree without parameter signatures and exit.
```

## CLI Boundary

- The current CLI only exposes root options and has no business subcommands.
- `--tree` and `--tree-brief` are generated from the real command registration by ChatStyle's shared Click tree runtime, with the public root fixed to the canonical `chatjixia` entrypoint.
- `--tree` retains command parameter signatures by default; `--tree-brief` omits signatures while preserving command nodes and descriptions. Because the current root-only CLI has no parameterized command nodes, both modes currently render the same tree content.
- When real JiXia/Lean analysis commands are added later, update the Click registration first and then sync docs from the real `chatjixia --tree` and `chatjixia --tree-brief` outputs.

## Layout

- `src/`: package source code
- `tests/code-tests/`: code tests and migrated historical tests
- `tests/cli-tests/`: real CLI tests, doc-first
- `tests/mock-cli-tests/`: mock/fake CLI tests, doc-first
- `docs/`: long-lived project docs built by MkDocs

## Development Notes

See `DEVELOP.md` and `AGENTS.md` before expanding the scaffold.
