import click
from click.testing import CliRunner

from chatjixia import __version__
from chatjixia.cli import main


EXPECTED_ROOT_ONLY_TREE = (
    "chatjixia\n"
    "├── --help  # Show this message and exit.\n"
    "├── --version  # Show the version and exit.\n"
    "├── --tree  # Print the registered CLI tree and exit.\n"
    "└── --tree-brief  # Print the registered CLI tree without parameter signatures and exit.\n"
)


def test_help_mentions_tree_options():
    result = CliRunner().invoke(main, ["--help"])

    assert result.exit_code == 0
    assert "--tree" in result.output
    assert "--tree-brief" in result.output


def test_version_option_reports_package_version():
    result = CliRunner().invoke(main, ["--version"])

    assert result.exit_code == 0
    assert f"chatjixia, version {__version__}" in result.output


def test_tree_reports_registered_root_only_surface_with_canonical_name():
    result = CliRunner().invoke(main, ["--tree"])

    assert result.exit_code == 0
    assert result.output == EXPECTED_ROOT_ONLY_TREE


def test_tree_brief_reports_registered_root_only_surface():
    result = CliRunner().invoke(main, ["--tree-brief"])

    assert result.exit_code == 0
    assert result.output == EXPECTED_ROOT_ONLY_TREE


def test_tree_modes_include_or_omit_command_signatures():
    @click.command("inspect-target", help="Inspect one target.")
    @click.argument("target")
    @click.option("--format", "output_format")
    def inspect_target(target: str, output_format: str | None) -> None:
        pass

    main.add_command(inspect_target)
    try:
        full = CliRunner().invoke(main, ["--tree"])
        brief = CliRunner().invoke(main, ["--tree-brief"])
    finally:
        main.commands.pop("inspect-target")

    assert full.exit_code == 0
    assert brief.exit_code == 0
    assert "inspect-target <TARGET> [--format OUTPUT-FORMAT]  # Inspect one target." in full.output
    assert "inspect-target  # Inspect one target." in brief.output
    assert "<TARGET>" not in brief.output
    assert "[--format OUTPUT-FORMAT]" not in brief.output
