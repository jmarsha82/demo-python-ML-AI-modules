"""Regression helpers based on the train/test and polynomial exercises."""

from __future__ import annotations

import numpy as np


def train_test_split(
    features,
    labels,
    train_size: float | int = 0.8,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Split features and labels without shuffling, matching the lesson scripts."""
    x = np.asarray(features)
    y = np.asarray(labels)
    if x.shape[0] != y.shape[0]:
        raise ValueError("features and labels must have the same length")
    if x.shape[0] == 0:
        raise ValueError("features and labels cannot be empty")

    if isinstance(train_size, float):
        if not 0 < train_size < 1:
            raise ValueError("float train_size must be between 0 and 1")
        split_index = int(x.shape[0] * train_size)
    else:
        split_index = int(train_size)

    if not 0 < split_index < x.shape[0]:
        raise ValueError("train_size must leave at least one train and test row")

    return x[:split_index], x[split_index:], y[:split_index], y[split_index:]


def polynomial_regression_r2(features, labels, degree: int) -> float:
    """Fit a polynomial and return the coefficient of determination."""
    if degree < 0:
        raise ValueError("degree cannot be negative")

    x = np.asarray(features, dtype=float)
    y = np.asarray(labels, dtype=float)
    if x.shape[0] != y.shape[0]:
        raise ValueError("features and labels must have the same length")
    if x.shape[0] <= degree:
        raise ValueError("not enough points to fit the requested degree")

    polynomial = np.poly1d(np.polyfit(x, y, degree))
    predictions = polynomial(x)
    residual_sum_of_squares = np.sum((y - predictions) ** 2)
    total_sum_of_squares = np.sum((y - np.mean(y)) ** 2)
    if total_sum_of_squares == 0:
        return 1.0 if residual_sum_of_squares == 0 else 0.0
    return float(1 - residual_sum_of_squares / total_sum_of_squares)
