"""The Command Line Interface."""

from typing import Optional

import typer
from typing_extensions import Annotated

from services_test4 import __version__
from services_test4.lib import hello_world

APP_NAME = "services-test4"
CONTEXT_SETTINGS = {"help_option_names": ["-h", "--help"]}

app = typer.Typer()


# https://typer.tiangolo.com/tutorial/options/version/
def version_callback(value: bool) -> None:
    if value:
        typer.echo(f"services-test4, version {__version__}")
        raise typer.Exit()


@app.callback(context_settings=CONTEXT_SETTINGS)
def cli(
    version: Annotated[
        Optional[bool],
        typer.Option("-V", "--version", callback=version_callback, is_eager=True, help="Show the version and exit."),
    ] = None,
) -> None:
    """services-test Command Line Interface."""


@app.command()
def hello(msg: str = typer.Argument(..., help="The message.")) -> None:  # noqa: B008
    """Hello world command."""
    typer.echo(hello_world(msg))


# TODO: Used only for documenting the CLI with mkdocs-click
click_object = typer.main.get_command(app)
