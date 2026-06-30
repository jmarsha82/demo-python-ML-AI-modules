"""Probability helpers based on the conditional-probability exercise."""

from __future__ import annotations

from collections.abc import Iterable
from random import Random


def conditional_probability(joint_count: int, condition_count: int) -> float:
    """Return P(A|B) from a joint count and a conditioning count."""
    if condition_count <= 0:
        raise ValueError("condition_count must be greater than zero")
    if joint_count < 0:
        raise ValueError("joint_count cannot be negative")
    if joint_count > condition_count:
        raise ValueError("joint_count cannot exceed condition_count")
    return joint_count / condition_count


def simulate_age_purchases(
    age_decades: Iterable[int],
    sample_size: int,
    purchase_probability: float,
    seed: int = 0,
) -> tuple[dict[int, int], dict[int, int], int]:
    """Simulate lesson-style purchase counts by age decade."""
    decades = list(age_decades)
    if not decades:
        raise ValueError("age_decades must contain at least one decade")
    if sample_size < 0:
        raise ValueError("sample_size cannot be negative")
    if not 0 <= purchase_probability <= 1:
        raise ValueError("purchase_probability must be between 0 and 1")

    # Deterministic lesson simulation; this is not used for secrets or security.
    random = Random(seed)  # nosec B311
    totals = dict.fromkeys(decades, 0)
    purchases = dict.fromkeys(decades, 0)
    total_purchases = 0

    for _ in range(sample_size):
        decade = random.choice(decades)  # nosec B311
        totals[decade] += 1
        if random.random() < purchase_probability:  # nosec B311
            purchases[decade] += 1
            total_purchases += 1

    return totals, purchases, total_purchases
