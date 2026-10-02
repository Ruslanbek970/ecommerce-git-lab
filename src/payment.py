"""Расчёт итоговой суммы заказа."""

TAX_RATE = 0.12  # НДС, Казахстан


def cart_subtotal(items):
    """Сумма позиций корзины без скидки и налога."""
    return sum(item["price"] * item["qty"] for item in items)


PROMO_CODES = {"SHOPKZ500": 500, "WELCOME1000": 1000, "SUMMER300": 300}


def promo_discount(promo_code, subtotal):
    """Скидка по промокоду в тенге, не больше суммы корзины."""
    return min(PROMO_CODES.get(promo_code, 0), subtotal)


def calculate_total(items, discount_percent=0, promo_code=None):
    """Итоговая сумма заказа с учётом скидки и НДС.

    items: [{"price": 1200, "qty": 2}, ...]
    discount_percent: скидка в процентах, например 10
    """
    subtotal = cart_subtotal(items)
    subtotal -= promo_discount(promo_code, subtotal)
    discounted = subtotal * (1 - discount_percent / 100)
    total = discounted * (1 + TAX_RATE)
    return round(total, 2)


def installment_plan(total, months):
    """Рассрочка: сумма платежа в месяц без процентов."""
    if months <= 0:
        raise ValueError("months must be positive")
    return round(total / months, 2)
