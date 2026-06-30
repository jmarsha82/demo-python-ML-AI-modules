"""Reusable helpers extracted from the ML/AI exercise scripts."""

from .probability import conditional_probability, simulate_age_purchases
from .regression import polynomial_regression_r2, train_test_split
from .similarity import item_distance, nearest_neighbors
from .statistics import covariance, de_mean, mean, median, mode, percentile

__all__ = [
    "conditional_probability",
    "covariance",
    "de_mean",
    "item_distance",
    "mean",
    "median",
    "mode",
    "nearest_neighbors",
    "percentile",
    "polynomial_regression_r2",
    "simulate_age_purchases",
    "train_test_split",
]
