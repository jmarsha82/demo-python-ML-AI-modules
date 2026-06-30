import pytest

from ml_ai_modules.probability import conditional_probability, simulate_age_purchases


def test_conditional_probability_uses_joint_and_condition_counts():
    assert conditional_probability(25, 100) == 0.25


@pytest.mark.parametrize(
    ("joint_count", "condition_count"),
    [(-1, 5), (6, 5), (1, 0)],
)
def test_conditional_probability_rejects_invalid_counts(
    joint_count,
    condition_count,
):
    with pytest.raises(ValueError):
        conditional_probability(joint_count, condition_count)


def test_simulate_age_purchases_is_seeded_and_counts_every_sample():
    totals, purchases, total_purchases = simulate_age_purchases(
        [20, 30],
        sample_size=10,
        purchase_probability=0.5,
        seed=11,
    )

    assert totals == {20: 5, 30: 5}
    assert purchases == {20: 3, 30: 2}
    assert total_purchases == sum(purchases.values()) == 5
    assert sum(totals.values()) == 10


@pytest.mark.parametrize(
    ("age_decades", "sample_size", "purchase_probability"),
    [([], 10, 0.5), ([20], -1, 0.5), ([20], 10, 1.1)],
)
def test_simulate_age_purchases_rejects_invalid_inputs(
    age_decades,
    sample_size,
    purchase_probability,
):
    with pytest.raises(ValueError):
        simulate_age_purchases(age_decades, sample_size, purchase_probability)
