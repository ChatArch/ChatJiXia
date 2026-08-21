from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_publish_workflow_is_tag_only_oidc_and_main_guarded():
    workflow = (ROOT / ".github" / "workflows" / "publish.yml").read_text(encoding="utf-8")

    assert 'tags:' in workflow
    assert 'workflow_dispatch' not in workflow
    assert 'id-token: write' in workflow
    assert 'pypa/gh-action-pypi-publish@release/v1' in workflow
    assert 'git fetch --no-tags origin main:refs/remotes/origin/main' in workflow
    assert 'git merge-base --is-ancestor "${GITHUB_SHA}" refs/remotes/origin/main' in workflow
    legacy_secret_markers = ["PYPI" + "_API_TOKEN", "TWINE" + "_PASSWORD", "secrets" + ".PYPI"]
    assert all(marker not in workflow for marker in legacy_secret_markers)


def test_docs_workflows_use_chatarch_site_url():
    preview = (ROOT / ".github" / "workflows" / "preview.yaml").read_text(encoding="utf-8")
    deploy = (ROOT / ".github" / "workflows" / "deploy.yaml").read_text(encoding="utf-8")
    ci = (ROOT / ".github" / "workflows" / "ci.yml").read_text(encoding="utf-8")

    assert 'CHATARCH_PREVIEW_URL' in preview
    assert 'site_url=$(python' in preview
    assert 'mkdocs.yml' in preview
    assert 'github.io' not in preview
    assert 'mkdocs gh-deploy --force' in deploy
    assert 'mkdocs build --strict' in ci
    assert 'chatjixia --version' in ci
    assert 'chatjixia --tree' in ci
    assert 'chatjixia --tree-brief' in ci


def test_project_uses_shared_cli_runtime_bounds():
    project = (ROOT / "pyproject.toml").read_text(encoding="utf-8")

    assert '"chatstyle>=0.2.0,<0.3.0"' in project
    assert '"chatenv>=0.2.10,<0.3.0"' in project


def test_mkdocs_material_renderer_and_public_domain():
    config = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")

    assert 'site_url: https://arch.gh.wzhecnu.cn/ChatJiXia/' in config
    assert 'pymdownx.emoji' in config
    assert 'material.extensions.emoji.twemoji' in config
    assert 'material.extensions.emoji.to_svg' in config
    assert 'cli-tree.md' in config
