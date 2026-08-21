"""CLI entrypoint for chatjixia."""

from __future__ import annotations

import click
from chatstyle import add_tree_option

from chatjixia import __version__


CLI_NAME = "chatjixia"


@click.group(invoke_without_command=True)
@click.version_option(__version__, prog_name=CLI_NAME)
@add_tree_option(renderer_options={"root_name": CLI_NAME})
@click.pass_context
def main(ctx: click.Context) -> None:
    """chatjixia command line interface."""
    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())


if __name__ == "__main__":
    main()
