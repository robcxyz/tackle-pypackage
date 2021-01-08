#!/usr/bin/env python

"""Tests for `this` package."""
import os

from app.main import main
import pytest


@pytest.fixture
def clean_outputs():
    """Clean the output files."""
    yield
    ouput_files = ["debug.yaml"]
    for o in ouput_files:
        if os.path.isfile(o):
            os.remove(o)


def test_command_line_interface(cli_runner):
    """Test the CLI."""
    result = cli_runner("this")
    assert result.exit_code == 0
    assert "this" in result.stdout


def test_cli_version(cli_runner):
    from app import __version__
    result = cli_runner("--version")
    assert result.exit_code == 0
    assert __version__ in result.stdout


def test_cli_debug(cli_runner, clean_outputs):
    result = cli_runner("--debug")
    assert result.exit_code == 0
    assert os.path.isfile("debug.yaml")

