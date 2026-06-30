import pytest

from ml_ai_modules.statistics import covariance, de_mean, mean, median, mode, percentile


def test_descriptive_statistics_match_lesson_examples():
    values = [1, 2, 2, 4, 9]

    assert mean(values) == pytest.approx(3.6)
    assert median(values) == 2
    assert mode(values) == 2
    assert percentile(values, 50) == 2


def test_de_mean_centers_values_around_zero():
    centered = de_mean([1, 2, 3])

    assert centered == [-1.0, 0.0, 1.0]
    assert sum(centered) == pytest.approx(0.0)


def test_covariance_returns_sample_covariance():
    assert covariance([1, 2, 3], [2, 4, 6]) == pytest.approx(2.0)


@pytest.mark.parametrize("function", [mean, median, mode, de_mean])
def test_statistics_reject_empty_inputs(function):
    with pytest.raises(ValueError):
        function([])


def test_percentile_rejects_out_of_range_percent():
    with pytest.raises(ValueError):
        percentile([1, 2, 3], 101)


def test_covariance_requires_matching_lengths_and_multiple_values():
    with pytest.raises(ValueError):
        covariance([1, 2, 3], [1, 2])

    with pytest.raises(ValueError):
        covariance([1], [1])
