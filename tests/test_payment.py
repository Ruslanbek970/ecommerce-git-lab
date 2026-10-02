from src.payment import calculate_total, cart_subtotal


def test_subtotal():
    items = [{"price": 1000, "qty": 2}, {"price": 500, "qty": 1}]
    assert cart_subtotal(items) == 2500


def test_total_without_discount():
    items = [{"price": 1000, "qty": 1}]
    assert calculate_total(items) == 1120.0


def test_empty_cart():
    assert calculate_total([]) == 0.0


def test_total_with_percent_discount():
    """Регрессия: скидка 10% на корзину 10000 тг = 10080 тг с НДС."""
    items = [{"price": 10000, "qty": 1}]
    assert calculate_total(items, 10) == 10080.0


def test_discount_does_not_exceed_subtotal():
    items = [{"price": 1000, "qty": 1}]
    assert calculate_total(items, 100) == 0.0
