from src.payment import calculate_total, cart_subtotal


def test_subtotal():
    items = [{"price": 1000, "qty": 2}, {"price": 500, "qty": 1}]
    assert cart_subtotal(items) == 2500


def test_total_without_discount():
    items = [{"price": 1000, "qty": 1}]
    assert calculate_total(items) == 1120.0


def test_empty_cart():
    assert calculate_total([]) == 0.0
