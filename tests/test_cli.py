from click.testing import CliRunner

from chatjixia import __version__
from chatjixia.cli import main


def test_help_mentions_tree_option():
    result = CliRunner().invoke(main, ["--help"])

    assert result.exit_code == 0
    assert "--tree" in result.output


def test_version_option_reports_package_version():
    result = CliRunner().invoke(main, ["--version"])

    assert result.exit_code == 0
    assert f"chatjixia, version {__version__}" in result.output


def test_tree_reports_registered_root_only_surface():
    result = CliRunner().invoke(main, ["--tree"])

    assert result.exit_code == 0
    assert result.output == (
        "chatjixia  # ChatArch JiXia Lean analysis integration entrypoint\n"
        "├── --help  # show command help\n"
        "├── --version  # show the installed package version\n"
        "└── --tree  # show this CLI tree\n"
    )
