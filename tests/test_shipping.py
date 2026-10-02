import pytest

from src.shipping import shipping_cost


def test_base_cost():
    assert shipping_cost(0) == 800


def test_cost_grows_with_weight():
    assert shipping_cost(2) == 1100


def test_negative_weight_rejected():
    with pytest.raises(ValueError):
        shipping_cost(-1)
