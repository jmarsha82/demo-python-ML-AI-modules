"""Similarity helpers based on the collaborative-filtering exercises."""

from __future__ import annotations

from collections.abc import Mapping

import numpy as np


def _cosine_distance(left: np.ndarray, right: np.ndarray) -> float:
    left_norm = np.linalg.norm(left)
    right_norm = np.linalg.norm(right)
    if left_norm == 0 and right_norm == 0:
        return 0.0
    if left_norm == 0 or right_norm == 0:
        return 1.0
    return float(1 - np.dot(left, right) / (left_norm * right_norm))


def item_distance(left, right) -> float:
    """Return the genre-plus-popularity distance from the movie exercise."""
    left_genres = np.asarray(left["genres"], dtype=float)
    right_genres = np.asarray(right["genres"], dtype=float)
    if left_genres.shape != right_genres.shape:
        raise ValueError("genre vectors must have the same shape")

    genre_distance = _cosine_distance(left_genres, right_genres)
    popularity_distance = abs(float(left["popularity"]) - float(right["popularity"]))
    return genre_distance + popularity_distance


def nearest_neighbors(
    item_id: int,
    items: Mapping[int, Mapping[str, object]],
    k: int,
) -> list[int]:
    """Return the IDs of the k closest neighbors for an item."""
    if item_id not in items:
        raise KeyError(f"unknown item_id: {item_id}")
    if k <= 0:
        raise ValueError("k must be greater than zero")
    if k >= len(items):
        raise ValueError("k must be smaller than the number of items")

    distances = [
        (candidate_id, item_distance(items[item_id], candidate))
        for candidate_id, candidate in items.items()
        if candidate_id != item_id
    ]
    distances.sort(key=lambda item: (item[1], item[0]))
    return [candidate_id for candidate_id, _ in distances[:k]]
