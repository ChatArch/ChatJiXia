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

[英文版](README.en.md) | [简体中文](README.md)
</div>

# ChatJiXia

ChatJiXia 是 ChatArch 的 JiXia Lean analysis integration 包入口。当前包保持最小 root-only CLI，用于保留可安装、可发现、可发布的集成壳；真实 JiXia/Lean 分析命令尚未暴露。

## 快速开始

```bash
pip install ChatJiXia
chatjixia --help
chatjixia --version
chatjixia --tree
```

## 当前 CLI 树

```text
chatjixia  # ChatArch JiXia Lean analysis integration entrypoint
├── --help  # show command help
├── --version  # show the installed package version
└── --tree  # show this CLI tree
```

## CLI 边界

- 当前 CLI 只有根选项，没有业务子命令。
- `--tree` 从实际 Click 命令注册面生成，用来校对 README、文档和测试。
- 后续新增真实 JiXia/Lean 分析命令时，必须先更新 Click 注册面，再用真实 `chatjixia --tree` 同步文档。

## 目录结构

- `src/`：包源码
- `tests/code-tests/`：代码测试和历史测试迁移
- `tests/cli-tests/`：真实 CLI 测试，doc-first
- `tests/mock-cli-tests/`：mock/fake CLI 测试，doc-first
- `docs/`：长期维护文档，由 MkDocs 构建

## 开发说明

扩展脚手架前，先阅读 `DEVELOP.md` 和 `AGENTS.md`。
