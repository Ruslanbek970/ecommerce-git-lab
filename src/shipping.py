"""Расчёт стоимости доставки."""

BASE_COST = 800      # базовая стоимость, ₸
PER_KG = 150         # за каждый килограмм, ₸


def shipping_cost(weight_kg):
    """Стоимость доставки заказа весом weight_kg."""
    if weight_kg < 0:
        raise ValueError("weight must not be negative")
    return (BASE_COST + PER_KG * weight_kg) // 100 * 100
