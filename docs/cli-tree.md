# CLI 树

`ChatJiXia` 当前是 root-only CLI。这个页面必须从真实 `chatjixia --tree` 和 `chatjixia --tree-brief` 输出同步，不能手写未来命令。

```text
chatjixia
├── --help  # Show this message and exit.
├── --version  # Show the version and exit.
├── --tree  # Print the registered CLI tree and exit.
└── --tree-brief  # Print the registered CLI tree without parameter signatures and exit.
```

## 当前状态

| 入口 | 状态 | 说明 |
| --- | --- | --- |
| `chatjixia --help` | 已实现 | 显示根命令帮助。 |
| `chatjixia --version` | 已实现 | 显示已安装包版本。 |
| `chatjixia --tree` | 已实现 | 显示当前真实 CLI 树，默认保留命令参数签名。 |
| `chatjixia --tree-brief` | 已实现 | 省略参数签名，同时保留命令节点和描述。 |
| JiXia/Lean 分析子命令 | 尚未实现 | 未来有实际分析能力后再加入 CLI。 |

公开树根由 ChatStyle 共享 Click 树运行时固定为规范入口 `chatjixia`。当前 root-only CLI 没有带参数的命令节点，因此完整和简略模式目前显示相同的树形内容。

## 更新规则

新增真实命令时，先更新 Click 注册面和测试，再运行 `chatjixia --tree` 与 `chatjixia --tree-brief` 回填 README 与本页。
