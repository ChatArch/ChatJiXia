# Changelog

## 0.1.2 - 2026-08-21

### Changed

- Migrated the top-level CLI tree to ChatStyle's shared `add_tree_option` runtime with the canonical `chatjixia` root.
- Added `--tree-brief`; the default tree keeps command parameter signatures while brief output omits them and preserves command descriptions.
- Raised the runtime bounds to `chatstyle>=0.2.0,<0.3.0` and `chatenv>=0.2.10,<0.3.0`.

## 0.1.1 - 2026-08-12

### Added

- Added real root-only `chatjixia --tree` generated from the Click command surface.
- Added MkDocs documentation with bilingual home and CLI tree pages.
- Added CLI/workflow/docs contract tests for the current root-only surface.

### Changed

- Aligned package documentation URL to `https://arch.gh.wzhecnu.cn/ChatJiXia/`.
- Hardened CI, Preview Docs, Deploy Docs, and tag-only OIDC publish workflows.

## 0.1.0 - 2026-07-10

### Added

- Initial workflow-verified ChatJiXia package release.
- Package module `chatjixia` and CLI command `chatjixia`.

## 0.0.1 - 2026-07-10

### Added

- PyPI placeholder release to reserve the `ChatJiXia` project name.
