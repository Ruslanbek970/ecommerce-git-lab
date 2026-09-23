import pytest

from src.loyalty import points_for_order, tier_for_customer


def test_points_for_order():
    assert points_for_order(10000) == 100


@pytest.mark.skip(reason="модуль уровней лояльности ещё не готов")
def test_tier_for_customer():
    assert tier_for_customer({"spent": 500000}) == "gold"


def test_tier_not_implemented_yet():
    with pytest.raises(NotImplementedError):
        tier_for_customer({"spent": 0})
