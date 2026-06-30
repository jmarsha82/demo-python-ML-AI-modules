"""Small statistics helpers based on the early Python exercise scripts."""

from __future__ import annotations

from collections import Counter

import numpy as np


def _as_non_empty_array(values) -> np.ndarray:
    array = np.asarray(values, dtype=float)
    if array.size == 0:
        raise ValueError("values cannot be empty")
    return array


def mean(values) -> float:
    """Return the arithmetic mean."""
    return float(np.mean(_as_non_empty_array(values)))


def median(values) -> float:
    """Return the median."""
    return float(np.median(_as_non_empty_array(values)))


def mode(values):
    """Return the most common value, breaking ties by first appearance."""
    sequence = list(values)
    if not sequence:
        raise ValueError("values cannot be empty")
    counts = Counter(sequence)
    return max(sequence, key=counts.get)


def percentile(values, percent: float) -> float:
    """Return a percentile using NumPy's default interpolation method."""
    if not 0 <= percent <= 100:
        raise ValueError("percent must be between 0 and 100")
    return float(np.percentile(_as_non_empty_array(values), percent))


def de_mean(values) -> list[float]:
    """Center values around a mean of zero."""
    array = _as_non_empty_array(values)
    average = np.mean(array)
    return [float(value - average) for value in array]


def covariance(left, right) -> float:
    """Return sample covariance for two equally sized collections."""
    x = _as_non_empty_array(left)
    y = _as_non_empty_array(right)
    if x.size != y.size:
        raise ValueError("left and right must have the same length")
    if x.size < 2:
        raise ValueError("at least two values are required")
    return float(np.dot(de_mean(x), de_mean(y)) / (x.size - 1))
