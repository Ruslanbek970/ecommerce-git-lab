"""Расчёт итоговой суммы заказа."""

TAX_RATE = 0.12  # НДС, Казахстан


def cart_subtotal(items):
    """Сумма позиций корзины без скидки и налога."""
    return sum(item["price"] * item["qty"] for item in items)


def calculate_total(items, discount_percent=0):
    """Итоговая сумма заказа с учётом скидки и НДС.

    items: [{"price": 1200, "qty": 2}, ...]
    discount_percent: скидка в процентах, например 10
    """
    subtotal = cart_subtotal(items)
    discounted = subtotal * (1 - discount_percent / 100)
    total = discounted * (1 + TAX_RATE)
    return round(total, 2)


def installment_plan(total, months):
    """Рассрочка: сумма платежа в месяц без процентов."""
    if months <= 0:
        raise ValueError("months must be positive")
    return round(total / months, 2)
