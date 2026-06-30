import importlib.util
from pathlib import Path

import numpy as np


def load_neural_network_class():
    module_path = (
        Path(__file__).resolve().parents[1]
        / "neural-network-template"
        / "neuralNetworkClass.py"
    )
    spec = importlib.util.spec_from_file_location("neural_network_class", module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.NeuralNetwork


def test_neural_network_initializes_expected_shapes_and_properties():
    np.random.seed(1)
    neural_network = load_neural_network_class()(3, 4, 2, 0.3)

    assert neural_network.get_inodes() == 3
    assert neural_network.get_hnodes() == 4
    assert neural_network.get_onodes() == 2
    assert neural_network.get_lr() == 0.3
    assert neural_network.wih.shape == (4, 3)
    assert neural_network.who.shape == (2, 4)


def test_neural_network_setters_update_properties():
    np.random.seed(1)
    neural_network = load_neural_network_class()(3, 4, 2, 0.3)

    neural_network.set_inodes(5)
    neural_network.set_hnodes(6)
    neural_network.set_onodes(7)
    neural_network.set_lr(0.05)

    assert neural_network.get_inodes() == 5
    assert neural_network.get_hnodes() == 6
    assert neural_network.get_onodes() == 7
    assert neural_network.get_lr() == 0.05


def test_neural_network_query_returns_column_vector_between_zero_and_one():
    np.random.seed(2)
    neural_network = load_neural_network_class()(3, 3, 2, 0.1)

    output = neural_network.query([1.0, 0.5, -1.0])

    assert output.shape == (2, 1)
    assert np.all(output > 0)
    assert np.all(output < 1)


def test_neural_network_train_updates_weights():
    np.random.seed(3)
    neural_network = load_neural_network_class()(2, 3, 1, 0.2)
    original_wih = neural_network.wih.copy()
    original_who = neural_network.who.copy()

    neural_network.train([0.1, 0.9], [0.7])

    assert not np.array_equal(neural_network.wih, original_wih)
    assert not np.array_equal(neural_network.who, original_who)
