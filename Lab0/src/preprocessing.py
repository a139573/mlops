"""
preprocessing.py

This module provides a set of data preprocessing utilities for:
- Cleaning and handling missing or duplicated values
- Normalizing, standardizing, and clipping numeric data
- Converting values and applying logarithmic transformations
- Tokenizing, cleaning, and filtering text
- Flattening and shuffling data structures

Each function is designed to be reusable and testable in an MLOps pipeline.
"""

import math
import random
import re
from typing import Any, List, Optional


def is_missing(value: Any) -> bool:
    """
    Check whether a value is considered missing.

    Missing values include:
    - None
    - Empty strings
    - NaN (float)

    Args:
        value (Any): Input value to check.

    Returns:
        bool: True if the value is missing, False otherwise.
    """
    try:
        return (
            value is None
            or value == ""
            or (isinstance(value, float) and math.isnan(value))
        )
    except TypeError:
        return False


def remove_missing_values(values: List[Any]) -> List[Any]:
    """
    Remove missing values (None, '', NaN) from a list.

    Args:
        values (List[Any]): Input list possibly containing missing values.

    Returns:
        List[Any]: List without missing values.
    """
    return [value for value in values if not is_missing(value)]


def fill_missing_values(values: List[Any], filling_value: Any = 0) -> List[Any]:
    """
    Replace missing values with a given value.

    Args:
        values (List[Any]): List of values possibly containing missing ones.
        filling_value (Any, optional): Value used to fill missing entries. Defaults to 0.

    Returns:
        List[Any]: List with missing values replaced.
    """
    return [filling_value if is_missing(value) else value for value in values]


def remove_duplicates(values: List[Any]) -> List[Any]:
    """
    Remove duplicate values from a list.

    Args:
        values (List[Any]): List of values.

    Returns:
        List[Any]: List with unique values (order not guaranteed).
    """
    return list(set(values))


def normalize_values(
    values: List[float], new_min: float = 0.0, new_max: float = 1.0
) -> List[float]:
    """
    Normalize numerical values to a new range using min–max scaling.

    Args:
        values (List[float]): List of numeric values.
        new_min (float, optional): New minimum value. Defaults to 0.0.
        new_max (float, optional): New maximum value. Defaults to 1.0.

    Returns:
        List[float]: Normalized list of values.

    Example:
        >>> normalize_values([1, 2, 3])
        [0.0, 0.5, 1.0]
    """
    if not values:
        return []

    old_min, old_max = min(values), max(values)
    if old_min == old_max:
        return [new_min for _ in values]

    return [
        ((v - old_min) / (old_max - old_min)) * (new_max - new_min) + new_min
        for v in values
    ]


def standardize_values(values: List[float]) -> List[float]:
    """
    Standardize numerical values using the z-score method.

    Args:
        values (List[float]): List of numeric values.

    Returns:
        List[float]: Standardized list of values (mean=0, std=1).
    """
    if not values:
        return []

    mean = sum(values) / len(values)
    std = (sum((value - mean) ** 2 for value in values) / len(values)) ** 0.5
    if std == 0:
        return [0 for _ in values]
    return [(value - mean) / std for value in values]


def clip_values(values: List[float], min_value: float, max_value: float) -> List[float]:
    """
    Clip numerical values to a given range.

    Args:
        values (List[float]): List of numeric values.
        min_value (float): Minimum allowed value.
        max_value (float): Maximum allowed value.

    Returns:
        List[float]: List with values clipped within [min_value, max_value].
    """
    return [max(min(value, max_value), min_value) for value in values]


def convert_to_int(strings: List[str]) -> List[int]:
    """
    Convert a list of strings to integers, ignoring non-numeric entries.

    Args:
        strings (List[str]): List of strings (may include non-numeric values).

    Returns:
        List[int]: List of successfully converted integers.
    """
    values: List[int] = []
    for string in strings:
        try:
            values.append(int(string))
        except (ValueError, TypeError):
            continue
    return values


def log_transform(values: List[float]) -> List[float]:
    """
    Apply a natural logarithmic transformation to positive numbers.

    Args:
        values (List[float]): List of numeric values.

    Returns:
        List[float]: Log-transformed values (only for positive inputs).
    """
    return [math.log(value) for value in values if value > 0]


def tokenize_text(text: str) -> List[str]:
    """
    Tokenize text into lowercase alphanumeric words.

    Args:
        text (str): Input text.

    Returns:
        List[str]: List of lowercase tokens.
    """
    return re.findall(r"\b[\w]+\b", text.lower())


def keep_alphanumeric_and_spaces(text: str) -> str:
    """
    Keep only alphanumeric characters and spaces in text.

    Args:
        text (str): Input text.

    Returns:
        str: Cleaned text (lowercased, without punctuation).
    """
    return re.sub(r"[^a-z0-9\s]", "", text.lower())


def remove_stopwords(text: str, stopwords: List[str]) -> List[str]:
    """
    Remove stop words from text.

    Args:
        text (str): Input text.
        stopwords (List[str]): List of stop words to remove.

    Returns:
        List[str]: List of remaining words (lowercased).
    """
    words = re.findall(r"\b[\w]+\b", text.lower())
    return [word for word in words if word not in stopwords]


def flatten_lists(lists: List[List[Any]]) -> List[Any]:
    """
    Flatten a list of lists into a single list.

    Args:
        lists (List[List[Any]]): List of lists.

    Returns:
        List[Any]: Flattened list containing all elements.
    """
    return [element for sublist in lists for element in sublist]


def shuffle_list(list_values: List[Any], seed: Optional[int] = 123) -> List[Any]:
    """
    Shuffle a list of values randomly, with an optional seed for reproducibility.

    Args:
        list_values (List[Any]): Input list.
        seed (Optional[int], optional): Random seed. Defaults to 123.

    Returns:
        List[Any]: Shuffled list.
    """
    random.seed(seed)
    shuffled = list_values.copy()
    random.shuffle(shuffled)
    return shuffled

