"""
Integration tests for CLI commands using Click's CliRunner.
"""

import ast
import math
import sys
from pathlib import Path

import pytest
from click.testing import CliRunner

# Add project path for imports
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.cli import cli


# Fixtures
@pytest.fixture
def cli_runner():
    """Return a CliRunner instance for invoking CLI commands."""
    return CliRunner()


# ------------------ Integration Tests ------------------ #
def test_clean_remove_missing(cli_runner):
    """Test 'clean remove-missing' command."""
    result = cli_runner.invoke(cli, ["clean", "remove-missing", "--values", "1,,2,None,3"])
    assert result.exit_code == 0
    assert result.output.strip() == "['1', '2', '3']"


def test_numeric_standardize(cli_runner):
    """Test 'numeric standardize' command."""
    result = cli_runner.invoke(cli, ["numeric", "standardize", "--values", "1,2,3"])
    assert result.exit_code == 0
    output_list = ast.literal_eval(result.output.strip())
    mean = sum(output_list) / len(output_list)
    assert math.isclose(mean, 0, abs_tol=1e-9)


def test_text_tokenize(cli_runner):
    """Test 'text tokenize' command."""
    result = cli_runner.invoke(cli, ["text", "tokenize", "--input-text", "Hello world!"])
    assert result.exit_code == 0
    assert result.output.strip() == "['hello', 'world']"


def test_struct_unique(cli_runner):
    """Test 'struct unique-struct' command."""
    result = cli_runner.invoke(cli, ["struct", "unique-struct", "--values", "1,2,2,3,a"])
    assert result.exit_code == 0
    output_list = ast.literal_eval(result.output.strip())
    assert sorted(output_list) == sorted(["1", "2", "3", "a"])
