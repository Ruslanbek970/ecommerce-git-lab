import pytest

from src.shipping import shipping_cost


def test_almaty_is_base_price():
    assert shipping_cost(2, "almaty") == 1100


def test_regions_are_more_expensive():
    assert shipping_cost(2, "regions") == 1540


def test_unknown_zone_rejected():
    with pytest.raises(ValueError):
        shipping_cost(1, "mars")


def test_fractional_weight_is_not_rounded_down():
    """Дробный вес не должен терять тенге при округлении."""
    assert shipping_cost(1.5) == 1025
