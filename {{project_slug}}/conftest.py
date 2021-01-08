"""Fixtures."""
import os
from click.testing import CliRunner
from app.main import main
import pytest


@pytest.fixture(scope='session')
def cli_runner():
    """Fixture that returns a helper function to run the cookiecutter cli."""
    runner = CliRunner()

    def cli_main(*cli_args, **cli_kwargs):
        """Run cookiecutter cli main with the given args."""
        return runner.invoke(main, cli_args, **cli_kwargs)

    return cli_main


@pytest.fixture(scope="function")
def change_dir(request):
    """Change to the current directory of the test."""
    os.chdir(request.fspath.dirname)

