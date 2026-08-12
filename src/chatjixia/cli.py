"""CLI entrypoint for chatjixia."""

from __future__ import annotations

import click

from chatjixia import __version__


def _format_tree() -> str:
    """Render the public CLI surface from the registered Click command."""
    ctx = click.Context(main, info_name="chatjixia")
    lines = ["chatjixia  # ChatArch JiXia Lean analysis integration entrypoint"]
    params = {param.name: param for param in main.get_params(ctx)}
    if "help" in params:
        lines.append("├── --help  # show command help")
    if "version" in params:
        lines.append("├── --version  # show the installed package version")
    lines.append("└── --tree  # show this CLI tree")
    return "\n".join(lines)


@click.group(invoke_without_command=True)
@click.version_option(__version__, prog_name="chatjixia")
@click.option("--tree", "show_tree", is_flag=True, is_eager=True, help="Show the CLI command tree and exit.")
@click.pass_context
def main(ctx: click.Context, show_tree: bool) -> None:
    """chatjixia command line interface."""
    if show_tree:
        click.echo(_format_tree())
        ctx.exit(0)
    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())


if __name__ == "__main__":
    main()
