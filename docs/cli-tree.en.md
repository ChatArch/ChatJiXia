# CLI Tree

`ChatJiXia` is currently a root-only CLI. This page must stay synchronized from the real `chatjixia --tree` and `chatjixia --tree-brief` outputs and must not invent future commands.

```text
chatjixia
├── --help  # Show this message and exit.
├── --version  # Show the version and exit.
├── --tree  # Print the registered CLI tree and exit.
└── --tree-brief  # Print the registered CLI tree without parameter signatures and exit.
```

## Current Status

| Entry | Status | Notes |
| --- | --- | --- |
| `chatjixia --help` | Implemented | Shows root command help. |
| `chatjixia --version` | Implemented | Shows the installed package version. |
| `chatjixia --tree` | Implemented | Shows the current real CLI tree and retains command parameter signatures by default. |
| `chatjixia --tree-brief` | Implemented | Omits parameter signatures while preserving command nodes and descriptions. |
| JiXia/Lean analysis subcommands | Not implemented | Add them only after real analysis capability exists. |

ChatStyle's shared Click tree runtime fixes the public root to the canonical `chatjixia` entrypoint. Because the current root-only CLI has no parameterized command nodes, the full and brief modes currently show the same tree content.

## Update Rule

When real commands are added, update the Click registration and tests first, then run `chatjixia --tree` and `chatjixia --tree-brief` to refresh README and this page.
