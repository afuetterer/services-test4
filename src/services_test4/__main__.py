import sys

try:
    from services_test4.cli import app

    app(prog_name="services-test4")
except ImportError:
    print("Please install 'services-test4[cli]' to use this command.")
    sys.exit(1)
