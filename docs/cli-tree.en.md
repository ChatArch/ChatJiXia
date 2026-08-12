# CLI Tree

`ChatJiXia` is currently a root-only CLI. This page must stay synchronized from the real `chatjixia --tree` output and must not invent future commands.

```text
chatjixia  # ChatArch JiXia Lean analysis integration entrypoint
├── --help  # show command help
├── --version  # show the installed package version
└── --tree  # show this CLI tree
```

## Current Status

| Entry | Status | Notes |
| --- | --- | --- |
| `chatjixia --help` | Implemented | Shows root command help. |
| `chatjixia --version` | Implemented | Shows the installed package version. |
| `chatjixia --tree` | Implemented | Shows the current real CLI tree. |
| JiXia/Lean analysis subcommands | Not implemented | Add them only after real analysis capability exists. |

## Update Rule

When real commands are added, update the Click registration and tests first, then run `chatjixia --tree` to refresh README and this page.
