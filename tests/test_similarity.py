import pytest

from ml_ai_modules.similarity import item_distance, nearest_neighbors


def test_item_distance_combines_genre_and_popularity_distance():
    left = {"genres": [1, 0, 0], "popularity": 0.25}
    right = {"genres": [1, 0, 0], "popularity": 0.75}

    assert item_distance(left, right) == pytest.approx(0.5)


def test_item_distance_rejects_mismatched_genre_shapes():
    with pytest.raises(ValueError):
        item_distance(
            {"genres": [1, 0], "popularity": 0.25},
            {"genres": [1, 0, 0], "popularity": 0.75},
        )


def test_item_distance_handles_zero_vectors():
    assert item_distance(
        {"genres": [0, 0], "popularity": 0.25},
        {"genres": [0, 0], "popularity": 0.25},
    ) == 0
    assert item_distance(
        {"genres": [0, 0], "popularity": 0.25},
        {"genres": [1, 0], "popularity": 0.25},
    ) == 1


def test_nearest_neighbors_returns_closest_items_with_stable_tie_breaking():
    items = {
        1: {"genres": [1, 0, 0], "popularity": 0.3},
        2: {"genres": [1, 0, 0], "popularity": 0.4},
        3: {"genres": [0, 1, 0], "popularity": 0.3},
        4: {"genres": [1, 0, 0], "popularity": 0.5},
    }

    assert nearest_neighbors(1, items, k=2) == [2, 4]


@pytest.mark.parametrize("k", [0, 4])
def test_nearest_neighbors_rejects_invalid_k(k):
    with pytest.raises(ValueError):
        nearest_neighbors(1, {1: {"genres": [1], "popularity": 0}}, k=k)


def test_nearest_neighbors_rejects_unknown_item_id():
    with pytest.raises(KeyError):
        nearest_neighbors(99, {1: {"genres": [1], "popularity": 0}}, k=1)
