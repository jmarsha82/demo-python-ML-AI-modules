import pytest

from ml_ai_modules.regression import polynomial_regression_r2, train_test_split


def test_train_test_split_preserves_order_and_splits_labels():
    train_x, test_x, train_y, test_y = train_test_split(
        [1, 2, 3, 4, 5],
        [10, 20, 30, 40, 50],
        train_size=0.6,
    )

    assert train_x.tolist() == [1, 2, 3]
    assert test_x.tolist() == [4, 5]
    assert train_y.tolist() == [10, 20, 30]
    assert test_y.tolist() == [40, 50]


@pytest.mark.parametrize("train_size", [0, 1.0, 5])
def test_train_test_split_rejects_sizes_without_train_and_test_rows(train_size):
    with pytest.raises(ValueError):
        train_test_split([1, 2, 3], [1, 2, 3], train_size=train_size)


def test_train_test_split_rejects_mismatched_lengths():
    with pytest.raises(ValueError):
        train_test_split([1, 2, 3], [1, 2])


def test_polynomial_regression_scores_perfect_linear_fit():
    score = polynomial_regression_r2([1, 2, 3, 4], [3, 5, 7, 9], degree=1)

    assert score == pytest.approx(1.0)


def test_polynomial_regression_rejects_degree_without_enough_points():
    with pytest.raises(ValueError):
        polynomial_regression_r2([1, 2], [1, 4], degree=2)


def test_polynomial_regression_rejects_negative_degree_and_mismatched_lengths():
    with pytest.raises(ValueError):
        polynomial_regression_r2([1, 2, 3], [1, 2, 3], degree=-1)

    with pytest.raises(ValueError):
        polynomial_regression_r2([1, 2, 3], [1, 2], degree=1)
