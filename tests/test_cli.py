import pytest
from typer.testing import CliRunner

from services_test4 import __version__
from services_test4.cli import app

runner = CliRunner()

HELP_OPTION_NAMES = ("-h", "--help")
VERSION_OPTION_NAMES = ("-V", "--version")


@pytest.mark.parametrize("help_option_name", HELP_OPTION_NAMES)
def test_help_option_displays_help(help_option_name: str) -> None:
    result = runner.invoke(app, [help_option_name])
    assert result.exit_code == 0
    assert "Usage" in result.stdout
    assert "Options" in result.stdout
    assert "Show this message and exit" in result.stdout


@pytest.mark.parametrize("version_option_name", VERSION_OPTION_NAMES)
def test_version_option_displays_version(version_option_name: str) -> None:
    result = runner.invoke(app, [version_option_name])
    assert result.exit_code == 0
    assert "services-test4" in result.stdout
    assert __version__ in result.stdout


def test_hello() -> None:
    result = runner.invoke(app, ["hello", "world"])
    assert result.exit_code == 0
    assert "WORLD" in result.stdout
