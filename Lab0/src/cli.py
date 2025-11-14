"""
Command Line Interface (CLI) for data preprocessing operations.

This CLI uses Click to expose functions from preprocessing.py for:
- Cleaning missing or duplicate values
- Normalizing and transforming numeric data
- Processing text
- Manipulating data structures
"""

import ast
from typing import Optional
import click
from preprocessing import (
    remove_missing_values,
    fill_missing_values,
    remove_duplicates,
    normalize_values,
    standardize_values,
    clip_values,
    convert_to_int,
    log_transform,
    tokenize_text,
    keep_alphanumeric_and_spaces,
    remove_stopwords,
    flatten_lists,
    shuffle_list,
)


@click.group(help="Main group of commands for data preprocessing.")
def cli() -> None:
    """Entry point."""


# CLEAN SUBGROUP
@cli.group(help="Commands for data cleaning operations.")
def clean() -> None:
    """Subgroup for cleaning operations."""


@clean.command(
    help=(
        "Remove missing values from a list. "
        "Example: python -m src.cli clean remove-missing --values '1,2,,None,4'"
    )
)
@click.option("--values", required=True, help="Comma-separated list of values.")
def remove_missing(values: str) -> None:
    """Remove missing values from a list."""
    values_list = [v.strip() if v.strip() not in ["None", ""] else None
                   for v in values.split(",")]
    result = remove_missing_values(values_list)
    click.echo(result)


@clean.command(
    help=(
        "Fill missing values in a list. "
        "Example: python -m src.cli clean fill-missing --values '1,2,,None,4' --fill 0"
    )
)
@click.option("--values", required=True, help="Comma-separated list of values.")
@click.option("--fill", default=0, show_default=True, help="Value to fill missing entries.")
def fill_missing(values: str, fill: str) -> None:
    """Fill missing values in a list."""
    values_list = [v.strip() if v.strip() not in ["None", ""] else None
                   for v in values.split(",")]
    result = fill_missing_values(values_list, fill)
    click.echo(result)


@clean.command(
    help="Remove duplicate values. Example: python -m src.cli clean unique --values '1,2,2,3'."
)
@click.option("--values", required=True, help="Comma-separated list of values.")
def unique(values: str) -> None:
    """Remove duplicate values from a list."""
    values_list = [v.strip() for v in values.split(",")]
    result = remove_duplicates(values_list)
    click.echo(result)


# NUMERIC SUBGROUP
@cli.group(help="Commands for numeric transformations.")
def numeric() -> None:
    """Subgroup for numeric operations."""


@numeric.command(
    help=(
        "Normalize numerical values. "
        "Example: python -m src.cli numeric normalize --values '1,2,3' --new-min 0 --new-max 1"
    )
)
@click.option("--values", required=True, help="Comma-separated list of numbers.")
@click.option("--new-min", default=0.0, show_default=True, help="New minimum value.")
@click.option("--new-max", default=1.0, show_default=True, help="New maximum value.")
def normalize(values: str, new_min: float, new_max: float) -> None:
    """Normalize numerical values using min-max scaling."""
    values_list = [float(v) for v in values.split(",")]
    result = normalize_values(values_list, new_min, new_max)
    click.echo(result)


@numeric.command(
    help="Standardize numerical values. Example: python -m src.cli numeric standardize --values '1,2,3'."
)
@click.option("--values", required=True, help="Comma-separated list of numbers.")
def standardize(values: str) -> None:
    """Standardize numerical values using z-score."""
    values_list = [float(v) for v in values.split(",")]
    result = standardize_values(values_list)
    click.echo(result)


@numeric.command(
    help=(
        "Clip numerical values to a range. "
        "Example: python -m src.cli numeric clip --values '1,5,10' --min-value 2 --max-value 8"
    )
)
@click.option("--values", required=True, help="Comma-separated list of numbers.")
@click.option("--min-value", default=0.0, show_default=True, help="Minimum clip value.")
@click.option("--max-value", default=1.0, show_default=True, help="Maximum clip value.")
def clip(values: str, min_value: float, max_value: float) -> None:
    """Clip numerical values to a given range."""
    values_list = [float(v) for v in values.split(",")]
    result = clip_values(values_list, min_value, max_value)
    click.echo(result)


@numeric.command(
    help="Convert strings to integers. Example: python -m src.cli numeric to-int --values '1,2,3,a'."
)
@click.option("--values", required=True, help="Comma-separated list of string numbers.")
def to_int(values: str) -> None:
    """Convert string values to integers, skipping invalid entries."""
    values_list = [v.strip() for v in values.split(",")]
    result = convert_to_int(values_list)
    click.echo(result)


@numeric.command(
    help="Apply logarithmic transformation. Example: python -m src.cli numeric log-transform --values '1,10,100'."
)
@click.option("--values", required=True, help="Comma-separated list of positive numbers.")
def log_transform_cmd(values: str) -> None:
    """Apply a logarithmic transformation to numeric values."""
    values_list = [float(v) for v in values.split(",")]
    result = log_transform(values_list)
    click.echo(result)


# ---------------------- TEXT GROUP ----------------------
@cli.group(help="Commands for text processing.")
def text() -> None:
    """Subgroup for text processing commands."""


@text.command(
    help="Tokenize text into words. Example: python -m src.cli text tokenize --input-text 'Hello World!'."
)
@click.option("--input-text", required=True, help="Input text to tokenize.")
def tokenize(input_text: str) -> None:
    """Tokenize input text into words."""
    result = tokenize_text(input_text)
    click.echo(result)


@text.command(
    help="Keep only alphanumeric and spaces. Example: python -m src.cli text clean --input-text 'Hello, World!!!'."
)
@click.option("--input-text", required=True, help="Input text to clean.")
def clean_text(input_text: str) -> None:
    """Remove punctuation and keep only alphanumeric characters and spaces."""
    result = keep_alphanumeric_and_spaces(input_text)
    click.echo(result)


@text.command(
    help="Remove stopwords. Example: python -m src.cli text remove-stopwords --input-text 'this is a test' --stopwords 'is,a'."
)
@click.option("--input-text", required=True, help="Input text to process.")
@click.option("--stopwords", required=True, help="Comma-separated stopwords.")
def remove_stopwords_cmd(input_text: str, stopwords: str) -> None:
    """Remove specified stopwords from input text."""
    stopword_list = [w.strip() for w in stopwords.split(",")]
    result = remove_stopwords(input_text, stopword_list)
    click.echo(result)


# ---------------------- STRUCT GROUP ----------------------
@cli.group(help="Commands for structural data manipulation.")
def struct() -> None:
    """Subgroup for structural list operations."""


@struct.command(
    help="Shuffle list values randomly. Example: python -m src.cli struct shuffle --values '1,2,3' --seed 42."
)
@click.option("--values", required=True, help="Comma-separated list of values.")
@click.option("--seed", default=None, show_default=True, type=int, help="Seed for reproducibility.")
def shuffle(values: str, seed: Optional[int]) -> None:
    """Shuffle a list with an optional random seed."""
    values_list = [v.strip() for v in values.split(",")]
    result = shuffle_list(values_list, seed)
    click.echo(result)


@struct.command(
    help="Flatten a list of lists. Example: python -m src.cli struct flatten --lists '[[1,2],[3,4]]'."
)
@click.option("--lists", required=True, help="String representation of list of lists.")
def flatten(lists: str) -> None:
    """Flatten a nested list structure."""
    try:
        parsed_lists = ast.literal_eval(lists)
        result = flatten_lists(parsed_lists)
        click.echo(result)
    except (ValueError, SyntaxError):
        click.echo("Invalid list format. Use e.g. '[[1,2],[3,4]]'.")


@struct.command(
    help="Remove duplicates. Example: python -m src.cli struct unique --values '1,2,2,3'."
)
@click.option("--values", required=True, help="Comma-separated list of values.")
def unique_struct(values: str) -> None:
    """Remove duplicate values from a list."""
    values_list = [v.strip() for v in values.split(",")]
    result = remove_duplicates(values_list)
    click.echo(result)

if __name__ == "__main__":
    cli()
