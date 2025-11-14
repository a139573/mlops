"""
Unit tests for functions in preprocessing.py.
"""

import math
import pytest

from src.preprocessing import (
    is_missing,
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


# -------------------- Fixtures -------------------- #
@pytest.fixture
def sample_numbers_fixture():
    """Return a sample list of numeric values."""
    return [1, 2, 3, 4, 5]


@pytest.fixture
def sample_strings_fixture():
    """Return a sample list of string values."""
    return ["1", "2", "a", "", None]


# -------------------- Unit Tests -------------------- #
def test_remove_missing_values(sample_strings_fixture):
    """Test removing missing values."""
    assert remove_missing_values(sample_strings_fixture) == ["1", "2", "a"]


@pytest.mark.parametrize(
    "missing_value,expected",
    [
        (None, True),
        ("", True),
        (float("nan"), True),
        ("hello", False),
        (4, False),
    ],
)
def test_is_missing_value(missing_value, expected):
    """Test the is_missing() function."""
    assert is_missing(missing_value) == expected


def test_fill_missing_values(sample_strings_fixture):
    """Test filling missing values with a specified value."""
    output = fill_missing_values(sample_strings_fixture, filling_value=0)
    assert output == ["1", "2", "a", 0, 0]


def test_remove_duplicates():
    """Test removing duplicate values from a list."""
    assert set(remove_duplicates([1, 2, 2, 3])) == {1, 2, 3}


@pytest.mark.parametrize(
    "input_list,new_min,new_max,expected_min,expected_max",
    [
        ([1, 2, 3, 4, 5], 0.0, 1.0, 0.0, 1.0),
        ([10, 20, 30], -1.0, 1.0, -1.0, 1.0),
        ([5, 5, 5], -1.0, 1.0, -1.0, -1.0),  # edge case: all values equal
    ],
)
def test_normalize_values(input_list, new_min, new_max, expected_min, expected_max):
    """Test min-max normalization."""
    normalized = normalize_values(input_list, new_min=new_min, new_max=new_max)
    assert min(normalized) == expected_min
    assert max(normalized) == expected_max


@pytest.mark.parametrize(
    "input_list,expected_mean",
    [
        ([1, 2, 3, 4, 5], 0),
        ([5, 5, 5, 5], 0),
    ],
)
def test_standardize_values(input_list, expected_mean):
    """Test z-score standardization."""
    standardized = standardize_values(input_list)
    mean = sum(standardized) / len(standardized)
    assert math.isclose(mean, expected_mean, abs_tol=1e-9)


def test_clip_values(sample_numbers_fixture):
    """Test clipping values to a specified range."""
    clipped = clip_values(sample_numbers_fixture, min_value=2, max_value=4)
    assert clipped == [2, 2, 3, 4, 4]


@pytest.mark.parametrize(
    "input_list,expected",
    [
        (["1", "a", "2"], [1, 2]),
        (["", None, "5"], [5]),
        (["-3", "0", "7"], [-3, 0, 7]),
        (["4.2", "5"], [5]),  # floats not cast to int
    ],
)
def test_convert_to_int_param(input_list, expected):
    """Test converting strings to integers, ignoring non-numeric values."""
    assert convert_to_int(input_list) == expected


def test_log_transform(sample_numbers_fixture):
    """Test applying logarithmic transformation."""
    log_vals = log_transform(sample_numbers_fixture)
    assert all(v >= 0 for v in log_vals)


def test_tokenize_text():
    """Test tokenizing text into lowercase words."""
    text = "Hello, World!"
    assert tokenize_text(text) == ["hello", "world"]


def test_keep_alphanumeric_and_spaces():
    """Test keeping only alphanumeric characters and spaces."""
    text = "Hello, World!"
    assert keep_alphanumeric_and_spaces(text) == "hello world"


def test_remove_stopwords():
    """Test removing stopwords from text."""
    text = "this is a test"
    stopwords = ["is", "a"]
    assert remove_stopwords(text, stopwords) == ["this", "test"]


def test_flatten_lists():
    """Test flattening a nested list."""
    nested = [[1, 2], [3, 4]]
    assert flatten_lists(nested) == [1, 2, 3, 4]


def test_shuffle_list(sample_numbers_fixture):
    """Test shuffling a list with a seed."""
    shuffled = shuffle_list(sample_numbers_fixture, seed=42)
    assert set(shuffled) == set(sample_numbers_fixture)