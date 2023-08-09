import sys

try:
    import typer  # noqa: F401
except ImportError:
    print("Please install 'services-test4[cli]' to use this command.")
    sys.exit(0)

from services_test4.cli import app

app(prog_name="services-test4")
